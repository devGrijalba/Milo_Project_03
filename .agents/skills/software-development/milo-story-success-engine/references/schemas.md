# JSON schemas — Success Engine artifacts (per episode, `01_historia/`)

## candidate_pool.json

Array of: `{id, author_model, concept, hook_0_5s, escalation_motor, payoff, guion, words, dur_s, hook_score, early_retention_score, eligible}`. `eligible` = hook_score ≥85 AND early_retention_score ≥90 (anti-compensation: no averaging around a weak hook).

## adversarial_reviews.json

Array of: `{candidate_id, attacks: [{role, claim, cited_second, cited_element}], defenses: [{claim, cited_second, cited_element}], verdict}`. Attacks/defenses without exact-second citations are noise — excluded, never scored.

## retention_simulation.json

`{candidate_id, rows: [{window: "0-1s"|"1-3s"|"3-5s"|"5-10s"|"10-20s"|"20-30s"|"30-38s"|"final", question, verdict: "PASS"|"FAIL", evidence}] , fail_early}`. `fail_early` = true if any row ≤5 s FAILs → candidate dead regardless of later rows.

## selection.json

`{winner_id, reasons: [citable], champion_comparison: {beats_champion: bool, criteria_deltas}, hypothesis: null|{variable, prediction}, losers: [{id, cause}]}`.

## story_evidence.md

Human-readable: winner, why (cited), survival curve summary, Champion verdict, experimental hypothesis if any. Real metrics appended post-publish (see performance-learning-loop.md).
