---
name: cdp-injection-handshake
description: "Web UI injection via CDP with a termination-safe handshake."
version: 1.2.0
author: Hermes Agent
license: MIT
---

# CDP Injection Handshake (transport-level, tool-agnostic)

## When to Use

Any task that injects prompts into a web UI (LLM chats, Google Flow,
generation tools) over `chrome --remote-debugging-port` and waits for the
response: prompt injection, completion detection, raw capture. Complements
tool-specific skills (e.g. Flow batch pipeline); this file owns only the
handshake that guarantees the round trip terminates. For one actor driving
many chats, see `references/adapters.md` (universal adapter-table pattern).
For UIs that return MEDIA TILES instead of text (image/video generators), see
`references/generation-ui-results.md` (result-identity and reference-attach
contract).

## Handshake (always on)

- Exact normalized read-back before submit; mismatch = abort, never send.
  After submit, confirm the composer cleared AND conversation state changed.
- Detect end-of-generation at ELEMENT level (button aria-label/data-testid),
  never body-text substrings — response content can contain those words
  (e.g. 'detener' inside Spanish prose) and the detector then reports
  'generating' forever.
- A probe that THROWS is not a target failure. Distinguish "could not read the
  page" from "the target reported an error": an expression that raises in page
  context must surface as a probe fault, never as a generation failure.
  Conflating them makes the wait loop exit early and discard a result that had
  already landed. Prefer `indexOf` + `slice` over regex for toast probes, and
  give a probe exception its own retry-or-report branch.
- Scope widget queries to the widget's own root element, never `document`. A
  global selector spanning a popover/panel returns the surrounding app chrome
  (toolbar buttons, model chips, nav labels) instead of the widget's rows, so an
  exact-name match finds nothing and the step reports NOMATCH with no obvious
  cause. Descend from the popover/panel custom element for both its search input
  and its result rows. Result-scope and composer-scope are usually DIFFERENT
  roots — do not reuse one for both.
- An ENABLED send button that ignores `.click()` is its own failure mode:
  scroll it into view and dispatch trusted `mouseMoved` / `mousePressed` /
  `mouseReleased` at its measured center. A synthetic click can no-op on an
  enabled control; treating the no-op as "sent" loses the whole round.
- Bind captures by CONTENT signature (head + length of the last message
  taken pre-injection), never by message index — chats virtualize old nodes
  out of the DOM and index slicing then returns empty forever.
- One hard deadline wrapping the whole cycle
  (inject → detect → stability → capture) plus a periodic heartbeat line
  (elapsed/last-length/streaming/is-new). On expiry: recapture once;
  valid → save + continue; invalid → recovery path. Never blindly reinject
  while a valid response to the first request may exist.
- Idempotency: never overwrite a valid captured artifact with a later
  capture (a late-finishing poller latches onto the wrong turn; quarantine
  conflicts instead). Idempotency protects VALID captures only: a capture
  matching the injected prompt, any earlier artifact from the same thread
  (stale-node capture past the pre-count), or carrying limit text is invalid —
  delete the file and retry, never keep it. Validate against the prompt
  hash, not just the pre-state signature (head+length passes echoes).
  One poller per conversation; kill stale pollers instead of leaving
  them to die alone. A skip-on-existing must also verify the kept file
  answers the CURRENT turn: when two rounds share output filenames, the
  guard protects a stale file and silently drops the fresh response — on
  mismatch, archive the stale file aside and save the new capture.
- Transport-level QC (expected dimensions, aspect tolerance, non-blank
  brightness) catches delivery failures only — empty renders, wrong shape. It
  cannot see visual artifacts: an image can pass aspect and brightness while its
  subject is structurally broken. Always vision-check the real bytes before
  delivering; never certify an artifact on numeric checks alone.
- Delivered-but-uncaptured = recoverable state: re-read the DOM and
  recapture; reinject only when no valid response actually exists.
- On a thread shared by sequential tasks, verify the capture answers the
  CURRENT turn: a response to a sibling task's prompt passes every generic
  check (non-empty, new hash, stable) yet belongs to the wrong file. Match
  the capture against this turn's prompt semantics before saving; on a
  mismatch, file it under the turn it answers (or discard it) and rerun
  the current turn on a fresh thread instead of stacking another prompt
  onto the tangle.
- Never pass functions into `page.evaluate` — Playwright serializes
  arguments, not closures; a function argument throws at call time. Pass
  data (uuids, indices, tuples) as serializable args instead.
- Probe hygiene for LLM panels: require the marker to appear at least twice
  (own echo + real answer) or a fresh assistant node, never body-substring
  presence alone — echoes false-pass. Avoid adversarial trigger words
  (e.g. 'inyección') in probe payloads; safety filters refuse the test
  instead of answering it. Run behavior probes that write (typing tests,
  selector checks with side effects) in a FRESH tab, never the working
  conversation thread — probe text lands in the live composer and pollutes
  subsequent captures.
- Every actor script ends with an explicit `process.exit(code)` and never
  calls `browser.close()` on a shared `connectOverCDP` instance (an open
  CDP socket keeps the Node loop alive forever; the supervisor owns
  lifecycle, the actor owns only its own tab).

## Framework-aware insert + multi-profile rotation

- Programmatic value-set + synthetic `InputEvent` often leaves framework
  (React) state empty: the DOM shows text but send stays disabled. Always
  verify send-enabled post-insert; on disabled, fallback to focus +
  select-all + trusted `keyboard.type` (registers in framework state),
  then re-verify before submitting.
- Clear-before-insert on `contenteditable` composers: they concatenate
  instead of replacing, and stale text causes read-back mismatch.
- When several fields match the composer selector, enumerate candidates
  with visibility + content length: the real composer is the visible one
  with content (a matching empty field may come first in DOM order).
- A found-but-disabled send button + `.click()` is a silent no-op: treat
  disabled-send as its own state (enable/Enter/keyboard path), never as sent.
- Triage submit-no-clear: limit text anywhere in DOM = `RATE_LIMITED` →
  failover to the next profile/port; no limit text = stuck tab → move the
  task to a healthy thread with a self-contained prompt (embed all fixes,
  never reference prior-turn context like 'your previous audit').
- Rotation: N profiles × N ports, one account per profile (the same login
  everywhere does NOT multiply rate limits); round-robin per platform with
  task-level port pin for thread continuity. Rotation counters reset per
  process, so every run starts on the same profile unless the cursor is
  persisted or tasks pin ports — persist the cursor alongside the block
  state when spread across runs matters. On a limit stating a wait,
  block that profile for the stated duration and skip it in rotation until
  release. Never two pollers on the same conversation: before launching any new round on tabs already in play, poll for still-running processes on those ports first — a second poller corrupts both captures, and an unnoticed dead run leaves stale composer text behind.
- After two submit failures on one tab while sibling tabs work, stop
  patching transport and relocate the task: the tab is stuck, the code is
  not broken.
- Lane changes reuse existing topology: when a platform is added, paused,
  or swapped, open it as a tab inside the project's existing browser
  windows — never spawn a parallel browser farm unasked (extra instances
  split logins, orphan profiles, and strand the user's logged-in sessions).
- A lane's first task starts a fresh chat: a reused thread serves its old
  response as your capture, and pre-state signature checks cannot tell it
  from success. Validate every new lane end-to-end (ping → send → real
  answer on fresh state) before trusting it inside a round.
