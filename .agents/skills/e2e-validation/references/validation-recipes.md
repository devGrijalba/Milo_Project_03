# Validation recipes — concrete measurements for E2E runs

Learned 2026-09-03 during a full chat-story video pipeline validation
(TEXTOPIA H27). Methods are general; the numbers are examples.

## 1. Audio-tail level (silence / remate check)

Measure the TAIL separately from the global mix. Global `volumedetect`
masks a non-silent tail.

- Seek **before** `-i` (input seeking) so the filter sees only the segment:
  `ffmpeg -ss <tail_start> -i out.mp4 -t <tail_len> -af volumedetect
  -vn -sn -dn -f null NUL`
- Pitfall: `-ss` **after** `-i` (output seeking) can report global-range
  values that look identical to the full-mix measurement — always compare
  tail readings against the global ones; identical figures mean the seek
  did not isolate the segment.
- Example: global `mean −11.6 / max −1.4 dB` vs tail `mean −38.7 /
  max −20.5 dB` → tail silence confirmed.

## 2. Frame comparison at exact event timestamps

Extract frames at the contract's own event times (never at estimated
percentages of the output), then compare objectively:

- `ffmpeg -ss <event_t> -i out.mp4 -frames:v 1 frame_t<event_t>.png`
- With PIL, record per-frame mean luminance + stddev. Expected pattern:
  bright chat frames vs darker frames once media appears; consecutive
  static-overlay frames may be near-identical (note it as an observation
  for the visual verdict, not as PASS/FAIL by itself).
- Build a contact sheet across evenly spaced frame numbers for the
  perceptual review handoff:
  `-vf "select='eq(n,0)+eq(n,90)+…',scale=270:480,tile=3x3"`.

## 3. Contract cross-check (scripted, not eyeballed)

Parse the build artifact and the source spec independently and assert
equality: event lists (`pops` vs `data-t`), totals (`total` vs duration
spec), interval encodings (typing windows vs narrative windows — a
narrative window is NOT automatically a typing window), effect params
(glow/glitch/blackout/silence), and asset `src` references. Any mismatch
is a cross-protocol defect even if each side looks valid alone.

## 4. Re-measure provider outputs

Never trust requested parameters (size, format) — open every generated
asset and record actual dimensions/mode/bytes. A provider silently
returning a nearby-but-off-spec asset is a real FAIL class that
legibility-only checks will pass through. Example seen: requested
720×900, delivered 686×858, caught only by PIL re-measurement.

## 5. Traceability manifest

Per run, write `manifest.json`: artifact name + sha256 + bytes (+ actual
dimensions for images) + generation source/seed. The next session must be
able to re-verify every byte cited in the report.

## 6. Motion-exists metric (MAE first-vs-last)

For each animated scene, extract the first and last intra-scene frames
(staying clear of transition overlaps) and take the mean absolute gray-level
difference: a landed camera move reads well above a frozen one (observed:
moving 5–19 vs frozen ~0.3 on photographic 1080p content). Set the PASS
threshold an order of magnitude above the frozen baseline, and record both
numbers — the baseline is what makes the verdict meaningful.

## 7. Spawning verification CLIs on Windows

Node `child_process.spawn('npx', …)` fails on Windows (`.cmd` needs a
shell): resolve to `npx.cmd` with `shell: true`, quote every argument that
contains spaces or metacharacters (paths like `D:\…\PROYECTO REMOTION\…`
split otherwise), and pass `FORCE_COLOR: 0` + `NO_COLOR: 1` so summary-line
regexes match (ANSI codes silently break `Test Files N passed` parsing).

## 8. Backup/restore drill (Postgres + S3-compatible object store)

Prove the restore on TEMPORARY infrastructure, never on the live environment:
backup → restore to a scratch database/bucket → verify functionally against the
scratch → destroy the scratch. Record observed times and sizes; never declare
RTO/RPO from a drill.

- DB: `pg_dump -F c` from inside the container, `pg_restore` into a scratch
database, then assert per-table row counts for every domain entity.
- Objects: download every key with a SHA-256 manifest, re-upload to a scratch
bucket, re-download and compare bytes + SHA per key.
- Functional check: boot the app pointed at the scratch (DB URL + bucket
overrides), then health → login → open record → download attachment and
 generated file → SHA equal to the originals.
- Cleanup order matters: stop the scratch app FIRST (open connections block
`DROP DATABASE`), then drop the scratch DB, delete the scratch bucket, remove
dump files and drill scripts. Verify the live database list shows only the
production database afterwards.

## 9. E2E runs against a rate-limited system

Use a UNIQUE client identity (IP header, user, or API key) per validation run.
Re-running E2E from the same identity trips the system's own rate limiter and
produces failures that look like product bugs (e.g. 429s surfacing as generic
login errors). Randomize the identity per run and keep error-path probes (which
must NOT be rate-limited into false failures) on a separate identity.
