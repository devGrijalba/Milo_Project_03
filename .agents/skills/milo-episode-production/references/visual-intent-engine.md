# VISUAL_INTENT_ENGINE (la imagen sirve al segundo, no al revés)

Image QC is not limited to generated / 9:16 / character right / no deformities. Every image answers: does it help retain the viewer at THIS exact second?

## 1. VISUAL INTENT (before each image, from the beat)

`{beat, must_show, must_not_show, viewer_must_understand, retention_function: anomaly|information|emotion|change|anticipation}`. Example: reflection behaves independently → MUST SHOW Martin serious + reflection smiling → MUST NOT SHOW both smiling/serious → viewer understands the reflection stopped copying → anomaly/escalation. The generator prompt carries the intent; the vision model validates the IMAGE against the intent, never against the prompt alone (a beautiful mirror shot that misses the anomaly fails).

## 2. Ten-axis visual QA (no averaging — critical fail rules)

Technical Quality · Narrative Alignment · Character Consistency · Scene Continuity · Mobile Readability · Emotional Salience · Visual Novelty · Retention Contribution · Prompt Compliance · Artifact Detection. Each PASS/FAIL with evidence. IMAGE_QUALITY 96 with RETENTION_VALUE 42 = CRITICAL FAIL: RETENTION CONTRIBUTION → REGENERATE. Same philosophy as the script gate: one critical fail fails the shot, never an 84.8 average pass.

## 3. Four mandatory narrative checks (subset of the ten, always evaluated)

SCRIPT_ALIGNMENT (exactly the beat) · VISUAL_CLARITY (readable fast on mobile) · RETENTION_VALUE (anomaly/information/emotion/change/anticipation at that second) · CONTINUITY (characters, space, objects, causality consistent). Any FAIL → regenerate that shot only, then re-verify.

## 4. Anti-formula guard

Track visual patterns across episodes: if the generator converges on one formula and repeats it, flag VISUAL NOVELTY fail and force variation. A winning look is a hypothesis, not a template.
