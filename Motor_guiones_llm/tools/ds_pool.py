"""Bounded pool of DeepSeek tabs, one owner at a time.

The rule this enforces: a tab has exactly one owner for the duration of a phase.
Five specialists running concurrently must not be able to reach each other's tab,
and a tab must not carry one role's conversation into the next role.

Session naming
    A caller reserves by LOGICAL NAME ("hook", "structure"), not by tab id.
    The pool maps name -> tab, so the caller never knows which physical tab it got.
    That is what makes tab reuse invisible and what makes contamination impossible:
    a different name can never land on a held tab.

Isolation
    reset_session() opens a FRESH chat on the tab. Reusing the tab's DOM while
    keeping the old conversation is how role N ends up answering with role N-1's
    context, so a fresh chat per role is the default, not an optimisation.

Concurrency
    Bounded by max_parallel_tabs, never by a global setting: stages that touch
    media, locks or paid APIs stay serial. This pool is only for free LLM calls.
"""
from __future__ import annotations

import threading
import urllib.parse

import tools.ds_session as ds_session
from tools.ds_session import _cdp


class PoolExhausted(RuntimeError):
    """More concurrent callers than tabs."""


class SessionHeld(RuntimeError):
    """A name already holds a tab."""


class DSPool:
    def __init__(self, ds):
        self.ds = ds or {}
        self.max_tabs = int(self.ds.get("max_parallel_tabs", 5))
        self._lock = threading.RLock()
        self._by_name = {}       # logical name -> DSSession
        self._idle = []          # DSSession ready for a new owner
        self._closed = []

    # ------------------------------------------------------------------ acquire
    def acquire(self, name, reuse_tab=False):
        """Reserve a tab for `name`. Raises if the name is already held."""
        with self._lock:
            if name in self._by_name:
                raise SessionHeld("SESSION_ALREADY_HELD:" + str(name))
            session = None
            if self._idle:
                session = self._idle.pop()
            elif len(self._closed) + len(self._by_name) + len(self._idle) < self.max_tabs:
                # resolve DSSession at CALL time, not import time, so a test can
                # substitute it and so a future session implementation is swappable
                session = ds_session.DSSession(self.ds, reuse_tab=reuse_tab)
            else:
                raise PoolExhausted(
                    "DS_POOL_EXHAUSTED:max=%d in_use=%d" % (
                        self.max_tabs, len(self._by_name)))
            session.reuse_tab = reuse_tab
            self._by_name[name] = session
            return session

    def release(self, name, close=False):
        with self._lock:
            session = self._by_name.pop(name, None)
            if session is None:
                return
            if close:
                try:
                    session.close()
                finally:
                    self._closed.append(session)
            else:
                self._idle.append(session)

    # ------------------------------------------------------------------ context
    def reset_session(self, name):
        """Give the owner's tab a FRESH chat.

        Navigating to the site root is what DeepSeek treats as a new conversation;
        it is cheaper and more reliable than clearing the DOM, which leaves the
        conversation id in the app state.
        """
        with self._lock:
            session = self._by_name.get(name)
            if session is None or session.tab is None:
                return False
            session.ev("window.location.href = %s" % _j(session.url))
            return True

    # ------------------------------------------------------------------ lifecycle
    def close_all(self):
        with self._lock:
            for session in list(self._by_name.values()) + self._idle + self._closed:
                try:
                    session.close()
                except Exception:
                    pass
            self._by_name.clear()
            self._idle.clear()
            self._closed.clear()

    def stats(self):
        with self._lock:
            return {"max": self.max_tabs, "in_use": len(self._by_name),
                    "idle": len(self._idle), "closed": len(self._closed),
                    "owners": dict.fromkeys(self._by_name, True)}


def _j(v):
    import json
    return json.dumps(v)


# ---------------------------------------------------------------- module pool
_POOL = None
_POOL_LOCK = threading.Lock()


def pool(ds):
    """Process-wide pool. One pool per config; a second pool would mean two owners
    racing for tabs it believes are its own."""
    global _POOL
    with _POOL_LOCK:
        if _POOL is None:
            _POOL = DSPool(ds)
        return _POOL


def reset_pool():
    global _POOL
    with _POOL_LOCK:
        if _POOL is not None:
            _POOL.close_all()
        _POOL = None