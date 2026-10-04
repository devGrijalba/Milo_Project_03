#!/usr/bin/env python3
"""Unit tests for the DeepSeek tab pool. No browser.

The guarantee under test: a tab has exactly one owner at a time, and a different
logical name can never land on a held tab. That is what keeps five concurrent
specialists from reading each other's conversation.
"""
import pathlib
import sys
import threading
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import tools.ds_session as ds_session
from tools.ds_pool import DSPool, PoolExhausted, SessionHeld

DS = {"cdp": "http://127.0.0.1:9222", "url": "https://chat.deepseek.com/",
      "max_parallel_tabs": 3, "selector": "textarea.ds-scroll-area"}


class FakeSession:
    made = 0
    open_tabs = 0
    closed_tabs = 0

    def __init__(self, ds=None, reuse_tab=False):
        FakeSession.made += 1
        self.ds = ds or {}
        self.reuse_tab = reuse_tab
        self.url = self.ds.get("url", "https://chat.deepseek.com/")
        self.tab = None
        self.closed = False
        self.navigated = []

    def open(self):
        FakeSession.open_tabs += 1
        self.tab = {"id": "t%d" % FakeSession.made}
        return self.tab

    def close(self):
        self.closed = True
        FakeSession.closed_tabs += 1

    def ev(self, expr):
        self.navigated.append(expr)
        return True


class TestOwnership(unittest.TestCase):
    def setUp(self):
        FakeSession.made = 0
        FakeSession.open_tabs = 0
        FakeSession.closed_tabs = 0
        ds_session.DSSession = FakeSession
        self.pool = DSPool(DS)

    def test_acquire_reserves_by_name(self):
        s = self.pool.acquire("hook")
        self.assertIsNotNone(s)
        self.assertEqual(["hook"], list(self.pool.stats()["owners"]))

    def test_same_name_twice_is_refused(self):
        self.pool.acquire("hook")
        with self.assertRaises(SessionHeld):
            self.pool.acquire("hook")

    def test_different_name_gets_different_tab(self):
        a = self.pool.acquire("hook")
        b = self.pool.acquire("structure")
        self.assertIsNot(a, b)

    def test_release_frees_the_name(self):
        self.pool.acquire("hook")
        self.pool.release("hook")
        self.pool.acquire("hook")          # must not raise SessionHeld

    def test_release_of_unknown_name_is_a_noop(self):
        self.pool.release("never-held")     # must not raise

    def test_in_use_tracks_acquires(self):
        self.pool.acquire("a")
        self.pool.acquire("b")
        self.assertEqual(2, self.pool.stats()["in_use"])


class TestBounds(unittest.TestCase):
    def setUp(self):
        FakeSession.made = 0
        ds_session.DSSession = FakeSession
        self.pool = DSPool(DS)

    def test_exhausts_at_max(self):
        for i in range(3):
            self.pool.acquire("r%d" % i)
        self.assertEqual(3, self.pool.stats()["in_use"])

    def test_fourth_acquire_raises_exhausted(self):
        for i in range(3):
            self.pool.acquire("r%d" % i)
        with self.assertRaises(PoolExhausted) as cm:
            self.pool.acquire("r3")
        self.assertIn("DS_POOL_EXHAUSTED", str(cm.exception))

    def test_released_tabs_are_reused_not_recreated(self):
        a = self.pool.acquire("a")
        self.pool.release("a")
        b = self.pool.acquire("b")
        self.assertIs(a, b)                 # same physical tab, new owner

    def test_five_specialists_fit_in_five_tabs(self):
        big = DSPool({"max_parallel_tabs": 5})
        for i, role in enumerate(["hook", "structure", "milo", "novelty", "ending"]):
            big.acquire(role)
        self.assertEqual(5, big.stats()["in_use"])

    def test_default_max_is_five(self):
        self.assertEqual(5, DSPool({}).max_tabs)


class TestIsolation(unittest.TestCase):
    def setUp(self):
        FakeSession.made = 0
        ds_session.DSSession = FakeSession
        self.pool = DSPool(DS)

    def test_reset_navigates_to_root(self):
        s = self.pool.acquire("hook")
        s.open()
        self.assertTrue(self.pool.reset_session("hook"))
        self.assertTrue(any("chat.deepseek.com" in e for e in s.navigated))
        self.assertTrue(any(e.startswith("window.location.href") for e in s.navigated))

    def test_reset_unknown_owner_is_false_not_error(self):
        self.assertFalse(self.pool.reset_session("nobody"))

    def test_reset_requires_an_open_tab(self):
        self.pool.acquire("hook")          # never opened
        self.assertFalse(self.pool.reset_session("hook"))


class TestConcurrency(unittest.TestCase):
    def setUp(self):
        FakeSession.made = 0
        ds_session.DSSession = FakeSession

    def test_five_threads_get_five_distinct_tabs(self):
        pool = DSPool({"max_parallel_tabs": 5})
        got, errors = [], []

        def work(i):
            try:
                got.append(pool.acquire("role%d" % i))
            except Exception as e:       # noqa: BLE001
                errors.append(e)

        threads = [threading.Thread(target=work, args=(i,)) for i in range(5)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual([], errors)
        self.assertEqual(5, len(got))
        self.assertEqual(5, len({id(s) for s in got}), "tabs must be distinct")

    def test_duplicate_name_under_threads_has_one_winner(self):
        pool = DSPool({"max_parallel_tabs": 5})
        ok, refused = [], []

        def work():
            try:
                ok.append(pool.acquire("same"))
            except SessionHeld:
                refused.append(1)

        threads = [threading.Thread(target=work) for _ in range(5)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        self.assertEqual(1, len(ok))
        self.assertEqual(4, len(refused))


class TestLifecycle(unittest.TestCase):
    def setUp(self):
        FakeSession.made = 0
        FakeSession.closed_tabs = 0
        ds_session.DSSession = FakeSession

    def _acquire_opened(self, pool, name):
        """acquire() reserves lazily: the tab is created but not opened until the
        caller uses it. A session that was never opened has no browser tab to
        close, so closing it is legitimately a no-op."""
        s = pool.acquire(name)
        s.open()
        return s

    def test_close_all_closes_everything(self):
        pool = DSPool(DS)
        self._acquire_opened(pool, "a")
        self._acquire_opened(pool, "b")
        pool.close_all()
        self.assertEqual(2, FakeSession.closed_tabs)
        self.assertEqual(0, pool.stats()["in_use"])

    def test_release_close_disposes_the_tab(self):
        pool = DSPool(DS)
        self._acquire_opened(pool, "a")
        pool.release("a", close=True)
        self.assertEqual(1, FakeSession.closed_tabs)

    def test_release_without_close_keeps_tab_alive(self):
        pool = DSPool(DS)
        self._acquire_opened(pool, "a")
        pool.release("a")
        self.assertEqual(0, FakeSession.closed_tabs)


if __name__ == "__main__":
    unittest.main(verbosity=2)