# Hermes-driven image generation in Google Flow via CDP

Hermes generates finals himself (user hand-delivery is the exception). All DOM injection over `chrome --remote-debugging-port` — never mouse/pixels, never screenshots-to-see for driving.

## 0. Click recipe (proven on flow.google.com project grid)

Never use synthetic `element.click()` for navigation buttons: resolve the button by visible text (`querySelectorAll('button')` + innerText match), `scrollIntoView({block:'center'})`, read `getBoundingClientRect()` center, then real CDP input (`Input.dispatchMouseEvent` mouseMoved → mousePressed → mouseReleased, left button) at those viewport coords. Verified: 'Nuevo proyecto' click opened a blank project URL (`flow.google.com/project/<uuid>`). Record the new project URL immediately — it is the worker tabs' base.

## 0b. Composer injection contract (proven: 'hola' round-trip)

The visible box is a `div[contenteditable=true]`; the `textarea` beside it is a React decoy (writes there never appear). Contract: real-click the composer's box center FIRST (rect of `div[contenteditable=true]`), then `document.execCommand('selectAll')` → Backspace keyDown/Up → `Input.insertText` → wait 1 s → READ BACK `innerText` and require equality — `focus()` alone leaves `insertText` silently failing (read-back mismatch), the real click fixed it. → after verification, select-all + Backspace again and confirm only `'\n'` remains, leaving the composer clean for real prompts. Never leave test text in the box.

## 0c. Fire sequence (proven end-to-end, Nano Banana 2 Lite)

`Input.insertText` takes a strict string (passing anything else raises -32602 and sends nothing); verify read-back equality; fire with real Enter keyDown/keyUp (`code: Enter`, vk 13); composer empties on accepted send; poll page text for `\d+\s*%` — fired jobs show progress (seen 25%) then settle (two consecutive reads without `%`); confirm with a `Page.captureScreenshot` showing the rendered thumbnail + prompt in the side panel before downloading. Proven 2026-09-16: Milo hallway still generated from text-only prompt matching identity.

## 0d. Anchor-reference generation (proven 2026-09-16, Nano Banana 2 Lite)

To generate from the identity anchor: shrink a JPEG copy to ~768px wide (~160KB) and dispatch a real `ClipboardEvent('paste')` with a `DataTransfer` carrying the File onto the focused `div[contenteditable=true]` — native Ctrl+V key events do NOT deliver image bytes to ProseMirror (composer stays empty), and the `textarea` is a decoy. Verify the anchor chip thumbnail appears above the composer (screenshot), then insertText the prompt naming the attached image as exact identity reference, verify equality, real Enter, %-settle. Proven: Milo-on-chair bulb still, identity 85/100 vs anchor. (Fallback that also works: 'Subir archivo…' → `DOM.setFileInputFiles` with the local path.)

## 0e. Agent config lock: 9:16 default (standing user rule)

Every session must generate at 9:16. Open the composer settings pill (Nano Banana row), click the 9:16 `BUTTON` by real mouse at its rect center, and verify machine-truth: the button's `aria-checked` must read `"true"` (others `"false"`) and the composer pill must contain `crop_9_16`. Never trust screenshot shading alone — panel focus styles mislead. Proven 2026-09-16.

## 0f. Chain runner (all-DOM, proven 2026-09-16)

One script runs anchor-paste → ratio-verify → prompt-fire → settle-detect with zero pixel-driving: paste the ~768px JPEG anchor via synthetic `ClipboardEvent`+`DataTransfer` File onto the focused composer DIV (native Ctrl+V delivers nothing to ProseMirror); assert 9:16 by `aria-checked` (never screenshot shading); focus + selectAll + Backspace, then `Input.insertText` strict-string and require read-back equality; real Enter; settle on two consecutive reads without `\d+\s*%`. Reference implementation: `flow_chain.py` (PROMPT constant at top). Proven: coffee still from anchor, 29% → settled.

