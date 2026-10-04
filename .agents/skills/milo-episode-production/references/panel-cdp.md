# Panel driving via CDP — Hermes operating the external chats itself

When Hermes (not the user) pastes the master and collects answers by driving
the four chat tabs through Playwright over `chrome --remote-debugging-port`,
these rules hold. They cost real rounds before being encoded.

## 1. Tab continuity is the context

A navigation kills the conversation and the prompt is lost with it, so never
`goto`/reload a tab that holds a live round — FASE 2 always goes in the SAME
tab as FASE 1. A brand-new tab always receives the MASTER first, never the
winning story alone (a winner without master context produces off-protocol
output). Restarting the browser loses every tab, so this pairs with rule 5:
rebuilding means master-first in fresh tabs.

Never call `browser.close()` on the shared `--remote-debugging-port` Chrome — it kills every tab including other rounds. Close only the worker pages you opened.

## 2. Verify delivery with the injection contract

All sends use `inject(page, text)` from `references/chrome-cdp-injection.md` §3 (sole injection contract for every model and for the Flow composer): resolve composer → fill → READ BACK the value actually present and compare equality (master >1000 chars, short sends >200; a `type()` that leaves no value is a failure, never a send) → human pause 8–15 s, one model at a time, never bursts → real-keyboard Enter over CDP → verified send (composer emptied AND page state advanced).

## 3. DONE detection must exclude your own message

The sent master contains the same markers you poll for (EN ESPERA, PLANO),
so marker presence alone fires on your own echo. DONE requires length growth
over the pre-send baseline plus real content (a `HOOK:` line with
non-placeholder text for FASE 1, `PLANO 01` for FASE 2), confirmed by a
second stable read seconds later. Tune growth thresholds per model — a compact
responder can finish well under a threshold set from a verbose one.

## 4. Supervise per model, alert on stall

Poll every ~2 s and extract + report each model the moment it completes —
process-level completion notices only fire at process exit, so a watcher that
finishes three models silently and waits on the fourth tells you nothing
until it ends. If a tab shows no response activity after ~5 min, raise it as
STALL (often a failed delivery — verify the tab actually received the
prompt) instead of waiting in silence.

## 5. Extract early, disk survives the browser

Chrome can die between commands and take every tab with it. Pull each
finished answer to disk immediately; saved extractions make a rebuild cheap
(master-first resend) instead of a total loss.

## 6. Anchor audits on the answer, never the echo

Extracted page text contains your sent prompt followed by the model's reply,
and the prompt itself carries every marker (PLANO, voice JSON template, EN
ESPERA) — so always anchor on the LAST occurrence of a marker; the first one
is your own echo and auditing it false-fails intact packages. Before
comparing voice text against the frozen script, unescape page-level quote
escaping (`\\"` → `"`); a naive compare false-fails on punctuation alone.
Then check the voice text starts where the frozen GUION starts: models merge
HOOK+GUION into the voice text whenever the two differ, which shifts word
count and duration and breaks G sync — a prepended hook is a structural
defect, not a variant.

## 7. Recovery = LLM_RECOVERY_ESCALATION (sole implementation)

Recovery lives ONLY in `references/chrome-cdp-injection.md` §7: after ≥3 failures on the same CDP step → pause → INCIDENT_PACKET → panel → synthesize → test → verify → record → continue. No parallel recovery rules anywhere. It instantiates the general AUTO-RECOVERY loop (`references/milo-story-performance-loop.md` §6): any solvable blockage gets detected → formulated → injected → contrasted → lowest-risk fix applied → QA re-run, automatically; the human stays only for the truly unresolvable.

Narrative authorship is separate: ChatGPT writes/rewrites stories (`references/chatgpt-author-service.md`); other LLMs criticize and judge. Recovery packets fix AUTOMATION; REPAIR packets fix STORY — never mix them.
