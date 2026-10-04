# Director auto-run episode execution (post-audio to COMPLETE)

For director packages that ship frozen script + approved takes + PASS Flows + deterministic microtimeline rules with an AUTO_RUN order (no `WAIT_FOR_CONTINUE` states): execute start to finish — voice, alignment, microtimeline, edit, mix, karaoke, subs QA, render, QA, package. Exits are only `COMPLETE` or `PARTIAL_WITH_HARD_BLOCK` (approved work kept, minimal documented block list). A local error never discards approved assets; isolate, continue independent branches, auto-apply only explicitly authorized fixes.

## Intake

Copy outside-workspace attachments into the episode `_incoming/` (chat reposts arrive with `-2` suffixes — dedupe by size/md5 before copying, keep one). Verify package zip integrity (`testzip`), stage images/audio/Flows into working dirs, transcribe delivered takes locally (faster_whisper, `word_timestamps=True`, language pinned) and select by script fidelity first.

## Alignment + microtimeline lock

Validate coverage count vs frozen script with UNACCENTED matching (NFD-strip) — accent-only diffs are recognizer noise; display text keeps tildes. Locate anchor phrases by sequential token matching in fixed order (never single-word search on repeated words). Quantize every cut: `F(t) = round(t*30)`, operate on `F(t)/30`. Flow windows: fixed-duration Flows anchor to voice (`IN = anchor`, `OUT = IN + dur`) with the package's fallback rule when the ideal window collides; merge still windows under 0.450 s into a neighbor without changing narrative order and log the merge. `MASTER_END = max(VOICE_END + 0.8, lastFlowOut + 0.5)`. Persist `MICROTIMELINE_LOCK` (beat/in/out/frames) before assembly — it is derived output, not a creative decision.

## Assembly rules

Stills get push-in via `zoompan` capped with frame-exact trim (`trim=start_frame=0:end_frame=N` — bare `trim=0:N` is seconds); conform delivered Flow videos to 30 fps and RMS-diff first/last frames against START/END stills plus a vision-checked mid frame before wiring. Music duck windows and SFX cues derive from anchor times, never hand-estimated seconds. Karaoke blocks from word-timings (punctuation split, stub merge); verify new segments with midpoint grabs, never boundary grabs. Omit optional SFX with no canonical resource and log `OPTIONAL_SFX_MISSING` — never synthesize or substitute.