## 0h. Lean runner (standing user rule — speed over peeking)

One background script per shot does paste → fire → settle with exactly two gates (prompt read-back equality, `%`-absent settle) and NOTHING else: no per-microstep DOM dumps, no screenshot per step, no separate poll scripts. Pattern: `flow_fire.py "<prompt>" [anchor.jpg]` (argv-driven, single file). Report only FIRED/SETTLED/FAILED. Extra verification round-trips cost more wall-time than the generation itself.

## 0g. Prompt language (standing user rule)

Generation prompts are ALWAYS in English, even when the brief, chat and subs are Spanish. Spanish prompts drift style and identity. Proven 2026-09-16: Spanish prompt fired fine technically but weakened identity lock; English prompt blocks are mandatory.

## 0i. Fire correction: Enter alone does NOT send (proven 2026-09-16)

§0c/§0f's real-Enter fire stopped working: prompt consumed (composer empties) but no job starts and no `%` ever appears. The working fire is clicking the send button (aria-label matching /iniciar generaci[oó]n/, the arrow_forward button) AFTER verified insertText. Multi-prompt batch requests and Agent-mode conversational sends are unverified — default to one prompt per fire. Single-fire order: real-click composer → insertText → assert equality → click send button → settle.

## 1. One blank project, parallel workers

Create ONE blank project (home → Nuevo proyecto), then open one worker tab per shot on the SAME project URL, each pasting its full Flow block (action order + expanded positive + merged `. Avoid:` negative, dimensions in natural language) into the session composer and firing generation.

MAX 4 workers in parallel — more trips Flow's too-fast throttle. Seven shots go in waves of 4+3 with a pause between waves. Stagger injections ~1 s apart (the 8–15 s human pause applies to LLM chat tabs, not to Flow prompts).

No reference upload needed: the fully expanded anchor inline carries identity (proven across episodes). A reference ingredient is optional, not required.

## 2. Settle detection per worker

A worker is done when no `\d+\s*%` remains in page text for two consecutive 15 s reads. Close only worker pages when finished — never `browser.close()` on the shared Chrome or every tab dies.

## 3. Download: project ZIP first, then 2K per shot

Top-right project options (⋮) → `descargar proyecto` → ZIP. The ZIP may hold only previews (~768px) or fewer files than generated — previews never render, so treat the ZIP as an index, not the final set.

Per shot: click its grid thumbnail → Descargar button → `2K` menu item → save. Verify every file at 1080x1920 or higher with identical dimensions across the set before anything enters `03_imagenes/`.

Grid/download pitfalls: filter thumbnails by rendered size (>100px), never by src substring (thumbs use rotating `/asb/` URLs); the grid re-renders after back-navigation and srcs rotate, so confirm the open viewer's content before each download and dedupe saved bytes by md5. A synthetic JS `.click()` may not open the viewer — click through a trusted element handle (`evaluateHandle` + `scrollIntoViewIfNeeded` + `click`). A stale tab can show an empty grid while a fresh tab on the same project URL shows the media — verify grid count >0 before starting the loop, else reload or use a fresh tab.

## 4. Assign by content, rename by copy-then-verify

Flow returns its own filenames — assign each image to its PLANO by CONTENT match against the shot list (beat, pose, object), never by arrival order. Copy to the canonical name (`MILO_<LANG>_R<NNN>_planoNN_<slug>.jpeg`), confirm with md5, only then remove originals. Close the used project tabs at the end.

## 5. Recovery reuses the unified protocol

No own recovery rule: stuck states use LLM_RECOVERY_ESCALATION from `references/chrome-cdp-injection.md` §7 (pause → INCIDENT_PACKET → panel → synthesize → test → verify → record). Flow-specific annex only: max 4 parallel workers (waves 4+3), ~1 s stagger, settle on absent `%`, 2K download, verify before archiving.
