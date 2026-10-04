"""Script stage: parallel specialists -> synthesis -> deterministic validation
-> independent critic -> selective repair -> conditional second review.

The external interface is unchanged: run(request, c, folder) still returns the
same QC dict and still writes the same artifact names, so milo.py produce keeps
working without adaptation. Thresholds, contract validation, exports and paid
stages are untouched.
"""
import pathlib
import time
import os
from src.runtime import cached_call,event

from src.common import ROOT, digest, write
from src.provider import call
from src.creative_qc import finalize
from src.exporter import export
from src import multiagent as ma

METRICS = 'script_stage_metrics.json'


def _metrics():
    return {
        'parallel_stage': {},
        'wall_clock_ms': 0,
        'sum_agent_ms': 0,
        'slowest_agent_ms': 0,
        'synthesis_ms': 0,
        'deterministic_validation_ms': 0,
        'critic_ms': 0,
        'repair_ms': 0,
        'total_script_stage_ms': 0,
        'second_review_reasons': [],
        'repair_cycles': 0,
    }


def _critic_once(c, request, candidate, folder, index, metrics, timeout, pass_id='primary'):
    """One independent critic session. Never reuses a previous session's scores."""
    started = time.monotonic()
    instructions = (ROOT / 'prompts/critic.md').read_text(encoding='utf8')
    payload = {
        'instructions': instructions,
        'review_pass_id': pass_id,
        'candidate': candidate,
        'candidate_hash': digest(candidate),
        'context': request['context'],
        'history': request['history'],
    }
    # argv is supplied only for the subprocess route. Under deepseek_cdp the
    # provider reads its own config and the argv is inert, so demanding it here
    # would block a working provider over a config field it never reads.
    command = c.get('critic_command')
    report = cached_call(command, payload, timeout, 'script_critic', folder, call)
    if not isinstance(report,dict) or len(report.get('reviews',[]))!=1:raise ValueError('CRITIC_MUST_RETURN_ONE_REVIEW_PER_SESSION')
    metrics['critic_ms'] += int((time.monotonic() - started) * 1000)
    write(folder / ('critic_%02d%s.json' % (index,'' if pass_id=='primary' else '_'+pass_id)), report)
    return report


def _deterministic_gate(candidate, request, folder, metrics, index):
    """Local validation before any critic session is paid for."""
    started = time.monotonic()
    errors = ma.deterministic_precheck(candidate, request)
    metrics['deterministic_validation_ms'] += int((time.monotonic() - started) * 1000)
    write(folder / ('precheck_%02d.json' % index), {
        'status': 'SCRIPT_CANDIDATE_CONTRACT_INVALID' if errors else 'PRECHECK_PASSED',
        'errors': errors,
    })
    return errors


def _merge_reviews(first, second):
    """Combine two independent critic sessions without copying any score."""
    reviews = (first.get('reviews') if isinstance(first, dict) else None) or [first]
    extra = (second.get('reviews') if isinstance(second, dict) else None) or [second]
    merged = {'reviews': list(reviews) + list(extra)}
    for key in ('role', 'critical_errors', 'perspectives', 'novelty_checked_against_history'):
        if isinstance(first, dict) and key in first:
            merged[key] = first[key]
    return merged


def _apply_repairs(c, request, candidate, repairs, folder, index, metrics, timeout):
    """Repair only what failed, via the narrow agent for that criterion."""
    started = time.monotonic()
    repaired = candidate
    for repair in repairs:
        command = c.get(repair['config_key'])
        # Only skip when the SUBPROCESS route is unusable. Under deepseek_cdp the
        # argv is legitimately absent and the provider works without it -- a bare
        # `continue` here silently dropped every repair, which is exactly what the
        # migrated test caught.
        subprocess_route = c.get('provider') != 'deepseek_cdp'
        if subprocess_route and (not command or not isinstance(command, list)):
            continue
        payload = {
            'role': repair['agent'],
            'instructions': (
                'Fix ONLY the listed failed criterion. Preserve every approved part '
                'byte for byte unless a narrative dependency makes it impossible, and '
                'say so explicitly when that happens. Never change seed facts, canon, '
                'or previously approved criteria. Return the full candidate package.'),
            'base_package': ma.base_package(request),
            'candidate': repaired,
            'candidate_hash': digest(repaired),
            'failed_criteria': [repair],
            'protected_criteria': [k for k in ('hook', 'narrative', 'emotion', 'visual',
                                               'voice', 'editing', 'shareability', 'milo')
                                  if k != repair['criterion']],
        }
        result = cached_call(command,payload,timeout,repair['agent'],folder,call)
        if not isinstance(result, dict):
            continue
        write(folder / ('repair_%02d_%s.json' % (index, repair['criterion'])), result)
        repaired = result
    repaired['_repaired'] = True
    metrics['repair_ms'] += int((time.monotonic() - started) * 1000)
    return repaired


