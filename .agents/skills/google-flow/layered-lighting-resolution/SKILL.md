---
name: layered-lighting-resolution
description: "Use when environment and emotion lights conflict."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [flow, lighting, environment, emotion, resolution]
    related_skills: [flow-bridge-operation, reference-authority]
---

# Layered lighting resolution

## When to Use

- An environment plate and an emotion both declare lighting for the same shot.
- The emotion's `avoid` list names the light the plate actually emits.
- A prompt overflows its word budget and light is one of the contributors.
- A `compact` lock value cannot be shortened without contradicting its
  `composition`.
- An emotion declares no lighting at all and the prompt must not lose its light.

Not for reference selection (see `reference-authority`).

Environment light and the emotional modifier describe the **same property**. If
they are concatenated, the model receives two instructions for one thing — and
when they disagree, it averages or ignores both. Resolve them into one string
first.

This skill governs the *resolution*. For reference selection see
`reference-authority`.

## The four outcomes

Resolve environment + emotion into one `resolved_light`. Exactly one applies:

| outcome | when | effect |
|---|---|---|
| `removed_conflict` | emotion's `avoid` names the light the plate emits | environment wins; emotion's light does not travel |
| `removed_redundant` | every family the emotion adds is already in the environment | environment wins |
| `fused` | emotion repeats some families **and** adds new ones | keep the environment's concrete sources, append only the emotion's new terms |
| `applied` | emotion shares no family with the environment | emotion's light replaces, as a subject modifier |

## Why overlap is detected by family, not by meaning

Two strings can say the same thing without sharing a single word:
`soft golden light against dark` and `blue shelf light, distant warm lamp` both
describe warm light in shadow. So the comparison runs over declared **families**
(warm, cool, dark, direct, diffuse) whose member tokens live in the lock. If the
lock does not declare them, you cannot detect overlap and you must not pretend
to.

## Fusing is not word-saving

The purpose of fusion is a single authority, not fewer tokens. A fused string can
be *longer* than the two inputs. Do not reject a fusion because it did not shrink
the prompt.

## Absence is not absence of light

When an emotion declares no lighting, the environment's light is used. Returning
`null` here silently drops lighting from the prompt entirely — that was a real
bug: a scene whose emotion had no `lighting` field produced a prompt with no light
at all.

## Always report the decision

Never remove the emotional modifier without recording why, or it looks like the
system forgot the emotion. The report names the outcome, the reason, the families
involved, and states that the emotion can still be carried by acting, pose,
composition and rhythm:

```json
{"lighting_resolution": {
  "environment": "…", "emotion_modifier": "…",
  "decision": "fused", "resolved_light_en": "…", "reason": "…",
  "familias_ambiente": ["…"], "familias_emocion": ["…"],
  "familias_repetidas": ["…"], "familias_nuevas": ["…"],
  "la_emocion_sigue_viva": "…"
}}
```

## Compact locks: complexity decides the limit

A plate whose composition declares two real light sources (e.g. "the blue
dominates, the only warm one is far away") cannot be compressed to one idea
without inverting the space. Declare it:

```json
{"lighting_complexity": "compound",
 "lighting_sources": [{"type":"ambient","priority":1,"description":"…"},
                      {"type":"accent","priority":2,"description":"…"}]}
```

The higher limit is earned by declaring the sources. An exception with no
sources is freedom, not a rule. And a compact that contradicts its own
`composition` is a regression — check for it before every send.