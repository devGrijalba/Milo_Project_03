# LEARNING_QUALITY_GATE (no auto-promote observations to knowledge)

Hermes never stores a conclusion as knowledge automatically. Full chain, every time:

OBSERVATION → HYPOTHESIS → EVIDENCE → ALTERNATIVE EXPLANATIONS → CONFIDENCE → REPLICATION → VALIDATED LEARNING

Example: a video with more images retains better → store OBSERVATION (R012, higher visual-change frequency, better early retention) + HYPOTHESIS (may improve retention) at CONFIDENCE: LOW + mandatory ALTERNATIVE EXPLANATIONS (stronger hook, better concept, shorter narration, better first frame, distribution variance). Replication moves LOW → MEDIUM → HIGH. Only HIGH becomes a rule.

## Per-variable attribution (anti-contamination)

Never learn "R008 good → everything in R008 good" or "R009 flopped → everything bad". Attribute separately: script, hook, concept, images, first frame, voice, music, SFX, pacing, editing, duration, payoff, publishing, distribution. A win with a weak hook teaches nothing about hooks.

## Memory / knowledge separation (paths under `00_PROJECT_ADMIN/memory/`)

`/raw/` (metrics.json, observations.json) · `/experiments/` (hypotheses.json, results.json) · `/learning/` (provisional_patterns.json) · `/knowledge/` (validated_patterns.json, validated_failures.json). The Master consumes ONLY validated patterns; experiments may consume provisional ones. Nothing observed enters MILO's rules without passing this gate.
