"""SEED_SELECTION_PIPELINE: mechanical batching + contract validation.

Where Hermes is allowed to act
    group families, balance batch sizes, apply a FIXED field projection,
    validate contracts, hydrate records from the bank, move artifacts.

Where Hermes is not allowed to act, and this module provides no way to do it
    score a seed, rank seeds, choose a winner, drop a candidate, merge lists,
    break a tie. There is deliberately no function here that returns "the best
    seed". Every output is a batch, a projection, or a validation verdict.

That is not a convention the caller must respect -- it is the shape of the API.
`build_batches` can only partition. `collect_semifinalists` can only concatenate.
Both are total functions over their input with no judgement parameter.

Source of truth
    data/seeds.json (config seed_bank). The GitHub markdown bank is not used at
    runtime: it is the same 1000 seeds in a shape an LLM cannot traverse.
"""
from __future__ import annotations

import copy
import json
import pathlib

from src.common import ROOT, config, read

# ------------------------------------------------------------------ contract
BATCH_COUNT = 4
TOP_N = 15
SEMIFINALISTS = BATCH_COUNT * TOP_N          # 60, never trimmed

# The projection. ONE field set for all 1000 seeds -- no per-seed decisions.
SCOUT_TOP_FIELDS = (
    "seed_id", "family_id", "narrative_cluster_id", "territorio", "angulo",
    "titulo", "semilla", "conflicto", "accion_visible", "objeto_emocional",
    "giro_posible", "personajes_requeridos", "milo_role", "motor_editorial",
)
SCOUT_REVISION_FIELDS = ("calidad", "afinidad", "novedad", "compuesto", "elegible")

# Stays in seeds.json for the specialists; never reaches a Scout.
EXCLUDED_FROM_SCOUT = ("desarrollo_requerido", "personajes_secundarios")

SEED_ID_RE = __import__("re").compile(r"^MILO-[SR]\d{4}$")


# ------------------------------------------------------------------ bank
def load_bank(config_path=None):
    """Read and structurally validate the seed bank. No creative filtering:
    a record is rejected only when it is structurally unusable."""
    c = config(config_path)
    p = pathlib.Path(c["seed_bank"])
    bank = read(p if p.is_absolute() else ROOT / p)
    if not isinstance(bank, dict) or not isinstance(bank.get("seeds"), list):
        raise ValueError("INVALID_SEED_BANK")
    seeds = bank["seeds"]
    if not seeds:
        raise ValueError("SEED_BANK_EMPTY")
    if bank.get("cantidad") not in (None, len(seeds)):
        raise ValueError("SEED_BANK_COUNT_MISMATCH")
    seen = set()
    for s in seeds:
        if not isinstance(s, dict):
            raise ValueError("INVALID_SEED_RECORD")
        sid = s.get("seed_id")
        if not sid or not SEED_ID_RE.match(sid):
            raise ValueError("SEED_ID_INVALID:" + str(sid))
        if sid in seen:
            raise ValueError("DUPLICATE_SEED_ID:" + sid)
        seen.add(sid)
        if not s.get("family_id"):
            raise ValueError("SEED_FAMILY_ID_MISSING:" + sid)
    return bank


# ------------------------------------------------------------------ projection
def scout_projection(seed):
    """The fixed decision projection. Same keys for every seed, present or not.

    A missing optional field becomes None rather than being dropped, so the
    model sees a stable shape and no seed appears to have been curated.
    """
    rev = seed.get("revision") or {}
    out = {k: seed.get(k) for k in SCOUT_TOP_FIELDS}
    out["revision"] = {k: rev.get(k) for k in SCOUT_REVISION_FIELDS}
    return out


def _cost(seeds):
    return sum(len(json.dumps(scout_projection(s), ensure_ascii=False)) for s in seeds)


# ------------------------------------------------------------------ batching
def group_families(seeds):
    """family_id -> [seeds]. A family is indivisible from here on."""
    fam = {}
    for s in seeds:
        fam.setdefault(s["family_id"], []).append(s)
    return fam


