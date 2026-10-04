---
name: e2e-validation
description: Run an end-to-end validation of a full system or pipeline.
---

# E2E Validation — execute before you judge

Class of task: proving that a complete pipeline (narrative, assets, build,
render, delivery — or any equivalent chain) works WHEN RUN TOGETHER, not that
each stage passes in isolation.

## Core sequence (never reorder)

```
EXECUTE → OBSERVE → VALIDATE → DIAGNOSE → REPORT
```

Run the chain as ONE continuous execution (`INPUT → … → FINAL OUTPUT`),
then report. Never `phase → stop → verdict → next phase`. A validator that
interrupts the run is testing stages, not the system.

## Rules

1. **Run the package's own verification chain first.** When a delivered pipeline ships built-in health/validate/score/test commands, execute all of them (not just one) before claiming the install works — a clean unzip is not a verified install, and one green check can hide a broken link the next command would catch.

1. **No fixes during the test.** Do not patch protocols, engines, configs,
   or assets to reach PASS; do not reshape the input to compensate for a
   pipeline defect. First know how the CURRENT system behaves.
2. **On FAIL: record, preserve evidence, assess continuability, continue**
   whenever technically possible. Trace each FAIL later as
   `ORIGIN → PROPAGATION → EFFECT → FINAL IMPACT` (did it get corrected,
   propagate, or stay in the final output?).
3. **Distinguish what the test proves.** A fully-specified input proves
   EXECUTION (`SPEC → output`), never autonomous GENERATION (`idea → SPEC`).
   State explicitly which one the run demonstrated.
4. **Estimated ≠ observed.** Predictions declared before the run (scores,
   quality claims) are estimates. Only post-run measurements are evidence.
   Never present a pre-run number as a result.
5. **Evidence chain per artifact** — verify every link, not just existence:
   `SPECIFIED → EXISTS → VALID → SELECTED → INJECTED → RENDERED → VISIBLE
   AT THE RIGHT MOMENT → CORRECT RESULT`. `EXISTS ≠ VALID ≠ CORRECTLY USED`.
6. **Contract PASS ≠ real PASS.** A timestamp/contract can be valid while
   perception is wrong (overlay on time but late for the narrative event;
   render completed but visually wrong). Where real inspection is impossible,
   declare that dimension **BLOCKED** (naming exactly what evidence is
   missing) — never simulate it, never average it away.
7. **Hunt interaction failures.** `A=PASS + B=PASS` can still yield
   `A+B=FAIL` (contradictory priorities, duplicated/ambiguous rules,
   dangerous defaults, lost data between stages, divergent interpretations
   of one instruction). List them separately from single-stage findings.
8. **False-pass analysis.** After the run, enumerate where validators could
   say PASS incorrectly (contract-vs-perception, asset-vs-usage,
   local-vs-global, story-vs-system).
9. **Verdict rule.** Never average results. One CRITICAL FAIL, or any
   BLOCKED load-bearing dimension, means NOT READY — regardless of PASS
   count. Possible verdicts: READY / NOT READY / BLOCKED, with the exact why.
10. **Registry parity.** When the pipeline declares effect/behavior names in
    a spec (motions, transitions, filters), the schema enum, the engine
    registry, and the tests must contain exactly the same set — enforced by
    an automated parity test, not by inspection. A name accepted by the
    schema but missing from the registry is a guaranteed silent wrong output.
    **One lookup path, not two.** When a data structure is split into
    namespaces (masters vs derived, primary vs auxiliary), expose a single
    accessor that reads the union, and make every consumer — including
    tests — call it. A test that indexes a sub-dictionary directly and
    another that calls the accessor will eventually disagree about the same
    file, and the failure reads as a data bug when it is a lookup bug. Add
    the parity assertion (accessor result == the declared dictionaries) as a
    test, since divergence is otherwise invisible until data changes.
11. **No silent fallback.** An undeclared/unsupported spec value must abort
    with a named error before/during the run — never degrade to a static or
    default output that looks valid. Prove it with negative tests (invented
    values rejected) on every run, not just once.
12. **Exit code ≠ verdict.** When a stage CLI exits nonzero on a recoverable
    verdict (e.g. RETRY with a resplit/retry path), the orchestrator must
    read the verdict artifact and follow the recovery branch — never treat
    any nonzero exit as terminal FAIL. Reserve STOP for FAIL verdicts or
    unreadable/missing verdict output.
