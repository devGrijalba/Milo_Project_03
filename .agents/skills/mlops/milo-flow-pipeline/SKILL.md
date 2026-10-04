---
name: milo-flow-pipeline
description: "Use when generating or auditing Milo images in Flow."
version: 1.0.0
author: Hermes Agent
license: MIT
---

# MILO Flow Pipeline (FLOW-PORTABLE-1.0.0)

The validated production path for Milo images. Replaces the CDP route, which
Google flags as `UNUSUAL_ACTIVITY`.

## Route

```
D:\01_NUEVOS PROYECTOS\01_PROYECTO_DARK\03_FLOW-PORTABLE-1.0.0
```

Live transport = **Flow I2I Assistant extension + local bridge**
`ws://127.0.0.1:8765`. NOT CDP. Only Nano Banana 2, 1K/preview, 9:16, one
generation at a time. Package reference lives at
`D:\01_NUEVOS PROYECTOS\01_PROYECTO_DARK\MILO_PRODUCTION_PACKAGE_v1`.

## Order of operations (never reorder)

```bash
node tools/pre-generation-gate.js          # 5 checks, blocks before quota
node tools/generate-milo.js                # dry run, prints the exact plan
node tools/generate-milo.js --authorized   # ONLY with explicit approval
```

The gate runs as a **separate spawned process**, not an import, so a crash in
the gate can never be read as "gate said nothing, continue". Never generate
without the user's explicit authorization — quota is their call, not the agent's.

## Gate: what it checks, and what it must not do

1. `INDEX.json` exists (declares the canon)
2. all sha256 intact
3. attribute contracts hold
4. **the scene's plate is `environment_anchor`**
5. nothing `superseded` in the generative canon

Blocking rules that each cost a regression test:
- only a MEASURED present forbidden attribute is a violation
- `verified` missing ⇒ FAIL, not PASS
- `null`/not-measured ⇒ AVISO, never PASS or FAIL
- a gate that always fails gets switched off; one that always passes is decoration

## Lock authoring rules (learned from real quota burns)

- `RENDER` (13 words) + action (5) are FIXED. In `character_focused` only **12
  words** remain for space + light. `"dark night study"` (6) fits;
  `"inner theatre of the mind"` does not.
- Priority when over budget: `environment_identity > light_detail > render_fixed`.
  Compress the light, never the space name, never the global RENDER block.
- `framing_variants.<id>.prompt_en` overrides `base_space.prompt_en` for that
  ONE framing. Use it instead of mutilating a shared space.
- `compact` may OMIT but must not CONTRADICT `full`, and must not use words the
  negative bans. `light_en.compact` is an **array of strings**, not a string.
- Read the resolver before writing a lock field: `location_materials[framing]`
  holds light; `base_space.framing_variants` holds the space override.

## Environment audit

5 plates: 3 `environment_anchor` (MAIN_STUDIO, DARK_LIBRARY, MIND_THEATER — all
three generated in production), 2 `environment_inspiration` (CITY_NIGHT,
ANALYSIS_ROOM, both with burned text: `burned_text_detected`).

`environment_risk` has four fields: `text`, `logos`, `real_people`,
`human_like_elements`. Only the FIRST THREE degrade a plate. Masks and
silhouettes are a declared risk, not contamination — MIND_THEATER has six
masks and Milo's identity held.

## Vision before asking about a feature

- Locate the zone FIRST. A misplaced crop returns a confident false negative.
- Do not crop-and-rescale to read small text. `ANALYSIS_ROOM`'s list was legible
  at 900px full-frame and invisible in three correct crops.
- `not_evaluable` is a valid verdict. Iris colour at 768px medium shot is a
  resolution limit, not a defect — never report it as FAIL or PASS.
- Proxies at 300–400px for classification, ~900px for OCR/detail.

## Composition validator (diagnostic, not enforcement)

`node tools/validate-composition.js` finds concept-level contradictions between
prompt and negative. `node tools/test-composition.js` is its 13-case matrix.
Both are deliberately OUTSIDE `npm test` and NOT wired into the gate: connecting
them would block validated framings. Wire only after the canon is clean.

Contradiction = `nucleo` + `modificador` + **polaridad**, never a literal string.
Negation scope is 3 words and must not cross another noun, else
`"nothing in the room, a hard overhead light"` silently passes.

## Known state

V1.0 frozen. 5 known contradictions in the lock, declared in
`contracts/known_debt.json`, none affecting a validated generation. V1.1 =
sanitize lock → update hashes → clean validator → integrate into `npm test` →
wire to gate.
