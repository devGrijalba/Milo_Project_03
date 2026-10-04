"""Run the seed selection funnel against DeepSeek.

    4 Scouts (independent tabs) -> 60 candidates, untrimmed
    -> 1 QC judge (own tab)     -> winner
    -> selected_seed.json

Hermes' role stops at arithmetic and contracts. `run_scouts` fans out and
collects; it has no scoring, ranking or trimming step, and `select_winner`
only writes what the judge returned. If a Scout returns 14, the run fails and
says so -- it does not fetch a 15th.

Run order is gated on purpose:
    python tools/seed_selection.py prepare      # offline, no browser
    python tools/seed_selection.py scout 1       # one batch, one real call
    python tools/seed_selection.py run          # 4 concurrent + QC
"""
from __future__ import annotations

import argparse
import concurrent.futures as futures
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.common import config, digest, write
from src.ds_provider import extract_json
from src import seed_pipeline as sp

ART = ROOT / "artefactos" / "seed_selection"


# ------------------------------------------------------------------ prompts
SCOUT_INSTRUCTIONS = """\
Eres un SEED SCOUT de MILO. Recibes un lote de {n} semillas ya proyectadas.

Tu pregunta no es "como desarrollo el episodio" sino "cual de estas semillas
merece convertirse en episodio".

Reglas:
- Examina TODAS las semillas del lote. No te quedes con las primeras.
- Compara familias entre si: una familia tiene la semilla base (angulo
  primera_vez) y sus arcos causales (R0002..R0010). Decide cual angulo de cada
  familia es el mas fuerte y por que.
- Los scores historicos (calidad, afinidad, novedad, compuesto) son EVIDENCIA
  SECUNDARIA. No elijas automaticamente el de mayor compuesto: indica cuando un
  score alto esconde una idea debil, y cuando un score moderado esconde una idea
  fuerte.
- No repitas familias distintas que en realidad cuentan lo mismo.
- Mira esto en cada semilla: hook, conflicto, accion visible, emocion,
  curiosidad, encaje con Milo, originalidad, giro, payoff, retencion,
  claridad, visualidad, viabilidad en menos de 45 segundos, diferenciacion
  respecto a lo ya publicado.
- Si dos semillas de la MISMA familia son casi identicas, elige la mas fuerte
  y descarta la otra (esta decision es tuya, no de quien te paso los datos).

Devuelve EXCLUSIVAMENTE JSON valido con esta forma exacta:

{{"candidates": [
  {{"rank": 1, "seed_id": "MILO-S0001",
    "why_selected": "2-4 frases: que potencial narrativo tiene y por que gana",
    "strengths": ["..."], "risks": ["..."]}}
]}}

Exactamente {top} candidatos. Los seed_id deben existir en el lote recibido.
Sin texto antes ni despues del JSON. Sin bloques de codigo markdown."""


QC_INSTRUCTIONS = """\
Eres el SEED QA/QC final de MILO. Recibes {n} semillas COMPLETAS que ya
sobrevivieron la fase de discovery.

Estas candidatas llegan conceptualmente como iguales. No recibes ningun ranking
anterior: no se te dice cual le gusto mas a nadie. Reevalua las {n} desde cero.

Tu pregunta es: cual de estas {n} semillas tiene mayor probabilidad de producir
el mejor episodio de MILO en este momento, considerando el historial de lo ya
publicado.

Evalua cada candidata en: hook, conflicto, accion visible, emocion, objeto
emocional, giro, encaje con Milo, originalidad frente a lo ya publicado,
potencial visual, viabilidad en menos de 45 segundos, claridad, y fuerza del
payoff.

Haz un embudo: de {n} a 15, de 15 a 5, de 5 a 3, y de 3 a 1.

Devuelve EXCLUSIVAMENTE JSON valido con esta forma exacta:

{{"top_15": [{{"seed_id": "MILO-SXXXX", "why": "..."}}],
 "top_5":  [{{"seed_id": "MILO-SXXXX", "why": "..."}}],
 "top_3":  [{{"seed_id": "MILO-SXXXX", "why": "..."}}],
 "winner": {{"seed_id": "MILO-SXXXX", "why": "..."}}}}

El winner DEBE pertenecer a top_3. Los tres niveles deben ir encajados: top_3
dentro de top_5, top_5 dentro de top_15. Sin texto antes ni despues del JSON.
Sin bloques de codigo markdown."""


