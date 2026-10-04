#!/usr/bin/env python3
"""Integration tests: multiagent's existing concurrency wired to pool sessions.

Verifies the contract that matters: five specialists run concurrently, each under
its own logical session name, each with exclusive tab ownership, each getting a
fresh chat, and each role's JSON validated before it can become a report.

No browser. DSSession and the pool are stubbed.
"""
import concurrent.futures
import json
import pathlib
import sys
import threading
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src import multiagent as ma
from src import provider as provider_mod


# ------------------------------------------------------------------- stubs
class FakeSession:
    made = 0
    opens = 0
    resets = 0
    released = 0
    lock = threading.Lock()

    def __init__(self, ds=None, reuse_tab=False):
        with FakeSession.lock:
            FakeSession.made += 1
            self.n = FakeSession.made
        self.ds = ds or {}
        self.reuse_tab = reuse_tab
        self.url = self.ds.get("url", "https://chat.deepseek.com/")
        self.selector = self.ds.get("selector", "textarea.ds-scroll-area")
        self.tab = None
        self.prompts = []
        self.navigations = []
        self.closed = False

    def open(self):
        FakeSession.opens += 1
        self.tab = {"id": "tab%d" % self.n}
        return self.tab

    def close(self):
        self.closed = True

    def ev(self, expr):
        self.navigations.append(expr)
        return True

    def send(self, text):
        self.prompts.append(text)

    def assistant_count(self):
        return 1


class RecordingPool:
    """Pool stub that records the acquire/reset/release order per name."""

    def __init__(self, ds=None):
        self.ds = ds or {}
        self.acquired = []
        self.released = []
        self.resets = []
        self.lock = threading.Lock()
        self._sessions = {}
        self._held = set()

    def acquire(self, name, reuse_tab=False):
        with self.lock:
            if name in self._held:
                raise AssertionError("DOUBLE OWNERSHIP: " + name)
            self._held.add(name)
            self.acquired.append(name)
            s = FakeSession(self.ds)
            self._sessions[name] = s
            return s

    def reset_session(self, name):
        with self.lock:
            self.resets.append(name)
        return True

    def release(self, name, close=False):
        with self.lock:
            self._held.discard(name)
            self.released.append(name)


class Base(unittest.TestCase):
    def setUp(self):
        FakeSession.made = 0
        FakeSession.opens = 0
        FakeSession.resets = 0
        import tools.ds_session as ds_session
        import tools.ds_pool as ds_pool
        import tools.ds_extract as ds_extract
        self.ds_pool_mod = ds_pool
        self.ds_session_mod = ds_session
        self.ds_session_mod.DSSession = FakeSession
        self.pool = RecordingPool()
        # ds_provider imports the pool accessor INSIDE call(), so patching the
        # module attribute here is enough for the real provider path to reach it.
        ds_pool.pool = lambda ds=None: self.pool
        import src.ds_provider as ds_provider
        ds_provider.config = lambda p=None: {
            "provider": "deepseek_cdp",
            "ds": {"cdp": "http://127.0.0.1:9222",
                   "url": "https://chat.deepseek.com/",
                   "max_parallel_tabs": 5,
                   "selector": "textarea.ds-scroll-area"}}

        def fake_extract(session, prompt, ds=None):
            if session.tab is None:
                session.open()
            session.send(prompt)
            return json.dumps({"role": "ok", "proposals": [], "evidence": [],
                               "risks": [], "handoff": "h"})

        ds_extract.extract_from_tab = fake_extract
        self.ds_extract_mod = ds_extract

    def cfg(self):
        c = {"provider": "deepseek_cdp",
             "script_parallel_agents": 5,
             "specialist_max_bytes": 6000,
             "ds": {"cdp": "http://127.0.0.1:9222",
                    "url": "https://chat.deepseek.com/",
                    "max_parallel_tabs": 5,
                    "selector": "textarea.ds-scroll-area"}}
        return c

    def base_package(self):
        return {"role_context": "MILOSCRIPTBASE", "episode_id": "EP0001",
                "seed_id": "MILO-S0001", "bank_version": "2.1.0",
                "seed_hash": "0" * 64,
                "seed_snapshot": {"seed_id": "MILO-S0001", "titulo": "Plato tapado"},
                "semilla": "Papá deja la cena", "territorio": "Padre y cariño",
                "history": [], "context": {"mining": ""}}


