#!/usr/bin/env python3
"""Unit tests for the DeepSeek provider.

NO BROWSER IS OPENED. tools.ds_session.DSSession is stubbed, so these tests
exercise prompt construction, payload guards, JSON extraction, timeouts and
failure handling in milliseconds and without a CDP dependency.

DeepSeek real is a separate, later gate.
"""
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src import ds_provider
from src.ds_provider import build_prompt, extract_json, validate_payload


# --------------------------------------------------------------------- stubs
class FakeSession:
    """Stands in for DSSession. Records what it was asked to send."""

    instances = []

    def __init__(self, ds=None, reuse_tab=False):
        self.ds = ds or {}
        self.url = self.ds.get("url", "https://chat.deepseek.com/")
        self.tab = None
        self.sent = None
        self.closed = False
        self.navigations = []
        self.open_calls = 0
        self.reply = FakeSession.next_reply
        self.raise_on_send = FakeSession.raise_on_send
        FakeSession.instances.append(self)

    next_reply = '{"ok": true}'
    raise_on_send = None

    def open(self):
        self.open_calls += 1
        self.tab = {"id": "fake"}
        return self.tab

    def close(self):
        self.closed = True

    def ev(self, expr):
        # the pool calls ev() to navigate a tab to a fresh chat
        self.navigations.append(expr)
        return True

    def send(self, prompt):
        if FakeSession.raise_on_send:
            raise FakeSession.raise_on_send
        self.sent = prompt


class NullPool:
    """No-op pool: acquire/release are pure bookkeeping.

    These provider tests are about the CALL contract, not about tab ownership.
    A real pool across tests would leak state (a held name refuses the next
    acquire), which is why the pool is stubbed here and tested in test_ds_pool.
    """

    def __init__(self, ds=None):
        self.ds = ds or {}
        self.acquired = []
        self.released = []
        self.resets = []

    def acquire(self, name, reuse_tab=False):
        self.acquired.append(name)
        return FakeSession(self.ds)

    def reset_session(self, name):
        self.resets.append(name)
        return True

    def release(self, name, close=False):
        self.released.append(name)


_LAST_POOL = [None]


def _last_pool():
    return _LAST_POOL[0]


def install_stub():
    import tools.ds_session as ds_session
    import tools.ds_extract as ds_extract
    import tools.ds_pool as ds_pool

    # The stub mirrors the real flow: open -> send -> wait. Modelling it as a bare
    # lambda would skip send() and hide transport failures from the tests.
    def fake_extract(session, prompt, ds=None):
        if session.tab is None:
            session.open()
        session.send(prompt)
        return session.reply

    ds_session.DSSession = FakeSession
    ds_extract.extract_from_tab = fake_extract
    def _new_pool(ds=None):
        p = NullPool(ds)
        _LAST_POOL[0] = p
        return p
    ds_pool.pool = _new_pool
    return ds_session, ds_extract


class Base(unittest.TestCase):
    def setUp(self):
        FakeSession.instances = []
        FakeSession.next_reply = '{"ok": true}'
        FakeSession.raise_on_send = None
        self.ds_mod, self.ex_mod = install_stub()
        self._orig_config = ds_provider.config
        ds_provider.config = lambda p=None: {
            "ds": {"cdp": "http://127.0.0.1:9222", "selector": "textarea.ds-scroll-area",
                   "response_timeout_s": 30, "stable_reads": 2, "poll_s": 0.1}}

    def tearDown(self):
        ds_provider.config = self._orig_config


# ------------------------------------------------------------ payload guards
class TestValidatePayload(Base):
    def test_rejects_non_object(self):
        self.assertTrue(validate_payload("script_hook_specialist", ["nope"]))

    def test_specialist_requires_base_package(self):
        self.assertIn("base_package", validate_payload("script_hook_specialist", {}))

    def test_specialist_accepts_base_package(self):
        self.assertEqual([], validate_payload("script_hook_specialist",
                                              {"base_package": {"x": 1}}))

    def test_synthesizer_requires_five_reports(self):
        payload = {"base_package": {"x": 1},
                   "specialist_reports": {"a": {}, "b": {}, "c": {}, "d": {}}}
        self.assertIn("five_specialist_reports",
                      validate_payload("script_synthesizer", payload))

    def test_synthesizer_five_reports_passes(self):
        payload = {"base_package": {"x": 1},
                   "specialist_reports": {k: {"r": 1} for k in "abcde"}}
        self.assertEqual([], validate_payload("script_synthesizer", payload))

    def test_critic_requires_candidate_and_hash(self):
        self.assertIn("candidate", validate_payload("script_critic", {}))

    def test_critic_empty_candidate_is_still_present(self):
        # presence, not truthiness: an empty candidate must reach the validator
        errs = validate_payload("script_critic", {"candidate": {}, "candidate_hash": "h"})
        self.assertEqual([], errs)


# ------------------------------------------------------------ prompt build
class TestBuildPrompt(Base):
    def test_contains_instructions_and_payload(self):
        p = build_prompt("script_hook_specialist", {"seed": "S1"}, "HOLA INSTRUCCIONES")
        self.assertIn("HOLA INSTRUCCIONES", p)
        self.assertIn('"seed": "S1"', p)

    def test_demands_json_only(self):
        p = build_prompt("script_hook_specialist", {"a": 1}, "X")
        self.assertIn("EXCLUSIVAMENTE", p)

    def test_payload_is_last_so_reply_ends_with_it(self):
        p = build_prompt("script_hook_specialist", {"a": 1}, "X")
        self.assertTrue(p.rstrip().endswith("```"))

    def test_accented_values_survive(self):
        p = build_prompt("script_hook_specialist", {"titulo": "Plato tapado"}, "X")
        self.assertIn("Plato tapado", p)

    def test_payload_does_not_break_on_braces_in_values(self):
        p = build_prompt("x", {"motivo": "{no es json}"}, "X")
        self.assertIn("{no es json}", p)


