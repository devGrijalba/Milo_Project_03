---
name: reference-authority
description: "Use when picking which image references to send."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [flow, references, identity, framing, experiments]
    related_skills: [flow-bridge-operation, layered-lighting-resolution, quota-preflight-and-completion]
---

# Reference authority — one function per reference

## When to Use

- Before sending image references to any generative image model.
- When deciding whether to add, keep or drop a reference.
- When two sends differ only in their references and the result must be explained.
- When a master reference seems to override a prompt instruction.

Not for generating references (see `flow-bridge-operation`) and not for
choosing which emotional state a shot needs.

A reference transmits **everything visible in it**. Two references covering the
same zone are two authorities fighting, and the model averages them. The
Director's instruction loses.

This skill is about **which references to send**. For generating them, see
`flow-bridge-operation`.

## The question to ask before every send

For each reference: *what authority does this own, and is that authority already
claimed by a stronger reference?*

If two references claim the same authority, one of them goes. Not because
references are bad, but because the weaker one is now noise.

## Measured authority map (DARK project, 2026-10-01)

| layer | owner | how |
|---|---|---|
| identity, proportions, wardrobe, face | **master reference** | image |
| expression | **prompt** (`action_en`) | words |
| pose, body language | **prompt** | words |
| scene, action, context | **prompt + environment plate** | words + image |
| **framing / camera** | **nobody** | — see below |

## The lesson is not "use fewer references"

The temptation is to turn "fewer references worked" into "use fewer
references". That is wrong, and it will eventually delete a reference that was
carrying its own unique authority.

The correct rule: **remove a reference when it competes for the same authority
with a stronger one.** That is the measured case. A non-competitive but useless
reference is a different case, and it has not been measured — do not write it as
a rule.

## A crop derived from its own source does not gain authority

The natural fix when "the master dominates the composition" is a framing crop cut
from that master. **This was tried and it failed**: master + its own crop left
the framing unchanged (still full body). A crop loses against its own source.

So framing has no reference-layer fix. Its candidates are architectural and are
evaluated as architecture, not as the next crop:

- a **generated** framing master (a new image base with the wanted composition —
  new authority, costs quota)
- a **local compositor** (control the framing in post: crop, scale, position)
- **shot planning before generating** (assets conceived for the final frame)

## Before generating

- Check whether the reference you want is already marked **retired**. Retired
  assets stay on disk with their reason; deleting them only invites retrying the
  same failed approach.
- Prefer the manifest declaring *complements* (`expression`, `view`) over
  declaring a crop: a complement cut from a *different* view has a chance of
  owning an authority the master cannot; a crop of the master cannot.

## Recording experiments

When two sends differ only in references, that is an experiment, and its verdict
belongs on disk (the DARK project keeps this in
`knowledge/experiments/<EXPERIMENT>.json`). A conclusion that lives only in a
conversation gets rediscovered by spending quota.

Keep the prompt **byte-identical** between variants and record its hash. If the
prompt differs, you measured two variables and learned nothing about references.

Do not run an experiment whose result the previous evidence already predicts —
record it as `NO_EJECUTADO` with the reason, so nobody proposes it again.