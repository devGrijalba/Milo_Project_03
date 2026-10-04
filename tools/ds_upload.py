#!/usr/bin/env python
"""Attach a file to DeepSeek via CDP and talk to it about the file.

    python tools/ds_upload.py --file test_seeds.json --prompt ask.txt
    python tools/ds_upload.py --file data/seeds.json --probe-only
    python tools/ds_upload.py --file x.json --prompt p.txt --out reply.txt

Why this is separate from ds_inject.py: ds_inject writes TEXT into the composer.
A 1.9 MB JSON cannot go through the composer at all -- it has to be attached as a
real file so DeepSeek indexes it. Different transport, different module.

Read-back discipline carries over: after attach we confirm the visible chip
names the file we meant to attach. A silent wrong-file upload is worse than a
visible failure, because the model's confident answer would then be about the
wrong data.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

try:
    import websocket
except ImportError:
    sys.exit("FALTA websocket-client -> pip install websocket-client")

DEFAULT_CDP = "http://127.0.0.1:9222"
DEFAULT_URL = "https://chat.deepseek.com/"

JS_ASSIST_N = ("document.querySelectorAll('[class*=assistant], "
               "[data-message-author-role=assistant]').length")
JS_ASSIST_LAST = """(() => {
  const ns = [...document.querySelectorAll('[class*=assistant], [data-message-author-role=assistant]')];
  const last = ns[ns.length - 1];
  if (!last) return '';
  return (last.innerText || last.textContent || '').trim();
})()"""


class Tab:
    def __init__(self, ws_url, timeout=40):
        # suppress_origin: Chrome's CDP rejects a websocket whose Origin is the
        # devtools endpoint unless --remote-allow-origins was passed. Suppressing
        # the header makes the client independent of how Chrome was launched,
        # instead of requiring a specific flag at every relaunch.
        self.ws = websocket.create_connection(ws_url, timeout=timeout,
                                              suppress_origin=True)
        self._id = 0

    def cmd(self, method, params=None):
        self._id += 1
        self.ws.send(json.dumps({"id": self._id, "method": method,
                                 "params": params or {}}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") != self._id:
                continue
            if "error" in msg:
                raise RuntimeError("%s: %s" % (method, msg["error"]))
            return msg.get("result", {})

    def ev(self, expr):
        # cmd() already unwrapped msg["result"], which for Runtime.evaluate is
        # {"result": {...}} -- so the value object sits one level below that.
        # Unwrapping twice is what made every probe read None while the page was
        # in fact healthy.
        res = self.cmd("Runtime.evaluate",
                       {"expression": expr, "returnByValue": True})
        if "exceptionDetails" in res:
            d = res["exceptionDetails"]
            raise RuntimeError(str(d.get("exception", {}).get("description")
                                   or d.get("text"))[:300])
        return res.get("result", {}).get("value")

    def enter(self):
        base = {"key": "Enter", "code": "Enter", "text": "\r",
                "windowsVirtualKeyCode": 13, "nativeVirtualKeyCode": 13}
        for kind in ("keyDown", "keyUp"):
            self.ws.send(json.dumps({"id": 0, "method": "Input.dispatchKeyEvent",
                                     "params": {**base, "type": kind}}))

    def close(self):
        try:
            self.ws.close()
        except Exception:
            pass


def find_tab(cdp, url):
    host = urllib.parse.urlparse(url).netloc
    try:
        tabs = json.load(urllib.request.urlopen(cdp + "/json/list", timeout=8))
    except Exception:
        tabs = []
    for t in tabs:
        if t.get("type") == "page" and host in t.get("url", ""):
            return t, False
    req = urllib.request.Request(
        cdp + "/json/new?" + urllib.parse.quote(url, safe=""), method="PUT")
    return json.load(urllib.request.urlopen(req, timeout=15)), True


def wait_ready(tab, limit_s=120):
    """Wait for a logged-in chat composer.

    The file input is intentionally display:none -- a hidden native input driven
    by the attach button, not something the user ever sees. Requiring it to be
    VISIBLE made this gate fail on a perfectly healthy page, so readiness is
    judged on the composer plus the absence of a login wall, which is what
    actually determines whether a message can be sent.
    """
    deadline = time.time() + limit_s
    while time.time() < deadline:
        try:
            if tab.ev("!!document.querySelector('input[type=password]')"):
                raise SystemExit("LOGIN_WALL: inicia sesion manualmente")
            if tab.ev("document.readyState") == "complete" and \
               tab.ev("document.querySelectorAll('textarea').length") and \
               tab.ev("document.querySelectorAll('input[type=file]').length"):
                return True
        except SystemExit:
            raise
        except Exception:
            pass
        time.sleep(2)
    raise SystemExit("DEEPSEEK_NOT_READY: sin composer tras %ds" % limit_s)


def file_input_accept(tab):
    return tab.ev("""(() => {
      const e = document.querySelector('input[type=file]');
      if (!e) return null;
      const a = (e.accept || '').split(',').map(s => s.trim());
      return JSON.stringify({accept_len: (e.accept||'').length,
                             allows_json: a.includes('.json'),
                             accepts_oversized: a.includes('.*'),
                             multi: !!e.multiple});
    })()""")


def attach(tab, path: Path, limit_s=300):
    """Hand the file to the real file input; confirm the chip names it."""
    tab.cmd("DOM.enable")
    doc = tab.cmd("DOM.getDocument", {"depth": 1})["root"]["nodeId"]
    node = tab.cmd("DOM.querySelector",
                   {"nodeId": doc, "selector": "input[type=file]"})["nodeId"]
    if not node:
        raise SystemExit("NO_FILE_INPUT")
    tab.cmd("DOM.setFileInputFiles", {"files": [str(path)], "nodeId": node})
    print("ATTACH_SENT  %s  (%.2f MB)" % (path.name, path.stat().st_size / 1e6))

    deadline = time.time() + limit_s
    last = ""
    while time.time() < deadline:
        try:
            body = tab.ev("document.body.innerText") or ""
            hits = [ln.strip() for ln in body.split("\n")
                    if path.name in ln or path.stem in ln]
            if hits:
                return hits[0][:200]
            last = body[:160].replace("\n", " ")
        except Exception:
            pass
        time.sleep(2)
    raise SystemExit("ATTACH_NOT_CONFIRMED: el chip no nombro el archivo. body=%r" % last)


def write_prompt(tab, prompt):
    js = ("(() => {const el=document.querySelector('textarea');if(!el)return 'NO_EL';"
          "el.focus();const s=Object.getOwnPropertyDescriptor("
          "Object.getPrototypeOf(el),'value').set;s.call(el,%s);"
          "el.dispatchEvent(new Event('input',{bubbles:true}));return 'WROTE';})()"
          % json.dumps(prompt))
    if tab.ev(js) != "WROTE":
        raise SystemExit("WRITE_FAIL")
    time.sleep(0.8)
    back = tab.ev("document.querySelector('textarea').value") or ""
    if back.strip() != prompt.strip():
        raise SystemExit("READBACK_MISMATCH: enviado=%d leido=%d"
                         % (len(prompt), len(back)))
    print("READBACK_OK  %d chars" % len(back.strip()))


def send_and_wait(tab, timeout=900, poll=3.0, stable=2):
    before = tab.ev(JS_ASSIST_N)
    tab.enter()
    time.sleep(2.5)
    print("SENT")

    deadline = time.time() + timeout
    last, n_stable, t0 = "", 0, time.time()
    while time.time() < deadline:
        txt = tab.ev(JS_ASSIST_LAST) or ""
        if txt and txt == last:
            n_stable += 1
            if n_stable >= stable:
                break
        else:
            n_stable = 0
            if txt:
                last = txt
                print("  [%d chars] %ds" % (len(txt), int(time.time() - t0)))
        time.sleep(poll)

    print("POST assistant_nodes %s -> %s  elapsed=%ds"
          % (before, tab.ev(JS_ASSIST_N), int(time.time() - t0)))
    if not last:
        raise SystemExit("NO_RESPONSE_TIMEOUT:%ds" % timeout)
    return last


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cdp", default=DEFAULT_CDP)
    ap.add_argument("--url", default=DEFAULT_URL)
    ap.add_argument("--file", required=True)
    ap.add_argument("--prompt", default=None)
    ap.add_argument("--timeout", type=int, default=900)
    ap.add_argument("--poll", type=float, default=3.0)
    ap.add_argument("--stable", type=int, default=2)
    ap.add_argument("--probe-only", action="store_true")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()

    path = Path(a.file).resolve()
    if not path.exists():
        raise SystemExit("NO_FILE:" + str(path))

    tdict, created = find_tab(a.cdp, a.url)
    print("TAB  %s  %s%s" % (tdict["id"][:12], tdict["url"],
                             "  (nueva)" if created else ""))
    tab = Tab(tdict["webSocketDebuggerUrl"])
    try:
        wait_ready(tab)
        if tab.ev("!!document.querySelector('input[type=password]')"):
            raise SystemExit("LOGIN_WALL: inicia sesion manualmente")
        print("ACCEPT  %s" % file_input_accept(tab))
        chip = attach(tab, path)
        print("ATTACH_CONFIRMED  chip=%r" % chip)
        if a.probe_only:
            return 0
        if a.prompt:
            write_prompt(tab, Path(a.prompt).read_text(encoding="utf-8"))
        reply = send_and_wait(tab, a.timeout, a.poll, a.stable)
        print("=" * 70)
        print(reply)
        print("=" * 70)
        if a.out:
            Path(a.out).write_text(reply, encoding="utf-8")
            print("SAVED %s" % a.out)
        return 0
    finally:
        tab.close()


if __name__ == "__main__":
    sys.exit(main())
