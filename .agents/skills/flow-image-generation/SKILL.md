---
name: flow-image-generation
description: "Use when generating images with Google Flow in batch."
version: 1.1.1
author: Hermes Agent
license: MIT
---

# Flow Image Generation

Core principle: blank project first, batch-first generation, verify once at the END on downloaded files. Never screenshot-verify intermediate steps.

## When to Use

- User asks for images from Google Flow (labs.google/flow or flow.google.com).
- Any task ending with "N downloaded images + QA report".
- Single-image fixes after a batch.

## Hard Constraints

- NEVER touch the user's daily browser. Dedicated Chrome with own `--user-data-dir` + `--remote-debugging-port`, headed; user logs into Google once manually. Drive via Playwright `connectOverCDP`. Never type passwords.
- **CDP route is deprecated for Milo.** Google flags CDP as `UNUSUAL_ACTIVITY`. The live route is the **Flow I2I Assistant extension + local bridge** (`ws://127.0.0.1:8765`). See skill `milo-flow-pipeline` for the working path; everything below describing CDP/grid/card-chains applies only to legacy projects.
- DOM/CDP only. No mouse, no pixels, no screenshots for decisions.
- Transport handshake from skill `cdp-injection-handshake` applies to every prompt send (read-back, composer-cleared, deadline + recapture).
- Credentials/prompts never pasted into external docs; keys live in project `.env`, read from disk.

## Approved Operating Procedure (user-mandated reference, overrides batch defaults)

1. Abrir el explorador.
2. Clic en Nuevo proyecto 0.5 s luego de abrir.
3. Inyectar la imagen modelo.
4. En loop: inyectar los prompts de las 5 imágenes.
5. Abrir la primera imagen: descargar, 2K.
6. Situarse en la segunda imagen: descargar, 2K.
7. Situarse en la tercera imagen: descargar, 2K.
8. Situarse en la cuarta imagen: descargar, 2K.
9. Situarse en la quinta imagen: descargar, 2K.

## Chaining Rule (prevents stall between inject and download)

Steps 1-9 run as ONE unbroken chain per batch: after the inject loop, poll the grid until the expected card count appears, then download in order without returning control between phases. A script that ends at step 4 strands the batch. Always navigate back to the CURRENT batch project (never a hardcoded prior project id) before the download phase.

## Hard-Learned Rules (session-validated, mandatory)

- Card order is newest-first; uploads/references sort after generations. Open the FIRST visible card, never the last in DOM. Verify the detail shows the beat's prompt keywords before downloading (a uuid route alone proves nothing — it can display the reference).
- One unbroken chain per beat: inject (read-back + arrow submit) → 12 s → open first card → download → 2K → back. No turn gaps or parallel watchers mid-chain: a second driver navigating the same page corrupts fills and clicks.
- Grid selectors rot: `/asb/` thumbnails today, `flow-content` URLs tomorrow. If the count reads 0 while images are visible, the selector is stale — screenshot and re-derive, never declare absence.
- Never inject raw SH/spec files (Visible/Contact/TO_DESIGN leak into generations as literal text and logos). Inject clean prompts only: action + identity anchor + style + merged Avoid, with the character reference attached.
- Map downloads to beats by VISION content, never by send order or grid position. Mislabels get renamed; wrong-beat files get REJECTed, not force-fit.
- The 2K menu has two shapes (resolution submenu vs direct 'Descargar contenido multimedia' = lower res). If no 2K option appears, the file is below minimum — retry from the card, don't accept it.

## Core Pattern

Before: reuse prior Flow project, send prompts one-by-one with screenshot checks, download thumbnails → uuid contamination, slow, 768px files below minimum.

After: fresh blank Flow project → inject ALL prompts (serialized, paced) → generate → download at MAX resolution via per-image menu → single file-level QA at end → regenerate rejects with delta prompts.

## Workflow

