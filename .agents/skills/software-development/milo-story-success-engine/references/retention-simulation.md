# Retention simulation procedure (Audience Simulator role)

For each eligible candidate, walk the survival curve and answer every row with PASS/FAIL + evidence (exact second + on-screen/narration element). Rules:

- 0–1 s: need a PERCEPTIBLE reason to stop scrolling (visual or verbal). Static Milo + setup voice = FAIL.
- 1–3 s: the viewer must grasp SOMETHING is happening without full explanation. Pure exposition = FAIL.
- 3–5 s: an open question must exist that demands resolution. No question = FAIL.
- 5–10 s: situation changed or escalated vs 0–5 s. Same state = FAIL.
- 10–20 s: at least one micro-reward delivered AND a new unknown opened.
- 20–30 s: story still advancing (no filler beats).
- 30–38 s: active anticipation of the payoff, not passive waiting.
- final: payoff justifies prior seconds (citable, rewatchable or quotable).

FAIL EARLY = FAIL STORY: any FAIL at or before 5 s kills the candidate even with a perfect later curve. Output `retention_simulation.json` per schemas.md. The Simulator never sees authorship (blind). Borderline rows resolve against the candidate (a doubtful PASS is a FAIL) — production slots are scarce, doubts are data.
