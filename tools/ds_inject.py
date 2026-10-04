#!/usr/bin/env python3
"""Inyeccion DOM en DeepSeek via CDP en un solo paso.

Descubrir selectores, escribir, verificar, enviar y capturar, sin scripts de
sondeo intermedios: los selectores se descubren una vez y se guardan en
ds_selectors.json para reutilizarlos.

    python tools/ds_inject.py                  # inyecta el prompt por defecto
    python tools/ds_inject.py --probe          # solo descubre y guarda selectores
    python tools/ds_inject.py --file prompt.txt
    python tools/ds_inject.py --text "..." --url https://chat.deepseek.com/

Disenos deliberados:
- El read-back del composer es OBLIGATORIO y exacto: si el texto no coincide
  byte a byte con lo que se iba a enviar, se aborta sin enviar nada. Un prompt
  truncado en silencio es peor que no enviar nada.
- Enter se envia como evento de teclado real (Input.dispatchKeyEvent), no con
  insertText: insertText escribe texto pero no dispara los keydown listeners
  con los que DeepSeek detecta el envio.
- La espera de respuesta exige texto ESTABLE (2 lecturas identicas separadas),
  no "aparecio algo": el primer chunk del streaming llega en milisegundos y salir ahi
  devuelve media respuesta.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.request
from pathlib import Path

try:
    import websocket
except ImportError:
    sys.exit("FALTA websocket-client -> pip install websocket-client")

HERE = Path(__file__).resolve().parent
SEL_FILE = HERE / "ds_selectors.json"
DEFAULT_CDP = "http://127.0.0.1:9222"
DEFAULT_URL = "https://chat.deepseek.com/"

DEFAULT_PROMPT = """Lee el documento MILO_SEEDS_COMPACTAS_GUIÓN_0001-1000.md completo que está en este repositorio público:

https://github.com/devGrijalba/Milo_Project_03

El archivo está en la raíz del repo. Si no puedes abrirlo desde la web, usa la URL directa:

https://raw.githubusercontent.com/devGrijalba/Milo_Project_03/main/MILO_SEEDS_COMPACTAS_GUI%C3%93N_0001-1000.md

Es un banco de 1000 semillas para generación de guiones (registros 0001-1000).

