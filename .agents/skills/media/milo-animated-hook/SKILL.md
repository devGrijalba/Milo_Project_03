---
name: milo-animated-hook
description: "Use when producing MILO animated 4s hooks."
version: 1.0.0
author: Hermes Agent
license: MIT
---

# STATUS: PAUSED (user decision 2026-09-23)

Transitions/video reverted; production stays image-only (Nano Banana, 9:16, x1). The UI map and procedures below are preserved for a future reactivation, NOT active work.

# MILO Animated Hook System V1 (active from post-EP003 episodes)

## Rule

Every episode OPENS with a mandatory animated clip, max 4s, designed BEFORE the script: IDEA -> HOOK MOTION CONCEPT -> SPEC LOCK -> GATES -> script -> beats -> lock -> execution. No locked hook spec = NO PRODUCTION.

## Design formula

VISIBLE ACTION + ANOMALY/CONFLICT + REACTION + OPEN QUESTION. Camera motion never substitutes character action. Invalid: zooms, pans, walking without conflict, cloth/hair motion, orbits, breathing, entering without opening a question, motion for dynamism.

## Hook must work MUTE

No voice/music/captions: viewer gets the action, notices failure, perceives reaction, wants more.

## Motion budget (30s)

- Beat 1 (hook): MANDATORY, max 4s.
- Beat 2: OPTIONAL only for twist, temporal decision, payoff, or action stills cannot carry. Never for dynamism.
- Test at 360p first; upscale to master only after Motion QA PASS.

## Generation loop

LOCKED base frame (Vision QA PASS) + LOCKED motion spec (action timeline, end state, forbidden list) -> 4s test -> Motion QA -> PASS registers / FAIL corrects (max 3) -> escalate only on premise/question/action/character/script-lock change.

## Approvals

Never ask human for: 360p tests, in-spec motion corrections, microtiming, anatomy/continuity regens, authorized upscale. Director reviews the full draft, not motion tests.

- Frames picker search does NOT filter (verified: identical mids before/after typing, manual or synthetic). Select frames by enumerating the virtualized grid (scroll `DIV.cdk-virtual-scrollable.page-container`, accumulate mid -> aria-label walk-up) and keyword-matching labels; attach via the tile's `add` (Ingrediente) button.

- Slot (Fotogramas) picker limits (verified): fixed ~12-tile scope, NO search input (page 'Buscar' belongs to another panel), typing never filters. Project tiles may NOT appear there. If target frames are absent: user uploads them, or capture how project tiles enter that panel. Do not burn runs retrying search in the slot picker.

## I2V attach procedure (verified live CDP 2026-09-23)

1. Video mode preset chip reads `Video · 360p · 4 s crop_9_16 x1`; settings popup toggles use `mat-button-toggle-checked` class (aria-pressed unreliable).
2. Frame slots are `Iniciar` (start) and `Finalizar` (end) buttons + `Intercambiar el primer y el último marco` swap. Finalizar appears after start frame is set.
3. Click `Iniciar`/`Finalizar` -> asset picker (`Buscar activos` input, native setter + input event).
4. Tile single/double-click OPENS the editor (/edit/<uuid>) — never attaches. Attach via the tile's `add` button (aria-label `Ingrediente`), nearest to the tile center.
5. Attached frames show as 56px `Imagen del ingrediente` thumbs flanking swap; generate (`Iniciar generación`) stays disabled until prompt + frames ready.
6. Cleanup: cancel/close buttons inside composer scope; verify `img[aria-label]` count = 0.

## I2V frame workflow (standing)

- Hermes selects frames per Director: generate START frame first, then END frame for the transition; both attach as Fotogramas, then video generates between them.
- Frame chips in DOM: `img` inside chip-ancestor with signed-URL srcs (`Signature=`), empty aria-labels — identify by chip container + src suffix, not labels. Same tile repeats across batches (dedupe by src).
- Any uploaded image can serve as a frame; director designates which.

## Flow video-mode UI map (detected live 2026-09-23, ES locale)

- Tabs Imagen/Video: text match only (no useful aria-pressed seen); aspect buttons carry icon prefixes: `crop_16_9` + `16:9`, `crop_9_16` + `9:16`.
- Frame mode: `Fotogramas` button has prefix `crop_free` (text `crop_freeFotogramas`); ingredients button prefix `chrome_extension`. Fotogramas = start/end frames for I2V.
- Model: dropdown button text `Omni 1.1 Flash arrow_drop_down` (role combobox/select fallback).
- Resolution: `360p` / `720p` buttons; duration: `4 s` / `6 s` / `8 s` / `10 s`; outputs `x1`–`x4`.
- Cost line: /usará \d+ créditos/ (4s·360p·x1 = 4 créditos). Bottom chip echoes `Video · 360p · 4 s ... x1` — use as read-back verify.
- Detection snippet lives in session history (console JS enumerating tabs/mode/aspect/res/dur/mult/model/credits). aria-pressed unreliable here — verify by chip text instead.

## Tooling gap (open)

No video-generation runner is wired yet (CDP runner does images only). When the next episode arrives: check Flow video/I2V availability via CDP first, then build the runner. Do not promise motion until generation path is verified.