def build_batches(seeds, n_batches=BATCH_COUNT):
    """Partition into family-indivisible, size-balanced, deterministic batches.

    Longest-processing-time first: heaviest family goes to the currently lightest
    batch, ties broken by lowest batch index then by family_id. Deterministic
    for a given input -- same bank, same batches, every run.

    The only inputs to the placement decision are family identity and serialized
    size. No score, territory, quality or narrative field is consulted.
    """
    fam = group_families(seeds)
    order = {s["seed_id"]: i for i, s in enumerate(seeds)}
    items = sorted(fam.items(), key=lambda kv: (-_cost(kv[1]), kv[0]))

    buckets = [[] for _ in range(n_batches)]
    costs = [0] * n_batches
    for fid, members in items:
        i = min(range(n_batches), key=lambda k: (costs[k], k))
        buckets[i].extend(members)
        costs[i] += _cost(members)

    # restore bank order inside each batch so families read as contiguous blocks
    return [sorted(b, key=lambda s: order[s["seed_id"]]) for b in buckets]


def batch_manifest(seeds, batches):
    """The record of a purely mechanical decision, for audit."""
    fam = group_families(seeds)
    return {
        "batch_count": len(batches),
        "top_n_per_batch": TOP_N,
        "expected_semifinalists": SEMIFINALISTS,
        "algorithm": "family-indivisible LPT by projected serialized size",
        "deterministic_inputs": ["family_id", "projected_size_chars"],
        "total_seeds": len(seeds),
        "total_families": len(fam),
        "batches": [
            {
                "index": i + 1,
                "role": "script_seed_scout_batch_%d" % (i + 1),
                "session_name": "seed_scout_batch_%d" % (i + 1),
                "seed_count": len(b),
                "family_count": len({s["family_id"] for s in b}),
                "projected_chars": _cost(b),
                "projected_tokens_est": _cost(b) // 4,
                "seed_ids": [s["seed_id"] for s in b],
                "family_ids": sorted({s["family_id"] for s in b}),
            }
            for i, b in enumerate(batches)
        ],
    }


def scout_input(seeds, batch, index, history=None, canon_digest=None):
    """Everything one Scout receives. Identical rubric for all four; only the
    projected batch differs."""
    return {
        "role": "script_seed_scout_batch_%d" % index,
        "instructions": (
            "Examina TODAS las semillas de este lote. Compara familias, variantes "
            "y arcos entre si. Selecciona las %d con mayor probabilidad de "
            "convertirse en episodios excepcionales de MILO. Los scores "
            "historicos son evidencia secundaria y no deben decidir "
            "automaticamente. Busca potencial narrativo real." % TOP_N
        ),
        "selection_criteria": [
            "hook", "conflicto", "accion_visible", "emocion", "curiosidad",
            "milo_fit", "originalidad", "giro", "payoff", "retencion",
            "claridad", "visualidad", "viabilidad_45s", "diferenciacion_reciente",
        ],
        "canon_digest": canon_digest,
        "recent_history": history or [],
        "batch_size": len(batch),
        "seeds": [scout_projection(s) for s in batch],
    }


# ------------------------------------------------------------------ validation
def validate_scout_output(payload, allowed_ids, top_n=TOP_N):
    """Contract check only. Returns (ok, problems).

    Does not judge the choice, the reasons, or the ranking -- only that the
    reply is well formed and that the 15 IDs are real and belong to this batch.
    """
    problems = []
    if not isinstance(payload, dict):
        return False, ["payload_not_object"]
    cands = payload.get("candidates")
    if not isinstance(cands, list):
        return False, ["candidates_not_list"]

    if len(cands) != top_n:
        problems.append("WRONG_COUNT:%d!=%d" % (len(cands), top_n))

    allowed = set(allowed_ids)
    seen = []
    for i, c in enumerate(cands):
        if not isinstance(c, dict):
            problems.append("candidate_%d_not_object" % i)
            continue
        for f in ("rank", "seed_id", "why_selected", "strengths", "risks"):
            if c.get(f) in (None, ""):
                problems.append("candidate_%d_missing_%s" % (i, f))
        sid = c.get("seed_id")
        if sid not in allowed:
            problems.append("NOT_IN_BATCH:%s" % sid)
        seen.append(sid)

    dupes = {x for x in seen if x is not None and seen.count(x) > 1}
    if dupes:
        problems.append("DUPLICATE_IDS:" + ",".join(sorted(dupes)))

    return (not problems), problems