13. **Negative contamination run.** After a positive E2E, plant a real
    artifact from a FOREIGN run (different episode/id) in the workdir and
    re-run from the consuming gate: the pipeline must BLOCK naming the
    provenance mismatch, produce zero deliverables, and never print a
    false COMPLETE.
14. **Resume-from-gate is part of the harness.** Long runs must accept
    `--from <stage>`, reusing prior valid artifacts; every resume is
    disclosed in the report (which stages were reused vs re-executed).
    A resume that skips a gate invalidates the run.
15. **Cross-artifact id consistency.** After delivery, assert the same
     publication/run id across every delivered artifact (report, QC files,
     gate seals, index) — one command reading each file, not eyeballing.
16. **Separate source truth from audit packaging.** When reviewing a snapshot, classify every finding as `ORIGINAL_CODE`, `PACKAGING_PATH`, or `ENVIRONMENT_EXTERNAL`. Verify critical claims by reading and executing the original project; a missing relative path in a relocated ZIP proves packaging behavior, not a source defect. Keep forensic and clean snapshots as separate artifacts.
17. **Adversarial false-PASS harness.** Before certification, run negative artifacts through the real production gate, not only a helper in isolation: black/corrupt frames, prohibited silence, missing MP4, stale QC hash, missing audio, and a foreign run ID. Any `PASS` or exit 0 with a load-bearing issue still present is a critical failure. Preserve command, input, output, and exit code as evidence.
18. **Chain closure requires linkage.** Intake, validation, repair, Flow, render, master audit, and delivery must share one run/publication ID and an immutable lock fingerprint. A delegated stage, file existence, isolated unit suite, or historical report is not completion. `MASTER_READY`/`FINAL` require the exact artifact bytes, QC hash, delivery evidence, and gate results to agree.
19. **Transactional creative repair.** Fingerprint Script Lock, spoken text, beats, canon, and Director decisions before repair; apply changes to a clone; discard the clone on escalation or failed revalidation. Never fill missing story/voice decisions with placeholders or mutate protected text.
20. **Evidence classes in the report.** Label every claim `VERIFIED`, `HISTORICAL`, `PACKAGING_ONLY`, or `BLOCKED`, with the command/path/version that supports it. Do not combine an old report with a fresh run without labeling the provenance.
21. **No version control means the documents ARE the history.** In a repo without git, the continuity protocol is the only record, so a single source of truth for the version number is a correctness requirement, not bookkeeping. Name one file as authoritative (the state document, written at the moment the work is done), one as the append-only history (changelog), and one as the architecture/vision document that follows the first. State in each of them which file wins on disagreement. When several documents declare different version numbers, the drift is the finding: report it, fix it, and add the cross-reference so the next session does not have to re-derive which document is stale.
22. **One declared source of truth, compared by content hash.** When several versions of an input exist and artifacts were derived across more than one of them, name the official version and gate on it. Compare by content hash, not filename or path: two paths holding identical bytes are the same source, and the same path holding different bytes is not. Absence of a version declaration is not exemption — a stage that receives the source as an argument and never records it produces an orphan artifact, and that is the defect to fix. Staleness cascades transitively through declared sources, so verify it by chaining each one rather than trusting a hand-written state field. Retire superseded versions on disk with their reason instead of deleting them, because deletion lets the same divergence reappear with no record of having been solved once. State the scope limit explicitly: a per-episode lock leaves other episodes unprotected by absence.

## An A/B that isolates one variable is the whole experiment

To prove a pipeline stage changed the output, hold everything else constant:
**same narrative, same voice asset, same images, same captions** — only the new
stage differs. Comparing a new render against an old one that also has a
different script, a different take, or different art proves nothing, because
every variable moved at once.

Two pieces produced to validate the same subsystem are not redundant if they
differ in the dimension the subsystem is sensitive to (duration, load, emotional
register). Conversely, if the second piece is scored under a direction the first
was not, **the two scores are not comparable and must not be placed side by side
as if they were** — say explicitly which axis differs and report each against its
own declared target.

