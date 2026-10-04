# Fail-closed regression and closure recipe

Use this reference when a multi-stage pipeline has gates, creative/technical locks, repairs, and a final deliverable.

## Evidence ladder

Run and record each level separately:

1. **Compile/typecheck** — proves syntax and static contracts.
2. **Focused regression** — reproduces the exact bug or invariant at the smallest seam.
3. **Full unit/integration suite** — detects regressions in the subsystem.
4. **Continuous E2E** — runs intake through final gates in one run.
5. **Delivery verification** — validates the exact delivered bytes, sidecars, hashes, and gate reports.

Only level 5 supports a delivery/completion claim. A green lower level must be reported as lower-level evidence, not extrapolated upward.

## Transactional repair sequence

```text
original
  → clone
  → protected fingerprint
  → technical-only mutation
  → owning gate / revalidation
  → atomic commit
  → trace
```

On escalation, protected mutation, exception, or failed revalidation:

```text
discard clone → restore original → applied=false → transaction_committed=false
```

A trace may record an escalation, but it must not describe a discarded mutation as `repaired`. `recorded=0` can mean an idempotent duplicate; use an explicit `ALREADY_RECORDED` state and inspect the event rather than inferring success or failure from the count.

## Same-run closure manifest

For every stage record:

- `run_id`;
- source/package hash;
- protected fingerprint before and after;
- input artifact paths and hashes;
- output artifact path, bytes, and SHA-256;
- owning gate command, complete output, and exit code;
- invalidation of previous QC when any derived artifact changes.

A `DELEGATED` label, file existence, historical report, or test from another run cannot enable `MASTER_READY`, `FINAL`, or equivalent state.

## False-PASS probe matrix

Before certifying a gate, run the real production gate against disposable artifacts:

- black/corrupt frame → explicit R03 failure;
- undocumented interior silence → R01 failure even in the tail;
- stale or mismatched QC hash → repeat audit on the exact MP4;
- missing required evidence → `NOT_EVALUABLE`/blocked;
- foreign `run_id` or fingerprint → provenance block;
- complete creative package with a missing Director decision → escalation with byte-identical source;
- render failure → no delegated/pass label.

For a new render, any audio, caption, timeline, mix, or export change invalidates the previous master QC and delivery report. Re-run the full chain from the changed stage and audit the new bytes.

## Legacy-test policy

When a test expects a mutation that the current contract forbids:

1. quote the current contract rule in the test name or assertion;
2. change the test to assert the fail-closed result and source immutability;
3. run the focused test;
4. run the full suite;
5. do not alter production merely to satisfy the obsolete expectation.

## Closeout wording

Use a status such as `PARTIAL` or `BLOCKED` when the lower-level tests are green but the continuous E2E or one load-bearing gate is missing. Name the missing artifact, hash, gate, or Director decision; do not convert historical evidence into a current PASS.
