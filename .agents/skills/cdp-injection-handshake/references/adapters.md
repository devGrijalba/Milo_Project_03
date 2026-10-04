# Multi-AI adapter table (universal injector)

Use when one actor must inject into any LLM chat (ChatGPT, Gemini, DeepSeek, Grok, ...) without forking per-site scripts.

## Shape

Each adapter is one row with the same five keys:

- `match`: URL substrings identifying the AI (e.g. `chatgpt.com`, `gemini.google.com`).
- `composer`: textarea or `div[contenteditable]` selector.
- `sendButton`: submit button selector (fallback is keyboard Enter).
- `stopElement`: element that exists ONLY while streaming (button aria-label / data-testid). Never a body-text substring.
- `messages`: message-node selector for the content-signature capture.
- `submit`: `"keyboard-enter"` or `"button-or-enter"` (try DOM click first, Enter as fallback).

Always ship a `generic` row (`textarea, div[contenteditable=true]` + Stop/Detener variants) as fallback.

## Validated rows

- `qwen` (chat.qwen.ai): composer `textarea`, send `button[aria-label="Enviar"]` (icon-only, enables only after framework registers text — use the keyboard.type fallback), messages `div.response-message-content` (assistant only; the last generic node on the page is UI chrome, so a broad selector captures labels instead of answers). New threads start at `/` (home); a reused thread serves its old response as your capture. Run one task family per fresh thread: when a capture's hash equals an already-saved artifact (or the thread's pre-existing content), delete the artifact, navigate the tab home, and retry there — never reinject into the tangled thread, the next capture will latch onto the same stale node.

## Procedure

1. `connectOverCDP`, list pages, pick tab by URL substring argument.
2. Autodetect adapter by matching tab URL against `match`; explicit `--adapter` flag overrides.
3. Inject via DOM only (value setter + `input`/`change` events for textarea; `textContent` + `InputEvent` for contenteditable), then run the SKILL.md handshake unchanged.
4. Verify new AI rows with a `ping: responde OK` prompt and confirm `READBACK_OK` + `SAVED` before batch use.
5. Verify syntax with `node --check` on actor + adapter files before reporting done.

## Pitfalls

- Probe a new adapter's `stopElement` while a generation is actually streaming — a selector that looks right in static DOM may never appear during streaming and the waiter then exits early with a partial capture.
- Keep `messages` broad enough to match the assistant turn but narrow enough to exclude the composer echo — an over-broad selector binds the pre-injection signature to the wrong node and every capture looks "not new".
- On Windows, launch Brave as `brave.exe --remote-debugging-port=<port> --user-data-dir="<dir>"` and keep it open; the supervisor owns lifecycle, the actor never closes the shared CDP browser.