Choose the pilot's second subject from material that already exists (approved
script, generated voice, existing plan) so the run costs no metered quota. A
validation cycle that spends budget before the machinery is proven spends the
budget twice.

## Closed historical fixtures and future-package E2E

A closed historical episode is immutable evidence, not a live acceptance target. When the
Director closes an episode, freeze its production artifacts and exclude it from intake,
repair, render, delivery, and positive E2E runs. Keep only isolated synthetic fixtures for
regression; historical hashes, reports, and delivery verdicts never satisfy a new run.

A positive autonomy result requires a new Director-approved package executed through the real
public entrypoint. Until that package exists, report the system as `PARTIAL` or
`BLOCKED_PENDING_APPROVED_INPUT`; do not substitute a closed episode under another ID and do not
claim autonomous readiness from unit or integration tests. If scope changes during a task, update
the active test plan and execution policy before continuing.

A stage name in a list or schema is not proof that the stage is implemented. Exercise the actual
dispatcher/CLI path, including fresh state and provenance, and fail the acceptance test when the
stage is missing, unreachable, or silently skipped. Add a regression test that invokes the public
entrypoint rather than only checking configuration membership.


- A green compile, unit suite, or focused integration suite proves only that level of evidence. Never promote it to `E2E VERIFIED`, autonomous readiness, or delivery completion without one continuous run that produced the final artifact and executed its load-bearing gates.
- After any production or artifact change, invalidate all downstream QC and delivery reports. Recompute hashes and run the owning gates again; editing paperwork or reusing a prior verdict is not a repair. The sole exception is a report-only correction: identical artifact bytes are acceptable only with a materialized corrected report plus a second full audit of those exact bytes — any audio, caption, or video change requires new bytes, a new hash, and a new audit.
- When a legacy test contradicts the current fail-closed policy, change the test to assert escalation, immutability, or `NOT_EVALUABLE` as the policy requires. Do not weaken the gate or restore a forbidden mutation merely to make the old expectation green.
- For transactional repair, use the order `clone → fingerprint → technical mutation → revalidate → commit → trace`. On escalation, protected mutation, or failed revalidation, discard the clone and report `applied=false`; only a committed and revalidated copy may report `applied=true`.
- `recorded=0` from an idempotent trace is not automatically a failure. Distinguish `ALREADY_RECORDED` from a write error, inspect the trace, and judge the event's impact. A shared historical trace can contain valid `repaired` events; scope the assertion to the current transaction rather than requiring an entire reused file to contain no successful event.
- Keep fixture traces, production traces, and run state isolated. A fixture that reuses a shared trace can prove a false contamination failure and can mask whether the current transaction was correctly discarded.

## A gate chain that never reads the canon cannot detect a wrong character

Every stage can pass while the thing the pipeline exists to produce is wrong.
Appearance, costume, proportions and style live in a bible/lock/registry, and
structural gates do not measure them: a valid manifest, a passing continuity
check and a clean render all describe a *coherent* wrong character.

- **An external description of canon is a claim, not a source.** Read the canon file and quote what it declares before generating anything that depends on it. Search the whole tree for the described trait first — **zero matches is the evidence**, and it costs nothing. An instruction that arrives with the confidence of a spec is the usual origin of the mismatch.
- **Make it a gate, not a habit.** Compare the canon against any externally-supplied description, block on conflict, and write a report naming the sources consulted, the version used, and the conflicts found. Report a conflict; do not settle it.
- **Registry-to-canon is one-directional.** A registry that maps a *subset* of the canon is healthy. Assert "if the registry declares it, the canon defines it" — requiring both sides to declare the same field set manufactures false reds on a correct registry, and a gate that cries wolf is a gate that gets bypassed.
- **Find a lock's fingerprint where the project actually stores it.** It is often a constant in the verifying code, not a field in the JSON; reading the wrong location reports "unlocked" about a locked lock.
- **Compare names for identity, not glyphs.** An em-dash in a spec and a hyphen in an API response are one name. Normalize punctuation before asserting equality, or the gate reports typography as identity failure.
- **Prove the gate both ways**: canon-only must PASS with zero red checks, and a synthetic conflicting description must FAIL and produce the report. A gate that has only ever returned PASS is untested.
- **A resumable stage must revalidate canon provenance.** See `gated-delivery/references/production-entrypoint-hardening.md` — an invalidation check over critical-source timestamps prevents resuming a run created under superseded rules.

