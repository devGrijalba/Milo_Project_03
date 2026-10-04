"""Wait for one DeepSeek reply on an open session, and return its text.

Completion is judged by ELEMENT, not by body-text substring: the stop button is the
signal. Waiting for the absence of a substring reads "still generating" forever when
the site changes its markup, and returns a half-streamed answer when it doesn't.

Secondary rule: require the text to be STABLE across N consecutive reads. DeepSeek's
first streamed chunk arrives in milliseconds; returning there yields half an answer
that looks like a complete one.
"""
from __future__ import annotations

import json
import time


def _last_assistant_text(session):
    sel = session.ds.get("assistant_selector",
                         "[class*=assistant],[data-message-author-role=assistant]")
    return session.ev("""(() => {
      const ns=[...document.querySelectorAll(%s)];
      const last=ns[ns.length-1];
      if(!last) return '';
      return (last.innerText||last.textContent||'').trim();
    })()""" % json.dumps(sel)) or ""


def extract_from_tab(session, prompt, ds=None):
    """Open (if needed), send prompt, wait for the reply, return its text.

    Raises TabUnavailable / ValueError on failure. Never returns partial text as if
    it were the whole answer: if the deadline passes with text, it is returned
    tagged by the caller deciding; here we raise instead so a truncated answer can
    never masquerade as a candidate.
    """
    ds = ds or session.ds or {}
    poll_s = float(ds.get("poll_s", 2.5))
    stable_reads = int(ds.get("stable_reads", 2))
    timeout_s = int(ds.get("response_timeout_s", 300))

    if session.tab is None:
        session.open()
    before = session.assistant_count()
    session.send(prompt)

    deadline = time.time() + timeout_s
    last, stable = "", 0
    while time.time() < deadline:
        count = session.assistant_count()
        if count > before:
            txt = _last_assistant_text(session)
            if txt and txt == last:
                stable += 1
                if stable >= stable_reads:
                    return txt
            else:
                stable = 0
                if txt:
                    last = txt
        time.sleep(poll_s)

    if last:
        # text arrived but never stabilised: report it, but do not pass it off as done
        raise TimeoutError("DEEPSEEK_REPLY_UNSTABLE:" + str(len(last)) + "_chars")
    raise TimeoutError("DEEPSEEK_NO_REPLY_WITHIN:" + str(timeout_s) + "s")