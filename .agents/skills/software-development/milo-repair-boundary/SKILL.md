---
name: milo-repair-boundary
description: 'Use when fixing MILO defects without touching intent.'
---

# MILO repair boundary

Intent is the Director's. Execution is Hermes'. Hermes repairs the
execution so the episode arrives intact — it does not make the episode
"better".

## Three levels

1. **AUTOFIX (continue)** — format, references, canon, decorative motion,
   explanatory voice markers, timeline recomposition to the real voice
   (breaths 0.6–1.2s, text intact, never pad).
2. **Conservative reinterpretation (continue, log)** — same meaning, safer
   representation. e.g. "memory of grandma" → non-verbal trace (ring stain,
   worn texture, hands only) + explicit ban on faces/entities in steam.
3. **ESCALATE (stop, one question)** — two incompatible valid readings, a
   fundamental creative decision (new beat, new twist, different character owns
   the object), or a canon conflict with no conservative fix.

**A duration gap is never an escalation trigger by default.** Classify it
before acting — the split is by proportion of declared target filled, not by
whether a gap exists at all:

- **Caso A — voice >=55% of target** (or the gap fits bounded breaths/holds):
  AUTOFIX. Rescale the beat map to the voice, set the new runtime yourself,
  and say in one line which constraint won and how it was measured.
- **Caso B — voice <55% of target** and no natural recomposition closes it:
  ESCALATE. The package is missing real content; filling it would require
  adding narration or beats, which is creation, not repair.

The two cases are different failure modes, not a single "always autofix"
posture. Offering "A: extend the script / B: shorten the episode?" is still a
failed handoff when the user has not been asked to decide; when Caso B is real,
returning the decision to the Director is the correct output, not a failure.
Supply the specific Director decision needed (widen the SCRIPT_LOCK, or accept
the real duration) instead of a generic question.

## Decide, don't ask

After a rejection, the next move is a decision, not a question. Real case:
the viewer rejected a 62.8s master; the obvious next step was to offer two
options. The correction was "NO pides, tomas decisiones que sean mejor para el
episodio, en eso consiste que seas creativo" — so recompose to ~25s with
0.7–1.2s breaths, a payoff hold, and ship. When a fix is reversible and sits
inside the execution, choose it, name the tradeoff in one line, and deliver.

## Hard prohibitions (any level)

Never rewrite narration text, add/remove beats, invent objects/characters/
twists, change the arc, the ending, the message, the character's decision,
the canonical voice, or pad audio with silence to hit a number.

## Guards

- `_guard(fix)` rejects prohibited fix descriptions.
- `assert_text_preserved(before, after, rule)` fails the repair if any token
  of the locked line is lost (a marker may be removed; words may not).
  This exists because a marker-stripping regex once turned
  "Recuerdo las manos de mi abuela" into "Recuerdo las".
- Autofix is a peer of production: output the repaired artifact, a log entry
  (error/evidence/level/fix/reason), and continue.

## When a rule is wrong

A gate must know the real output of the engine and accept documented
exceptions. Real case: `pix_fmt=yuvj420p` is what Remotion emits (accepted),
and a payoff hold of 2.9s is legitimate when FINAL_QC H05 documents it.
A gate that blocks correct output trains you to ignore gates.

Before blaming a gate for a false positive, check whether your own first
implementation is the idealization (e.g. demanding `yuv420p` when the engine
writes `yuvj420p`, or blocking any >2s hold when the payoff legitimately holds
2.9s in the last 35%). Fix the detector to the artifact reality, not the
artifact to the detector, and exempt only what the QC report documents.

## Duration is measured, never declared

A package's own duration arithmetic (`50s visual + 38s voice = 50s`) is a
proposal until the produced audio is measured. A real case: the lock declared
38s of voice from words/second arithmetic; the six rendered TTS lines measured
17.92s. Filling the 27s gap produced a 62.8s master the viewer rejected as
"too many pauses, unusable". Rule: **ffprobe the sum of the actual voice lines
first**; a declared duration never justifies silence padding. Then apply the
Caso A/B split: voice >=55% of target -> rescale the beat map to the voice
(0.6-1.2s breaths, hold in the payoff) and re-render, so the voice defines the
runtime; voice <55% -> ESCALATE with the specific decision the Director owes.
Never rewrite the package's declared target to hide the gap, and never report a
declared number as if it were measured.

## A Director lock is not self-validating

Even a "validated" Story Time Lock / scorecard in a structured package — or a handoff/CHANGELOG marked COMPLETED — is a proposal.

- On resume, a project's own handoff doc, README or completed-phase report is a claim about the past, not a measurement of the present. Re-derive the state from the artifacts before reporting it or building on it: probe the rendered duration instead of trusting the declared runtime, read the per-asset QC verdicts instead of the summary line, count the beats against the promised count, read `aprobado`/`experimental` flags rather than assuming a file named `final` is finished. A completed-phase doc and a placeholder master routinely coexist; reporting project state from the doc hands over the wrong picture and every later decision inherits it.
proposal. If the numbers it asserts cannot be reproduced from the produced
assets (voice duration, physical anchor paths, episode_id format), the preflight
still BLOCKS and the package returns. Re-running the gate over the real
environment catches what the package's own `approved: true` hides — e.g. an
episode_id that ignores the chain's `MILO_<FORMAT>_EP###_V#` contract, and
reference filenames (`taza_antigua_ref.png`) that do not exist as physical
anchors. Report which blocks are real defects vs which are your own detector's
false positives, in that order.

## Judge and evidence strictness (learned live)