## A gate that declares more than it runs is worse than a broken gate

A test file that fails to parse does not report its tests as failing. It
contributes nothing, and the suite reports fewer tests than the tree contains —
while still exiting green on everything else. A file-level parse error
masquerades as a quiet reduction in coverage, so the suite gets *less* strict
exactly when it appears to be passing.

Make the runner self-checking: discover test files, count the tests actually
executed, and fail if that count is below what the tree declares. Also gate
syntax separately from test execution, because a parse error hides inside a
test run's output.

The same trap applies one level up: **a gate that crashes while printing its
own verdict reports nothing and is indistinguishable from a pass.** A validator
whose early-return path returns an empty detail dict, then reads that dict in
its reporter, dies exactly when it has a real finding — so the finding never
reaches anyone. Give every return path the same complete detail shape, and
prove the failure path prints: run the gate against an input it must reject and
assert it produced output, not a traceback.

Corollary for code inside a test file: a stray top-level block left outside any
`test()` call is a parse error for the whole file. If the runner reports a
per-file failure with a vague "test failed" and no subtests, run the file
directly (`node path/to/file.test.js`) to get the real line and message — the
suite's summary does not surface it.

A third variant: **an escape hatch that exists only in the docstring.** A gate
that documents a flag as the sanctioned way to accept the one legitimate
exception (`--rotated`, `--force`, `--known-issue`) and then never reads it in
the failing check reports a permanent red on a clean tree — the worst outcome,
because a gate that is always red is a gate everyone learns to route around.
Wire the flag into the check, keep the strict path as the default, and prove
both directions: the legitimate case fails without the flag and passes with it,
while the case the gate exists to catch (secret inside an archive, stale hash,
foreign run id) still fails with the flag ON.

So when you inherit a red gate, read the failing check's body before believing
the red. Classify it: the inspected artifact is wrong → real defect; the check is
stricter than its own documentation → gate bug, report it with file:line and the
one-line fix; a dependency is missing → report as a blocker, never as a verdict.

Assert count deltas in the changelog when a fix changes how many tests run
("371 -> 378, all executing"). A count change is evidence the gate's reach
changed; without it, a test-count regression looks like routine churn.

## When you are the one writing the gate, not just running it

Every gate added to a system is an unverified claim until it has been attacked.
The protocol, in order:

1. **Self-test runs before the gate judges anything.** Encode the cases that
   must FAIL, run them, and exit nonzero *without scanning* if the self-test
   fails. A gate that has not demonstrated it can say "no" has not earned the
   right to say "yes".
2. **A failing self-test is a finding about the LOGIC, not about the
   expectation.** When a case you expected to pass is rejected, the usual cause
   is that the rule is too narrow to describe its own domain. Widening the rule
   is usually right; loosening the case to make it green is usually wrong. Ask
   which side is wrong before editing either.
3. **Tri-state verdicts, never two.** `BLOCK / WARN / PASS`. The middle state is
   the one that matters: it is the difference between "this violates the rule"
   and "I cannot observe this" — two claims that look identical to a boolean and
   must never be collapsed. A gate that can only see a narrow window cannot
   declare absence through it.
4. **Execute every recipe, never read it.** A catalog entry, a shell command, or
   a filter chain that has never been run is an intention. Run each one in the
   real runtime before declaring it `verificado`, and keep the verified flag in
   the artifact so the next reader knows what was actually executed.
5. **A degraded path must be declared in the output.** When a requested
   behavior is unavailable (missing layer, unsupported filter, one input instead
   of two), degrading silently makes the artifact lie about what the viewer sees.
   Record `degradado_a` / a WARN in the result.
6. **Empty is not equal.** When comparing a schema enum against its registry,
   both being empty is not a match — it is a word with no content that lets a
   deleted catalog pass. Require non-empty on both sides.
7. **An inter-stage gate closes a hole no existing gate covers.** Per-stage gates
   each validate their own stage, so two stages can describe different artifacts
   and every gate passes. The gate that finds this compares the producer against
   the CONSUMER: does the derived artifact actually come from the current
   source, and does the accurate stage's output actually reach the renderer?
   Run it on the real artifacts first — a gate that is correct on synthetic
   fixtures can still be silent on the divergence it was built for.
