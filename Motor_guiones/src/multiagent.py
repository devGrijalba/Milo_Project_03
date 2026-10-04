"""Multiagent parallel creation for the script stage.

Five narrow specialists run concurrently on ONE self-contained base package,
then a single synthesizer integrates them, deterministic validators run locally,
and an independent critic judges. Parallelism is used to cut LATENCY: the
specialists do not each write a script, they each answer one question.

Design rules that must not regress:
  - The base package is self-contained. A specialist never walks the project to
    rebuild context the orchestrator already has.
  - A failed specialist yields no script. There is no partial-candidate path.
  - Deterministic validation runs BEFORE any critic session is paid for.
  - Thresholds (90 per criterion, zero critical errors) are untouched.
  - No media, locks or paid calls live here: script creation is free.

Concurrency is bounded by script_parallel_agents, NOT by the global
max_parallel_tasks: stages that touch media, locks or paid APIs stay serial.
"""
import concurrent.futures
import json
import pathlib
import time

from src.common import ROOT, digest, read, write
from src.provider import call
from src.runtime import cached_call

# role -> (adapter config key, output contract summary)
SPECIALISTS = (
    ('script_hook_specialist', 'hook_specialist_command',
     'Find the best opening. Stop the scroll. Trigger recognition fast, '
     'introduce the conflict without over-explaining, never reveal the payoff, '
     'keep Milo identity. Return at most 3 genuinely different hooks.'),
    ('script_structure_specialist', 'structure_specialist_command',
     'Design the progression: order the beats, establish the open loop, the '
     'conflict, the shift in meaning and the reveal. Validate causality. '
     'Return a structure/beat map, not the final script.'),
    ('script_milo_voice_specialist', 'milo_voice_specialist_command',
     'Own Milo narrative identity, tone, naturalness and restraint. No moralising, '
     'no over-explaining, no generic sentimentality. Flag phrases that do not '
     'sound like this project. May propose specific wordings. Never alter seed facts.'),
    ('script_novelty_specialist', 'novelty_specialist_command',
     'Compare against the supplied history and flag repetition of conflict, '
     'twist, structure, arc, phrase, object or treatment. Do NOT invent virality '
     'metrics. Declare NOVELTY_UNVERIFIABLE when evidence is insufficient.'),
    ('script_ending_specialist', 'ending_specialist_command',
     'Own the close: emotional validation, shareability, last line. No artificial '
     'CTA, no school moral. Preserve the reinterpretation earned in the story. '
     'Return at most 3 options.'),
)

SYNTHESIZER = ('script_synthesizer', 'synthesizer_command')

# Narrow repair agents, selected by failed criterion instead of rewriting all.
REPAIR_AGENTS = {
    'hook': ('script_hook_repair', 'hook_repair_command'),
    'narrative': ('script_structure_repair', 'structure_repair_command'),
    'milo': ('script_milo_voice_repair', 'milo_voice_repair_command'),
    'voice': ('script_milo_voice_repair', 'milo_voice_repair_command'),
    'shareability': ('script_ending_repair', 'ending_repair_command'),
}


class ScriptStageBlocked(RuntimeError):
    """Structural block: no candidate exists and none will be invented."""


def base_package(request):
    """The self-contained package every specialist receives.

    Contains the seed, conflict, twist, canon, constraints and history the
    specialists need, so none of them has to traverse the project with tools to
    rediscover it.
    """
    sel = request['seed_selection']
    seed = sel['seed']
    return {
        'role_context': 'MILOSCRIPTBASE',
        'episode_id': request['episode_id'],
        'seed_id': seed['seed_id'],
        'bank_version': sel['bank_version'],
        'seed_hash': sel['seed_hash'],
        'seed_snapshot': seed,
        'territorio': seed.get('territorio'),
        'semilla': seed.get('semilla'),
        'conflicto': seed.get('conflicto') or seed.get('semilla'),
        'giro_disponible': seed.get('giro_posible') or seed.get('giro') or seed.get('payoff'),
        'context': request.get('context'),
        'history': request.get('history') or [],
        'constraints': request.get('constraints'),
        'previous_candidate': request.get('previous_candidate'),
        'revision_feedback': request.get('revision_feedback'),
        'base_hash': digest({
            'episode_id': request['episode_id'],
            'seed_hash': sel['seed_hash'],
            'context': request.get('context'),
            'history': request.get('history') or [],
        }),
    }