def _run(request, c, folder):
    folder = pathlib.Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    write(folder / 'request.json', request)
    metrics = _metrics()
    stage_started = time.monotonic()
    timeout = c['timeout_s']

    base = ma.base_package(request)
    write(folder / 'specialist_base_package.json', base)

    # 1. Five specialists, concurrently. Bounded by script_parallel_agents and
    #    NOT by the global max_parallel_tasks: media/locks/paid stages stay serial.
    results, timings, wall_clock_ms = ma.parallel_specialists(c, base, timeout, folder=folder)
    metrics['parallel_stage'] = timings
    metrics['wall_clock_ms'] = wall_clock_ms
    metrics['sum_agent_ms'] = sum(timings.values())
    metrics['slowest_agent_ms'] = max(timings.values()) if timings else 0
    write(folder / 'specialist_reports.json', results)

    # 2. One synthesizer writes the complete candidate.
    candidate, synth_ms = ma.synthesize(c, base, results, timeout, folder=folder)
    metrics['synthesis_ms'] = synth_ms
    write(folder / 'candidate_00.json', candidate)

    # 3. Deterministic validation first: no critic session is paid for a package
    #    the local code can already reject in milliseconds.
    for attempt in range(c['max_revisions'] + 1):
        errors = _deterministic_gate(candidate, request, folder, metrics, attempt)
        if errors:
            qc, exported = finalize(candidate, request, c)
            export(folder, exported, qc)
            metrics['total_script_stage_ms'] = int((time.monotonic() - stage_started) * 1000)
            write(folder / METRICS, metrics)
            return qc

        qc, exported = finalize(candidate, request, c)
        if qc.get('technical_errors'):
            export(folder,exported,qc)
            metrics['total_script_stage_ms']=int((time.monotonic()-stage_started)*1000)
            write(folder/METRICS,metrics)
            return qc
        if qc['status'] == 'AWAITING_CREATIVE_QC':
            export(folder, exported, qc)

            critic = _critic_once(c, request, exported, folder, attempt, metrics, timeout)
            qc, exported = finalize(candidate, request, c, critic)

            # 4. Conditional second review: objective triggers only.
            reasons = ma.needs_second_review(critic, exported, c)
            metrics['second_review_reasons'] = reasons
            if reasons and len(critic.get('reviews',[]))==1:
                second = _critic_once(c, request, exported, folder, attempt, metrics, timeout, pass_id='independent_second')
                write(folder / ('critic_%02d_conditional_second.json' % attempt), second)
                merged = _merge_reviews(critic, second)
                merged['_conditional_second_review'] = reasons
                qc, exported = finalize(candidate, request, c, merged)
                critic = merged

        export(folder, exported, qc)
        if qc['status'] == 'SCRIPT_APPROVED':
            metrics['total_script_stage_ms'] = int((time.monotonic() - stage_started) * 1000)
            write(folder / METRICS, metrics)
            return qc

        # 5. Selective repair: narrow agent per failed criterion, not a rewrite.
        if attempt < c['max_revisions']:
            repairs = ma.select_repair(critic, exported, c)
            if repairs:
                metrics['repair_cycles'] += 1
                before_repair=digest({k:v for k,v in candidate.items() if k not in ['_repaired','timing']})
                candidate = _apply_repairs(c, request, candidate, repairs, folder,
                                           attempt, metrics, timeout)
            else:
                qc['optimization_block']='NO_APPLICABLE_REPAIR_NO_UNCHANGED_REVIEW'
                export(folder,exported,qc)
                break
            if digest({k:v for k,v in candidate.items() if k not in ['_repaired','timing']})==before_repair:
                qc['optimization_block']='REPAIR_DID_NOT_CHANGE_CANDIDATE'
                export(folder,exported,qc)
                break
            write(folder / ('candidate_%02d.json' % (attempt + 1)), candidate)

    metrics['total_script_stage_ms'] = int((time.monotonic() - stage_started) * 1000)
    write(folder / METRICS, metrics)
    return qc


def run(request,c,folder):
    folder=pathlib.Path(folder);folder.mkdir(parents=True,exist_ok=True)
    lock=folder/'script_optimization.lock'
    fd=os.open(lock,os.O_CREAT|os.O_EXCL|os.O_WRONLY);os.close(fd)
    started=time.monotonic()
    event(folder,'orchestrator','RUNNING')
    try:
        result=_run(request,c,folder)
        event(folder,'orchestrator',result['status'],elapsed_ms=int((time.monotonic()-started)*1000))
        return result
    except Exception as exc:
        event(folder,'orchestrator','BLOCKED',elapsed_ms=int((time.monotonic()-started)*1000),reason=str(exc))
        write(folder/'script_failure.json',{'status':'SCRIPT_STAGE_BLOCKED','reason':str(exc),'elapsed_ms':int((time.monotonic()-started)*1000)})
        raise
    finally:lock.unlink(missing_ok=True)