1. **Setup.** Launch dedicated Chrome: `chrome.exe --remote-debugging-port=9222 --remote-allow-origins=* --user-data-dir=C:/Users/Ivan/AppData/Local/hermes/cdp-chrome-profile --no-first-run --no-default-browser-check`. The origins flag is MANDATORY (without it the WS returns 403). Confirm with `curl -s http://127.0.0.1:9222/json/version`. Open Flow, confirm login. If sign-in → stop, user logs in. Then run `97_CDP_RUNBOOK/cdp/0_recon.py` before anything else.
2. **Blank project.** Create a fresh empty Flow project. Never reuse a prior project (grid contamination breaks uuid tracking).
3. **Prepare batch.** Prompt list = one entry per image: `{beat, prompt, aspect, count}`. Reference upload (if any) via Playwright filechooser/`setFiles`, never native dialogs.
4. **Inject (serialized, paced).** Resolve the composer FRESH before every send: Flow mutates it between sends (contenteditable DIV ↔ TEXTAREA). Wait up to 90s for either visible selector. Inject per tag (TEXTAREA → native value setter; DIV → focus + `execCommand('insertText')` + `beforeinput` chain). Read-back exact. Submit confirm = the PROMPT LEFT THE BOX (differs from sent text), NOT an empty box — after submit Flow holds a job token in the composer. Sends SERIALIZED with ≥8s pacing. Parallelism = N worker tabs for generation (CAP 4 — Flow throttles).
5. **Generate + track.** Grid thumbnails use `/asb/` urls (dedupe repeats — collect UNIQUE); the DETAIL view (`/edit/<uuid>`) holds the `flow-content` uuid AND the full prompt text. Map cards to beats by prompt keywords in detail view (never grid order; never thumbnail text — grid cards carry no text). When the user directs card selection, open the FIRST visible card (not the last in DOM — uploads/references sort after generations). Clicking a grid card may navigate the tab in place: re-acquire the grid tab every iteration and close detail tabs after each download (keep single project tab).
6. **Download at MAX.** Per-image card → Descargar → 2K/4K menuitem → download event → `saveAs` canonical name. Never the 768px display fetch; project-zip is review/spares only (1K). Map ids to beats by content-md5, never grid order.
7. **Single QA at end.** Vision/file check on DOWNLOADED files only (resolution ≥ minimum, prompt match, artifacts). Re-check only on anomaly or final delivery.
8. **Fix loop.** Single corrections: inject ONLY that beat's prompt, regenerate, download ONLY that image. Never re-run the full batch for one fix. Regenerate rejects with delta prompts until PASS.
9. **Deliver.** Only PASS candidates + QA report (`*_FLOW_QA.md`: per-image PASS/REJECT + reason + file path). Never present candidates for the user to choose from — pick the best, deliver it.

## Defaults & Schemas (self-contained)

| Param | Value |
|-------|-------|
| CDP port / profile | `9222` / `C:/Users/Ivan/AppData/Local/hermes/cdp-chrome-profile` (dedicated, headed; V2 project) |
| Send pacing | SERIALIZED, 8–12s between submits; input must empty ≤5s else resend once |
| Per-prompt deadline | 180s (inject→asset visible); on expiry recapture grid once, then resend missing only |
| Worker tabs | NONE in V2 — no batch runner exists. SEQUENTIAL, one image at a time via `97_CDP_RUNBOOK/cdp/` (grid + batches are SHARED → parallel submits risk cross-attribution) |
| Batch size | 1 per chain; never full re-run for single fix |

Batch entry schema:

```json
{ "beat": "beat02", "prompt": "...", "aspect": "16:9", "count": 1, "reference": "optional/path.png" }
```

Defaults: `aspect = "16:9"`, `count = 1`. Slug for filenames = lowercase ASCII, no spaces (`a-z0-9-`, max 40 chars).

## Download & Naming

- Canonical file: `<batch>_<beat>_<slug>_v001.png` (e.g. `h57_beat02_calle-lluvia_v001.png`). Version increments, never overwrite.
- Download path: per-image card → `Descargar` → menuitem `2K` (fallback `4K`/`1K original` if 2K absent) → download event → `saveAs` canonical. NEVER display-fetch thumbnails.
- Minimum resolution: width ≥ 1024px hard floor; 2K menu target width ≥ 1920 (accept ≥ 1600 if Flow labels 2K differently). Measure with:
  `ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 file.png`
- Map asset→beat by file content-md5 (`md5sum` / `Get-FileHash -Algorithm MD5`), never grid order. Dedupe repeated grid thumbnail URLs (collect UNIQUE per worker).
- QA report: `<batch>_FLOW_QA.md` with one row per image: `beat | file | PASS/REJECT | reason`.

