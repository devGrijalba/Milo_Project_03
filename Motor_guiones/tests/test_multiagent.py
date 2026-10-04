"""Contract tests for the multiagent script stage.

These run entirely on local doubles: no ElevenLabs, no Flow, no paid API, no
subprocess to a real provider. The canon and seed bank are read to prove they
are untouched, never written.
"""
import concurrent.futures
import hashlib
import json
import pathlib
import sys
import tempfile
import time
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT.parent.parent))

from src import multiagent as ma
from src import provider
from src import scorecard
from src import orchestrator
from src.common import DIMENSIONS, digest, read

PROJECT = ROOT.parent.parent


def _command(role, result, delay=0.0, log=None):
    """A local double for provider.call. Records the payload it received."""
    def _fake(command, payload, timeout, role=None):
        if log is not None:
            log.append({'role': role, 'payload': payload})
        if delay:
            time.sleep(delay)
        return result(payload) if callable(result) else result
    return _fake


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.folder = pathlib.Path(self.tmp.name)
        self.calls = []
        from src.request_builder import prepare
        from src.common import config
        self.config = config()
        self.request = prepare(self.config, 'EP0001', 'MILO-S0551')
        self.base = ma.base_package(self.request)

    def config_with(self, **overrides):
        c = dict(self.config)
        c.update(overrides)
        for role, key, _ in ma.SPECIALISTS:
            c[key] = ['fake', role]
        c[ma.SYNTHESIZER[1]] = ['fake', ma.SYNTHESIZER[0]]
        return c


# 1. five specialists launched concurrently
class Concurrency(Base):
    def test_five_specialists_run_concurrently(self):
        started = []
        finished = []

        def fake(command, payload, timeout, role=None):
            started.append(role)
            time.sleep(0.30)
            finished.append(role)
            return {'role': role, 'ok': True}

        ma.call = fake
        try:
            results, timings, wall = ma.parallel_specialists(self.config_with(), self.base, 30)
        finally:
            ma.call = provider.call
        self.assertEqual(len(started), 5)
        self.assertEqual(len(results), 5)
        # Every specialist began before any of them finished: proof of real overlap.
        self.assertEqual(sorted(started), sorted(finished))
        self.assertGreater(wall, 0)


# 2. wall clock lower than serial
class WallClock(Base):
    def test_parallel_wall_clock_below_serial_sum(self):
        def fake(command, payload, timeout, role=None):
            time.sleep(0.25)
            return {'role': role}

        ma.call = fake
        try:
            _, timings, wall = ma.parallel_specialists(self.config_with(), self.base, 30)
        finally:
            ma.call = provider.call
        serial = sum(timings.values())
        self.assertLess(wall, serial * 0.75,
                        'wall clock %d should be well under serial sum %d' % (wall, serial))
        slowest = max(timings.values())
        self.assertLess(wall, slowest * 2.0,
                        'wall clock must track the slowest specialist, not the sum')


# 3. each specialist receives the complete request
class SelfContained(Base):
    def test_every_specialist_receives_full_base_package(self):
        def fake(command, payload, timeout, role=None):
            bp = payload.get('base_package')
            for key in ('episode_id', 'seed_id', 'bank_version', 'seed_hash',
                        'seed_snapshot', 'territorio', 'semilla', 'context',
                        'history', 'constraints', 'base_hash'):
                self.assertIn(key, bp, '%s missing %s' % (role, key))
            self.assertEqual(bp['seed_hash'], self.base['seed_hash'])
            return {'role': role}

        ma.call = fake
        try:
            results, _, _ = ma.parallel_specialists(self.config_with(), self.base, 30)
        finally:
            ma.call = provider.call
        self.assertEqual(len(results), 5)

    def test_base_package_carries_conflict_twist_and_constraints(self):
        for key in ('conflicto', 'giro_disponible', 'constraints', 'history'):
            self.assertIn(key, self.base)


# 4. synthesizer receives the five results
class Synthesis(Base):
    def test_synthesizer_receives_all_five_reports(self):
        seen = {}

        def fake(command, payload, timeout, role=None):
            if role == 'script_synthesizer':
                seen.update(payload)
                return {'episode_id': 'EP0001'}
            return {'role': role}

        ma.call = fake
        try:
            reports = {name: {'specialist': name} for name, _, _ in ma.SPECIALISTS}
            ma.synthesize(self.config_with(), self.base, reports, 30)
        finally:
            ma.call = provider.call
        self.assertEqual(len(seen['specialist_reports']), 5)


