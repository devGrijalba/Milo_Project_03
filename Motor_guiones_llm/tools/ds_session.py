"""ONE DeepSeek tab: open, reuse, send, wait, close.

Owns exactly one tab and one websocket. Knows nothing about pooling or
parallelism -- that is tools/ds_pool.py's job. Knows nothing about JSON -- that
is src/ds_provider.py's job.

Fresh chat per call is the default: a specialist must never inherit another
role's conversation, or the "self-contained payload" rule in multiagent.py stops
being true. Set reuse_tab=True only for roles that need history (critic, repair).
"""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request


class TabUnavailable(RuntimeError):
    """The browser refused the tab or the composer never appeared."""


def _cdp(cdp, path, method="GET"):
    req = urllib.request.Request(cdp.rstrip("/") + path, method=method)
    return json.load(urllib.request.urlopen(req, timeout=20))


class DSSession:
    """One tab, one websocket, one conversation."""

    def __init__(self, ds, reuse_tab=False):
        self.ds = ds or {}
        self.cdp = self.ds.get("cdp", "http://127.0.0.1:9222")
        self.url = self.ds.get("url", "https://chat.deepseek.com/")
        self.selector = self.ds.get("selector", "textarea.ds-scroll-area")
        self.poll_s = float(self.ds.get("poll_s", 2.5))
        self.stable_reads = int(self.ds.get("stable_reads", 2))
        self.timeout_s = int(self.ds.get("response_timeout_s", 300))
        self.read_back_required = bool(self.ds.get("read_back_required", True))
        self.reuse_tab = reuse_tab
        self.tab = None
        self.ws = None
        self._id = 0

    # ------------------------------------------------------------ lifecycle
    def open(self):
        if self.reuse_tab:
            found = self._find_existing()
            if found:
                self.tab = found
                self._connect(found)
                return self.tab
        self.tab = _cdp(self.cdp, "/json/new?" + urllib.parse.quote(self.url, safe=""), "PUT")
        self._connect(self.tab)
        self._await_ready()
        return self.tab

    def close(self):
        if self.ws is not None:
            try:
                self.ws.close()
            except Exception:
                pass
            self.ws = None
        # close the tab too when we opened it, so a 5-role run does not
        # accumulate tabs that outlive their call
        if self.tab and not self.reuse_tab:
            try:
                _cdp(self.cdp, "/json/close/" + self.tab["id"])
            except Exception:
                pass
        self.tab = None

    def _find_existing(self):
        try:
            tabs = _cdp(self.cdp, "/json/list")
        except Exception:
            return None
        host = urllib.parse.urlparse(self.url).netloc
        for t in tabs:
            if t.get("type") == "page" and host in t.get("url", ""):
                return t
        return None

    def _connect(self, tab):
        import websocket  # imported here so unit tests need not have it
        self.ws = websocket.create_connection(tab["webSocketDebuggerUrl"], timeout=40)

    # ------------------------------------------------------------ eval
    def ev(self, expr):
        if self.ws is None:
            raise TabUnavailable("session not open")
        self._id += 1
        self.ws.send(json.dumps({
            "id": self._id, "method": "Runtime.evaluate",
            "params": {"expression": expr, "returnByValue": True},
        }))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") != self._id:
                continue
            res = msg.get("result", {})
            if "exceptionDetails" in res:
                d = res["exceptionDetails"]
                raise TabUnavailable(str(
                    d.get("exception", {}).get("description") or d.get("text"))[:200])
            return res.get("result", {}).get("value")

    def _await_ready(self, limit_s=60):
        deadline = time.time() + limit_s
        while time.time() < deadline:
            try:
                if self.ev("document.readyState") == "complete" and self.ev(
                        "!!document.querySelector(%s)" % json.dumps(self.selector)):
                    return True
            except Exception:
                pass
            time.sleep(1.5)
        raise TabUnavailable("DEEPSEEK_COMPOSER_NOT_READY")

    # ------------------------------------------------------------ send
    def send(self, text):
        js = ("(() => {const el=document.querySelector(%s);if(!el)return 'NO_EL';"
              "el.focus();const s=Object.getOwnPropertyDescriptor("
              "Object.getPrototypeOf(el),'value').set;s.call(el,%s);"
              "el.dispatchEvent(new Event('input',{bubbles:true}));return 'WROTE';})()"
              % (json.dumps(self.selector), json.dumps(text)))
        if self.ev(js) != "WROTE":
            raise TabUnavailable("DEEPSEEK_WRITE_FAILED")
        time.sleep(0.8)
        if self.read_back_required:
            back = self.ev("document.querySelector(%s).value" % json.dumps(self.selector))
            if (back or "").strip() != text.strip():
                raise ValueError("DEEPSEEK_READBACK_MISMATCH")
        self._press_enter()

    def _press_enter(self):
        base = {"key": "Enter", "code": "Enter", "text": "\r",
                "windowsVirtualKeyCode": 13, "nativeVirtualKeyCode": 13}
        for kind in ("keyDown", "keyUp"):
            self.ws.send(json.dumps({"id": 0, "method": "Input.dispatchKeyEvent",
                                     "params": {**base, "type": kind}}))

    def assistant_count(self):
        sel = self.ds.get("assistant_selector",
                          "[class*=assistant],[data-message-author-role=assistant]")
        return self.ev("document.querySelectorAll(%s).length" % json.dumps(sel))