# ------------------------------------------------------------ json extract
class TestExtractJson(Base):
    def test_plain_object(self):
        self.assertEqual({"a": 1}, extract_json('{"a": 1}'))

    def test_fenced(self):
        self.assertEqual({"a": 1}, extract_json('```json\n{"a": 1}\n```'))

    def test_fenced_no_lang(self):
        self.assertEqual({"a": 1}, extract_json('```\n{"a": 1}\n```'))

    def test_prose_around(self):
        txt = 'Aqui tienes:\n```json\n{"titulo": "Plato tapado"}\n```\nEspero sirva.'
        self.assertEqual({"titulo": "Plato tapado"}, extract_json(txt))

    def test_bare_with_prose_no_fence(self):
        self.assertEqual({"a": 2}, extract_json('Listo {"a": 2}fin'))

    def test_nested_object(self):
        self.assertEqual({"a": {"b": [1, 2]}}, extract_json('{"a": {"b": [1, 2]}}'))

    def test_braces_inside_strings_do_not_break_balance(self):
        self.assertEqual({"motivo": "{a}"}, extract_json('{"motivo": "{a}"}'))

    def test_escaped_quote_inside_string(self):
        self.assertEqual({"q": 'say "hi"'}, extract_json('{"q": "say \\"hi\\""}'))

    def test_returns_none_on_prose_only(self):
        self.assertIsNone(extract_json("Lo siento, no puedo."))

    def test_returns_none_on_truncated_json(self):
        self.assertIsNone(extract_json('{"a": 1, "b": '))

    def test_returns_none_on_empty(self):
        self.assertIsNone(extract_json(""))

    def test_returns_none_on_array_not_object(self):
        # a top-level array is not the contract shape
        self.assertIsNone(extract_json('[1, 2, 3]'))

    def test_never_returns_partial_dict(self):
        out = extract_json('{"a": 1')
        self.assertIsNone(out)


# ------------------------------------------------------------ the call seam
class TestCall(Base):
    def test_returns_parsed_json(self):
        FakeSession.next_reply = '{"ok": true}'
        out = ds_provider.call(None, {"base_package": {"x": 1}}, 30,
                               role="script_hook_specialist")
        self.assertTrue(out["ok"])

    def test_pool_session_is_reset_and_released_on_success(self):
        # With a pooled session the tab is NOT closed: it is reset to a fresh
        # chat and released back to the pool for the next owner.
        ds_provider.call(None, {"base_package": {"seed_id": "MILO-S0001"}}, 30,
                         role="script_hook_specialist")
        self.assertEqual(["specialist_script_hook_specialist"], _last_pool().released)
        self.assertEqual(["specialist_script_hook_specialist"], _last_pool().resets)

    def test_unpooled_session_is_closed(self):
        # no role -> no pool owner -> the session must be closed outright
        ds_provider.call(None, {"base_package": {"x": 1}}, 30, role=None)
        self.assertTrue(any(s.closed for s in FakeSession.instances))

    def test_blocked_payload_never_opens_a_tab(self):
        with self.assertRaises(ValueError) as cm:
            ds_provider.call(None, {}, 30, role="script_hook_specialist")
        self.assertIn("HERMES_TASK_BLOCKED", str(cm.exception))
        self.assertEqual([], FakeSession.instances)   # nothing was spent

    def test_no_json_in_reply_raises_not_partial(self):
        FakeSession.next_reply = "No puedo hacer eso."
        with self.assertRaises(ValueError) as cm:
            ds_provider.call(None, {"base_package": {"seed_id": "MILO-S0001"}}, 30, role="script_hook_specialist")
        self.assertIn("DEEPSEEK_NO_JSON_IN_REPLY", str(cm.exception))

    def test_worker_block_propagates_as_error(self):
        FakeSession.next_reply = json.dumps(
            {"status": "HERMES_TASK_BLOCKED", "reason": "sin contexto"})
        with self.assertRaises(ValueError) as cm:
            ds_provider.call(None, {"base_package": {"seed_id": "MILO-S0001"}}, 30, role="script_hook_specialist")
        self.assertIn("HERMES_TASK_BLOCKED", str(cm.exception))

    def test_empty_reply_raises(self):
        FakeSession.next_reply = ""
        with self.assertRaises(ValueError) as cm:
            ds_provider.call(None, {"base_package": {"seed_id": "MILO-S0001"}}, 30, role="script_hook_specialist")
        self.assertIn("DEEPSEEK_EMPTY_REPLY", str(cm.exception))

    def test_pool_released_even_when_transport_fails(self):
        # A transport failure must still hand the tab back, or one dead tab
        # would starve the pool for the rest of the run.
        FakeSession.raise_on_send = RuntimeError("tab died")
        with self.assertRaises(RuntimeError):
            ds_provider.call(None, {"base_package": {"seed_id": "MILO-S0001"}}, 30,
                             role="script_hook_specialist")
        self.assertEqual(["specialist_script_hook_specialist"], _last_pool().released)

    def test_command_argument_is_ignored(self):
        # interface parity: an argv is accepted and ignored, not executed
        FakeSession.next_reply = '{"ok": 1}'
        out = ds_provider.call(["definitely", "not", "executed"], {"base_package": {"seed_id": "MILO-S0001"}},
                               30, role="script_hook_specialist")
        self.assertEqual(1, out["ok"])


if __name__ == "__main__":
    unittest.main(verbosity=2)