def scoped_base(base, role):
    import copy,re
    result=copy.deepcopy(base)
    context=result.get('context') or {}
    mining=context.get('mining','')
    # Canon, characters, constraints, full seed and history remain intact.
    # Only mining excerpts are selected; absence is explicit and never novelty proof.
    terms=set(re.findall(r'[^\W_]{5,}',str(base.get('semilla',''))+' '+str(base.get('territorio','')),re.UNICODE))
    sections=mining.split('\n\n')
    ranked=sorted(enumerate(sections),key=lambda x:(-sum(t.lower() in x[1].lower() for t in terms),x[0]))
    selected=[];size=0;budget=3500
    for index,section in ranked:
        if not any(t.lower() in section.lower() for t in terms):continue
        n=len(section.encode('utf8'))
        if size+n>budget:continue
        selected.append((index,section));size+=n
    context['mining']='\n\n'.join(x[1] for x in sorted(selected))
    context['mining_scope']={'source_sha256':digest(mining),'source_bytes':len(mining.encode('utf8')),'excerpt_bytes':size,'selection':'whole paragraphs matching seed/territory; not exhaustive','full_context_at_synthesis_and_qc':True}
    result['context']=context
    result['specialist_role']=role
    return result


def specialist_payload(base, brief):
    return {
        'role': base['role_context'],
        'instructions': brief,
        'base_package': base,
    }


def _run_specialist(name, key, brief, command, base, timeout, folder=None, max_bytes=6000):
    started = time.monotonic()
    payload = specialist_payload(scoped_base(base,name), brief + '\nReturn a concise JSON report: role, proposals (max3), evidence (max6), risks (max6), handoff. At most 600 words and '+str(max_bytes)+' UTF-8 bytes. Address only your assigned specialty. No final script or expanded production manual. Do not rediscover context through filesystem tools. If mining/history evidence is insufficient state that explicitly; never certify novelty from excerpts.')
    try:
        result = cached_call(command,payload,timeout,name,folder,call,max_bytes)
    except ValueError as exc:
        raise ScriptStageBlocked(str(exc)) from exc
    elapsed_ms = int((time.monotonic() - started) * 1000)
    if not isinstance(result, dict):
        raise ScriptStageBlocked('SPECIALIST_RESULT_NOT_OBJECT:' + name)
    # A specialist that reports a block is a block, not a stub candidate.
    if result.get('status') in ('HERMES_TASK_BLOCKED', 'HERMES_CAPABILITY_BLOCKED'):
        raise ScriptStageBlocked('SPECIALIST_BLOCKED:%s:%s' % (
            name, result.get('reason') or result.get('status')))
    return name, result, elapsed_ms


def parallel_specialists(c, base, timeout, executor=None, folder=None):
    """Run the five specialists concurrently. Wall clock is bounded by the
    slowest specialist, never by their sum."""
    commands = []
    for name, key, brief in SPECIALISTS:
        command = c.get(key)
        if not command or not isinstance(command, list):
            raise ScriptStageBlocked('SPECIALIST_ADAPTER_NOT_CONFIGURED:' + key)
        commands.append((name, key, brief, command))

    started = time.monotonic()
    results = {}
    timings = {}
    pool = executor or concurrent.futures.ThreadPoolExecutor(
        max_workers=max(1, int(c.get('script_parallel_agents') or len(commands))))
    try:
        futures = {
            pool.submit(_run_specialist, name, key, brief, command, base, timeout, folder, c.get('specialist_max_bytes',6000)): name
            for name, key, brief, command in commands
        }
        for future in concurrent.futures.as_completed(futures):
            name, result, elapsed_ms = future.result()
            results[name] = result
            timings[name] = elapsed_ms
    finally:
        if executor is None:
            pool.shutdown(wait=True)
    wall_clock_ms = int((time.monotonic() - started) * 1000)
    # Every specialist must have answered: a partial set yields no script.
    missing = [name for name, _, _ in SPECIALISTS if name not in results]
    if missing:
        raise ScriptStageBlocked('SPECIALIST_MISSING:' + ','.join(missing))
    return results, timings, wall_clock_ms