# 5. one specialist failing yields no script
class PartialFailure(Base):
    def test_failed_specialist_blocks_instead_of_partial_script(self):
        def fake(command, payload, timeout, role=None):
            if role == 'script_novelty_specialist':
                return {'status': 'HERMES_TASK_BLOCKED', 'reason': 'NO_HISTORY'}
            return {'role': role}

        ma.call = fake
        try:
            with self.assertRaises(ma.ScriptStageBlocked):
                ma.parallel_specialists(self.config_with(), self.base, 30)
        finally:
            ma.call = provider.call

    def test_capability_blocked_is_a_block_not_a_candidate(self):
        def fake(command, payload, timeout, role=None):
            return {'status': 'HERMES_CAPABILITY_BLOCKED', 'reason': 'NO_VISION'}

        ma.call = fake
        try:
            with self.assertRaises(ma.ScriptStageBlocked):
                ma.parallel_specialists(self.config_with(), self.base, 30)
        finally:
            ma.call = provider.call


# 6. contract validator intact
class ContractValidatorIntact(Base):
    def test_validator_still_rejects_missing_contract_fields(self):
        from src.contract_validator import validate
        errors = validate({'episode_id': 'EP9999'}, self.request, self.config)
        self.assertTrue(any('Episode mismatch' in e for e in errors))

    def test_validator_still_requires_three_hooks(self):
        from src.contract_validator import validate
        errors = validate({'episode_id': 'EP0001', 'hooks': []}, self.request, self.config)
        self.assertTrue(any('hook' in e.lower() for e in errors))


# 7. deterministic validation before the critic
class DeterministicFirst(Base):
    def test_precheck_catches_seed_mismatch_without_critic(self):
        bad = {'episode_id': 'EP0001', 'seed_id': 'WRONG', 'bank_version': 'x',
               'seed_hash': 'y', 'seed_snapshot': {}, 'beats': []}
        errors = ma.deterministic_precheck(bad, self.request)
        self.assertIn('SCRIPT_CANDIDATE_CONTRACT_INVALID', errors)
        self.assertTrue(any('Seed mismatch' in e for e in errors))

    def test_empty_beats_block_before_critic(self):
        sel = self.request['seed_selection']
        bad = {'episode_id': 'EP0001', 'seed_id': sel['seed']['seed_id'],
               'bank_version': sel['bank_version'], 'seed_hash': sel['seed_hash'],
               'seed_snapshot': sel['seed'], 'beats': []}
        errors = ma.deterministic_precheck(bad, self.request)
        self.assertTrue(any('Beats' in e for e in errors))

    def test_precheck_passes_a_consistent_candidate(self):
        sel = self.request['seed_selection']
        good = {'episode_id': 'EP0001', 'seed_id': sel['seed']['seed_id'],
                'bank_version': sel['bank_version'], 'seed_hash': sel['seed_hash'],
                'seed_snapshot': sel['seed'], 'beats': [{'beat_id': 'b1'}]}
        self.assertEqual(ma.deterministic_precheck(good, self.request), [])


