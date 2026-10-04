---
name: live-window-triage
description: "Use when reading a page already open on the desktop."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [windows, macos, linux]
metadata:
  hermes:
    tags: [desktop, browser, triage, inspection]
    category: desktop
    related_skills: []
---

# Live Window Triage

Find and read the user's real open window when automation sees a different instance.

## Procedure

1. Enumerate native windows first with `computer_use(action="list_windows")` — it returns app_name, pid, window_id, title, z_index for every window. Without computer_use on Windows, fall back to `tasklist /V` and grep the TITLE text across every process.
2. Match by title + app_name, not by assumption: several Chromium apps (Chrome, GinsBrowser, Brave) report separately and each carries its own pid.
3. Never conclude "not open" from chrome-devtools `list_pages` alone — it only sees its own debug Chrome instance, never the user's real windows.
4. Capture the candidate with BOTH pid and window_id together — either alone fails to resolve.
5. Read page content with `mode="vision"` plus vision_analyze: AX/som captures on Chrome expose only browser chrome (address bar, bookmarks, tabs), never web-page DOM.
6. When several candidates match (same title family, multiple browsers), show titles found and confirm which to inspect before going deep.

## Pitfalls

- Never pre-filter enumeration by a single exe name — the visible window frequently belongs to a sibling process under a different exe (manager vs browser session), so an exe-filtered query reports 'nothing open' while the tab sits one process away. Match by title text across ALL processes first, then resolve the owning pid.
- An Electron manager process (renderer running `app.asar`, no `--remote-debugging-port`, no page renderer children) means only the profile dashboard is open — no browsable tabs exist to inspect, so stop there instead of hunting ports.
- Capture targeting requires pid AND window_id together — passing only one returns an empty capture, not an error worth retrying alone.
- AX tree on a browser window lists browser UI only; treat absence of page text in AX as expected, not as an empty page — switch to vision.
