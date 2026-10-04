#!/usr/bin/env python3
"""GITHUB_SEED_ACCESS_GATE — can DeepSeek actually read the 1000-seed file?

This gate answers ONE question before any Scout or QA/QC is built: does DeepSeek,
through this CDP transport, genuinely reach the bank at GitHub and read content
from across its whole length -- or does it only see the head and invent the rest?

The seed source is delivered as a URL, NOT pasted into the prompt. The full bank
is ~566k tokens and cannot fit in one context window (measured), so the scout
depends entirely on DeepSeek fetching it itself.

Five probes at roughly 0%, 25%, 50%, 75% and 100% of the file. A model that only
read the beginning will fail probes 3-5, which is exactly what this gate exists
to detect. Every returned id is checked against the local bank: a hallucinated id
is a failure, not a curiosity.

Hermes validates access and ids. It makes no creative judgement.
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.ds_pool import DSPool
from tools.ds_session import DSSession
from src.ds_provider import extract_json

REPO_URL = "https://github.com/devGrijalba/Milo_Project_03"
RAW_URL = ("https://raw.githubusercontent.com/devGrijalba/Milo_Project_03/"
           "main/MILO_SEEDS_COMPACTAS_GUI%C3%93N_0001-1000.md")
OUT = ROOT / "artefactos" / "seed_selection" / "github_access_gate"

PROMPT = """Debes trabajar unicamente con esta fuente:

""" + REPO_URL + """

Localiza el archivo:

MILO_SEEDS_COMPACTAS_GUIÓN_0001-1000.md

Si no puedes abrir el repositorio, usa la URL directa:

""" + RAW_URL + """

No uses conocimiento previo ni inventes contenido.

Necesito comprobar que realmente puedes consultar TODO el archivo, no solo el
comienzo. Devuelve JSON estricto con exactamente estas cinco muestras, tomadas
de posiciones repartidas por el archivo:

1. una semilla del primer 5% del archivo
2. una semilla de alrededor del 25%
3. una semilla de alrededor del 50%
4. una semilla de alrededor del 75%
5. una semilla del ultimo 5%

Para cada una dame: seed_id, titulo y el numero de registro que deduces.

Ademas indica: total_semillas_detectadas.

Reglas:
- No inventes IDs.
- Si no puedes acceder a alguna parte del archivo, indicarlo explicitamente con
  un campo "acceso_parcial" y explica cual.
- Si no pudiste leer mas alla del inicio, dilo. Prefiero una negativa honesta a
  una lista inventada.