8. **Prove it finds the known case.** Take a real, already-confirmed divergence
   and confirm the new gate blocks on it. A gate that has never rejected
   anything is indistinguishable from a gate that cannot reject.

Two standing traps when writing one:

- **A self-test whose expectations cannot match its own output.** Comparing a
  number against a prefixed label (`3` vs `"check3"`) reports every negative case
  as failing while the gate is correct. Normalize both sides, derive the count
  from the case table, and make the evaluation root injectable so negative cases
  can build fixtures.
- **Fix the source, not the gate.** When the new gate reports a stage as
  untraceable, the defect is usually a stage that RECEIVES the source as an
  argument and never records it. Patch that producer to declare it; do not widen
  the gate to accept an artifact that cannot say what it came from.

Recipe and worked example: `references/gate-authoring.md`.

## A relocatable package is only proven by running it from a copy

When a deliverable must run from any location (portable tool, hand-off bundle,
extracted archive), the source tree proves nothing about the artifact. Static
checks, the project test suite, and a dry run in the build directory all go
green on a package that cannot start one directory over.

**The only acceptance run is: build the artifact, extract it to a NEW directory
with a NEW name, and execute the real entrypoint from there.** A portability
linter is a hypothesis generator, not the verdict — the same way a contract is
not perception.

Corollary, and the most common cause of a package that passes everything and
still fails on first use elsewhere: **"no dependencies" must be true at the byte
level.** `node_modules` does not travel inside an archive, so a bare
`import pkg` is a first-run `ERR_MODULE_NOT_FOUND` in the extracted copy — and
that error reads as an installation problem, not a packaging one, so it gets
debugged in the wrong place. Audit the package for non-stdlib imports with a
grep over the shipped tree, and count the call sites before deciding whether the
dependency earns its place.

Relative paths written by hand are the second cause, and they are worse because
they work until someone runs from elsewhere. Anchor every filesystem access to a
root computed at runtime (`import.meta.url`), and route it through one accessor
so consumers and tests cannot disagree (rule 10).

Full recipe, including the linter's own failure modes: `references/relocatable-package.md`.

## Implementation closure rules

- **Wire and test the public entrypoint, not just a stage list.** Adding a name to `STAGES` is not implementation: update the real dispatcher/CLI, run the stage through that boundary, and assert its persisted handoff. Dispatch maps can capture function objects at import time, so a test that patches helpers after construction may observe stale references; verify artifacts/state or rebuild the dispatch boundary in that test.
- **Keep one canonical creative fingerprint.** The protected boundary covers Script Lock, spoken text, beat identity/order, canon, and authorized Director decisions. Split logical identity from physical binding: the fingerprint protects an anchor's logical identity (anchor/identity/name/type) but never filename, path, or bytes hash — rebinding the same logical anchor to a different file must leave the fingerprint unchanged, while swapping the logical anchor must change it. Exclude technical derivatives such as compiled prompts, motion cleanup, and bare physical-reference strings when those are execution fields. A repair that only fills physical bindings must therefore never trip the protected-mutation check. Verify raw and normalized package shapes produce the same fingerprint, then mutate a protected field and verify the fingerprint changes.
- **Make stage dependencies explicit and fail closed.** Render must not run before required audio/captions PASS; pack must not run before render, master audit, technical repair completion, and same-run sidecar hashes. Persist `run_id` and fingerprint at every handoff and test missing, stale, and foreign inputs at the real consuming gate.
- **Only the final tree earns a final count.** Earlier green runs are historical evidence after code changes. Re-run the full suite and the owning engine tests on the final tree before reporting completion; keep focused-test and full-suite results separate.

## Support file

- `references/validation-recipes.md` — concrete measurement recipes
  (audio-tail levels, frame comparison, contract cross-checks, manifests).
- `references/web-app-release-e2e.md` — real-browser release proof for web
  apps (login chain, CSP/hydration rule, dead-form diagnosis, 401-vs-429).
- `references/closed-episode-and-future-e2e.md` — classify closed history, isolated fixtures, and Director-approved future packages; execute the public chain and collect same-run evidence.
