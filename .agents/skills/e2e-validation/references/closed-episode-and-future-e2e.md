# Closed episodes and future-package acceptance

## Classify before execution

Classify every input as one of:

- `CLOSED_HISTORY`: Director-closed episode. Keep artifacts immutable; do not intake, repair,
  render, audit as an active episode, or deliver it.
- `FIXTURE`: isolated synthetic input used for negative or contract tests. It proves a rule or
  adapter behavior, never autonomous production.
- `FUTURE_APPROVED`: new package explicitly approved by the Director. Only this class can
  produce the positive autonomy E2E.

A closed episode may be cited as historical evidence, but its hashes and verdicts do not satisfy
a later run. Never rename it or copy it under a new ID to turn it into positive evidence.

## Future package sequence

1. Run the read-only doctor and reject any closed ID before reading or extracting production
   inputs.
2. Validate the source package before extraction. Reject unsafe paths, symlinks, case collisions,
   missing required locks, incomplete narrative fields, and unknown references.
3. Create a fresh `run_id`, source-byte SHA-256, and one canonical protected fingerprint. The same
   fingerprint algorithm must work for the raw Director package and any normalized adapter output.
4. Execute the real public entrypoint. Test the dispatcher/CLI, not only helper functions: a stage
   in `STAGES` is not implemented until it can run and hand off its artifact.
5. Verify Flow assets from physical bytes, with beat IDs and order preserved. Mark generated
   assets explicitly so a filtered generator does not silently skip them.
6. Measure and lock audio from the exact approved text; record selected take, bytes, duration,
   hash, and QA. Build captions from that same text and selected timing; text changes escalate.
7. Render a real MP4, calculate its SHA-256, and audit those exact bytes. A changed MP4 invalidates
   prior QC and delivery evidence.
8. If an authorized technical repair changes the render, persist the new artifact, calculate its
   new hash, and run the complete applicable master audit again. Do not change only the report hash.
9. Run delivery on the same run, fingerprint, MP4 hash, sidecars, and evidence. Emit at most
   `READY_FOR_DIRECTOR_REVIEW` without the Director's explicit final verdict.

## Version drift and director-owned bytes

When a package arrives in a newer format than the intake parser supports, run the existing gate first and return its exact refusal list — never hand-edit the Director's bytes to force a PASS. A syntax error in the delivered JSON goes back to the Director with position and snippet; guessing the intended field is invention, and a truncated disk copy is re-checked against the chat-delivered content before judging validity. If the new format is the standing standard, add an explicit versioned adapter (field mapping plus its own red-green tests and dispatcher coverage) behind Director approval; do not silently widen the existing parser's accepted shapes, and preserve the refused original byte-identical for audit.

## Minimum acceptance evidence

Record commands, exit codes, paths, hashes, run ID, fingerprint, stage handoffs, and evidence class
for every claim. A positive closeout requires:

```text
FUTURE_APPROVED input → one continuous run → MP4 → master PASS → delivery PASS → sealed package
```

Synthetic fixtures can prove the negative cases (black/corrupt MP4, invalid silence, stale hash,
foreign run, missing sidecar, missing physical reference), but cannot substitute for that future
package.

## Common false completion

- A historical `PASS` report is treated as a current run.
- A new function exists but is absent from the public dispatcher.
- A generated beat has no explicit generation marker and is skipped by the executor.
- A repaired master reuses the old QC hash.
- A structural gate passes while audio, captions, or perceptual evidence is missing.
