---
name: milo-caption-narrative
description: "Use when building narrative captions for MILO episodes."
version: 1.0.0
author: Hermes Agent
license: MIT
---

# MILO Narrative Caption Engine (V4 standard, proven EP001/EP002)

## Pipeline (mandatory order)

```text
AUDIO_MASTER → Whisper word timestamps → Caption Director → CAPTION_PLAN.json → cues + decisions → Remotion semantic-cues → render
```

Whisper is SYNC SOURCE ONLY: words + timestamps. It never decides cuts, importance, or highlights.

## Iron rules

- Position TOP always (global identity rule). Never lower-third, never adaptive, unless the user explicitly orders an A/B test.
- 1 emotional thought = 1 card. Never 1 sentence = 1 card, never fixed word counts.
- Word-active = emotional emphasis only (characters, narrative objects, emotional concepts). Never every-word karaoke.
- Reveal scenes: minimal text, solo card, emphasis level.
- Continuous speech (Whisper gaps 0.0s) stays ONE card even if the director wants a split — never fight the audio.
- Engine renders semantic cues EXACTLY (no merging). The legacy time-gap combiner fuses continuous-speech cards into giant blocks — always use `presentation: semantic-cues` with `cuesSrc` + `decisionsSrc` (anchors = highlight keywords).
- If a card needs splitting, split at Whisper word boundaries with real timestamps; verify grouping by replicating the combiner (new block when gap > combineMs).

## CAPTION_PLAN schema per card

`caption_id, text, start, end, emotion, narrative_function (setup/conflict/turn/discovery/hook/reveal/closing), highlight_words, pause_after, position: TOP, animation: soft_word_emphasis`

## Caption QC (automatic, before render)

Every card: <=10 words, has highlight, reveal cards <=6 words, position TOP. Result to `07_RENDER/CAPTION_QC.json`. Fix anchors pointing at words not in the card (invalid anchor fail).

## Learnings home

`10_CADENA/memory/learnings/02_VISUAL_LEARNINGS.md` accumulates caption lessons; this skill holds the process.