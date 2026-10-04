---
name: chrome-cdp-automation
description: "Use when driving desktop Chrome via CDP from scripts."
---

# Chrome CDP Automation

Drive a real desktop Chrome instance through `--remote-debugging-port` from scripts
(Python + websocket): open/navigate tabs, evaluate JS, read DOM, capture screenshots,
emulate device metrics. For DOM-free prompt injection into web AI chats use the
injection skill instead; this skill is the transport layer beneath such work.

## Procedure

0. A bare "abre un CDP" / "open a CDP" means: bring the endpoint up and hand it over ready to
   drive — launch, health-check, report browser version + profile dir + the usable `page`
   target, then ask which URL to load. Do NOT guess a destination and navigate there; the
   next task decides the target. Keep the browser alive afterwards (background session) and
   say so, so the next call reuses it instead of relaunching a second Chrome.
   0a. Exception — "abre N CDP para agregar/iniciar sesion en cuentas": the sites ARE the
   request. Launch one window per account, each with its own profile dir and each opened
   straight at that account's site, and never two accounts in the same profile dir (the
   second login evicts the first). Give the user one table back — port, profile dir, site —
   so they know which window to log into, and state the rule that logs are manual and never
   guessed. Do not ask which sites when the rotation map already fixes them.
   0b. When N windows are needed and the user did not name them, open the first N of the
   rotation rather than stalling on a question; say which N you opened.
1. Launch Chrome with an isolated profile and permissive origins (binary lives at
   `C:\Program Files\Google\Chrome\Application\chrome.exe` on this host):
   `--remote-debugging-port=9222 --remote-allow-origins=* --user-data-dir=<profile-dir>`.
   Without the allow-origins flag, websocket clients connect then drop.
   1a. Confirm the remembered profile dir still EXISTS before launching (`ls -d <dir>`, or
   `find <project-root> -maxdepth 4 -iname "*cdp-profile*" -type d` when the project path
   comes from memory/note). Chrome silently creates a fresh empty profile when
   --user-data-dir points at nothing, so a path broken by a renamed or moved project dir
   hands you a logged-out browser with zero errors: the port answers, the session is gone.
   1b. On the git-bash host, launch as a BACKGROUND terminal call — a foreground command
   with a trailing `&` is rejected by the runner. Pass NATIVE forward-slash paths to the
   native binary, quoted when they contain spaces (`--user-data-dir="D:/dir/cdp-profile"`);
   MSYS path conversion is off, so `/d/dir/...` fails as "cannot find". Keep the returned
   session id: it is the handle for polling or stopping the browser.
   1b-bis. ONE BROWSER PER LAUNCH JOB. Chrome's process does not return, so the first
   `nohup chrome` keeps the job's shell busy and every browser queued after it in the same
   script never executes — the symptom is the first port healthy while the rest refuse CDP,
   which reads as "port blocked" and sends you chasing firewall/port problems. Launch each
   window as its own `background=true` job (one `nohup` line), then health-check all of them
   together.
   1b-ter. Resolve the profile ROOT by searching for marker files (`browser_routes.json`,
   `multi_inject.js`, `launch-browsers.bat`, or the `.chrome-<ai>` dirs themselves) rather
   than trusting a path recorded in a doc or note — projects get archived/renamed, and the
   documented root is the first thing to go stale. Report the resolved root to the user.
   1c. Health-check in a FOLLOW-UP call, not in the launch call: `curl -s
   http://127.0.0.1:9222/json/version` for the browser handshake, `/json/list` for tabs.
   The two answers mean different things: `/json/version` proves the PROCESS is alive,
   `/json/list` proves a usable TAB exists. A port that answers `/json/version` but lists no
   target URL is a blank profile — treat it as NOT ready, never inject into it. Filter the
   list to the expected URL substring (STRICT) and ignore the `browser_ui` / `service_worker`
   / `chrome-extension://` noise. `scripts/cdp_health.sh <port> [expected-url-substring]`
   does this for a whole port row in one call.
2. Verify liveness with `GET /json/list` before any automation; enumerate targets and
   select by `type == "page"` plus a URL substring. The list is the only reliable tab index.
   Expect noise alongside the real tabs — `type == "browser_ui"` (Omnibox Popup),
   `service_worker` and extension targets are not pages; never navigate or close them.
3. Open tabs with `PUT /json/new?<url-encoded-target>` (PUT, with the URL percent-encoded) —
   a plain GET with a raw URL fails silently. Then re-poll `/json/list` to pick up the new
   target's `webSocketDebuggerUrl`.
4. Send CDP over the websocket with incrementing `id`s and match replies by `id`; wrap
   `Runtime.evaluate` results defensively (`result.result.value` nests two levels and KeyErrors
   on protocol errors) and return a truncated error string instead of crashing the loop.
5. For screenshots: `Page.enable`, then `Page.captureScreenshot` (base64 PNG in
   `result.data`). For fixed-size captures, set `Emulation.setDeviceMetricsOverride`
   (width/height/deviceScaleFactor) first and allow a beat for re-layout. After
   driving page state (seek, toggle, inject), await two animation frames
   (`new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))` with
   `awaitPromise:true`) before capturing, and byte-compare each capture against
   the previous one — recapture (sleep 1s, up to 5x) while bytes are identical
   during a segment that must be moving. The compositor intermittently serves
   the last-composited frame, so a batch can silently fill with frozen pixels
   and zero errors; sleeps alone do not fix it, the compare-and-recapture does.
   (Static holds legitimately repeat bytes — cap the retries and accept.)
6. For long batch jobs (scroll sweeps, frame captures), make every step resumable: skip
   already-produced outputs on start, retry each unit up to 3x with a sleep, and reconnect
   the websocket on drop — the browser kills idle sockets mid-run.
