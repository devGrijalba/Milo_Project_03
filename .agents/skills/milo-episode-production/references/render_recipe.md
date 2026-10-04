# MILO render recipe (ffmpeg, 1080x1920@30fps)

## Inputs and working directory

- Pass image/audio `-i` paths ABSOLUTE — the filter graph runs with
  `cwd=04_video`, so episode-relative image paths fail there.
- Keep the `subtitles=` filename free of drive colons — the colon
  breaks filter parsing. A bare name next to the output works, and so does
  a relative subdir (`subtitles='_qa/x.ass'`); only `C:/...` absolute paths
  fail. The `.ass` source of truth lives in `02_voz/`; the burn copy is archived to `04_video/_qa/` afterwards with the QA frames.
- Looped image inputs MUST declare `-framerate 30` before `-loop 1`
  (the image demuxer defaults to 25fps; zoompan branches do not renormalize,
  so without it every zoom segment silently loses ~1/6 of its frames and the
  video stream ends ~2s before the audio — R004 v004/v005 proved it).
- After every render, verify per-stream durations with
  `ffprobe -select_streams v:0/a:0 -show_entries stream=duration` — video and
  audio durations must match the planned total before any QA.

## zoompan without frame multiplication

- With `-loop 1 -t <dur>` inputs every input frame is real: set `d=1` so
  each input frame yields exactly one output frame. `d=N` duplicates every
  input frame and the segment comes out N× too long — the mechanism behind
  any mysteriously oversized render duration.
- Upscale first for headroom (`scale=1620:2880...crop=1620:2880`), then e.g.
  zoom-in `z='min(1.0+<step>*on\,1.2)'`, eye-biased zoom
  `y='(ih-ih/zoom)*0.15'`, downward pan at fixed zoom
  `y='(ih-ih/zoom)*on/<frames>'`, all with `s=1080x1920:fps=30`.
- Bare `trim=0:N` trims SECONDS, never frames — cap every looped still with
  `trim=start_frame=0:end_frame=N` (or `trim=duration=<dur>`); a bare-args
  trim on a `-loop 1` input is a silent no-op and the segment runs infinite.
- An infinite zoompan/loop branch stalls `concat` on the first segment while
  `-t` still cuts a full-length file, so the failure reads as a complete
  master frozen on shot 1 with correct audio and subs — after every render,
  md5-hash probe frames across the timeline; identical scenes minutes apart
  mean a stall, not a repeated set.
- Static shots: `scale=1080:1936,crop=1080:1920,fps=30,trim=duration=<dur>,setpts=PTS-STARTPTS`.
- Append `setsar=1` to EVERY video branch before `concat` — `scale`/`crop`/`zoompan` each leave a different SAR and concat fails on the mismatch with an `in0:v0 parameters do not match` error.
- The muxed audio index is the count of video inputs: 6 `-loop` shots plus the audio file means `[6:a]`, not `[7:a]` — recount it whenever the shot count changes, the filtergraph error names the bad index directly.

## Subtitles (ASS, Milo style)

- Base style is the house standard from the subtitle gate (`references/subtitle_qc_milo_v1.md`: white Arial Bold, subtle outline+shadow, 1 line max 2) — not the legacy E01 numbers; do not copy old fontsize/MarginV values from prior episodes without re-verifying.
- Placement is per shot, decided from each frame's negative space (see the
  protocol file): default upper-third with top margin 170-220px at 1080x1920
  wherever the upper frame is free; a lower position is an EXCEPTION (tight
  close-up whose dramatic focus fills the top) requiring a platform-UI
  safe-zone check, never the default. Emit both styles in one ASS and assign
  by dialogue start time; a fixed position for all shots covers key narrative
  elements on some planes.
- Hook blocks expose the full premise from second zero: lay the hook as one multi-line karaoke block (numeral+unit always on the same line — a dangling `27` reads as a buffering error) so the question is readable before the highlight sweep finishes, then compact a slow hook by cutting inter-phrase silence middles, never by time-stretching speech.
- Wrapping must be on: `WrapStyle: 0` in `[Script Info]` — `WrapStyle: 2`
  disables word wrapping, so any line wider than the frame is silently cut at
  the edges (the failure looks like a bad SRT, but the SRT is fine).
- Wrapping is not a substitute for segmentation: after render, count the
  rendered lines per block on the QA frames — a single-line SRT block can
  wrap to 3 lines at large sizes, which breaks the max-2-lines rule even
  though the SRT is valid. Split the SRT block at a word boundary
  (timed to the words) and re-render as a new version.