def collect_semifinalists(outputs):
    """Concatenate 4x15 into 60. No sorting, no dedup, no trimming.

    Hermes has no authority to remove candidates, so this function does not
    offer a parameter to remove one. Duplicates or a short list are caught by
    validation upstream and fail loudly rather than being silently fixed.
    """
    ids = []
    for i, out in enumerate(outputs, start=1):
        if not isinstance(out, dict) or not isinstance(out.get("candidates"), list):
            raise ValueError("SCOUT_OUTPUT_MISSING:candidates:batch_%d" % i)
        for c in out["candidates"]:
            if not isinstance(c, dict) or not c.get("seed_id"):
                raise ValueError("SCOUT_CANDIDATE_INVALID:batch_%d" % i)
            ids.append(c["seed_id"])
    if len(ids) != SEMIFINALISTS:
        raise ValueError("SEMIFINALISTS_NOT_%d:%d" % (SEMIFINALISTS, len(ids)))
    return ids


def hydrate(bank, ids):
    """Original, unmodified records for the QA/QC judge -- including
    desarrollo_requerido, which the Scouts never saw. The judge ends up with
    strictly more information than the Scouts did."""
    by_id = {s["seed_id"]: s for s in bank["seeds"]}
    missing = [i for i in ids if i not in by_id]
    if missing:
        raise ValueError("HYDRATE_MISSING:" + ",".join(missing))
    return [copy.deepcopy(by_id[i]) for i in ids]


def validate_qc_output(payload, candidate_ids):
    """Contract check on the judge's funnel. Winner must come from the 60."""
    problems = []
    if not isinstance(payload, dict):
        return False, ["payload_not_object"]

    allowed = set(candidate_ids)
    for stage, size in (("top_15", TOP_N), ("top_5", 5), ("top_3", 3)):
        v = payload.get(stage)
        if not isinstance(v, list):
            problems.append("%s_not_list" % stage)
            continue
        if len(v) != size:
            problems.append("%s_WRONG_COUNT:%d!=%d" % (stage, len(v), size))
        ids = [x.get("seed_id") if isinstance(x, dict) else x for x in v]
        for sid in ids:
            if sid not in allowed:
                problems.append("%s_NOT_IN_60:%s" % (stage, sid))
        if len(set(ids)) != len(ids):
            problems.append("%s_DUPLICATE_IDS" % stage)

    # funnel must be nested: top_3 inside top_5 inside top_15
    def as_set(k):
        v = payload.get(k) or []
        return {x.get("seed_id") if isinstance(x, dict) else x for x in v}
    if as_set("top_3") and not as_set("top_3") <= as_set("top_5"):
        problems.append("FUNNEL_3_NOT_IN_5")
    if as_set("top_5") and not as_set("top_5") <= as_set("top_15"):
        problems.append("FUNNEL_5_NOT_IN_15")

    w = payload.get("winner")
    wid = w.get("seed_id") if isinstance(w, dict) else w
    if not wid:
        problems.append("WINNER_MISSING")
    elif wid not in allowed:
        problems.append("WINNER_NOT_IN_60:" + str(wid))
    elif as_set("top_3") and wid not in as_set("top_3"):
        problems.append("WINNER_NOT_IN_TOP_3")

    return (not problems), problems


def selected_seed_document(episode_id, seed_id):
    """Created only from a validated judge reply."""
    return {
        "episode_id": episode_id,
        "seed_id": seed_id,
        "selected_by": "deepseek_seed_qc",
        "status": "SEED_APPROVED",
    }