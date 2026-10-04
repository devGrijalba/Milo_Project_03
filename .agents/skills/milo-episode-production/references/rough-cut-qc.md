# ROUGH_CUT_MULTIMODAL_QC (validate the combination, not just the parts)

Script ✓ + images ✓ + audio ✓ can still make a mediocre video — failure appears in combination. Pipeline: ASSETS → ROUGH CUT → MULTIMODAL QC → FINAL RENDER.

## 1. Rough cut first

Assemble the full timeline (images at take-scaled durations + take audio + timed subs) as a review cut before any final render decisions. Cheap to rebuild, expensive to regret.

## 2. Windowed multimodal pass (evaluator watches the whole cut)

Windows 0–1 s, 1–3 s, 3–5 s, 5–10 s, then per-beat: hunt dead zones, over-static image, narration running ahead of image, image spoiling the twist, visual repetition, slow cuts, weak payoff visibility, AV desync. Cite window + symptom + evidence frame/time.

## 3. LOCAL PATCH, never full rebuild on partial failure

A failing window gets a local fix (re-time cut, swap/regen one shot, shift a sub block, duck a silence) → re-verify that window → continue. Full regeneration only for structural failure (wrong story, broken continuity). Record every patch with cause; patches are learning data (which fixes recur = which upstream step leaks).