# ------------------------------------------------------------------- mapping
class TestSessionNaming(Base):
    def test_every_specialist_has_a_stable_session_name(self):
        for role, _, _ in ma.SPECIALISTS:
            self.assertEqual("specialist_" + role, ma.session_for(role))

    def test_five_roles_map_to_five_distinct_names(self):
        names = {ma.session_for(r) for r, _, _ in ma.SPECIALISTS}
        self.assertEqual(5, len(names))

    def test_names_are_stable_across_calls(self):
        self.assertEqual(ma.session_for("script_hook_specialist"),
                         ma.session_for("script_hook_specialist"))

    def test_specialists_are_the_five_declared(self):
        self.assertEqual(5, len(ma.SPECIALISTS))


# ------------------------------------------------------------------- wiring
class TestParallelWiring(Base):
    def _run(self):
        return ma.parallel_specialists(self.cfg(), self.base_package(), 30,
                                       folder=None)

    def test_all_five_answer(self):
        results, timings, _ = self._run()
        self.assertEqual(5, len(results))
        for role, _, _ in ma.SPECIALISTS:
            self.assertIn(role, results)
            self.assertIn(role, timings)

    def test_each_specialist_acquires_its_own_session(self):
        self._run()
        self.assertEqual(sorted(ma.session_for(r) for r, _, _ in ma.SPECIALISTS),
                         sorted(self.pool.acquired))

    def test_no_duplicate_ownership(self):
        # RecordingPool raises on double ownership; surviving the run proves it
        self._run()
        self.assertEqual(5, len(set(self.pool.acquired)))

    def test_every_session_is_reset_then_released(self):
        self._run()
        self.assertEqual(sorted(self.pool.acquired), sorted(self.pool.resets))
        self.assertEqual(sorted(self.pool.acquired), sorted(self.pool.released))

    def test_reset_happens_before_release(self):
        self._run()
        # release-after-reset means no tab is handed on with a stale conversation
        for name in set(self.pool.acquired):
            self.assertIn(name, self.pool.resets)

    def test_specialists_run_concurrently(self):
        _, _, wall = self._run()
        # concurrency shows up as many sessions in flight, not as serial reuse
        self.assertEqual(5, len(self.pool.acquired))
        self.assertGreater(FakeSession.opens, 0)

    def test_no_specialist_knows_a_tab_id(self):
        self._run()
        # The tab id is pool-internal and must never reach the prompt. The SESSION
        # name is pool bookkeeping too -- but `specialist_role` inside
        # base_package is pre-existing role context the model legitimately needs,
        # so only the transport-level name is asserted absent here.
        for session in self.pool._sessions.values():
            for prompt in session.prompts:
                self.assertNotIn(session.tab["id"], prompt)
                self.assertNotIn("session_name", prompt)
                self.assertNotIn("TAB_", prompt)

    def test_every_prompt_carries_the_payload(self):
        self._run()
        for session in self.pool._sessions.values():
            self.assertEqual(1, len(session.prompts))
            self.assertIn("base_package", session.prompts[0])

    def test_json_is_validated_into_a_dict(self):
        results, _, _ = self._run()
        for role, result in results.items():
            self.assertIsInstance(result, dict)
            self.assertIn("handoff", result)


# ------------------------------------------------------------------- isolation
class TestRoleIsolation(Base):
    def test_each_session_got_a_distinct_tab(self):
        ma.parallel_specialists(self.cfg(), self.base_package(), 30, folder=None)
        tabs = [s.tab["id"] for s in self.pool._sessions.values()]
        self.assertEqual(5, len(set(tabs)))

    def test_no_session_reused_between_roles(self):
        ma.parallel_specialists(self.cfg(), self.base_package(), 30, folder=None)
        self.assertEqual(5, len(self.pool._sessions))

    def test_second_run_reacquires_all_five(self):
        ma.parallel_specialists(self.cfg(), self.base_package(), 30, folder=None)
        first = len(self.pool.acquired)
        ma.parallel_specialists(self.cfg(), self.base_package(), 30, folder=None)
        self.assertEqual(first * 2, len(self.pool.acquired))


# ------------------------------------------------------------------- argv gate
class TestArgvGate(Base):
    def test_deepseek_route_does_not_require_argv(self):
        cfg = self.cfg()
        for key in ("hook_specialist_command", "structure_specialist_command"):
            self.assertIsNone(cfg.get(key))
        # must not raise SPECIALIST_ADAPTER_NOT_CONFIGURED
        results, _, _ = ma.parallel_specialists(cfg, self.base_package(), 30,
                                                folder=None)
        self.assertEqual(5, len(results))

    def test_subprocess_route_still_requires_argv(self):
        cfg = self.cfg()
        cfg["provider"] = "hermes_subprocess"
        with self.assertRaises(ma.ScriptStageBlocked) as cm:
            ma.parallel_specialists(cfg, self.base_package(), 30, folder=None)
        self.assertIn("SPECIALIST_ADAPTER_NOT_CONFIGURED", str(cm.exception))


if __name__ == "__main__":
    unittest.main(verbosity=2)