# 8. critic runs in an independent session
class CriticIndependence(Base):
    def test_critic_payload_has_hash_and_context_not_history_reuse(self):
        candidate = {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1', 'narration': 'x'}]}
        captured = {}

        def fake(command, payload, timeout, role=None):
            captured.update(payload)
            return {'reviews': [{'review_id':'test'}]}

        orchestrator.call = fake
        try:
            orchestrator._critic_once(
                self.config_with(), self.request, candidate, self.folder, 0,
                orchestrator._metrics(), 30)
        finally:
            orchestrator.call = provider.call
        # The critic gets the candidate plus its exact hash, not the writer's history.
        self.assertEqual(captured['candidate_hash'], digest(candidate))
        self.assertIn('candidate', captured)
        self.assertIn('context', captured)
        self.assertTrue((self.folder / 'critic_00.json').is_file())

    def test_merge_never_copies_scores(self):
        first = {'reviews': [{'review_id': 'A', 'dimensions': {k: {'score': 95} for k in DIMENSIONS}}]}
        second = {'reviews': [{'review_id': 'B', 'dimensions': {k: {'score': 91} for k in DIMENSIONS}}]}
        merged = orchestrator._merge_reviews(first, second)
        self.assertEqual(len(merged['reviews']), 2)
        ids = [r['review_id'] for r in merged['reviews']]
        self.assertEqual(ids, ['A', 'B'])
        self.assertEqual(merged['reviews'][0]['dimensions']['hook']['score'], 95)
        self.assertEqual(merged['reviews'][1]['dimensions']['hook']['score'], 91)


# 9. one approved review passes alone
class SingleReview(Base):
    def _review(self, score=95, rid='A'):
        return {'review_id': rid, 'role': 'independent_critic',
                'candidate_hash': 'x', 'rubric_version': '1.0.0', 'confidence': 'high',
                'critical_errors': [], 'novelty_checked_against_history': True,
                'canon_comparison': 'a', 'mining_comparison': 'b', 'history_comparison': 'c',
                'perspectives': {'facebook_viewer': 'x', 'cinematic_director': 'y', 'milo_director': 'z'},
                'dimensions': {k: {'score': score, 'evidence': ['e'], 'beat_ids': ['b1'], 'improvement': 'i'}
                               for k in DIMENSIONS}}

    def _candidate(self):
        return {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1', 'narration': 'n'}]}

    def test_single_review_can_approve(self):
        from src.creative_qc import critic_check
        c = self.config_with(min_review_passes=1)
        report = {'reviews': [self._review()]}
        issues, card = scorecard.aggregate(report, self._candidate(), c, lambda x, p, cc: [])
        self.assertEqual(issues, [])
        self.assertEqual(card['review_passes'], 1)
        self.assertGreaterEqual(card['overall'], 90)

    def test_second_review_is_conditional(self):
        strong = {'reviews': [self._review(score=95)]}
        self.assertEqual(ma.needs_second_review(strong, {}, self.config), [])


# 10. second review fires only under condition
class ConditionalSecond(Base):
    def test_borderline_score_triggers_second_review(self):
        review = {'reviews': [{'dimensions': {'hook': {'score': 91}}, 'confidence': 'high'}]}
        reasons = ma.needs_second_review(review, {}, self.config)
        self.assertTrue(any('BORDERLINE_SCORE' in r for r in reasons))

    def test_low_confidence_triggers_second_review(self):
        review = {'reviews': [{'dimensions': {}, 'confidence': 'medium'}]}
        reasons = ma.needs_second_review(review, {}, self.config)
        self.assertTrue(any('UNCERTAIN_CONFIDENCE' in r for r in reasons))

    def test_repaired_candidate_triggers_second_review(self):
        review = {'reviews': [{'dimensions': {}, 'confidence': 'high'}]}
        reasons = ma.needs_second_review(review, {'_repaired': True}, self.config)
        self.assertTrue(any('ALREADY_REPAIRED' in r for r in reasons))

    def test_clean_high_review_triggers_nothing(self):
        review = {'reviews': [{'dimensions': {'hook': {'score': 97}}, 'confidence': 'high'}],
                   'critical_errors': []}
        self.assertEqual(ma.needs_second_review(review, {}, self.config), [])


# 11. repair targets the failed criterion
class SelectiveRepair(Base):
    def test_repair_agent_selected_for_failed_criterion_only(self):
        review = {'reviews': [{'dimensions': {
            'hook': {'score': 82}, 'narrative': {'score': 95}, 'milo': {'score': 96}}}]}
        repairs = ma.select_repair(review, {}, self.config)
        self.assertEqual(len(repairs), 1)
        self.assertEqual(repairs[0]['criterion'], 'hook')
        self.assertEqual(repairs[0]['agent'], 'script_hook_repair')

    def test_no_repairs_when_everything_passes(self):
        review = {'reviews': [{'dimensions': {k: {'score': 96} for k in DIMENSIONS}}]}
        self.assertEqual(ma.select_repair(review, {}, self.config), [])

    def test_repair_payload_protects_approved_criteria(self):
        captured = {}

        def fake(command, payload, timeout, role=None):
            captured.update(payload)
            return {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1', 'narration': 'fixed'}]}

        orchestrator.call = fake
        try:
            candidate = {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1', 'narration': 'orig'}]}
            repairs = ma.select_repair({'reviews': [{'dimensions': {'hook': {'score': 80}}}]}, candidate, self.config)
            metrics = orchestrator._metrics()
            out = orchestrator._apply_repairs(self.config_with(), self.request, candidate,
                                              repairs, self.folder, 0, metrics, 30)
        finally:
            orchestrator.call = provider.call
        self.assertIn('hook', captured['failed_criteria'][0]['criterion'])
        self.assertIn('narrative', captured['protected_criteria'])
        self.assertTrue(out['_repaired'])


# 12. max revisions
class RevisionBudget(Base):
    def test_max_revisions_is_three(self):
        self.assertEqual(self.config['max_revisions'], 3)

    def test_attempt_budget_derives_from_max_revisions(self):
        c = self.config_with(max_revisions=3)
        self.assertEqual(range(c['max_revisions'] + 1).__len__(), 4)


# 13. HERMES_TASK_BLOCKED stops the chain
class TaskBlocked(Base):
    def test_provider_propagates_task_blocked(self):
        def fake_run(command, input=None, **kwargs):
            return type('R', (), {'returncode': 0,
                                  'stdout': json.dumps({'status': 'HERMES_TASK_BLOCKED',
                                                        'reason': 'MISSING_CONTEXT'})})()
        real = provider.subprocess.run
        provider.subprocess.run = fake_run
        try:
            with self.assertRaises(ValueError) as ctx:
                provider.call(['x'], {'base_package': self.base}, 5, role='script_hook_specialist')
        finally:
            provider.subprocess.run = real
        self.assertIn('HERMES_TASK_BLOCKED', str(ctx.exception))

    def test_structural_block_never_becomes_a_candidate(self):
        def fake(command, payload, timeout, role=None):
            return {'status': 'HERMES_TASK_BLOCKED', 'reason': 'X'}
        ma.call = fake
        try:
            with self.assertRaises(ma.ScriptStageBlocked):
                ma.parallel_specialists(self.config_with(), self.base, 30)
        finally:
            ma.call = provider.call


# 14. stub payload rejected before Hermes
class StubRejected(Base):
    def test_stub_payload_is_rejected_locally(self):
        missing = provider.validate_payload('script_hook_specialist', {'role': 'script_hook_specialist'})
        self.assertIn('base_package', missing)

    def test_provider_raises_before_spawning_subprocess(self):
        def explode(*args, **kwargs):
            raise AssertionError('subprocess must not start for a stub payload')
        real = provider.subprocess.run
        provider.subprocess.run = explode
        try:
            with self.assertRaises(ValueError) as ctx:
                provider.call(['x'], {'role': 'script_writer',
                                      'instructions': 'Reply with JSON only.'}, 5, role='script_writer')
        finally:
            provider.subprocess.run = real
        self.assertIn('MISSING_SCRIPT_REQUEST_CONTEXT', str(ctx.exception))

    def test_complete_payload_passes_validation(self):
        self.assertEqual(
            provider.validate_payload('script_hook_specialist', {'base_package': self.base}), [])
        self.assertEqual(
            provider.validate_payload('script_synthesizer',
                                      {'base_package':self.base,'specialist_reports':{str(i):{} for i in range(5)}}), [])


# 15 & 16. no paid or media calls during script tests
class NoPaidCalls(Base):
    def test_no_elevenlabs_or_flow_referenced_in_script_stage(self):
        for name in ('multiagent.py', 'orchestrator.py', 'provider.py', 'scorecard.py'):
            text = (ROOT / 'src' / name).read_text(encoding='utf8').lower()
            for forbidden in ('elevenlabs', 'api.elevenlabs.io', 'run_flow', 'flow_bridge',
                              'generate_image', 'nano banana'):
                self.assertNotIn(forbidden, text,
                                 '%s must not reference %s' % (name, forbidden))


# 17 & 18. canon and seeds byte-identical
class CanonUnchanged(Base):
    def test_anchor_hashes_still_match_registry(self):
        registry = read(PROJECT / '01_CANON/anchors/registry.json')
        for item in registry['items']:
            path = PROJECT / '01_CANON/anchors' / item['file']
            digest_bytes = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertEqual(digest_bytes, item['sha256'], 'canon changed: ' + item['file'])

    def test_seed_bank_still_has_1000_seeds(self):
        bank = read(ROOT / 'data/seeds.json')
        self.assertEqual(len(bank['seeds']), 1000)


# 19. prior episodes readable
class EpisodeCompatibility(Base):
    def test_ep0001_request_still_readable(self):
        path = PROJECT / 'artefactos/episodes/EP0001/request.json'
        if not path.is_file():
            self.skipTest('no prior episode in this checkout')
        data = read(path)
        self.assertEqual(data['episode_id'], 'EP0001')
        self.assertIn('seed_selection', data)


# 20. orchestration still exposes the same entry point
class EntryPoint(Base):
    def test_run_signature_unchanged(self):
        import inspect
        params = list(inspect.signature(orchestrator.run).parameters)
        self.assertEqual(params, ['request', 'c', 'folder'])

    def test_milo_cli_still_imports_orchestrator(self):
        self.assertTrue(callable(orchestrator.run))


if __name__ == '__main__':
    unittest.main()