7. Never pipe a verification command through `tail/head` when its exit code matters; the
   pipe reports the last stage's status, not the check's.

## Pitfalls

- Replicating an extension? Decode its real DOM primitives from the bundle first (how it clicks, types, waits) — inferring from logs builds a replica that looks right and fails silently.

- Prefer `127.0.0.1` over `localhost` in every CDP URL — IPv6/localhost resolution
  mismatches cause intermittent connection refusals on Windows.
- One websocket per task phase; open a fresh connection per scroll/action batch rather than
  holding one socket for the whole session — stale sockets time out and every subsequent
  evaluate fails with the same opaque error.
- `file://` navigation works for local harnesses (test pages, render stages); pass the
  absolute path with forward slashes, percent-encoded, via the PUT form above.
- Keep credentials out of automation artifacts: authenticated profiles live in the
  `--user-data-dir`, never export cookies/tokens into deliverables or logs.
- When a human shares the browser window, never re-attach workers by URL substring — their navigation changes URLs under you. Use the `id` + `webSocketDebuggerUrl` returned by the PUT `/json/new` response as the worker's permanent handle for the whole run.
- A reused tab serves the STALE file: after editing the HTML/SVG/JS on disk,
  `Page.navigate` to the same URL (reload) before capturing — otherwise screenshots
  show the old DOM and a full batch renders empty or outdated pixels with zero errors.
- Lazy panels (comment drawers, theaters) do not hydrate on scroll alone: click the opener control first, then poll for content markers (article count, sentinel text) with a stable-rounds stop rule — fixed short sleeps read skeletons and pass silently with zero articles.
- Close only your own instance with `Browser.close` over the browser-level websocket from `/json/version` — a taskkill on chrome.exe also kills the user's unrelated windows, and the port stays bound until YOUR instance exits, so re-poll `/json/version` afterwards to confirm it is free.
- Read evaluate failures as `exceptionDetails.text || exception.description` — text alone is frequently empty (`Uncaught` with no message) and a text-only check reports a blank error that hides the real cause.
- Click framework-UIs by coordinates, not `el.click()`: wait for visibility, `scrollIntoView`, compute x = left + 25% width / y = vertical center from `getBoundingClientRect`, send `Input.dispatchMouseEvent` moved → pressed → released with ~300ms pause. Synthetic `.click()` silently no-ops on some controls (no navigation, no panel). Re-measure the rect after the scroll settles (instant scroll + second read): smooth scrolling leaves the first measurement stale and the click lands in a gap.
- Gate every click on visibility: `:visible`, not `:disabled`, rect > 0, computed `display`/`visibility`/`opacity` healthy, inside the viewport. Apply the gate to the final target only.
- Keys that must trigger autocomplete/menus go through real `Input.dispatchKeyEvent` (keyDown/keyUp with `code`, `keyCode`, `text`, `modifiers`); `Input.insertText` types visible text but never fires the keydown listeners that open suggestion popups.
- Completion waits in two phases: first wait for the stop/busy control to DISAPPEAR (long poll), then wait for result nodes to actually carry payload (e.g. `img`/`video` with `src`). Exiting on 'stop gone plus any node exists' downloads pending/empty nodes.
- Gate completion on elements created AFTER your action: snapshot result-node keys (URLs, ids) before submitting, then count only fresh ones — otherwise a previous run's artifact satisfies the wait and you download a byte-identical stale success with zero errors.
- In virtualized lists, locate targets by stable key (media `src`, id), never positional `:eq` indexes — scrolling re-renders rows and indexes shift under you.
- Signed/cookie-gated URLs 403 outside the page session: download via in-page `fetch` (cookies travel) or `Browser.setDownloadBehavior` with an absolute `downloadPath` plus `Browser.downloadWillBegin`/`downloadProgress` watched on a browser-level websocket; never `curl` them from the shell.
- Hover (`mouseMoved` to the element center) before reading state of controls the page only reveals on hover.
- Before menu/hover work, assert zero stale transparent overlays (e.g. `.cdk-overlay-backdrop` count is 0; Escape to dismiss): leftover backdrops from earlier popovers swallow the mouse invisibly, so hovers never register and clicks miss with zero errors.
- Re-inject page-side helpers after every `Page.navigate` — navigation destroys the execution context and all previously defined functions with zero errors.
- When emulating jQuery selectors (`:has`/`:contains`/`:eq`), evaluate them PER COMPOUND with their combinators (Sizzle semantics): flatten-and-filter mis-scopes `:has` to the final element and breaks on nested `:has(button:contains('x'))`. Parse balanced parens, resolve each compound left-to-right, apply positional pseudos within their own compound.
- Enter SPA states by direct URL (`Page.navigate` to the deep link) instead of mimicking list clicks — list-row buttons often rename/select rather than open.
- Upload files natively: `Page.setInterceptFileChooserDialog {enabled:true}`, click the control that opens the picker, catch `Page.fileChooserOpened` on the page session, then `DOM.setFileInputFiles {files:[absolutePath], backendNodeId}` (needs `DOM.enable`). Only fall back to DOM-hook base64 injection when no chooser event arrives — hook interception depends on the page's internal input wiring and fails silently on builds that open the picker another way.
- MV3 service workers suspend after ~30s idle and kill persistent sockets with zero errors: keep the worker alive with a periodic `chrome.runtime.sendMessage` ping from a visible page/panel (each message wakes the SW; the SW re-runs its reconnect check on wake), plus a server-side reconnect loop. Never assume a registered worker stays registered — check presence immediately before dispatch and fail explicit ('no worker') instead of silently falling back to another route.
- Verify vendor-supplied selector templates against the live DOM before trusting them (icon-name and label mappings rot; a template that matches nothing makes the run WARN-and-continue through every step).