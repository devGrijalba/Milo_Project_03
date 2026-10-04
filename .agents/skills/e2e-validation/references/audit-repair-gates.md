# Audit and repair gate reference

Use this when a review package contains a relocated or reduced source tree and the task is to decide whether a defect belongs to the original implementation or to the package.

## Provenance classification

| Class | Meaning | Required evidence |
|---|---|---|
| `ORIGINAL_CODE` | The original repository has the defect. | Read the original file and reproduce from the original entrypoint/gate. |
| `PACKAGING_PATH` | The snapshot moved, omitted, or renamed a file. | Compare source path, archive path, and runtime resolution; reproduce the resolver failure. |
| `ENVIRONMENT_EXTERNAL` | Browser, provider, credentials, model, or installed dependency is outside the artifact. | Name the missing external evidence; never infer PASS or FAIL from the snapshot. |
| `HISTORICAL` | A prior report/log is being cited. | Preserve it as history and run a fresh check before claiming current behavior. |

## Minimal false-PASS probe

For a critical gate, create a disposable temporary project and invoke the real production gate. Vary one input at a time:

1. valid artifact → establish baseline;
2. black/corrupt frame or prohibited silence → expect explicit issue and nonzero/stop state;
3. missing master or stale QC hash → expect `RENDER_QC_PENDING`/FAIL;
4. altered run ID or protected-lock fingerprint → expect provenance/lock failure;
5. missing evidence for a declared rule → expect `NOT_EVALUABLE` or blocked, never PASS.

Record `INPUT → COMMAND → STDOUT/STDERR → EXIT → ARTIFACT HASH`. A unit test of a helper does not replace this gate-level probe.

## Chain closure checklist

- One run/publication ID is present in intake, plan, flow state, render evidence, QC, and delivery.
- Script Lock, spoken text, beats, canon, and Director decisions have a before/after fingerprint.
- Repair runs on a clone; escalation discards all mutations.
- Render is not `DELEGATED` evidence. Require the exact MP4, ffprobe measurements, QC hash, and delivery result.
- Historical reports and fresh observations are labeled separately.

## Report wording

Use: “The clean ZIP reproduces a path-resolution failure; the original-code claim is blocked until the same command is run from the original project.”
Do not use: “The system is broken” when only the relocated snapshot is demonstrably broken.
