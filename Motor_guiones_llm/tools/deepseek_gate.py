#!/usr/bin/env python3
"""DEEPSEEK_REAL_GATE_01 — one tab, one specialist, real DeepSeek.

Chain under test, end to end:

    request_builder -> provider.call -> ds_provider -> ds_pool -> DSSession
    -> DeepSeek -> ds_extract -> JSON parse -> contract -> reset -> release

Scope is deliberately minimal: script_hook_specialist on MILO-S0001, parallelism 1,
critic/synthesizer/repair OFF. This gate answers one question: does the transport
work against the real site, and if not, WHICH layer failed.

Failure classification (the reason this script exists):
    TRANSPORT   browser/tab/composer/timeout — DeepSeek was never reached
    EXTRACTION  reply arrived but no JSON could be recovered
    FORMAT      JSON parsed but is not the specialist contract
    CONTRACT    structurally valid JSON, wrong shape for a specialist
Prompts are NEVER modified on failure. Calibration is a separate, deliberate step.

Artifacts land in artefactos/deepseek_gate_01/ for inspection.
"""
from __future__ import annotations

import json
import pathlib
import sys
import time
import traceback

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.common import config, read, write
from src.request_builder import prepare
from src import multiagent as ma
from src.ds_provider import build_prompt, extract_json
from tools.ds_pool import DSPool
from tools.ds_session import DSSession

OUT = ROOT / "artefactos" / "deepseek_gate_01"
EPISODE = "EP0001"
SEED = "MILO-S0001"
ROLE = "script_hook_specialist"


class Gate:
    def __init__(self):
        self.criteria = []
        self.classification = None
        self.notes = []

    def check(self, name, ok, detail=""):
        self.criteria.append({"criterion": name, "pass": bool(ok), "detail": str(detail)})
        print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  — {detail}" if detail else ""))
        return bool(ok)

    def fail_class(self, cls, why):
        self.classification = cls
        self.notes.append(why)
        print(f"\n>>> FAILURE CLASS: {cls}\n>>> {why}")


