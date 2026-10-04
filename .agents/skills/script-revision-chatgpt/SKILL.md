---
name: script-revision-chatgpt
description: "Use when writing, auditing, or rewriting short-video scripts with ChatGPT."
version: 0.1.0
author: Hermes Agent
license: MIT
---

# Script Revision with ChatGPT

Core principle: every script version is audited by ChatGPT in a closed loop (V1→V2→Vn) before spending on visuals, voice, or editing. No probability of virality is ever invented — only editorial diagnosis with quoted evidence until calibrated data exists.

## When to Use

- User asks to write, audit, or rewrite a Reel/Short script (30–90s).
- Any task ending with "audited script version + verdict READY/OPTIMIZE/REWRITE/HOLD saved to file".
- Iterative redaction review: hook, retention, emotion, visual, conversion, compliance.

## Hard Constraints

- NEVER touch the user's daily browser. ChatGPT runs in the kit's dedicated Chrome: `--remote-debugging-port=9222 --user-data-dir="<kit>/.chrome-chatgpt"`, headed; login is manual once by the user.
- DOM/CDP only: `querySelector`, ProseMirror insert + `InputEvent`, JS `click()`, Enter. Forbidden: mouse, pixels, screenshots for state decisions.
- Handshake per send (read-back exact, composer-cleared, stop-ELEMENT visibility + 2 stable polls, content-signature capture, one deadline, recapture-once, never blind reinject). Actor ends with `process.exit(code)`, never `browser.close()` on shared CDP.
- One FAIL on a critical gate (originality, factuality, hook-payoff deception) = HOLD/NO PRODUCIR, even with a 98/100 creative score.
- Scores use 0–4 anchored scale (0=absent/harmful, 1=weak, 2=functional, 3=strong, 4=exceptional). Every score cites the exact quoted fragment. Missing sources/assets/identity info = REVIEW/INSUFFICIENT EVIDENCE, never PASS.

## Core Pattern

Before: ask ChatGPT "is this viral? rate 0–100" → plausible number with no evidence, template rewrites, facts silently changed.

After: P0 iteration contract → per-dimension audit (0–4 + quote) → gates → scene/temporal map → directed rewrite of weak beats only, facts preserved → versioned save → next loop until READY.

## Workflow

1. **Launch / connect.** Start kit Chrome 9222 (see `launch-browsers.bat`). Playwright `connectOverCDP('http://127.0.0.1:9222')`, find `chatgpt.com` tab. Sign-in page → stop, user logs in manually.
2. **P0 contract (once per chat).** Inject the P0 prompt from `tasks/script_rev_task_example.json` (or §Prompts below). Require `CONTRATO ACEPTADO`. Use `?temporary-chat=true` for probe runs, normal chat for versioned work.
3. **Audit (Pn per turn).** Send ONE prompt per turn: P1 architecture, P2 hook+retention, P3 directed rewrite, P4 human-voice checklist, P5 scenes+temporal, P6 compliance gate, P7 decision. Capture each response to `out/<script_id>_q<N>__chatgpt.md` (idempotent, never overwrite valid file).
4. **Score outside the LLM.** Convert 0–4 items to dimensions: `D = 25 * mean(items)` (0–100). Editorial score: `EDS = .18H + .25R + .10N + .14E + .11O + .10V + .12C`. Compute in JS/Python, never let the LLM total its own score.
5. **Non-compensatory rules.** Hook clarity<2 or hook-payoff alignment<2 → `H=min(H,50)`. Scene redundancy `A=0 ∧ I=0` → merge/delete candidate. Two consecutive beats `T≤1 ∧ I≤1` → retention-valley flag.
6. **Directed rewrite.** Rewrite ONLY beats scoring 0–1, preserving verified facts (names, dates, claims). Each fix: exact weakness + 1-sentence viewer consequence + 1 concrete rewrite instruction. Never touch 3–4 beats unless they cause a structural failure.
7. **Compliance before production.** Evaluate `G = C_R×C_AI×C_L×C_D×C_O×C_M×C_S` (rights, AI disclosure, likeness/voice, deception/factuality, originality/reuse, monetization safety, sponsorship). Any critical FAIL → HOLD regardless of EDS. File a Rights&AI manifest per script version.
8. **Verdict + version.** Output per version: gates | dimension scores | top-3 strengths | top-3 failures | mandatory changes | verdict (READY/OPTIMIZE/REWRITE/HOLD) | confidence. Save `out/<script_id>_<version>_AUDIT.md`. Loop until READY or HOLD. Terminal: READY without arena duel + winner delivery = INCOMPLETE (see reel-contest-arena §Terminal State).
9. **Recover.** 3 straight TIMEOUTs or stuck chat → fresh chat, close stuck tab, 1 retry. One poller per conversation.

## Scoring Dimensions (initial editorial priors, NOT algorithm weights)

| Dim | Weight | Items (0–4 each) |
|---|---|---|
| Hook (H) | 18% | clarity, specificity, curiosity gap, stakes, expectation violation, relevance, payoff promise, first-frame visual |
| Retention (R) | 25% | central question, causal progression, revelation density, escalation, compression, transition pull, climax, payoff |
| Narrative anchor (N) | 10% | goal/question, stakes, agency/motion, vulnerability, contradiction, specificity, change/resolution (genre-adapted) |
| Emotion (E) | 14% | dominant emotion, identification, activation, progression, contrast, earnedness, human detail, residual payoff |
| Distinctiveness (O) | 11% | novel angle, non-cliché, concrete details, voice, believable surprise, low template risk |
| Visual (V) | 10% | concreteness, distinct states, opening image, iconic shot, movement, continuity feasibility, visuals add info |
| Conversion (C) | 12% | share motive, comment motive, identification, follow reason, series potential, CTA naturalness |