- Any size increase invalidates the planned position — re-verify face/action clearance on the rendered frames, not the plan: type that cleared at 68pt can sit on the face at 102pt in centered compositions, and the fix is position/size together, never size alone.
- Word-by-word karaoke runs in this same ffmpeg path: one Dialogue per SRT
  block with a `{\kf<centiseconds>}` tag per word from
  `..._words.json` (assert every speech word is consumed in order, tags
  excluded), style with `PrimaryColour` = highlight (`&H66E0FF&`) and
  `SecondaryColour` = dim grey (`&H00B0B0B0`) — libass fills Primary over
  Secondary as each word is spoken. Keep the static-block ASS as fallback.

## ASS technical pitfalls (libass via the subtitles filter)

- Extract QA frames with output-seeking (`-i FILE -ss T`), not input-seeking
  (`-ss T -i FILE`): input seeks near end-of-stream can silently yield zero
  frames with exit code 0 while the master is intact — a missing grab is an
  extraction artifact, not a render defect. Always `ls` the grabs before
  vision-checking them.

## Frame-exact assembly and delivery

- Derive segment frame counts from cumulative boundaries (`round(t*30)` per
  cut point, segment = difference), never from per-segment `round(dur*30)` —
  banker's rounding on halves (e.g. 70.5 → 70) silently drops a frame and the
  stream ends at 794 instead of 795.
- Join segments with the `concat` filter (one re-encode), not the concat
  demuxer with `-c copy` — the demuxer drops a frame at a segment join with
  no error, which reads as a mysterious one-frame-short master.
- Verify `nb_read_frames` (`ffprobe -count_frames`) equals `dur*30` and that
  container/video/audio durations all match before QA.
- Prove clip-to-slot wiring WITHOUT vision by cross-matching each master grab
  against per-segment reference frames (one frame pulled from each built
  segment file): the temporally correct segment must win near-exact, since
  both come from the same pixels — palette-MSE against the SOURCE stills
  cannot distinguish same-palette watercolors and false-matches everything
  to the warmest close-up. Compare phase-aware (reference frames at two
  zoom phases per segment): a grab matching the same segment at a different
  zoom phase is a PASS, because zoom progress shifts MSE more than a
  same-palette still swap does.
- Apply `+faststart` (remux copy) to every deliverable MP4 and verify
  `moov` precedes `mdat`; players without it stall on stream start.
- Prove variant integrity with stream hashes, not durations: the no-music
  variant must share the master's video MD5, the no-subs variant the
  master's audio MD5 (`-map 0:v/-map 0:a -c copy -f md5`).
- Declare intentional holds (tail retention, slow-zoom tails) in the QA
  report with their time ranges — `freezedetect` flags them and an
  undeclared freeze reads as an accidental render defect.

## Music beds: crossfade + duck + loudness fix

- Crossfade two beds (e.g. intimacy → warmth at the emotional turn) with
  `atrim` windows + `afade` in/out + `adelay` alignment into `amix=inputs=2:normalize=0` at `-19dB`; duck the mixed bed under narration with `sidechaincompress=threshold=0.02:ratio=4:attack=120:release=300` keyed by the voice, never the reverse. Pin SFX cues to visual action times (whoosh on transition, tap on touch, quiet-send on closing beat) at low gain with `apad=whole_dur=<total>` tails so no cue truncates at the mux.
- Single-pass `loudnorm` can undershoot dialogue-heavy mixes by ~5 LUFS; when it does, apply a UNIFORM gain (`volume=+NdB`) + limiter (`alimiter=limit=0.89`) on the finished mix and re-measure — uniform gain preserves the voice/music/SFX balance, re-mixing does not.

## Silence trim (recorte)

- Never trust `..._words.json` gaps for pause measurement — ElevenLabs stretches word end times through trailing pauses, so inter-word gaps read near-zero while the audio holds long silences. Measure ground truth with `ffmpeg -af silencedetect=noise=-35dB:d=0.3 -f null -`.
- Cut silence middles with `atrim`/`concat` (start each cut ≥0.10s after silence onset so voiced energy is never touched), keep payoff and comic-breath pauses intact, then shift every word timestamp by the durations removed before it and rebuild SRT/ASS as NEW versions — never hand-edit timestamps into place.
- Verify every splice is click-free (sample step at each boundary must sit in digital silence) and re-run silencedetect to confirm the new pause inventory before rendering.

## Foley and loop cushion
- Minimal crack/snap SFX, fully synthetic:
  `anoisesrc=color=white:duration=0.2:seed=7,highpass=f=2500,`
  `afade=t=out:st=0:d=0.15,volume=0.18,adelay=<ms>|<ms>`, mixed under the
  voice with `amix=inputs=2:normalize=0` so the voice level is untouched.
- Loop cushion: extend the final static shot by 0.4s AND pad the voice with
  `apad=whole_dur=<total>`; drive length with explicit `-t <total>` instead
  of `-shortest` so the freeze survives the mux.
