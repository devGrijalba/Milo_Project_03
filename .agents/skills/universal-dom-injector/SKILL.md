---
name: universal-dom-injector
description: "Use when injecting prompts into any web AI chat via DOM/CDP on Chrome (one browser per AI) and capturing responses."
version: 0.5.0
author: Hermes Agent
license: MIT
---

# Universal DOM Injector (Hermes Browser Operator)

Injects prompts into any web AI (ChatGPT, DeepSeek, Grok, Gemini, ...) over
`--remote-debugging-port` on Chrome and captures responses.
One Chrome per AI (own `--user-data-dir` + own CDP port), so agents run truly
in parallel without focus conflicts. PROJECT_01 never touches the user's
Brave/Chrome: all instances use project-local profiles.
Transport-level handshake lives in skill `cdp-injection-handshake`; this skill
owns the PROJECT_01 operator layout and workflow.

## Hard constraints

- Only project Chrome instances (9222 chatgpt, 9223 deepseek,
  9225 gemini) with persistent project `--user-data-dir`
  (`data/browser/profiles/.chrome-<ai>`; sessions survive restarts, no profile picker).
  Grok omitted by operator decision (9224 off, adapter kept for later).
- DOM only (`querySelector`, JS `click()`, keyboard Enter). Forbidden:
  mouse/pixels, vision/screenshots, coordinate clicks.
- End-of-generation at ELEMENT level (`stopElement`), never body-text
  substrings. Captures bound by CONTENT+POSITION signature (head+length
  pre-injection, nodes past the pre-count so back-to-back identical answers
  count as new, own-prompt echo excluded), never index.
- Actor scripts end with `process.exit(code)`, never `browser.close()` on a
  shared `connectOverCDP` instance.

## Layout (PROJECT_01)

```text
tools/   inject/supervisor/benchmark/status/consensus/validator/recovery/adapters/fresh_chat/browser.js
tools/data/  browser/ tasks/ memory/ out/ debug/ logs/ knowledge/   # runtime data
tools/launch-browsers.bat            # one Chrome per AI (own profile + CDP port)
skills/universal-dom-injector/SKILL.md
skills/FLUJO_DE_TRABAJO.md           # full workflow doc (review copy)
skills/README.md
```

## TASK protocol

```json
{
  "id": "agent_chatgpt",
  "platform": "chatgpt",
  "url": "chatgpt.com",
  "cdp": "http://127.0.0.1:9222",
  "prompt": "ping de prueba: responde OK",
  "attachments": [],
  "expected_output": "text",
  "timeout": 120000,
  "status": "pending"
}
```

Launch each Chrome with explicit `--remote-debugging-port` + project
`--user-data-dir` + `--no-first-run --no-default-browser-check` (explicit
dirs skip the OS profile picker entirely).

Run: `node tools/inject.js --task ./data/tasks/task_0001.json`

## Cycle

1. Connect CDP → find tab (autodetect adapter by URL) → logical DOM snapshot
   `{platform, input_found, send_found, response_found, adapter, timestamp}`
   (metadata only, no screenshot).
2. Recovery for composer/send if adapter selectors miss; abort
   `INPUT_NOT_FOUND` when all levels fail.
3. Inject via native setter + `InputEvent(input, bubbles)`; exact normalized
   read-back before submit, mismatch = abort.
4. Submit via DOM button click or Enter; confirm composer cleared.
5. Poll `stopElement` for VISIBLE presence (`offsetParent`/`getClientRects` —
   a hidden stop button in the DOM reads as 'still generating' forever) +
   2-poll stability with heartbeat; read text as `innerText || textContent`
   (virtualized chats return empty `innerText`) from the last non-empty node
   excluding your own prompt echo (user and assistant can share one class).
   On deadline expiry recapture once (valid → save, invalid → recovery,
   never blind reinject).
6. `validator.js`: non-empty, `stopVisible === false`, `hash !== prevHash`.
7. Save to `data/out/` (idempotent per task) + insert row into `runs.sqlite`
   `(task_id, platform, prompt, response, duration, success, error)`.
8. `tools/consensus.js`: normalize → vote (uniform weights V1, calibrated
   later) → majority + confidence; `<60%` = abstain, ask human.
9. Observability: per-run checkpoints (`CONNECTED → … → ASSISTANT_DETECTED
   → … → VALIDATED`) in `data/memory/states/`; DOM-only debug dump in `data/debug/`
   on failure. 3 straight TIMEOUTs on a platform → `FAILED_CHAT_STATE`,
   open a fresh chat instead of sending.
10. Stuck conversation (turns grow, no assistant text): open a fresh chat,
    close the old tab — never blindly retry. Full flow: `FLUJO_DE_TRABAJO.md`.
11. V0.5 incident memory (passive): `data/knowledge/incidents/<ai>/*.md` + approved
    rules only; failure codes 4/7/8/9 (`NO_RESPONSE_TIMEOUT`=log only).

## Multi-agent (3 browsers + 3 agents + 1 supervisor; grok omitted)

- One agent = one Chrome + one tab/IA: `data/tasks/agent_<platform>.json`
  (TASK object + `cdp` port + `status`). Launch: `tools/launch-browsers.bat`.
- `data/tasks/queue.json` lists the 3 agents; `tools/supervisor.js` dispatches them.
  `--parallel` runs all 3 at once (separate browsers, no focus conflict);
  default is sequential. States: `pending → running → completed | failed`.
  Run: `node tools/supervisor.js --parallel`; rerun done: `--rerun`.
  Auto-recovery: exit 7 (`FAILED_CHAT_STATE`) or 8 (`STUCK_GENERATING`) →
  `tools/fresh_chat.js` (fresh tab, close stuck) + 1 retry.
  Overall deadline 600s.
- Never run supervisor while a manual `inject.js` targets the same agent's
  port (one poller per conversation).

## Dashboard V2 (read-only)
- `tools/dashboard_snapshot.js` → `data/out/dashboard.{json,html}` (reads
  queue+sqlite+CDP+knowledge only; never DOM). Registry
  `data/agents/registry.json` holds per-agent adapter versions.
- Cards: conexion, version, exito historico, confianza (Alta≥90/Media≥60),
  tendencia ult-20 (↑/↓/→), tiempo medio, ultima tarea, ultimo incidente.
  Panel = torre de control, no piloto.

## Sessions

- Persistent project profile dirs keep logins; export per-AI backups with
  `context.storageState({ path: 'data/browser/<ai>-session.json' })`.
- If a tab lands on a sign-in page, stop and ask the user to log in manually
  in that AI's project Chrome window, then re-save the session. Never guess
  credentials. Thin backup files (few cookies) mean that AI keeps its session
  in localStorage — the live profile dir is still the real persistence.

## Adding a new AI

1. Launch a project Chrome with its own `--user-data-dir` and free CDP port;
   open the AI there, log in if needed, inspect composer / send button /
   stop element.
2. Add entry to `tools/adapters.js` + `data/tasks/agent_<ai>.json` (with its `cdp`).
3. Test: `node tools/inject.js --task ./data/tasks/agent_<ai>.json --out ./data/out`.
4. Expect `READBACK_OK` + `VALIDATE {"valid":true}` + `SAVED`.