Devuelve SOLO el objeto JSON."""

ID_RE = re.compile(r"MILO-[SR]\d{4}")


class Gate:
    def __init__(self):
        self.criteria = []
        self.cls = None

    def check(self, name, ok, detail=""):
        self.criteria.append({"criterion": name, "pass": bool(ok), "detail": str(detail)})
        print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
        return bool(ok)

    def fail(self, cls, why):
        self.cls = cls
        print(f"\n>>> FAILURE CLASS: {cls}\n>>> {why}")


def local_ids():
    bank = json.loads((ROOT / "data" / "seeds.json").read_text(encoding="utf-8"))
    return {s["seed_id"] for s in bank["seeds"]}, bank["seeds"]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "prompt.txt").write_text(PROMPT, encoding="utf-8")
    g = Gate()
    t0 = time.monotonic()

    print("=" * 68)
    print("GITHUB_SEED_ACCESS_GATE")
    print("=" * 68)
    print(f"repo: {REPO_URL}")
    print(f"prompt: {len(PROMPT):,} chars (the BANK is NOT pasted)\n")

    valid_ids, seeds = local_ids()
    index = {s["seed_id"]: s for s in seeds}

    cfg = json.loads((ROOT / "config" / "engine.json").read_text(encoding="utf-8"))
    ds = cfg.get("ds") or {}
    pool = DSPool({"max_parallel_tabs": 1, **ds})
    session = None
    acquired = False
    reply = ""
    before = 0

    try:
        try:
            session = pool.acquire("github_seed_access_test")
            acquired = True
            g.check("tab_acquired", True, "session=github_seed_access_test")
            session.open()
            composer = session.ev("!!document.querySelector(%s)"
                                  % json.dumps(ds.get("selector", "textarea.ds-scroll-area")))
            g.check("composer_present", bool(composer))
            if not composer:
                g.fail("TRANSPORT", "composer not found")
                return 2
            before = session.assistant_count()
        except Exception as exc:
            g.fail("TRANSPORT", f"session setup: {exc}")
            return 2

        js = ("(() => {const el=document.querySelector(%s);if(!el)return 'NO_EL';"
              "el.focus();const s=Object.getOwnPropertyDescriptor("
              "Object.getPrototypeOf(el),'value').set;s.call(el,%s);"
              "el.dispatchEvent(new Event('input',{bubbles:true}));return 'WROTE';})()"
              % (json.dumps(ds.get("selector", "textarea.ds-scroll-area")), json.dumps(PROMPT)))
        wrote = session.ev(js)
        time.sleep(1.2)
        back = session.ev("document.querySelector(%s).value"
                          % json.dumps(ds.get("selector", "textarea.ds-scroll-area")))
        rb = (back or "").strip() == PROMPT.strip()
        g.check("prompt_injected", wrote == "WROTE")
        g.check("read_back_exact", rb, f"{len((back or '').strip())} chars in composer")
        if not rb:
            g.fail("TRANSPORT", "composer differs from prompt")
            return 2

        key = {"key": "Enter", "code": "Enter", "text": "\r",
               "windowsVirtualKeyCode": 13, "nativeVirtualKeyCode": 13}
        for kind in ("keyDown", "keyUp"):
            session.ws.send(json.dumps({"id": 0, "method": "Input.dispatchKeyEvent",
                                        "params": {**key, "type": kind}}))
        time.sleep(3)
        g.check("composer_cleared", (session.ev("document.querySelector(%s).value"
                                                 % json.dumps(ds.get("selector", "textarea.ds-scroll-area")))
                                     or "").strip() == "")

        print("\nwaiting for DeepSeek to fetch and read the file...", flush=True)
        sel = ds.get("assistant_selector", "[class*=assistant],[data-message-author-role=assistant]")
        deadline = time.time() + int(ds.get("response_timeout_s", 300))
        last, stable, polls = "", 0, 0
        while time.time() < deadline:
            polls += 1
            if session.assistant_count() > before:
                txt = session.ev("""(() => {const ns=[...document.querySelectorAll(%s)];
                    const l=ns[ns.length-1];return l?(l.innerText||l.textContent||'').trim():'';})()"""
                                 % json.dumps(sel)) or ""
                if txt and txt == last:
                    stable += 1
                    if stable >= int(ds.get("stable_reads", 2)):
                        reply = txt
                        break
                else:
                    stable = 0
                    if txt:
                        last = txt
                        print(f"  [{len(txt):,} chars] …")
            time.sleep(float(ds.get("poll_s", 2.5)))

        (OUT / "raw_response.txt").write_text(reply or last or "[sin respuesta]", encoding="utf-8")
        elapsed = time.monotonic() - t0
        got = bool(reply or last)
        g.check("response_received", got,
                f"{len(reply or last):,} chars in {elapsed:.0f}s, {polls} polls")
        if not got:
            g.fail("TRANSPORT", f"no reply within {ds.get('response_timeout_s', 300)}s")
            return 2

        parsed = extract_json(reply or last)
        (OUT / "parsed_response.json").write_text(
            json.dumps(parsed, ensure_ascii=False, indent=2) if parsed is not None else {},
            encoding="utf-8")
        g.check("json_extracted", parsed is not None)
        if parsed is None:
            g.fail("EXTRACTION", "no JSON recovered; see raw_response.txt")
            return 2

        # ---- pull every id the model claimed, wherever it put them ----
        raw_text = reply or last
        claimed = ID_RE.findall(json.dumps(parsed, ensure_ascii=False))
        if len(set(claimed)) < 5:
            extra = ID_RE.findall(raw_text)
            claimed = list(dict.fromkeys(claimed + extra))

        invalid = [i for i in claimed if i not in valid_ids]
        validation = {
            "claimed_ids": claimed,
            "invalid_ids": invalid,
            "total_detected_by_model": parsed.get("total_semillas_detectadas"),
            "samples_found": len(claimed),
            "access_partial": bool(parsed.get("acceso_parcial")),
        }
        g.check("ids_exist_in_local_bank", not invalid,
                f"{len(claimed)} ids, {len(invalid)} unknown")
        if invalid:
            validation["invalid_detail"] = [i for i in invalid]

        # distribution: ids must span the file, not cluster at the head
        nums = sorted(int(re.search(r"(\d{4})$", i).group(1)) for i in claimed if i in valid_ids)
        bands = []
        if nums:
            lo, hi = min(nums), max(nums)
            spread = (hi - lo) / 999.0
            bands = {"min": lo, "max": hi, "spread_pct": round(spread * 100, 1)}
            g.check("samples_span_the_file", spread > 0.5,
                    f"registros {lo}..{hi} = {spread*100:.0f}% del rango")
        else:
            g.check("samples_span_the_file", False, "no valid ids to compare")

        total = parsed.get("total_semillas_detectadas")
        try:
            total_ok = int(total) == 1000
        except (TypeError, ValueError):
            total_ok = False
        g.check("total_is_coherent", total_ok, f"model reported {total}")
        if not total_ok:
            validation["total_note"] = ("DeepSeek did not report exactly 1000. "
                                        "That is a FACT check, not an access check; "
                                        "recorded, not failed on its own.")
        validation["gate_verdict"] = ("PASS" if not invalid and len(set(claimed)) >= 5
                                     else "FAIL")

    except Exception as exc:
        g.fail("TRANSPORT", f"unexpected: {exc}")
    finally:
        try:
            if acquired:
                pool.reset_session("github_seed_access_test")
                g.check("tab_reset", True)
        except Exception as exc:
            g.check("tab_reset", False, str(exc))
        try:
            if acquired:
                pool.release("github_seed_access_test")
                g.check("tab_released", True)
        except Exception as exc:
            g.check("tab_released", False, str(exc))
        try:
            pool.close_all()
        except Exception:
            pass

    passed = sum(1 for x in g.criteria if x["pass"])
    total = len(g.criteria)
    (OUT / "validation.json").write_text(
        json.dumps(validation if "validation" in dir() else {}, ensure_ascii=False, indent=2),
        encoding="utf-8")
    verdict = "PASS" if g.cls is None and passed == total else "FAIL"
    print("\n" + "=" * 68)
    print(f"GITHUB_SEED_ACCESS = {verdict}   {passed}/{total} criteria   "
          f"class={g.cls or 'none'}")
    print(f"artefacts: {OUT}")
    print("=" * 68)
    return 0 if verdict == "PASS" else 2


if __name__ == "__main__":
    sys.exit(main())