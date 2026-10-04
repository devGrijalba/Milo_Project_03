---
name: browser-session-observation
description: "Use when recording the user's own live browser session."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [windows, macos, linux]
metadata:
  hermes:
    tags: [browser, cdp, observation, recording, desktop]
    category: desktop
---

# Browser Session Observation

Record what the USER does in their own browser: DOM interactions (clicks,
inputs, navigations), network request/response pairs, console errors — and
only add screen video or screenshots if the user asked for them. The
observer never clicks, types, or navigates the observed browser; driving
it is a separate, explicitly confirmed task (a replay can spend the user's
money, e.g. AI generation credits).

## Procedure

1. **Confirm capture scope FIRST.** Ask or confirm: DOM interaction log
   only, plus screenshots, plus video? Do not start recorders the user did
   not ask for — each layer is a separate process to stop later.
2. **Launch a dedicated observed Chrome** (never the user's daily browser):
   `chrome --remote-debugging-port=PORT --user-data-dir="<session>/chrome-profile" --start-maximized about:blank`
   One account per profile; Brave and the user's normal Chrome stay untouched.
3. **Write an ID file** in the session dir: CDP HTTP base, browser
   `webSocketDebuggerUrl` (from `/json/version`), port, profile path, and
   the rule "observe ONLY this instance (this port)". Every watcher agent
   gets this file as its identification of the target.
4. **Start the DOM logger** (`scripts/cdp-session-logger.mjs`):
   `node cdp-session-logger.mjs <browserWsUrl> <eventos.jsonl>`
   It attaches to every page target, enables Page/Runtime/Network/Log, and
   installs an interaction hook (click/input/change/submit/enter/scroll)
   via `Page.addScriptToEvaluateOnNewDocument` plus `Runtime.evaluate` for
   the live document. Hook events arrive as `console.log('__HOOK<'+json)`
   and are stored with `layer:"user"`; CDP events with `layer:"cdp"`.
5. **Optional layers.** Tab poller: stdlib-only loop over `/json/list`
   every 5 s plus a STOP-file convention for clean shutdown and a
   `resumen.json` with visited tabs/URLs. Video (only if asked): desktop
   capture MUST use fragmented MP4
   (`-movflags +frag_keyframe+empty_moov`) — see pitfall.
6. **Verify by reading artifacts, never by process-start success.**
   `eventos.jsonl` grows with timestamped lines, `video.mp4`/captures grow
   on disk, `/json/list` shows the expected tabs. Report "recording" only
   after this read-back. When the user asks "confirm you are saving",
   answer with current sizes and a sample line.
7. **Stop everything on "finalizamos"/stop.** Signal pollers via their
   STOP file (they exit cleanly and write their summary); kill logger and
   recorder processes; close temp tabs opened for read-only inspection;
   delete temp diagnostic scripts; verify each artifact a final time and
   report what is saved, what is damaged, and what was left open.

## Pitfalls

- **Plain MP4 killed with force loses its index and is unplayable**
  (moov atom lives at the end; the scan finds thousands of slice NALs but
  zero SPS/PPS, so no rebuild). Record screen with fragmented MP4 from the
  start so a forced kill still leaves a playable file.
- **Never taskkill node/python by guessed PID** — the box runs several
  (Hermes itself, MCP servers, harnesses). Identify the exact process via
  its CommandLine first (`Get-CimInstance Win32_Process | Select
  ProcessId,CommandLine`), then kill only that PID.
- **CDP `/json/new` requires PUT** — GET returns a "use PUT" error page,
  not JSON. Close tabs with `/json/close/<id>`.
- **Node's global WebSocket takes no `headers` option** (that is
  ws-library syntax and throws). Plain `new WebSocket(url)` connects to
  local CDP fine.
- **File inputs log as `C:\fakepath\<name>` only** — the real path is
  never in the DOM event. Recover it by searching the disk for the
  filename (there may be several homonyms; disambiguate with the user or
  with download-timing evidence).
- **Prompt text typed into rich editors is NOT an `input` event on a
  text field** — the hook sees the send-click but not the text. Recover it
  read-only from the app itself (open the resulting project/exchange in a
  temp tab, evaluate, close the tab), or ask the user.
- **Replaying a recorded session is a side-effecting task**, not a
  replay of the log: new projects, uploads, downloads, paid generations.
  Confirm full replay explicitly (including who pays) before executing.
- **Foreground terminal rejects `&` backgrounding** — relaunch with
  `background=true`. `wmic` is absent on current Windows hosts — use
  PowerShell `Get-CimInstance` instead.
