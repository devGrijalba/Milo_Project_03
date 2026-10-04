# CHATGPT_AUTHOR_SERVICE (autoría narrativa de MILO)

ChatGPT is the PRIMARY STORY AUTHOR for MILO, operated by Hermes via browser injection. Authorship and orchestration are strictly separated.

## Policy

Hermes MUST NOT independently write, complete, improvise, or substantially rewrite the final narrative. Hermes acts as orchestrator, context assembler, prompt injector, response collector, validator, evaluator coordinator, repair coordinator, production coordinator. FINAL STORY AUTHOR: ChatGPT via browser injection.

Other LLMs (Claude, Gemini, others) act as CRITIC / JUDGE / SECOND OPINION / PROBLEM SOLVER / DEBUGGER — never as automatic replacements of the author. Their observations return to ChatGPT, which produces the corrected narrative version. Never let successive models edit the text in chain (no Frankenstein scripts).

## Layers (strict)

MILO STORY SYSTEM → CHATGPT_AUTHOR_SERVICE → LLM_PROVIDER_ROUTER → CHATGPT_BROWSER_ADAPTER → CHROME → CHATGPT. The Success Engine never knows where ChatGPT's send button is — that belongs exclusively to the adapter. If the UI changes, fix one adapter, not MILO.

## STORY_CONTEXT_PACKET (assembled per run, no megaprompt resends)

`{system: MASTER_VERSION, task: GENERATE_FINAL_STORY, story_id, target_s, language, concept, winning_opening, champion_patterns, avoid_patterns, experiment, constraints, required_output_schema}`. ChatGPT receives exactly the needed context.

Authoring flow: Hermes assembles packet → activates designated ChatGPT session → injects MASTER + runtime context → injects generation request → waits → captures → validates → stores IMMUTABLE raw response (`..._chatgpt_raw_vNNN.md`, never edited) → forwards to Success Engine.

## REPAIR_PACKET (targeted, no full rewrites)

`{story_id, failure, evidence, do_not_modify: [ranges, hook, twist, ending], objective, max_additional_words}`. Example: weak escalation 11.2–17.4 s, do not touch hook/ending, introduce a state change before 14 s, ≤8 words. ChatGPT returns the repair; Hermes PATCHes → RETESTs. On validation failure Hermes diagnoses and reinjects — never silently rewrites the story itself.

## Versions

Every ChatGPT story version is `STORY VERSION +N` (raw stored, validated after). Repair constraints from the engine travel in the packet, not as free prose.
