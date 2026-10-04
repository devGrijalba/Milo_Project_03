---
name: milo-story-success-engine
description: 'Use when choosing a MILO story before production.'
---

# MILO_STORY_SUCCESS_ENGINE

Sits between story design (`MILO_STORY_DESIGN_MASTER`) and production (`milo-episode-production`): no images, TTS or render run on a weak story. Goal is statistical, not oracular — maximize success probability and learn per publication. Nobody guarantees a script wins before publishing (algorithm, audience, execution, competition, timing, distribution luck all count).

## Pipeline

IDEA → CANDIDATOS → OPENING LAB → ADVERSARIAL REVIEW → SIMULACIÓN DE RETENCIÓN → SELECCIÓN → GUION FINAL → PRODUCCIÓN → MÉTRICAS REALES → APRENDIZAJE

## 1. Retention-first generator contract

Never ask for "a viral 40 s story". Force retention architecture first; internally produce Idea → Promesa → Curiosity Gap → Hook visual/verbal → Pregunta abierta → Escalada → Micro-recompensas → Giro → Payoff → Última impresión. Iron rule: EVERY segment must justify why the viewer needs the next one — a scene that only explains without raising curiosity, tension, emotion or expectation gets cut or rewritten.

## 2. Five roles (panel LLMs via Chrome CDP, `inject()` contract)

Writer = ChatGPT, PRIMARY STORY AUTHOR (see `milo-episode-production/references/chatgpt-author-service.md`: STORY_CONTEXT_PACKET in, immutable raw out, REPAIR_PACKET for targeted fixes — Hermes never rewrites narrative itself) · Retention Critic (attacks retention) · Audience Simulator (predicts abandonment per second) · Story Editor (proposes repairs as packets, never direct edits) · Judge (blind — never knows which model made each candidate). Blindness is structural: strip authorship before judging. Critics never replace the author; their observations return to ChatGPT, which produces the corrected STORY VERSION +N (no Frankenstein chains).

## 3. Survival curve (predicted, per candidate)

| Tiempo | Pregunta del sistema |
|---|---|
| 0–1 s | ¿Hay motivo inmediato para detener el scroll? |
| 1–3 s | ¿Entiendo que algo ocurre sin recibir toda la explicación? |
| 3–5 s | ¿Existe una pregunta que quiero resolver? |
| 5–10 s | ¿La situación cambió o escaló? |
| 10–20 s | ¿Recibí recompensa y apareció una nueva incógnita? |
| 20–30 s | ¿La historia sigue avanzando? |
| 30–38 s | ¿Estoy esperando activamente el desenlace? |
| final | ¿El payoff justifica los segundos anteriores? |

Each row gets PASS/FAIL with cited evidence (exact second + element). Procedure: `references/retention-simulation.md`.

## 4. FAIL EARLY = FAIL STORY

Even with an extraordinary twist at second 35, a candidate the Opening Lab expects to bleed too much audience before second 5 never enters production. Improving the payoff is useless if most viewers never reach it (Textopia/MILO precedent).

## 5. Champion / Challenger

The best historical pattern is CHAMPION; every new script is CHALLENGER. A Challenger enters production only by beating the Champion on defined criteria or by carrying a concrete experimental hypothesis (one variable, recorded). This stops Hermes forgetting what it learned and rewriting pretty but unretentive stories.

## 6. Prediction is not evidence (calibration)

LLM scores (HOOK_SCORE, VIRAL_SCORE) select WHAT to publish; Facebook metrics decide WHO WAS RIGHT. Keep both series per episode; when 90–100-scored stories stop consistently beating 80–89 ones, the evaluator is miscalibrated — say so and adjust weights with evidence, never silently.

## 7. Artifacts (per episode, `01_historia/`)

`candidate_pool.json` · `adversarial_reviews.json` · `retention_simulation.json` · `selection.json` (winner + citable reasons + losers with cause) · `story_evidence.md` (human-readable why). Schemas: `references/schemas.md`.

## 8. Failure handling

Any step failure runs AUTO-RECOVERY (`milo-story-performance-loop.md` §6, CDP steps via `chrome-cdp-injection.md` §7): detect → formulate → inject → contrast → lowest-risk fix → QA re-run → continue. Human only for the truly unresolvable.
