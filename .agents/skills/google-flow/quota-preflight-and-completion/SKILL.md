---
name: quota-preflight-and-completion
description: "Use before and during any paid generation."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [flow, quota, preflight, completion, bridge]
    related_skills: [flow-bridge-operation, reference-authority]
---

# Quota preflight and completion authority

## When to Use

- Immediately before any command that spends a paid generation.
- After a gate block, to tell a sequencing error from a real motor failure.
- While waiting for a generation that is already running in the background.
- Before reporting a generation as done, to confirm the artifact exists.

Not for choosing *what* to generate (see `reference-authority`).

Two rules about the boundary of a paid action: what must be true *before* you
spend, and what counts as "finished" *after*.

## Preflight: 5 checks, then submit

A `--go` launched while the bridge was still connecting returned `GATE_BLOCKED`
in 0.5 s. No quota was spent — the guard stops before sending — but the run was
lost and it was indistinguishable from a real motor failure.

The block was correct. The sequence was wrong.

Before any authorized generation:

1. **bridge ping** — it answers
2. **worker connected** — the extension is live (not automatable from outside; ask
   the user to open or reload the side panel)
3. **bridge free** — not `busy`, no active cooldown
4. **manifest resolves** — dry run only, 0 quota
5. **prompt hash confirmed** — the hash that will be submitted is the hash you
   checked

All five green → submit. Any red → 0 quota, report, fix.

**The distinction this rule buys you:** a gate block *with* preflight green is a
real motor failure and worth investigating. A gate block *without* preflight is
our sequencing error. Without the rule those two look the same.

Check the network first because it is the only thing that fails silently and the
only one you can verify for free. If the bridge is down there is no point
resolving the prompt. The order matters for diagnosis, not for safety.

## Completion: the artifact is the authority

The real end of a job is **a new, stable file in the downloads folder** — not the
`job_done` message, and not the process exiting. Timeouts are 18 min with no file
and no notice.

- **Do not poll a background process that already notifies.** Duplicate mechanisms
  waste turns, can report "still working" for a job that finished minutes ago, and
  hide failures that already happened.
- **Verify the file on disk before analysing it.** If no file and no notice after
  the timeout, that is a real timeout.
- **Then** verify the run record: the submitted prompt and the manifest hash must
  match what you preflighted. A record that disagrees with the artifact means the
  wrong thing was sent.

## Ordering after a generation

```
request (background, notify)
  → notification
    → artifact exists on disk
      → run record matches the preflighted hash
        → analyse
```

Skipping a step to save time reintroduces the exact failure the preflight exists
to prevent.