---
name: milo-batch-production
description: "Use when producing 2+ MILO episodes with no humans."
version: 1.0.0
author: Hermes Agent
license: MIT
---

# MILO Batch Production Protocol (self-sufficient, no human consults)

## Intake contract (fail-closed)

Each episode arrives as a ZIP with: SCRIPT_LOCK (hook + story), visual blueprint (S01-S06), audio direction, caption rules, thumbnail direction, behavior log seed. Two intake tiers: (a) FULL script with narration beats → produce directly; (b) BIBLE-only (premise/wound/symbol/structure, no voiceover) → Hermes authors the narration (Spanish, MILO tone, hook = wound in S01, connection-loss before reveal, protected reveal). Premise/wound/symbol are IMMUTABLE; only the wording is authored. Missing premise itself = log BLOCKED, continue with the rest. Never ask the human.

## Phase 1 — Season bible (sequential, all episodes, before producing any)

Read every script. Write `PROJECTS/BATCH_<n>/SEASON_BIBLE.md`: emotional arc per episode (one line each), conflict-similarity matrix (flag pairs sharing mechanism), differentiation fixes (minimal script-neutral direction notes). This prevents 6 clones.

## Phase 2 — Scaffold all (sequential, cheap)

Per episode: create `PROJECTS/EP00X/` with 00_SESSION/01_SCRIPT/02_VISUAL/03_AUDIO/04_CAPTIONS/05_THUMBNAIL/06_QC/07_MEMORY/08_LOG + applied-patches record. `orchestrator.py log EP00X SCRIPT PASS` then `advance`. Stop scaffolding only on corrupt ZIP (BLOCKED + continue).

## Phase 3 — Flow image queue (STRICTLY SEQUENTIAL, one runner)

> **Route changed.** The CDP driver below is superseded: Google detects CDP as `UNUSUAL_ACTIVITY`. The live path is the Flow I2I Assistant extension + local bridge, references staged into `insumos/`, manifest driving `generate-milo.js`, with `pre_generation_gate` run BEFORE any submit. See skill `milo-flow-pipeline`.

> **Route changed.** The CDP driver below is superseded: Google detects CDP as `UNUSUAL_ACTIVITY`. The live path is the Flow I2I Assistant extension + local bridge, with references staged into `insumos/` and a manifest driving `generate-milo.js`. Run `pre_generation_gate` BEFORE any submit; it blocks a vetada plate and a violated contract before quota is spent. See skill `milo-flow-pipeline`.

Flow's composer/grid/batches are SHARED per project: parallel submits cross-attribute results. Never run two cdp_episode.py against the same project concurrently, not even via subagents.

Per episode, in order: build plan (anchor-first: MILO_CHILD + world anchor + prev-scene chain; new characters get a MASTER asset first with refs []), pilot S01 alone, Gemini QC >=80, then batch S02-S06. Launch contract from `flow-cdp-operation` applies (4 env vars, live project id, seeded locklabels for thumb runs). Promote 6 PNGs to `04_ASSETS/`, `log VISUAL PASS`.

## Phase 4 — Audio + captions + thumbs (parallel-safe per episode)

ElevenLabs (audio_agent.py), faster-whisper local, caption director, ffmpeg render, thumb CDP run: all parallelizable ACROSS episodes except Flow CDP. Flow thumb runs join the Phase-3 queue. Caption rules: TOP always, 1 thought = 1 card, <=10 words, reveal <=6, QC file before render.

## Phase 5 — Render + director QC (sequential audit, EP order)

First episode sets the bar: full director QC (identity/continuity/captions-top/connection-loss) before rendering the rest. ffmpeg render contract: `-loop 1` image inputs REQUIRE `trim=end_frame=N,setpts=PTS-STARTPTS` per segment or concat sticks on S01 (verified live). Pixel-verify day/night progression per scene after every render.

## Phase 6 — Batch quality report + close

Write `PROJECTS/BATCH_<n>/BATCH_QUALITY_REPORT.json` (identity x/6, emotional consistency, visual consistency, retention risks, per-episode issues). Per episode: PUBLISHING_PACKAGE.json (3 headlines, copy, hashtags, first comment), `log PUBLISH PASS`, `advance` → DONE.

## Autonomy rules

- Retry budgets: Gemini QC 3 attempts then transport-cooldown (90s+), never PASS on API_FAIL. OpenRouter free is second-opinion only, never a gate.
- Spend: ElevenLabs + Flow are pre-authorized episode costs; log usage per episode in the batch report.
- Human contact: only on external blocks (CDP profile logout, Flow outage, corrupt intake). Reviews pasted later apply as surgical corrections on the edit, never full rebuilds.
