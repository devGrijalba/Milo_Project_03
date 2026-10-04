# Editing a JSON lock without losing canon

Locks are the canon. A careless edit deletes it silently, and the loss is
invisible in the prompt and in the plan — you find out by diffing after the
fact, or worse, not at all.

## Why round-tripping is dangerous

`json.load` → mutate → `json.dump` rewrites the entire file: indentation is
normalised, and **arrays that were spread over several lines collapse onto one
line**. In a lock where `light_en.full` is a multi-line array of strings, that
reformat can drop entries. The write reports success, the resolver keeps working,
and canon you never intended to touch is gone.

Observed: a cleanup script intended to shorten two `compact` values deleted two
strings from an unrelated `full` array in the same plate.

## Procedure

1. `git status --short` before touching anything. If the file is clean, you can
   revert in one command.
2. Prefer a **targeted patch on the exact field**. `patch` with enough context
   to be unique changes one value and leaves the rest byte-identical.
3. If a script must write the file, **copy it to a backup first**, and after
   writing, diff the two parsed structures field by field and print the count of
   real differences. Formatting rewrites show up as a wall of `-`/`+` lines and
   will bury a genuine one-liner removal.
4. `git diff -- <lock>` and read the `-` lines. Every one must be a field you
   meant to change. Anything else is data loss: `git checkout -- <lock>` and redo
   it as a patch.

## Gate scripted lock edits with a structural diff

The manual diff-and-read procedure above only protects you while you remember
to run it, and it reads as noise when a formatter touched every line. Turn it
into an executable check that compares the lock against a known-good version
(usually git `HEAD`) field by field and **fails on any change outside an explicit
allowlist** — the fields a cleanup is permitted to touch, such as `compact`, its
audit string, and any new declaration the rule introduces.

Report two counts: allowed changes and forbidden ones. Forbidden non-zero is a
hard fail naming the paths.

This earns its keep for two reasons that both showed up. First, a cleanup script
that re-serialises the lock *can* pass every functional test and still delete
unrelated canon, because the tests read the resolved values, not the file. Second,
a diff full of formatting churn hides a one-line deletion: the real loss scrolls
off under hundreds of reformatted lines. A structural diff reports "N allowed, 0
forbidden" in one line, which is the only way to know a scripted edit was clean
without reading the whole file.

Derive the allowlist from the rule being enforced, not from what the current
diff happens to contain — otherwise the first bad run teaches the gate to accept
whatever it just did.

Pair it with a content audit, not instead of it: the structural diff proves the
edit was scoped, the semantic audit proves the value is still correct (a light
compact that no longer names its dominant colour is scoped correctly and still
wrong).

## Auditing compact projections

`compact` is a production serialisation, not a description. It exists so the
word gate fits; `full` is the documentation.

- **The word ceiling depends on declared lighting complexity, not a constant.**
  A plate with ONE light source is `simple` and holds to 6 words. A plate with an
  ambient plus a differently-roled accent is `compound` and holds to 8. Declare
  it per plate (`lighting_complexity`, plus `lighting_sources` listing each
  source with type and priority) and have the validator read the declaration —
  never infer complexity from word count, and never derive it from prose. The
  exception is not licence: a `compound` plate that does not declare its
  sources fails the audit, or the ceiling becomes an open door.
- **3-6 words, one idea, no prose** for `simple` plates. Compare siblings before
  writing: a plate whose compact runs to 10 words while its neighbours hold 4 is
  the bloat.
- **Never let compact contradict `composition`.** Read the plate's `composition`
  field before compressing its light. A space described as *blue light dominant
  with one distant warm lamp* cannot compress to the warm lamp alone — that
  inverts the room. Where a space has two light sources with different roles,
  both belong in compact, even past the ceiling of a `simple` plate. An inverted
  space is a canon defect.
- **Stamp each compact with its own audit** (`n/max words [complexity]`) so the
  next reader can see whether it was checked or merely inherited.
- A cheap automated audit catches regressions: assert the ceiling *for the
  declared complexity*, assert every compact carries its audit string, assert a
  `compound` plate declares at least two sources, and assert that a plate whose
  composition names a dominant colour still has it in compact.
- **The fixed render tail is part of the budget.** The style/render suffix is a
  global constant (around 11 words including `no text`) that no lock may
  shorten, so a 30-word gate leaves roughly 19 for everything else. When a gate
  overflows, subtract it before blaming the variable parts, and count words per
  contribution rather than guessing which one grew.

## Deduplicate lighting before growing the gate

When the gate still overflows after the locks are clean, the next suspect is not
length — it is **two systems describing the same property**. The general rule
that also governs identity and framing:

> **One visual zone, one authority.**

Applied to light: before sending the emotion's subject modifier, compare what it
would add against what the environment already declares. If every lighting
family it contributes is already present in the environment, it adds no
information — drop it and record why. Repeating a property is not reinforcing
it; it is two instructions for one zone plus budget the director paid for.

Classify each side into declared families (warm / cool / dark / direct /
diffuse) before comparing. Then:

- **Drop the modifier and record the decision in the resolved scene** —
  `decision`, `reason`, the families on each side, and which families repeated.
  Never drop it silently: an emotion that vanishes without a trace reads as a
  bug, and the next session re-adds it.
- **Record that the emotion is still expressed**, just through another channel:
  acting, pose, composition, cutting rhythm. Removing a duplicate light does not
  remove the emotion from the shot; it moves it to where it is not redundant.
- **Partial overlap is not redundancy.** If the modifier contributes even one
  family the environment lacks, it carries information and travels. A warm
  modifier over a warm-and-cool space adds penumbra the space never declared.
  Test for *full* coverage of the modifier's families, not any overlap.

This is why a layered-light resolver needs both the conflict path (the emotion
`avoid`s the environment's light) and the dedup path (the emotion repeats it).
Conflicting and redundant are different failures with the same symptom: a gate
that will not fit.

## Detect conflicts by resolving layers, not by priority

When two sources describe the same property (light from the space and from the
emotion), priority-based substitution hides the contradiction and can hand the
model two opposite instructions. Resolve layers instead: the space is the
environment and is always preserved; the emotion is a subject modifier applied
only when it does not contradict; the conflict is declared in the resolved scene
with both sources and the reason.

Test each `avoid` entry against the plate's light tokens to detect the conflict.
Keep the emotion's own fields untouched in the lock — only its application to
that shot changes.

Keep the layer marker cheap. Wrapping a modifier in a phrase (`soft X on
subject`) costs words that push previously-fitting shots over the gate; one word
is enough to mark it.