## QA Checklist (concrete PASS criteria)

| Check | PASS | How |
|-------|------|-----|
| Resolution | width ≥ 1024 (target ≥ 1920) | ffprobe above |
| Prompt match | main subject + setting present, no contradicting element | file-level visual check |
| Artifacts | no garbled faces/hands/text, no watermarks | file-level visual check |
| Aspect | matches requested ±5% ratio | ffprobe w/h |
| File | opens, non-zero bytes, md5 logged | `ls` + md5 |

Any FAIL → REJECT with reason → regenerate that beat with delta prompt until PASS.

## Prompt QA Protocol (mandatory, silent — never show the audit, deliver only the approved prompt)

No image prompt is delivered straight after drafting. Internally audit and rewrite until every gate below is PASS. Responsibility = minimize generator misinterpretation, not write pretty prompts.

1. Requirements extraction: identity, reference, composition, shot/framing, element hierarchy, exact object counts, positions, expression, wardrobe, setting, light, style, aspect, zones to fill vs keep free, banned elements, text/logo policy. Nothing omitted.
2. Conflict detection: no instruction may contradict another (close-up vs wide staging; full-bleed vs white fades; POV-holding-phone vs no-realistic-hands — resolve HOW the phone is held). Ambiguity resolved before delivery.
3. Visual hierarchy: explicit main/secondary/background, attention order, relative sizes, what may blur.
4. Composition control: subject position, scale, depth (fg/mg/bg), camera direction/distance, head/foot room, edge treatment. Every zone that must not be empty gets NAMED visual content to fill it — 'no blank area' alone is insufficient.
5. Identity control: reference wins absolutely; no age/gender/anatomy/clothes/color reinterpretation, no added or beautified traits.
6. Counts as hard constraints: 'four blocks' = exactly four; 'one person' = no silhouettes, reflections, extra hands or figures.
7. Negative review per item: no generic negative list as substitute for good composition; positive prompt must not induce what the negative bans.
8. Text/UI control: banned legible text = no real words, numbers, app names or recognizable interfaces — abstract shapes/blocks/unreadable marks only, exact structure/count/order respected.
9. Adversarial read: ask how the generator could misread this (white zones, tiny hero, deformed hands, extra people, invented text, duplicates, wrong counts, identity drift, color shift, fades, wrong crop) and close each hole.
10. Final simulation: mentally render ONLY from what's written; any plausible violation = rewrite, no delivery.
11. Approval checklist — all PASS or no delivery: identity, composition, hierarchy, framing, counts, colors, style, background, canvas edges, text/UI, negatives, no contradictions, no material ambiguity.
12. Post-generation: compare the produced image against EVERY original requirement (PASS/FAIL each, no 'close enough'); any relevant FAIL → locate the prompt hole, fix it, return a corrected prompt version automatically.

## Milo Series Failure Registry (regression tests — every past failure is a preventive check on all future Milo prompts)

**THE FIVE EXPENSIVE ONES (measured in the FLOW-PORTABLE canon, each cost real generations). These are not style advice — each one is a proven quota-burner:**

- **A reference file's name does not describe its content.** A file named `TORSO_WARDROBE` was a near-full body WITH a complete face. Flow blended that face with the identity reference and produced a human face for a smooth-sphere character. Fix: every reference declares an `attribute_contract` with `allowed`/`forbidden`, and a `verified` block recording what was MEASURED (not what was declared). A `forbidden_attribute` present is blocking.
- **A gate that approves what it did not measure is not a gate.** `verified` missing ⇒ FAIL, never PASS by default. `null` (not measured) ⇒ AVISO, never PASS and never FAIL. A gate that always fails gets ignored, which is worse than having none.
- **Crop coordinates belong to the FILE, not the concept.** Waist is at 47% in one anchor and 69–79% in another. Reusing a fraction across files cuts through the chest and the crop ships a face nobody declared.
- **A face crop that includes clothing contaminates the identity reference.** Identity crop must exclude collar/shoulders; wardrobe crop must exclude head.
- **A `compact` tier may not contradict its own `full`.** The mapper picks `compact` in short mode. A compact of `"a dark void"` under a full of `"an inner theatre of the mind"` silently deletes the environment's identity, and the shot becomes un-evaluable against its own criteria.

