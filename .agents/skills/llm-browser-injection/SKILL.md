---
name: llm-browser-injection
description: "Use when querying web LLM chats via browser automation."
version: 1.1.1
author: Hermes Agent
license: MIT
---

# LLM Browser Injection

Core principle: one dedicated browser per AI, DOM-only driving, element-level completion detection. No mouse, no pixels, no screenshots for decisions.

## When to Use

- User asks to query ChatGPT, Claude, Gemini, DeepSeek, Grok, or any web LLM through the browser.
- Any task ending with "prompt sent + response captured to file".
- Parallel queries to multiple AIs at once.

## Hard Constraints

- NEVER touch the user's daily browser. Each AI gets its own Chromium/Chrome instance with its own `--user-data-dir` and its own CDP port (e.g. 9222, 9223, 9225). Sessions persist in those dirs; login is manual by the user once.
- DOM only: `querySelector`, native input setter + `InputEvent`, JS `click()`, Enter key. Forbidden: mouse movement, pixel coordinates, vision/screenshots for state decisions.
- Transport handshake lives in skill `cdp-injection-handshake` — always apply it (read-back, composer-cleared confirm, element-level stop detection, content-signature capture, one deadline, recapture-once).
- Actor scripts end with `process.exit(code)`, never `browser.close()` on a shared `connectOverCDP` session.

## Core Pattern

Before: reuse one browser for all AIs, click by coordinates, detect "done" by body text, slice messages by index → focus conflicts, false-done, empty captures after virtualization.

After: one browser per AI → snapshot composer/send/stop → inject + exact read-back → submit + composer-cleared → poll stop ELEMENT visible + 2-poll stability + heartbeat → capture by content signature → validate → save.

## Workflow

1. **Launch / connect.** One headed Chrome per AI: `chrome --remote-debugging-port=<port> --user-data-dir=<project>/.chrome-<ai> --no-first-run --no-default-browser-check`. Connect via Playwright `connectOverCDP('http://127.0.0.1:<port>')`. Find tab by URL; if sign-in page → stop, user logs in manually.
2. **Snapshot.** Wait for hydration FIRST: `waitForSelector(composer, 15s) + sleep 2s`, up to 3 tries (ProseMirror/Slate mount late; a first-try miss is timing, not absence). Then logical DOM snapshot only: `{platform, input_found, send_found, stop_found, adapter, timestamp}`. Abort `INPUT_NOT_FOUND` only after adapter + recovery selectors + 3 hydration tries.
3. **Capture pre-state.** Record last-message head + length (content signature) before injecting. Own-prompt echo excluded later.
4. **Inject.** ProseMirror/contenteditable DIVs (ChatGPT `#prompt-textarea` is a DIV, not a textarea): `focus + selectAll/collapseToEnd + execCommand('insertText')` first, then `beforeinput/input` chain, then textContent fallback. Read `innerText || textContent` (never `.value` on a DIV). Exact normalized read-back; mismatch = abort, never send. Gemini quirk: never wrap embedded scripts in single/double quotes — its composer normalizes them and read-back mismatches even on fresh threads; append the script bare after a colon (V1-style).
5. **Submit.** DOM button `click()` or Enter. Confirm composer cleared AND conversation state changed.
6. **Wait.** Poll stop ELEMENT visibility (`offsetParent`/`getClientRects`, never DOM presence) + 2-poll text stability. One hard deadline for the whole cycle + heartbeat log (elapsed/last-length). On expiry: recapture once; valid → save; invalid → recovery.
7. **Capture.** Read `innerText || textContent` from nodes past the pre-count, excluding own echo. Never index-slice (chats virtualize old nodes).
8. **Validate + save.** Non-empty, stop hidden, hash != prev hash. Save to `<out>/<task_id>.md` (idempotent) + optional sqlite row. Never overwrite a valid artifact with a later capture.
9. **Recover.** 3 straight TIMEOUTs or stuck chat (turns grow, no assistant text) → open fresh chat, close stuck tab, 1 retry. One poller per conversation; kill stale pollers.

## Defaults (self-contained — no external skill needed)

| Param | Value |
|-------|-------|
| Hard deadline per prompt (inject→capture) | 120s default, 180s for long answers |
| Poll interval | 1500ms |
| Stability | 2 consecutive polls with identical text length |
| Heartbeat log | every 5s: `elapsed / last_len / stop_visible` |
| Read-back normalize | `trim + collapse \s+ to single space`; exact match required |
| Content signature | `head = first 40 chars + len` of last message, taken pre-inject |
| Hash | `sha256(text).hexdigest()[:12]`; new response requires `hash != prev_hash` |
| Resend policy | submit → if composer not cleared in 5s → resend ONCE → else recovery |
| Recovery | 3 straight TIMEOUTs or stuck chat → fresh chat + close stuck tab + 1 retry |

## Ports & Profiles (4 browsers × 4 accounts — rotation matrix)

Four headed Chromes (9222–9225), each with its own `--user-data-dir` (`.chrome-chatgpt`, `.chrome-grok2/3/4`) holding a DIFFERENT account per LLM. Every browser carries tabs for all active LLMs; tasks pin continuity via `task.port`, otherwise round-robin across the row; `tasks/port_state.json` holds timed blocks parsed from limit messages (a blocked port is skipped, never retried blind). Grok paused (`GROK_ENABLED=false`) → 3-LLM rows until quota returns.