# ------------------------------------------------------------------ prepare
def prepare(config_path=None, history=None):
    """Offline stage. Builds batches and writes inputs. No browser, no model."""
    c = config(config_path)
    bank = sp.load_bank(config_path)
    seeds = bank["seeds"]
    batches = sp.build_batches(seeds)

    folder = ART / "current"
    write(folder / "batch_manifest.json", sp.batch_manifest(seeds, batches))
    for i, b in enumerate(batches, start=1):
        write(folder / ("scout_batch_%d_input.json" % i),
              sp.scout_input(seeds, b, i, history=history))

    tot = sum(sp._cost(b) for b in batches)
    print("banco: %d semillas, %d familias" % (len(seeds), len(sp.group_families(seeds))))
    for i, b in enumerate(batches, start=1):
        print("  lote %d: %3d semillas / %2d familias / ~%5d tokens"
              % (i, len(b), len({s['family_id'] for s in b}), sp._cost(b) // 4))
    print("  total Scout: ~%d tokens" % (tot // 4))
    return folder


# ------------------------------------------------------------------ scouts
def _scout_one(index, config_path=None, top_n=sp.TOP_N, history=None):
    """One batch on its own tab. Never sees another batch's selections."""
    from tools.ds_pool import pool as get_pool
    from tools.ds_extract import extract_from_tab

    ds = (config(config_path).get("ds") or {})
    p = ART / "current" / ("scout_batch_%d_input.json" % index)
    payload = json.loads(p.read_text(encoding="utf-8"))
    allowed = [s["seed_id"] for s in payload["seeds"]]
    name = "seed_scout_batch_%d" % index

    head = SCOUT_INSTRUCTIONS.format(n=len(allowed), top=top_n)
    body = json.dumps(payload, ensure_ascii=False)
    prompt = "%s\n\n--- LOTE (JSON) ---\n%s\n" % (head, body)

    tabpool = get_pool(ds)
    session = tabpool.acquire(name)
    try:
        reply = extract_from_tab(session, prompt, ds)
        (ART / "current" / ("scout_batch_%d_raw_response.txt" % index)).write_text(
            reply, encoding="utf-8")
    finally:
        # fresh chat before handing the tab on: a Scout must not be able to
        # see what another Scout answered
        try:
            tabpool.reset_session(name)
        finally:
            tabpool.release(name)

    obj = extract_json(reply)
    ok, problems = sp.validate_scout_output(obj, allowed, top_n)
    write(ART / "current" / ("scout_batch_%d_output.json" % index), {
        "batch_index": index,
        "contract_ok": ok,
        "problems": problems,
        "payload": obj,
    })
    print("lote %d: %s (%s)" % (index, "PASS" if ok else "FAIL", ",".join(problems) or "-"))
    return ok


def scout(index, config_path=None):
    return _scout_one(index, config_path)


def run_scouts(config_path=None, top_n=sp.TOP_N):
    """Four independent Scouts, concurrently. Returns the outputs in batch order."""
    p = ART / "current"
    if not (p / "batch_manifest.json").exists():
        raise SystemExit("run prepare first")

    outs = []
    with futures.ThreadPoolExecutor(max_workers=sp.BATCH_COUNT) as ex:
        jobs = {ex.submit(_scout_one, i, config_path, top_n): i for i in range(1, sp.BATCH_COUNT + 1)}
        for job in futures.as_completed(jobs):
            outs.append((jobs[job], job.result()))     # raises -> the run fails

    outs.sort(key=lambda x: x[0])
    if not all(ok for _, ok in outs):
        raise ValueError("SCOUT_CONTRACT_FAILED")

    results = [json.loads((p / ("scout_batch_%d_output.json" % i)).read_text(encoding="utf-8"))
               for i in range(1, sp.BATCH_COUNT + 1)]
    write(p / "semifinalists_60_ids.json", {
        "count": len(results) * sp.TOP_N,
        "trimmed_by_hermes": False,
        "seed_ids": sp.collect_semifinalists([r["payload"] for r in results]),
    })
    return results


# ------------------------------------------------------------------ judge
def qc_prompt_payload(ids, config_path=None, history=None):
    c = config(config_path)
    bank = sp.load_bank(config_path)
    full = sp.hydrate(bank, ids)
    write(ART / "current" / "seed_qc_candidates_full.json", full)
    return {
        "role": "script_seed_qc",
        "instructions": QC_INSTRUCTIONS.format(n=len(ids)),
        "canon_digest": digest(sp.group_families(bank["seeds"])),
        "recent_history": history or [],
        "candidate_count": len(ids),
        "candidate_seed_ids": ids,
        "seeds": full,
    }


def select_winner(ids=None, config_path=None, history=None):
    """Independent judge session. Does not see the Scouts' rankings."""
    from tools.ds_pool import pool as get_pool
    from tools.ds_extract import extract_from_tab

    ds = (config(config_path).get("ds") or {})
    p = ART / "current"
    if ids is None:
        ids = json.loads((p / "semifinalists_60_ids.json").read_text(encoding="utf-8"))["seed_ids"]

    payload = qc_prompt_payload(ids, config_path, history)
    (p / "seed_qc_prompt.txt").write_text(
        "%s\n\n--- CANDIDATAS (JSON) ---\n%s\n"
        % (payload["instructions"], json.dumps(payload["seeds"], ensure_ascii=False)),
        encoding="utf-8")

    name = "seed_qc"
    tabpool = get_pool(ds)
    session = tabpool.acquire(name)
    try:
        reply = extract_from_tab(session,
                                 "%s\n\n--- CANDIDATAS (JSON) ---\n%s\n"
                                 % (payload["instructions"],
                                    json.dumps(payload["seeds"], ensure_ascii=False)),
                                 ds)
        (p / "seed_qc_raw_response.txt").write_text(reply, encoding="utf-8")
    finally:
        try:
            tabpool.reset_session(name)
        finally:
            tabpool.release(name)

    obj = extract_json(reply)
    ok, problems = sp.validate_qc_output(obj, ids)
    write(p / "seed_qc_output.json", {
        "contract_ok": ok, "problems": problems, "payload": obj})

    if not ok:
        print("QC: FAIL (%s)" % ",".join(problems))
        raise ValueError("SEED_QC_CONTRACT_FAILED")

    wid = obj["winner"]["seed_id"] if isinstance(obj["winner"], dict) else obj["winner"]
    doc = sp.selected_seed_document("EP0001", wid)
    write(p / "selected_seed.json", doc)
    print("QC: PASS -> %s" % wid)
    return doc


# ------------------------------------------------------------------ cli
def main():
    ap = argparse.ArgumentParser(description="SEED_SELECTION_PIPELINE")
    ap.add_argument("stage", choices=["prepare", "scout", "run", "qc"])
    ap.add_argument("--batch", type=int, default=1)
    ap.add_argument("--config")
    a = ap.parse_args()

    if a.stage == "prepare":
        prepare(a.config)
    elif a.stage == "scout":
        scout(a.batch, a.config)
    elif a.stage == "run":
        run_scouts(a.config)
        ids = json.loads((ART / "current" / "semifinalists_60_ids.json").read_text(encoding="utf-8"))["seed_ids"]
        select_winner(ids, a.config)
    elif a.stage == "qc":
        select_winner(config_path=a.config)


if __name__ == "__main__":
    main()