Seeded from production history; append each new confirmed failure with date-free lesson form ('trigger → preventive check'):
- white/paper fade lower third → verify every prompt names painted content for the bottom 25% AND bans blank/vignette-to-white.
- phone/timer/list too small or secondary when hero → verify hero size/position explicit.
- realistic/detailed hands or extra fingers → mitten-like simplified hands + no-realistic-hands in Avoid + staging that minimizes hands.
- legible AI text/numbers in UI → abstract UI only, exact text in post; never describe words/numbers.
- wrong block/item counts → exact count stated twice (positive + negative).
- Milo over-protagonist when background role needed → explicit scale/position/role per beat.
- identity drift (tuft/hair/ears/hoodie color) → full identity anchor verbatim + identity-only reference attached.
- reference composition copied (blank area) → reference is identity-only, never layout.
- generic garment in the identity lock ('hoodie') overriding the attached suit ref → wardrobe is NEVER in the lock; per-anchor WARDROBE map (`wardrobe_for()`), world/set anchors resolve to no-clothing, unknown refs hard-stop the prompt.
- bald dome head → lock must name hair explicitly (messy spiky black hair + cyan-blue rim highlights); never assume the ref's hair transfers.
- slit/cyan eyes vs round white dot eyes → lock must name eye SHAPE ('two small perfectly round circular pure-white glowing dot eyes'); 'glowing eyes' alone drifts.
- full-photoreal character vs anime turnaround ref → CHARACTER_STYLE: anime cel-shaded character inside cinematic night scene; never let a 'photorealistic' suffix touch the character.
- legible text copied from text-bearing refs (mug/books/laptop) → refs with text infect generations despite negative; flag in QC, fix in positive prompt ('blank covers, no legible text') or accept as world aesthetic.
- 'glowing white eyes' positive vs 'white burned-out eyes' negative → model paints pure-white discs; describe eyes with shape + gentle halo instead.
- prompt requires a concept the negative bans → compare `nucleo + modificadores + polaridad`, never a literal string. `"one hard overhead light"` violates `"hard directional light"`; `"no direct source"` does NOT (it negates it). Negation scope is 3 words and must not cross another noun.
- a conceptual environment does not fit the word budget → `environment_identity > light_detail > render_fixed`. Compress the LIGHT. Never the space name, never the global RENDER block. Then scope the fix with `framing_variants.<id>.prompt_en`.
- micro-detail (iris colour) unverifiable at 768px wide in a medium shot → report `not_evaluable`, never FAIL and never PASS. Repeated failed zooms mean a RESOLUTION limit, not a defect; fix with a closer framing, not a retry.
- prompt requires a phrase the negative bans → the concept is `nucleo + modificadores + polaridad`, never a literal string. `"one hard overhead light"` violates `"hard directional light"`; `"no direct source"` does NOT (it negates it). Negation scope is 3 words and must not cross another noun.
- a conceptual environment does not fit the word budget → `environment_identity > light_detail > render_fixed`. Compress the LIGHT. Never the space name, never the global RENDER block. Then use `framing_variants.<id>.prompt_en` as an override scoped to that single framing.
- micro-detail (iris colour) unverifiable at 768px wide in a medium shot → report `not_evaluable`, never FAIL and never PASS. Four zoom attempts that all fail to resolve a detail is a RESOLUTION limit, not a defect. Fix is a closer framing, not a retry.
A previously seen failure must never recur for lack of prompt precision — check the registry before approving each new prompt.

## Script-to-Visual Quality Gate (mandatory before ANY image prompt)

Pipeline is: script → visual beat → SCENE CONTRACT → prompt → semantic QA → continuity QA → approve/reject → deliver. Never script → pretty prompt → deliver.

### Scene contract (internal, per scene)

1. NARRATIVE BEAT: single story event the image must communicate.
2. REQUIRED ACTION: what the character physically does.
3. REQUIRED OBJECTS: objects explicitly needed by the script.
4. REQUIRED EMOTION: emotional state to communicate.
5. TEMPORAL CONTINUITY: time of day, location, lighting, relation to adjacent scenes.
6. POST-PRODUCTION ELEMENTS: text, subtitles, exact clock values, karaoke, UI labels, SFX — reserved for post, NEVER generated in-image.
7. FORBIDDEN INVENTIONS: no prominent objects, actions, occupations, routines or story events unsupported by script, continuity, or character bible.

