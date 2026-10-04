# Paid generative pilot ladder (Magnific pattern, reusable for any metered provider)

For validating a generative model/provider before production. Order isolates
variables so each paid task answers exactly one question.

## Ladder

1. Paper first: request files (prompt, refs with hashes, params, seed) with
   `allowPaidCall=false`. No spend without an explicit per-task authorization.
2. Verify the exact endpoint in the provider's official API index/spec
   (paths, params, limits) before authorizing — a web-app feature never
   proves a public endpoint exists.
3. Fixed seed across comparative runs; change ONE variable per task
   (language → prompt structure → reference cleanliness/count → model).
4. Clean references beat more references: single-function refs
   (identity / environment / style), 2-4 per call; full sheets with
   panels/text/palettes read as noise.
5. Score every output on fixed axes (identity, environment, style, light,
   composition, artifacts) with a numeric gate for model promotion.
6. Moderation/4xx terminal states: diagnose by machine-readable code,
   record it, STOP that front — never loop retries on terminal states and
   never re-spend to confirm randomness (fixed seed makes repeats identical).
7. Report per task: task_id, statuses, latencies, output hash + dims,
   cost (or UNKNOWN_NOT_EXPOSED + official table range), paid-call count.
8. Default-model decision needs a clean A/B (same scene/prompt/refs/seed,
   only model changes); cost-per-quality decides, not single-image beauty.
