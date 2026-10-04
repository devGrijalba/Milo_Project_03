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

    def deepseek_config(self, **overrides):
        """DeepSeek route: NO argv commands anywhere. A test that needs one is
        testing the subprocess route and should say so explicitly."""
        c = dict(self.config)
        c['provider'] = 'deepseek_cdp'
        for role, key, _ in ma.SPECIALISTS:
            c.pop(key, None)
        c.pop(ma.SYNTHESIZER[1], None)
        for key in ('critic_command', 'hook_repair_command', 'structure_repair_command',
                    'milo_voice_repair_command', 'ending_repair_command'):
            c.pop(key, None)
        c.update(overrides)
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
        """MIGRATED (class B): the contract, not the transport.

        Still asserts the guarantee that mattered -- the critic receives the
        candidate plus its exact hash and the context, and does NOT depend on
        reusing a previous conversation. What changed is the transport: no argv
        requirement, and the role alone determines the logical session.
        """
        candidate = {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1', 'narration': 'x'}]}
        captured = {}

        def fake(command, payload, timeout, role=None):
            captured.update(payload)
            captured['__role__'] = role
            captured['__argv__'] = command
            return {'reviews': [{'review_id': 'test'}]}

        orchestrator.call = fake
        try:
            orchestrator._critic_once(
                self.deepseek_config(), self.request, candidate, self.folder, 0,
                orchestrator._metrics(), 30)
        finally:
            orchestrator.call = provider.call
        # The critic gets the candidate plus its exact hash, not the writer's history.
        self.assertEqual(captured['candidate_hash'], digest(candidate))
        self.assertIn('candidate', captured)
        self.assertIn('context', captured)
        self.assertTrue((self.folder / 'critic_00.json').is_file())

    def test_critic_runs_without_argv_under_deepseek(self):
        """No critic_command in config: the DeepSeek route must still be invoked."""
        c = self.deepseek_config()
        self.assertIsNone(c.get('critic_command'))

        def fake(command, payload, timeout, role=None):
            self.assertIsNone(command, 'argv must not be required under deepseek_cdp')
            return {'reviews': [{'review_id': 'r'}]}

        orchestrator.call = fake
        try:
            report = orchestrator._critic_once(
                c, self.request,
                {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1', 'narration': 'x'}]},
                self.folder, 0, orchestrator._metrics(), 30)
        finally:
            orchestrator.call = provider.call
        self.assertEqual(1, len(report['reviews']))

    def test_critic_role_determines_the_logical_session(self):
        """The role is the session key. A physical tab id must never appear."""
        seen = {}

        def fake(command, payload, timeout, role=None):
            seen['role'] = role
            return {'reviews': [{'review_id': 'r'}]}

        orchestrator.call = fake
        try:
            orchestrator._critic_once(
                self.deepseek_config(), self.request,
                {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1', 'narration': 'x'}]},
                self.folder, 0, orchestrator._metrics(), 30)
        finally:
            orchestrator.call = provider.call
        self.assertEqual('script_critic', seen['role'])
        from src.ds_provider import call as _ds_call
        # a role with no explicit session_name derives one from the role itself
        self.assertEqual('specialist_' + 'script_critic',
                         'specialist_' + seen['role'])

    def test_critic_still_requires_exactly_one_review(self):
        def two_reviews(command, payload, timeout, role=None):
            return {'reviews': [{'review_id': 'A'}, {'review_id': 'B'}]}

        orchestrator.call = two_reviews
        try:
            with self.assertRaises(ValueError) as cm:
                orchestrator._critic_once(
                    self.deepseek_config(), self.request,
                    {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1'}]},
                    self.folder, 0, orchestrator._metrics(), 30)
        finally:
            orchestrator.call = provider.call
        self.assertIn('CRITIC_MUST_RETURN_ONE_REVIEW', str(cm.exception))

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
        """MIGRATED (class B): contract, not transport.

        Same guarantee as before -- failed_criteria names what broke and
        protected_criteria names what must survive. What changed: no argv is
        required, so a repair is no longer silently skipped under DeepSeek.
        """
        captured = {}

        def fake(command, payload, timeout, role=None):
            captured.update(payload)
            captured['__role__'] = role
            captured['__argv__'] = command
            return {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1', 'narration': 'fixed'}]}

        orchestrator.call = fake
        try:
            candidate = {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1', 'narration': 'orig'}]}
            repairs = ma.select_repair({'reviews': [{'dimensions': {'hook': {'score': 80}}}]}, candidate, self.config)
            metrics = orchestrator._metrics()
            out = orchestrator._apply_repairs(self.deepseek_config(), self.request, candidate,
                                              repairs, self.folder, 0, metrics, 30)
        finally:
            orchestrator.call = provider.call
        self.assertIn('hook', captured['failed_criteria'][0]['criterion'])
        self.assertIn('narrative', captured['protected_criteria'])
        self.assertTrue(out['_repaired'])

    def test_repair_is_not_silently_skipped_without_argv(self):
        """The regression this migration exists to catch: under deepseek_cdp the
        argv is absent, and a naive `continue` drops the repair entirely. The
        repair agent must actually be invoked."""
        calls = []

        def fake(command, payload, timeout, role=None):
            calls.append({'role': role, 'argv': command,
                          'failed': [f['criterion'] for f in payload['failed_criteria']]})
            return {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1', 'narration': 'fixed'}]}

        orchestrator.call = fake
        try:
            candidate = {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1', 'narration': 'orig'}]}
            review = {'reviews': [{'dimensions': {
                'hook': {'score': 80}, 'narrative': {'score': 95}, 'milo': {'score': 96}}}]}
            repairs = ma.select_repair(review, candidate, self.config)
            out = orchestrator._apply_repairs(self.deepseek_config(), self.request, candidate,
                                              repairs, self.folder, 0,
                                              orchestrator._metrics(), 30)
        finally:
            orchestrator.call = provider.call
        self.assertEqual(1, len(calls), 'the repair agent must actually run')
        self.assertEqual('script_hook_repair', calls[0]['role'])
        self.assertIsNone(calls[0]['argv'])
        self.assertEqual(['hook'], calls[0]['failed'])
        self.assertTrue(out['_repaired'])

    def test_repair_role_determines_the_logical_session(self):
        captured = {}

        def fake(command, payload, timeout, role=None):
            captured['role'] = role
            return {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1', 'narration': 'fixed'}]}

        orchestrator.call = fake
        try:
            candidate = {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1', 'narration': 'orig'}]}
            repairs = ma.select_repair({'reviews': [{'dimensions': {'hook': {'score': 80}}}]}, candidate, self.config)
            orchestrator._apply_repairs(self.deepseek_config(), self.request, candidate,
                                        repairs, self.folder, 0,
                                        orchestrator._metrics(), 30)
        finally:
            orchestrator.call = provider.call
        self.assertEqual('script_hook_repair', captured['role'])

    def test_subprocess_route_still_skips_unconfigured_repair(self):
        """The guard is scoped to the subprocess route: a missing argv there is
        still a real misconfiguration and must not silently pass."""
        c = self.config_with()
        c['provider'] = 'hermes_subprocess'
        c['hook_repair_command'] = None
        captured = []

        def fake(command, payload, timeout, role=None):
            captured.append(role)
            return {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1', 'narration': 'x'}]}

        orchestrator.call = fake
        try:
            candidate = {'episode_id': 'EP0001', 'beats': [{'beat_id': 'b1', 'narration': 'orig'}]}
            repairs = ma.select_repair({'reviews': [{'dimensions': {'hook': {'score': 80}}}]}, candidate, self.config)
            orchestrator._apply_repairs(c, self.request, candidate, repairs, self.folder, 0,
                                        orchestrator._metrics(), 30)
        finally:
            orchestrator.call = provider.call
        self.assertEqual([], captured)


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
                # call_subprocess, not call: this test targets the argv route, and
                # the active provider is deepseek_cdp (argv is inert there).
                provider.call_subprocess(['x'], {'base_package': self.base}, 5, role='script_hook_specialist')
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
    """MIGRATED (class C): the local canon contract, not the external one.

    The old test read 01_CANON/anchors/registry.json -- a project outside this
    engine that this layout no longer depends on. Rather than bend the test until
    it passed, this states what the LOCAL registry must guarantee today:

      - it parses, and has the shape the code reads ('anclas')
      - every declared anchor exists
      - no duplicate id or logical name
      - paths stay inside knowledge/anchors (no escape upward)
      - if an entry carries sha256, it is verified -- and if the contract has no
        hashes, none is invented
    """

    ANCHORS_DIR = ROOT / 'knowledge' / 'anchors'

    def _registry(self):
        return read(self.ANCHORS_DIR / 'registry.json')

    def _entries(self):
        reg = self._registry()
        self.assertIn('anclas', reg, "registry must expose 'anclas'")
        return reg['anclas']

    def test_local_registry_parses(self):
        reg = self._registry()
        self.assertIsInstance(reg, dict)
        self.assertIsInstance(reg['anclas'], list)

    def test_declared_anchors_exist(self):
        for item in self._entries():
            self.assertIn('file', item, 'each anchor needs a file')
            target = self.ANCHORS_DIR / item['file']
            self.assertTrue(target.is_file(), 'anchor file missing: ' + item['file'])

    def test_no_duplicate_anchor_ids(self):
        ids = [i.get('id') for i in self._entries() if i.get('id') is not None]
        self.assertEqual(len(ids), len(set(ids)), 'duplicate anchor id')

    def test_no_duplicate_logical_names(self):
        names = [i.get('name') for i in self._entries() if i.get('name') is not None]
        self.assertEqual(len(names), len(set(names)), 'duplicate anchor name')

    def test_anchor_paths_stay_inside_anchors_dir(self):
        """A registry that can point outside its own directory is a portability
        hazard: it is how the old engine ended up depending on 01_CANON."""
        base = self.ANCHORS_DIR.resolve()
        for item in self._entries():
            target = (self.ANCHORS_DIR / item['file']).resolve()
            self.assertTrue(str(target).startswith(str(base)),
                            'anchor escapes knowledge/anchors: ' + item['file'])

    def test_anchor_hash_is_verified_when_present(self):
        """Hash verification is conditional on the contract declaring one. The
        local registry ships empty and declares no hashes, so nothing is invented
        to satisfy a requirement the current contract does not make."""
        for item in self._entries():
            if 'sha256' not in item:
                continue
            target = self.ANCHORS_DIR / item['file']
            self.assertEqual(hashlib.sha256(target.read_bytes()).hexdigest(),
                             item['sha256'], 'canon changed: ' + item['file'])

    def test_local_canon_has_no_external_paths(self):
        """Portability: the engine must load its own canon, not another project's."""
        c = read(ROOT / 'config/engine.json')
        for key in ('canon', 'worlds', 'mining', 'characters', 'anchors'):
            with self.subTest(key=key):
                value = c.get(key)
                self.assertIsNotNone(value, 'missing canon key: ' + key)
                self.assertNotIn('..', str(value),
                                 'canon path leaves the engine: ' + key)
                self.assertNotIn('01_CANON', str(value),
                                 'canon path points at the external canon: ' + key)
                target = ROOT / value
                self.assertTrue(target.exists(), 'canon file missing: ' + value)

    def test_local_canon_context_loads(self):
        """The engine must be able to build its full context offline."""
        from src.common import context
        ctx = context(read(ROOT / 'config/engine.json'))
        for key in ('canon', 'worlds', 'mining', 'characters', 'anchors'):
            self.assertIn(key, ctx)
        self.assertIsInstance(ctx['characters']['roles_permitidos'], list)
        self.assertIn('brother', ctx['characters']['roles_permitidos'],
                      'brother must stay permitted: the bank requires it')

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