Priority: narrative accuracy > visual beauty. Decorative environment (lamp, sofa, plant, cup, curtain) allowed only if it cannot alter narrative meaning. Every prominent object/action must trace to (A) script, (B) established continuity, or (C) visual bible — else remove it.

### Mandatory QA (silent)

- QA-1 SCRIPT MATCH: prompt shows the exact scene beat?
- QA-2 NO HALLUCINATED STORY ELEMENTS: any significant object/action absent from source?
- QA-3 VISUAL READABILITY: without voice-over, is the beat roughly understandable? Complete: 'The image communicates ___.' — must equal the beat.
- QA-4 CHARACTER LOCK: identity vs master reference intact (insert MILO_IDENTITY_LOCK verbatim, never reworded per scene).
- QA-5 CONTINUITY: location, lighting, time, emotional state coherent with adjacent scenes?
- QA-6 PRODUCTION SEPARATION: text/clocks/captions/karaoke reserved for post?
- QA-7 PAYOFF PROTECTION: setup/reversal/punchline visually preserved? (Final scenes: the payoff event must be UNMISTAKABLE in-image.)

HARD-FAIL: QA-1, QA-2, QA-3 or QA-7 FAIL = prompt never leaves; rewrite + re-QA. No numeric pass ('83/100') overrides a story mismatch.

BEAUTIFUL-BUT-WRONG RULE: an aesthetically strong prompt that tells the wrong story is INVALID. Story fidelity > style > decorative richness.

## POST-QA: Image Gate (mandatory AFTER generation, before any human review)

Two gates, never one: Gate 1 = prompt QA (is the prompt right?); Gate 2 = image QA (did the IMAGE achieve it?). Evaluate the pixels, never the prompt's intentions. A beautiful-but-wrong image is REJECTED, not forwarded.

Per generated image, verdict PASS/FAIL/PARTIAL each:

- ORIENTATION: truly upright native composition in the requested aspect (not rotated/sideways)? FAIL = auto-regenerate, never reaches the user.
- SCRIPT MATCH: does the produced image show the scene's beat?
- REQUIRED ELEMENTS: did every mandatory contract element actually appear?
- HALLUCINATION: did the model add anything that changes the story?
- CHARACTER LOCK: is the character still on-model?
- CONTINUITY: time, room, light, wardrobe, emotional progression vs adjacent scenes?
- PUNCHLINE (payoff scenes, strictest): would a muted viewer grasp the gag? Ambiguous gag = FAIL.

Any FAIL → REJECT with reason → single-beat regenerate with delta prompt → re-POST-QA. PARTIAL (e.g. base image right but an action beat missing like 'scheduling before sleep') → approve base ONLY with a mandatory motion/post bridge note (animation, overlay, SFX), never silent approval.

## CULPA_VISUAL_LOCK (Milo series continuity element)

The guilt is always: violet/lilac hues, ethereal mist-wisp form, soft glow, similar scale, no human face, same watercolor language. One wisp arriving (S02), one waiting (S04), two wisps as second alarm (S05). Never reinterpret per scene.

## Quick Reference

| Step | Rule |
|------|------|
| Project | blank, fresh every run |
| Inject | paste-event chain + read-back, serial ≥8s |
| Workers | N tabs, CAP 4, each closes its own tab |
| Download | per-image menu, 2K+, content-md5 mapping |
| QA | once at end, on files |
| Fix | single beat only, delta prompt |

## Common Mistakes

- Reusing a project → uuid/grid contamination. Blank first, always.
- Downloading display thumbnails (768px) instead of menu 2K → below minimum.
- Mapping by grid order → wrong beat after dedup. content-md5 only.
- Full batch re-run for one bad image → wasted quota. Single-beat fix.
- Screenshot-verifying each step → 10x slower. Batch-first, verify once.

## Red Flags

- Prior project reused.
- Download without opening the per-image menu.
- Grid-order mapping.
- Candidates presented to user for choosing instead of agent picking best.