Scene vitality: `SVS = 25*(.20A+.20T+.20I+.15E+.15V+.10F)` (advance, tension, info, emotion, visual, forward-pull). Bands: 80–100 keep, 65–79 compress, 50–64 rewrite/merge, <50 cut/merge candidate.

## Prompts (P0–P7, copy-paste ready)

**P0 — iteration contract:** "Actúa como comité editorial adversarial para guiones de Reels/Shorts 30–90s. REGLAS: (1) nunca inventes probabilidades de viralidad; (2) escala 0–4 con fragmento citado por score; (3) distingue originalidad-plataforma vs distinción creativa; (4) flag AI-genericity observable, nunca claims de detector; (5) por cada 0–1: debilidad + consecuencia en 1 frase + 1 instrucción de reescritura preservando hechos; (6) puedes devolver REWRITE/HOLD; (7) sin fuentes/assets/identidad info → REVIEW, nunca PASS; (8) salida fija: Gates|Scores|Top3+|Top3−|Cambios|Veredicto(READY/OPTIMIZE/REWRITE/HOLD)|Confianza. Confirma con CONTRATO ACEPTADO."
**P1 — architecture:** "Con gates + 7 dimensiones + SVS + mapa temporal, diseña el loop V1→Vn: estados con criterios de salida, qué pido yo vs devuelves tú por turno, definición de READY, qué se guarda por versión."
**P2 — hook+retention audit:** "Audita HOOK y RETENCIÓN del guion pegado con la tabla de items 0–4 + citas. Aplica H=min(H,50) si claridad<2 o hook-payoff<2. Flags de redundancia y valle de retención."
**P3 — directed rewrite:** "Reescribe SOLO los beats 0–1, preservando hechos verificados. Formato: debilidad exacta + consecuencia + instrucción + texto reescrito. Marca INSUFFICIENT EVIDENCE donde falte dato."
**P4 — human voice:** "Convierte la lista AI-genericity (abstracción, superlativos vacíos, moraleja no ganada, vaguedad, ritmo template, cliché, duplicación visual, sentimentalismo) en checklist con señal + ejemplo malo + reescritura + test de especificidad. Cierra con 5 frases prohibidas y reemplazo."
**P5 — scenes+temporal:** "Auditoría escena-por-escena (A/T/I/E/V/F 0–4 + SVS + decisión KEEP/REWRITE/MERGE/DELETE) y mapa por fases 0–3/3–10/medio/clímax/cierre: pregunta viewer, info, tensión/emoción DOWN-FLAT-UP, cambio visual, riesgo LOW-MED-HIGH + causa."
**P6 — compliance:** "Evalúa G=C_R×C_AI×C_L×C_D×C_O×C_M×C_S (PASS/REVIEW/FAIL + evidencia + acción). Un FAIL crítico=HOLD aunque EDS=98. Incluye manifiesto Rights&AI YAML. Recuerda: disclosure IA ≠ permiso copyright ≠ permiso likeness ≠ disclosure publicitario."
**P7 — decision:** "De EDS a decisión PRODUCE/OPTIMIZE/REWRITE/HOLD sin inventar probabilidad: qué guardar por guion, normalización por cohorte (plataforma×nicho×duración×formato×periodo→percentil), HIT=top-quartile de cohorte propia, expected utility Σa_k·Lift−λ·Costo, loop Score→Lock→Produce→Publish→Collect→Retrain."

## Output Convention

- Per-turn: `out/<script_id>_q<N>__chatgpt.md` (prompt quoted + `---` + response + `<!-- hash:<12> duration:<s> -->`). Idempotent.
- Per-version audit: `out/<script_id>_<version>_AUDIT.md` (gates, scores, SVS table, temporal map, verdict).
- Never overwrite a valid artifact with a later capture. Hash = sha256(text)[:12]; new response requires hash != prev hash.

## Quick Reference

| Step | Check | Fail action |
|---|---|---|
| Snapshot | composer + send found (3 hydration tries) | recovery selectors → abort INPUT_NOT_FOUND |
| Read-back | exact normalized match | abort, never send |
| Submit | composer cleared ≤5s | resend once, else recovery |
| Done | stop ELEMENT hidden + 2 stable polls | deadline → recapture once |
| Capture | non-empty, new hash, echo excluded | recovery, never blind reinject |
| Score | computed outside LLM | reject LLM totals |

## Common Mistakes

- Asking "rate 0–100 / viral %?" → false precision. Always 0–4 items + external math.
- Letting the LLM rewrite verified facts → lock names/dates/claims, flag gaps.
- Compensating a gate FAIL with a high EDS → HOLD always wins.
- Capturing by message index → content signature only (chats virtualize).
- `browser.close()` on shared CDP → kills every agent. `process.exit()` only.
- Driving the daily Brave/Chrome → kit profiles only.

## Red Flags

- Response contains a "viral probability %" without calibrated model outputs.
- Scores with no quoted evidence from the script.
- Rewrite changed names, dates, or factual claims silently.
- Valid artifact overwritten by a later capture.
- Two pollers on port 9222 at once.


## Additional Story Intelligence Audit (v2.0)

Before approving a rewrite, perform:

### Character Continuity Check
If a recurring character exists:
- Do not reintroduce them unnecessarily.
- Preserve voice, worldview and behavioral patterns.
- Ensure the episode belongs to that character.

### Humanity Check
Find at least one detail that could only belong to this person.

### Boredom Check
Identify any sentence that can disappear without reducing story value.

### Promise Contract
State:
- Opening promise
- Viewer expectation
- Required payoff
- Whether ending satisfies it

### Replaceability Test
Flag generic characters, places or conflicts.