def build_request():
    c = config()
    req = prepare(c, EPISODE, SEED)
    write(OUT / "request.json", req)
    return c, req


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    g = Gate()
    t0 = time.monotonic()

    print("=" * 68)
    print("DEEPSEEK_REAL_GATE_01")
    print("=" * 68)
    print(f"episode={EPISODE}  seed={SEED}  role={ROLE}  parallelism=1")
    print("critic=OFF  synthesizer=OFF  repair=OFF\n")

    # ---------------- request ----------------
    try:
        c, req = build_request()
        base = ma.base_package(req)
        brief = next(b for r, k, b in ma.SPECIALISTS if r == ROLE)
        scoped = ma.scoped_base(base, ROLE)
        payload = ma.specialist_payload(
            scoped, brief + "\nReturn a concise JSON report: role, proposals (max3), "
                            "evidence (max6), risks (max6), handoff.")
        if not g.check("request_built", True, f"seed={req['seed_selection']['seed']['seed_id']}"):
            return 2
    except Exception as exc:
        g.fail_class("CONTRACT", f"request_builder failed: {exc}")
        traceback.print_exc()
        return 2

    prompt = build_prompt(ROLE, payload, (ROOT / "prompts" / "writer.md").read_text(encoding="utf-8"))
    (OUT / "prompt.txt").write_text(prompt, encoding="utf-8")
    print(f"\nprompt: {len(prompt):,} chars -> artefactos/deepseek_gate_01/prompt.txt")

    # ---------------- transport ----------------
    ds = c.get("ds") or {}
    pool = DSPool({"max_parallel_tabs": 1, **ds})
    session = None
    reply = ""
    acquired = False

    try:
        try:
            session = pool.acquire("specialist_" + ROLE)
            acquired = True
            g.check("tab_acquired", True, f"owner=specialist_{ROLE}")
        except Exception as exc:
            g.fail_class("TRANSPORT", f"pool.acquire failed: {exc}")
            return 2

        # open + composer
        try:
            session.open()
            ready = session.ev("document.readyState")
            composer = session.ev("!!document.querySelector(%s)" % json.dumps(ds.get("selector", "textarea.ds-scroll-area")))
            login = session.ev("!!document.querySelector('input[type=password]')")
            g.check("composer_present", bool(composer), f"readyState={ready} login_wall={login}")
            if not composer:
                g.fail_class("TRANSPORT", "composer not found (selector or page shape changed)")
                return 2
            if login:
                g.fail_class("TRANSPORT", "tab is on the sign-in page")
                return 2
        except Exception as exc:
            g.fail_class("TRANSPORT", f"session.open / probe failed: {exc}")
            return 2

        before = session.assistant_count()

        # inject
        try:
            js = ("(() => {const el=document.querySelector(%s);if(!el)return 'NO_EL';"
                  "el.focus();const s=Object.getOwnPropertyDescriptor("
                  "Object.getPrototypeOf(el),'value').set;s.call(el,%s);"
                  "el.dispatchEvent(new Event('input',{bubbles:true}));return 'WROTE';})()"
                  % (json.dumps(ds.get("selector", "textarea.ds-scroll-area")), json.dumps(prompt)))
            wrote = session.ev(js)
            time.sleep(1.2)
            back = session.ev("document.querySelector(%s).value"
                              % json.dumps(ds.get("selector", "textarea.ds-scroll-area")))
            readback_ok = (back or "").strip() == prompt.strip()
            g.check("prompt_injected", wrote == "WROTE", f"wrote={wrote}")
            g.check("read_back_exact", readback_ok,
                    f"sent={len(prompt.strip())} chars, composer={len((back or '').strip())} chars")
            if not readback_ok:
                g.fail_class("TRANSPORT", "composer content differs from what was sent")
                (OUT / "raw_response.txt").write_text("[read-back mismatch]\n" + (back or ""), encoding="utf-8")
                return 2
        except Exception as exc:
            g.fail_class("TRANSPORT", f"injection failed: {exc}")
            return 2

        # send
        base_k = {"key": "Enter", "code": "Enter", "text": "\r",
                  "windowsVirtualKeyCode": 13, "nativeVirtualKeyCode": 13}
        for kind in ("keyDown", "keyUp"):
            session.ws.send(json.dumps({"id": 0, "method": "Input.dispatchKeyEvent",
                                        "params": {**base_k, "type": kind}}))
        time.sleep(3)
        cleared = (session.ev("document.querySelector(%s).value"
                              % json.dumps(ds.get("selector", "textarea.ds-scroll-area"))) or "").strip() == ""
        g.check("composer_cleared_after_send", cleared)

        # ---------------- wait for reply ----------------
        print("\nwaiting for DeepSeek (this is the slow part)...", flush=True)
        sel = ds.get("assistant_selector", "[class*=assistant],[data-message-author-role=assistant]")
        deadline = time.time() + int(ds.get("response_timeout_s", 300))
        last, stable, polls = "", 0, 0
        while time.time() < deadline:
            polls += 1
            count = session.assistant_count()
            if count > before:
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
            g.fail_class("TRANSPORT", f"no reply within {ds.get('response_timeout_s',300)}s "
                                       f"(composer cleared={cleared}, nodes before={before})")
            return 2

        # ---------------- extraction ----------------
        parsed = extract_json(reply or last)
        write(OUT / "parsed_response.json", parsed if parsed is not None else {})
        g.check("json_extracted", parsed is not None,
                type(parsed).__name__ if parsed else "None")
        if parsed is None:
            g.fail_class("EXTRACTION",
                         "reply contained no recoverable JSON. Raw text saved. "
                         "Do NOT edit prompts yet: inspect raw_response.txt first.")
            return 2

        # ---------------- contract ----------------
        validation = {"is_object": isinstance(parsed, dict),
                      "keys": sorted(parsed.keys()) if isinstance(parsed, dict) else [],
                      "errors": []}
        for key in ("role", "proposals", "evidence", "risks", "handoff"):
            if key not in parsed:
                validation["errors"].append("missing:" + key)
        if isinstance(parsed, dict):
            if parsed.get("role") is not None and ROLE.split("_")[-1] not in str(parsed.get("role", "")):
                validation["errors"].append("role_mismatch:" + str(parsed.get("role")))
            for key in ("proposals", "evidence", "risks"):
                v = parsed.get(key)
                if v is not None and not isinstance(v, list):
                    validation["errors"].append("not_a_list:" + key)
            size = len(json.dumps(parsed, ensure_ascii=False).encode("utf-8"))
            validation["bytes"] = size
            limit = int(c.get("specialist_max_bytes", 6000))
            if size > limit:
                validation["errors"].append(f"too_large:{size}>{limit}")
        ok_contract = isinstance(parsed, dict) and not validation["errors"]
        write(OUT / "validation.json", validation)
        g.check("specialist_contract_valid", ok_contract,
                "errors=" + ",".join(validation["errors"]) if validation["errors"]
                else f"{validation.get('bytes',0):,} bytes, keys={len(validation['keys'])}")
        if not ok_contract:
            got_keys = validation["keys"][:12]
            validation["returned_shape"] = (
                "script_package(candidate)" if "beats" in validation["keys"]
                else "unknown")
            write(OUT / "validation.json", validation)
            g.fail_class("FORMAT" if not validation["is_object"] else "CONTRACT",
                         "JSON parsed but does not satisfy the specialist contract: "
                         + ",".join(validation["errors"])
                         + " | returned keys: " + ",".join(got_keys))

    except Exception as exc:
        g.fail_class("TRANSPORT", f"unexpected: {exc}")
        traceback.print_exc()

    finally:
        # ---------------- reset + release ----------------
        try:
            if acquired:
                pool.reset_session("specialist_" + ROLE)
                g.check("tab_reset", True, "navigated to a fresh chat")
        except Exception as exc:
            g.check("tab_reset", False, str(exc))
        try:
            if acquired:
                pool.release("specialist_" + ROLE)
                g.check("tab_released", True)
        except Exception as exc:
            g.check("tab_released", False, str(exc))
        try:
            pool.close_all()
        except Exception:
            pass

    # ---------------- report ----------------
    passed = sum(1 for x in g.criteria if x["pass"])
    total = len(g.criteria)
    elapsed = time.monotonic() - t0
    report = {
        "gate": "DEEPSEEK_REAL_GATE_01",
        "episode": EPISODE, "seed": SEED, "role": ROLE, "parallelism": 1,
        "criteria": g.criteria,
        "passed": passed, "total": total,
        "failure_class": g.classification,
        "notes": g.notes,
        "elapsed_s": round(elapsed, 1),
    }
    write(OUT / "validation.json", read(OUT / "validation.json") if (OUT / "validation.json").exists() else {})
    (OUT / "gate_result.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = ["# DEEPSEEK_REAL_GATE_01 — run report", "",
             f"- episode: `{EPISODE}`", f"- seed: `{SEED}`", f"- role: `{ROLE}`",
             f"- parallelism: 1 (critic/synthesizer/repair OFF)",
             f"- elapsed: {elapsed:.0f}s", f"- criteria: {passed}/{total} PASS",
             f"- failure class: **{g.classification or 'none'}**", "", "## Criteria", ""]
    for x in g.criteria:
        lines.append(f"- {'PASS' if x['pass'] else 'FAIL'} — {x['criterion']}"
                     + (f" ({x['detail']})" if x["detail"] else ""))
    lines += ["", "## Artifacts", "",
              "- `request.json` — the built request",
              "- `prompt.txt` — exactly what was typed into the composer",
              "- `raw_response.txt` — DeepSeek's reply, unmodified",
              "- `parsed_response.json` — what the extractor recovered",
              "- `validation.json` — contract check",
              "- `gate_result.json` — machine-readable result", ""]
    if g.classification:
        lines += ["## Failure classification", ""] + [f"- {n}" for n in g.notes] + \
                 ["", "Prompts were NOT modified. Calibration is a separate step.", ""]
    (OUT / "run_report.md").write_text("\n".join(lines), encoding="utf-8")

    print("\n" + "=" * 68)
    print(f"{passed}/{total} PASS   elapsed={elapsed:.0f}s   class={g.classification or 'none'}")
    print(f"artefacts: {OUT}")
    print("=" * 68)
    return 0 if passed == total and g.classification is None else 2


if __name__ == "__main__":
    sys.exit(main())