- A judge ACCEPT with failing numbers or style flags is a contradiction, never a pass: block registration/review and say so.
- A judge FAIL whose own notes describe the artifact as correct is a defective criterion, not a defective artifact. A bare criterion name carries no polarity — `is_human_face` reads as "must be present" and "must be absent" equally, so on a canon that bans human features the correct render satisfies the very token that fails it. Every criterion must declare its polarity (`must_be_present` / `must_be_absent`) or the verdict must spell out the reading. When flag and notes disagree, re-read the criterion and re-verify the existing artifact before regenerating anything: the pixels already on disk passed.
- An STT REVIEW against a locked PASS closes only with a written per-word reconciliation (seseo homophone, same-lemma inflection, accent-only); any unexplained word keeps REVIEW.
- Text-correct captions are not Reels-legible captions: gate ≤2 visible lines with split points for long cues, declare position, verify against render — never assume.
- Sanitize banned terms at the assembly boundary (even when the Director's own source carries them), log the substitution, never weaken the ban.
- A global 'no changes' lock that contradicts a scripted change is a prompt bug: use per-beat state + a contradiction detector instead.
- Judge repair prompts apply as deltas over preserved blocks only — never pasted verbatim as the new prompt.

## Severity means action, not just ordering

A preflight rule's severity must state what happens next, and the mapping must
be stable across every layer that consumes it (`defects.yaml`, the guard
engine, the CLI, the tests) because a detector whose severity vocabulary drifts
from its engine silently loses authority:

| severity | action |
|---|---|
| `AUTOFIX` | correct, revalidate, continue |
| `CONSERVATIVE_REPAIR` | reinterpret with an approved equivalent, revalidate, continue |
| `WARN` | record only; continue (may promote after repeated occurrences) |
| `ESCALATE` | stop; return a specific decision to the Director |
| `BLOCK_FATAL` | stop; the package cannot be executed at all |

Introduce a new severity vocabulary in ONE place and derive older vocabularies
from it via a compatibility map, so a rename cannot silently convert a repair
into a block. When severities change, update the test assertions in the same
pass: tests still expecting the old vocabulary are the cheapest detector of a
half-applied policy change.

## An unresolved reference must never pass silently

A reference that does not resolve to a physical anchor and has no approved
equivalent cannot be dropped, renamed, or filtered out of the list — dropping
it makes the preflight PASS while quietly weakening the prompt. Three outcomes,
never a fourth:

1. Resolve to an existing physical anchor -> `CONSERVATIVE_REPAIR`, confidence 0.9.
2. It is a prompt descriptor, not a file (`gotero_ref.png` describes "a
   dropper") -> mark it a descriptor, keep it out of the anchor list, log the
   substitution.
3. No equivalent exists -> `ESCALATE` with confidence 0.95, preserving the
   original in `_unresolved_refs` so the residue is auditable.

Keep the equivalence catalogue covering BOTH the semantic anchor names
(`MILO_CHILD`, `BEDROOM_DAY`) and the physical filenames the chain uses
(`02_MILO_CHILD_TIMELINE_MASTER`, `09_BEDROOM_DAY_STATE_MASTER`): a catalogue
that knows only one naming family will escalate anchors physically present on
disk and make a conservative policy fail a clean package. Index entries by
anchor ID and accepted filename aliases, but bind bytes only through the
canonical file — IDs and aliases resolve to it, never around it. A
Director-declared descriptor (explicit policy, no physical file) may pass
planning flagged not-for-flow, but the executor must refuse it before any
metered spend: a plan-time pass is never a generation license.

## A conclusion about an artifact you are still writing is not a result

Two writers on one artifact produce two failure modes, and both read as a
technical defect when they are a coordination defect. Freeze the artifact before
anything measures it, asserts about it, or reports on it.

- **Stale verdict.** A subagent auditing a model while I was mid-correction
  returned a correct PASS/FAIL table for bytes that no longer existed. I
  regenerated the artifact afterwards, so the bundle shipped a report claiming
  7/7 FAIL next to a model that measured 7/7 PASS. Re-run the measurement after
  the last write, or explicitly re-verify every claim at pack time.
- **Partial read.** A rebuild loop that rewrites the model on each iteration
  raced a manual edit of the same model; the loop's next iteration read the file
  mid-write and reported structural nonsense ("the model has no animations").
  Timestamps on the artifact and its outputs localize this immediately: outputs
  older AND newer than the artifact's mtime mean the outputs straddle two
  different versions.
- **Rule:** one writer per artifact at a time. Either the pipeline owns the file
  or I do, never both. A pipeline that regenerates an artifact must not run
  alongside a manual edit of it; serialize them or edit a copy.
- Serialize before diagnosing. A coherence failure explained as a tool bug sends
  the next session hunting a defect in a tool that is fine.

## Repairs carry confidence and an auditable log

Every finding emitted by preflight must carry its policy severity, a numeric
confidence, the triggering evidence, the action actually applied, and a
post-repair revalidation flag. Repaired findings still appear in the report —
never as a silent mutation of the package. After repairing, re-run the same
detectors over the repaired copy; reporting `revalidated: true` without a
second pass is a fabricated OK.

## Distinguish a genuine escalation from a path bug before reporting

A detector that stops firing after an unrelated fix is usually broken, not
clean. Two real mechanisms: normalizing an `episode_id` changed the folder name
the voice-duration check looked in, so the duration check found no lines and
reported nothing; and a range regex on `duration_target` ("45-60s") extracted
the low bound and compared against it. Before concluding a defect is absent,
confirm the detector actually reached the data: verify the lookup path it uses
still exists after the earlier repair, and parse a declared range using its
actual bounds rather than the first number matched. A rule that vanished from
the output is a bug to fix before it is a result to publish.