| AI | Ports | Profile dirs (1 account each) | Tab match (STRICT) |
|----|------|-------------------------------|--------------------|
| chatgpt | 9222, 9223, 9224, 9225 | per-browser profile | `chatgpt.com` |
| deepseek | 9222, 9223, 9224, 9225 | per-browser profile | `chat.deepseek.com` |
| gemini | 9222, 9223, 9224, 9225 | per-browser profile | `gemini.google.com` |
| qwen | 9222, 9223, 9224, 9225 | per-browser profile | `chat.qwen.ai` |
| grok | (paused) | per-browser profile | `grok.com` |

Rules: one poller per conversation; never two pollers on the same tab. STRICT tab match — `pages.find(url.includes(match))` only; if no tab matches, abort `NO_TAB`, NEVER inject into another AI's tab (cross-injection pollutes threads and wastes quota). LIMIT FAILOVER: a rate-limit signal (limit text on screen or in response) blocks that platform:port in `port_state.json` for the parsed wait (default 15min) and the task immediately fails over to the next port in the row — same LLM, next browser, different account. Only when all 4 ports for that LLM are blocked is the LLM skipped. New/fresh threads via helper scripts (`fresh_qwen*.js`, tab-restore scripts) that `goto` the home URL, never by reusing a foreign tab. Launch flags always: `--remote-debugging-port=<port> --user-data-dir=<dir> --no-first-run --no-default-browser-check` (headed). If all 4 ports refuse (`ECONNREFUSED`), all browsers are down — relaunch via `launch-browsers.bat` + `launch-extra-chromes.bat`, restore tabs, then resume. After any relaunch, verify tabs per port (`/json/list`) before injecting: a blank profile window means `NO_TAB` for every task.

| AI | Port | Profile dir | Tab match |
|----|------|-------------|-----------|
| chatgpt | 9222 | `<project>/.chrome-chatgpt` | `chatgpt.com` |
| claude | 9223 | `<project>/.chrome-claude` | `claude.ai` |
| gemini | 9224 | `<project>/.chrome-gemini` | `gemini.google.com` |
| deepseek | 9225 | `<project>/.chrome-deepseek` | `chat.deepseek.com` |
| grok | 9226 | `<project>/.chrome-grok` | `grok.com` |

Rules: one browser = one port = one AI. Never two pollers on the same port. Launch flags always: `--remote-debugging-port=<port> --user-data-dir=<dir> --no-first-run --no-default-browser-check` (headed).

## Adapters (composer / send / stop per platform)

Try adapter row first, then recovery row. Stop detection is ELEMENT visibility (`offsetParent !== null && getClientRects().length > 0`), never DOM presence, never body text.

| Platform | Composer | Send | Stop element |
|----------|----------|------|--------------|
| chatgpt | `#prompt-textarea` | `[data-testid="send-button"]` | `[data-testid="stop-button"]` |
| claude | `[contenteditable="true"]` | `button[aria-label*="Send" i]` | `button[aria-label*="Stop" i]` |
| gemini | `.ql-editor[contenteditable="true"]` | `button[aria-label*="Send" i]` | `button[aria-label*="Stop" i]` |
| deepseek | `textarea` | `button[type="submit"]` | `button:has-text("Stop")` |
| grok | `[contenteditable="true"]` | `button[aria-label*="Submit" i]` | `button[aria-label*="Stop" i]` |
| qwen | RETIRADO de la rotación (2026-09-11). Adapter histórico: `textarea` / `button[aria-label="Enviar"]` / `button[aria-label*="Detener" i]` |
| recovery (any) | `textarea, [contenteditable="true"], #prompt-textarea` | `button[type="submit"], button[aria-label*="Send" i]` | any `button` with `aria-label` matching `/stop|detener/i` |

If all composer selectors miss → abort `INPUT_NOT_FOUND`. If stop element never appears AND text grows + stabilizes 2 polls → treat as done (some UIs hide stop fast).

## Output Convention

- File: `<out>/<task_id>__<platform>.md` (e.g. `out/task_0001__chatgpt.md`). Idempotent: existing valid file is never overwritten.
- Content: prompt echo (quoted) + `---` + response text + footer `<!-- hash:<12> duration:<s> -->`.
- Optional sqlite row: `(task_id, platform, prompt, response, duration_s, success, error)`.

## Quick Reference

| Step | Check | Fail action |
|------|-------|-------------|
| Snapshot | composer + send + stop found | recovery selectors → abort |
| Read-back | exact normalized match | abort, never send |
| Submit | composer cleared | resend once, else recovery |
| Done | stop ELEMENT hidden + 2 stable polls | deadline → recapture once |
| Capture | non-empty, new hash, echo excluded | recovery, never blind reinject |

## Common Mistakes

- Driving the user's daily Brave/Chrome → session loss. Always project-local profiles.
- Detecting end by body-text substring ("detener" inside prose reads as generating forever) → element-level stop only.
- Capturing by message index → empty after virtualization. Content signature only.
- `browser.close()` on shared CDP → kills every agent's browser. `process.exit()` only.
- Passing functions into `page.evaluate` → serialization throw. Serializable args only.

## Red Flags

- Screenshot used to decide state.
- Coordinate click proposed.
- Blind reinject after timeout without recapture.
- Supervisor + manual inject on the same CDP port at once.

REGLA FIJA: toda apertura/inyeccion de navegador se hace SIEMPRE en Chromium CDP del kit (puertos 9222-9225), jamas en GinsBrowser/DICloak ni en el Brave diario (intocable). GinsBrowser es solo-lectura salvo orden explicita con disrupcion visible aceptada.

RUTA FIJA NAVEGADORES (`tasks/browser_routes.json` + `tasks/launch_browsers.ps1`): 9222 deepseek / 9223 chatgpt / 9224 gemini / 9225 grok. Cookies persistidas por perfil; jamas borrar perfiles ni mezclar cuentas.
