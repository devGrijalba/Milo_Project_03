# Run discipline — incidents, inputs, reproducibility (E2E companion)

Companion to `references/validation-recipes.md`. Learned 2026-09-03 during
the TEXTOPIA H27 end-to-end run. General rules; examples are illustrative.

## 1. Operator incidents are not system FAILs (but missing input validation is)

When YOUR invocation is wrong (relative path, bad flag, wrong cwd), log it
as an INCIDENT: fix the call, re-run, disclose it in the report. Do not
count it against the system — and do not silently count the successful
retry as first-try success either.

However: if the tool accepted the bad input and died with a cryptic error
(e.g. a `TypeError` deep in the code instead of "file not found"), the
missing input validation IS a system finding (robustness class). Tools
under test should resolve inputs to canonical form (relative paths →
absolute, e.g. via `pathlib.Path.resolve()` / `as_uri()`) and fail fast
with an actionable message plus a non-zero exit code.

In TDD the same split governs the RED step: a red test must fail on the
asserted behavior — an import, cwd, or harness error is an operator
incident, not the expected failure. Fix the invocation and re-run until
the output names the missing behavior.

## 2. Reproducibility check (run it, don't assume it)

After the run, ask explicitly — this is a separate verdict input, not a
vibe:

- Same inputs → same outputs? Positive signal: deterministic stages
  produce bit-identical measurements across runs (e.g. same synth params
  → same dB readings to 0.1 dB).
- Nondeterministic providers: generators may silently vary output by seed
  or request (dimensions, framing). Record seed/source per artifact; a
  FAIL that moves between runs is still a FAIL, but tag it flaky.
- Hidden persistent state: stale frames/caches, occupied ports, leftover
  temp files, prior-run artifacts in shared dirs. Clean before the run;
  verify outputs are fresh (counts, timestamps, hashes), not skipped or
  reused.
- Manual spec effort: if the input arrived fully specified (timings,
  params hand-solved), the run proves EXECUTION, not autonomous
  generation. State which one was demonstrated.
