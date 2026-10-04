---
name: milo-thumbnail
description: "Use when generating MILO episode thumbnails."
version: 1.0.0
author: Hermes Agent
license: MIT
---

# MILO Thumbnail Engine (proven EP001)

## Title formula (mandatory)

`CONFLICTO + PREGUNTA ABIERTA`, never summary + ending. Prefer misunderstanding (PENSE QUE NO LE IMPORTABA), unanswered questions (NUNCA SUPE POR QUE), direct mystery (POR QUE DEJABA LA LUZ?). Avoid poetic summaries, conclusions, explanations. Gate: curiosity > 80 AND spoiler < 40.

## Timing rule (standing)
- Thumbnails generate IN PARALLEL with the episode's initial image batch (same Flow plan, 3 extra assets) — never as an afterthought.
- Delivery is always video + thumbnail together. A video delivered without its thumbnail is an incomplete delivery.

## Generation

- Google Flow via CDP (`flow-cdp-operation` skill), 9:16, character + world anchors attached, baked display text in prompt with EXACT spelling quoted.
- Typography in prompt: rounded heavy cartoon, thick black outline, deep shadow, white/yellow contrast, mobile readable, small EP badge.
- Minimum 3 variants with different angles (curiosidad / emocion / momento). Text overlays via PIL are the fallback when Flow garbles spelling.

## QC (mandatory before lock)

- Gemini (or OpenRouter cascade) transcribes baked text letter-by-letter: spelling must be exact (accents count). Score curiosity/spoiler/legibility per variant; winner = highest curiosity with spoiler < 40.
- Operator vision may be down (503) — never approve spelling by eye; the judge transcript is the authority.
- Lock winner in `07_RENDER/THUMBNAIL_REPORT.json` (`THUMBNAIL_LOCK`); keep losers + PIL fallbacks archived.

## Learnings home

Title lessons accumulate in `10_CADENA/memory/learnings/SUCCESS_PATTERNS.md`; this skill holds the process.