Cuando lo hayas leído, confírmame únicamente esto:
1. cuántas semillas tiene,
2. qué campos trae cada semilla,
3. y el título exacto de las 3 primeras semillas (0001, 0002, 0003).
No me resumas el banco entero todavía. Solo esa confirmación."""

# El prompt viaja como argumento de JS via json.dumps: nunca dentro de un
# f-string, donde una llave o un % del prompt rompe el archivo en silencio.
JS_WRITE = """(() => {
  const el = document.querySelector(SELECTOR);
  if (!el) return 'NO_EL';
  el.focus();
  const proto = Object.getPrototypeOf(el);
  const setter = Object.getOwnPropertyDescriptor(proto, 'value').set;
  setter.call(el, TEXT);
  el.dispatchEvent(new Event('input', {bubbles: true}));
  return 'WROTE';
})()"""

JS_PROBE = """(() => {
  const vis = e => e.offsetParent !== null && e.getBoundingClientRect().height > 10;
  const tas = [...document.querySelectorAll('textarea')].filter(vis);
  const ces = [...document.querySelectorAll('div[contenteditable="true"]')].filter(vis);
  const pick = tas[0] || ces[0];
  if (!pick) return 'NONE';
  return JSON.stringify({
    tag: pick.tagName,
    sel: pick.tagName === 'TEXTAREA' ? 'textarea' : 'div[contenteditable="true"]',
    id: pick.id || '',
    ph: pick.getAttribute('data-placeholder') || pick.getAttribute('placeholder') || ''
  });
})()"""

JS_ASSIST_N = "document.querySelectorAll('[class*=assistant], [data-message-author-role=assistant]').length"
JS_ASSIST_LAST = """(() => {
  const ns = [...document.querySelectorAll('[class*=assistant], [data-message-author-role=assistant]')];
  const last = ns[ns.length - 1];
  if (!last) return '';
  return (last.innerText || last.textContent || '').trim();
})()"""


class Tab:
    """Un websocket por fase: sockets frescos, no reutilizados."""

    def __init__(self, ws_url: str):
        self.ws = websocket.create_connection(ws_url, timeout=30)
        self._id = 0

    def ev(self, expr: str):
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
                det = res["exceptionDetails"]
                text = det.get("exception", {}).get("description") or det.get("text") or "?"
                raise RuntimeError(str(text)[:300])
            return res.get("result", {}).get("value")

    def enter(self):
        base = {"key": "Enter", "code": "Enter", "text": "\r",
                "windowsVirtualKeyCode": 13, "nativeVirtualKeyCode": 13}
        for kind in ("keyDown", "keyUp"):
            self.ws.send(json.dumps({
                "id": 0, "method": "Input.dispatchKeyEvent",
                "params": {**base, "type": kind},
            }))

    def close(self):
        try:
            self.ws.close()
        except Exception:
            pass


def find_tab(cdp: str, need_url: str | None, opener=None):
    """Devuelve (tab_dict,(created_bool)). Reutiliza una pestaña existente que
    coincida; solo abre una si no hay ninguna."""
    host = need_url.split("/")[2] if need_url else None
    tabs = json.load(urllib.request.urlopen(cdp + "/json/list", timeout=8))
    pages = [t for t in tabs if t.get("type") == "page"]
    for t in pages:
        if host and host in t.get("url", ""):
            return t, False
    if need_url and opener:
        req = urllib.request.Request(cdp + "/json/new?" + need_url, method="PUT")
        return json.load(urllib.request.urlopen(req, timeout=10)), True
    raise SystemExit("NO_TAB: no hay pestana de DeepSeek y no se pudo abrir")


def probe(tab: Tab) -> str:
    raw = tab.ev(JS_PROBE)
    if raw == "NONE" or not raw:
        raise SystemExit("PROBE_FAIL: no hay composer visible")
    info = json.loads(raw)
    SEL_FILE.write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"PROBE_OK  tag={info['tag']}  placeholder={info['ph']!r}  -> {SEL_FILE.name}")
    return info["sel"]


def load_selector() -> str | None:
    if not SEL_FILE.exists():
        return None
    try:
        return json.loads(SEL_FILE.read_text(encoding="utf-8"))["sel"]
    except Exception:
        return None


def norm(s: str) -> str:
    return (s or "").strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cdp", default=DEFAULT_CDP)
    ap.add_argument("--url", default=None, help="abre esta URL si no hay pestana")
    ap.add_argument("--text", default=None)
    ap.add_argument("--file", default=None)
    ap.add_argument("--probe", action="store_true", help="solo descubre selectores")
    ap.add_argument("--timeout", type=int, default=300)
    ap.add_argument("--stable", type=int, default=2, help="lecturas identicas para cerrar")
    args = ap.parse_args()

    if args.file:
        prompt = Path(args.file).read_text(encoding="utf-8")
    elif args.text:
        prompt = args.text
    else:
        prompt = DEFAULT_PROMPT

    opener = (lambda: None) if args.url else None
    tdict, created = find_tab(args.cdp, args.url or DEFAULT_URL, opener)
    print(f"TAB  {tdict['id'][:12]}  {tdict['url']}" + ("  (nueva)" if created else ""))

    tab = Tab(tdict["webSocketDebuggerUrl"])
    try:
        print(f"URL  {tab.ev('location.href')}")
        if tab.ev("!!document.querySelector('input[type=password]')"):
            raise SystemExit("LOGIN_WALL: la pestana esta en sign_in; inicia sesion manualmente")

        if args.probe:
            probe(tab)
            return 0

        sel = load_selector()
        if not sel:
            sel = probe(tab)

        pre = tab.ev(JS_ASSIST_N)
        print(f"PRE  assistant_nodes={pre}")

        wrote = tab.ev(JS_WRITE.replace("SELECTOR", json.dumps(sel))
                              .replace("TEXT", json.dumps(prompt)))
        if wrote != "WROTE":
            raise SystemExit(f"WRITE_FAIL: {wrote}")
        time.sleep(1.0)

        back = tab.ev(f"document.querySelector({json.dumps(sel)}).value")
        if norm(back) != norm(prompt):
            print(f"READBACK_MISMATCH  enviado={len(norm(prompt))} leido={len(norm(back))}")
            print(f"  leido: {norm(back)[:160]!r}")
            return 2
        print(f"READBACK_OK  {len(norm(prompt))} chars")

        tab.enter()
        time.sleep(2.5)
        if norm(tab.ev(f"document.querySelector({json.dumps(sel)}).value")) != "":
            raise SystemExit("SEND_FAIL: el composer no se limpio tras Enter")
        print("SENT  composer limpio")

        deadline = time.time() + args.timeout
        last, stable, t0 = "", 0, time.time()
        while time.time() < deadline:
            txt = tab.ev(JS_ASSIST_LAST) or ""
            if txt and txt == last:
                stable += 1
                if stable >= args.stable:
                    break
            else:
                stable = 0
                if txt:
                    last = txt
                    print(f"  [{len(txt)} chars] …")
            time.sleep(3)

        post = tab.ev(JS_ASSIST_N)
        print(f"POST assistant_nodes={post}  elapsed={int(time.time() - t0)}s")
        if not last:
            print("NO_RESPONSE_TIMEOUT")
            return 3
        print("=" * 70)
        print(last)
        print("=" * 70)
        return 0
    finally:
        tab.close()


if __name__ == "__main__":
    sys.exit(main())