def synthesize(c, base, results, timeout, folder=None):
    """The ONLY creative agent that writes the complete candidate."""
    command = c.get(SYNTHESIZER[1])
    if not command or not isinstance(command, list):
        raise ScriptStageBlocked('SYNTHESIZER_ADAPTER_NOT_CONFIGURED')
    started = time.monotonic()
    payload = {
        'role': 'MILOSCRIPTSYNTHESIZER',
        'instructions': (
            'You are the only creative agent that writes the complete script. '
            'Integrate the five specialist reports below; do not concatenate them '
            'and do not discard a specialist to save words. Respect the seed, the '
            'canon, the constraints and the duration limit. Copy episode_id, seed_id, '
            'bank_version, seed_hash and seed_snapshot EXACTLY from base_package. '
            'Return the full candidate package object only. Follow the supplied writer contract exactly, including hooks, director_direction, voice texts and subshots.'),
        'base_package': base,
        'specialist_reports': results,
        'writer_contract': (ROOT/'prompts/writer.md').read_text(encoding='utf8'),
        'candidate_schema': read(ROOT/'schemas/script_package.schema.json'),
    }
    candidate = cached_call(command,payload,timeout,SYNTHESIZER[0],folder,call)
    if not isinstance(candidate, dict):
        raise ScriptStageBlocked('SYNTHESIZER_RESULT_NOT_OBJECT')
    return candidate, int((time.monotonic() - started) * 1000)


def deterministic_precheck(candidate, request):
    """Run everything Python can decide BEFORE paying for a critic session."""
    if not isinstance(candidate, dict):
        return ['Candidate must be a JSON object']
    errors = []
    sel = request['seed_selection']
    if candidate.get('episode_id') != request['episode_id']:
        errors.append('Episode mismatch')
    if candidate.get('seed_id') != sel['seed']['seed_id']:
        errors.append('Seed mismatch')
    if candidate.get('bank_version') != sel['bank_version']:
        errors.append('Bank version mismatch')
    if candidate.get('seed_hash') != sel['seed_hash']:
        errors.append('Seed snapshot hash mismatch')
    if candidate.get('seed_snapshot') != sel['seed']:
        errors.append('Seed snapshot changed')
    beats = candidate.get('beats')
    if not isinstance(beats, list) or not beats:
        errors.append('Beats missing or empty')
    if errors:
        return ['SCRIPT_CANDIDATE_CONTRACT_INVALID'] + errors
    return []


def needs_second_review(critic, candidate, c):
    """Conditional second critic. Replaces the old mandatory-exactly-two gate.

    Triggers only on an objective condition: a borderline score, a borderline
    confidence, a disagreement signal, or a candidate that was already repaired.
    Thresholds are unchanged; this changes WHEN a second opinion is bought, not
    what counts as approval.
    """
    reasons = []
    reviews = critic.get('reviews') or []
    for review in reviews:
        for name, item in (review.get('dimensions') or {}).items():
            score = item.get('score') if isinstance(item, dict) else None
            if isinstance(score, (int, float)) and not isinstance(score, bool) and 90 <= score <= 92:
                reasons.append('BORDERLINE_SCORE:%s=%s' % (name, score))
        if review.get('confidence') not in ('high',):
            reasons.append('UNCERTAIN_CONFIDENCE:' + str(review.get('confidence')))
    if any(isinstance(x, str) and 'DISAGREE' in x.upper() for x in (critic.get('critical_errors') or [])):
        reasons.append('CRITIC_DISAGREEMENT')
    if candidate.get('_repaired'):
        reasons.append('CANDIDATE_ALREADY_REPAIRED')
    # A single review has no internal disagreement to measure, so cap the trigger
    # list rather than inventing one.
    return sorted(set(reasons))


def select_repair(critic, candidate, c):
    """Pick the narrow repair agent for the failed criteria only."""
    repairs = []
    seen = set()
    for review in (critic.get('reviews') or []):
        for name, item in (review.get('dimensions') or {}).items():
            score = item.get('score') if isinstance(item, dict) else None
            threshold = c['min_milo_score'] if name == 'milo' else c['min_creative_score']
            if isinstance(score, (int, float)) and not isinstance(score, bool) and score < threshold:
                key = REPAIR_AGENTS.get(name)
                if key and key[0] not in seen:
                    seen.add(key[0])
                    repairs.append({
                        'criterion': name,
                        'score': score,
                        'threshold': threshold,
                        'agent': key[0],
                        'config_key': key[1],
                    })
    return repairs
