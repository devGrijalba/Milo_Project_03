# The lock chain, field by field

Reference for `flow-bridge-operation`. Read the package's own `START.md` too;
this file is the condensed map of what each stage resolves and what blocks.

## Stage 1 — Catalog: which keys exist

Valid values are **derived from the locks**, not written in code:

- `character` = subfolders of `knowledge/characters/` (each needs `bible.json`)
- `base_space` = `world_lock.space_architecture.base_spaces[].id`
- `shot` = the union of every `framing_variants[*].camera` in the world lock
- `framing` = keys of `framing_variants` **of that base space**
- `emotion` = keys of `emotional_objects`
- `pose` = keys of the bible's `pose_library.available`
- `material`, `typography_register` likewise derived

Adding a scenario, emotion or pose must not require touching code. An unknown
key throws with the list of valid ones; it is never replaced by a default,
because a default produces a scene nobody chose.

## Stage 2 — SceneResolver: manifest → scene with provenance

Required: `character`, `base_space`, `emotion`, `message`. At least one of
`shot` / `framing`; if both, they must agree with the lock's declared camera.
Optional: `framing`, `shot`, `typography_register`, `ratio`, `notes`, `id`,
`why`, `pose`, `action_en`. Everything else is rejected.

`id` and `why` are documentary. `action_en` is the **only** field a human writes
that reaches the prompt: it carries the action in English, and the word gate
decides whether it fits. Without it, every shot in the same space generates the
same picture and the action is inherited from the reference image.

Resolution per element:

| Element | Source of truth | Blocks when |
|---|---|---|
| character refs | `bible.master.canonical_references` | absent → no character |
| per-attribute refs | `bible.attribute_sources[attr].file` + class | file missing from canon → substitution refused |
| banned refs | `bible[*].DO_NOT_USE.file` | declared source is vetoed → reported, not sent |
| materials | `world_lock.location_materials[framing].materials` ∩ `scene_lock.materials.locked` | plate has no materials, or a key is not in the lock |
| material variants | `scene_lock.materials.variants` filtered by `base` ∈ scene AND `where` ∋ framing | a variant whose `where` omits this framing must NOT appear |
| lighting | `light` (Spanish editorial) + `light_en.compact/full` | light without `light_en` blocks; the adapter does not translate |
| emotional light | `emotional_objects[emotion].lighting` | `null` is legal = keep the framing's light |
| typography | `typography_lock.registers`, chosen by rule unless the manifest declares one | — |
| pose | `bible.pose_library.available[pose].atomic_reference` | declared pose without an image = invented posture |

The emotional light **replaces** the framing light, it does not add to it: the
base light already travels in the plate image, and describing both gives the
model two descriptions of the same light.

## Stage 3 — PromptMapper: English, inside a word gate

Order of the parts: action → subject (only when the text must carry identity) →
space/framing text → light → camera → typography → render boilerplate.

- Materials are deliberately **absent** from the text: the plate image carries
  them better than a list of nouns, and the budget cannot afford it.
- Character appearance is deliberately absent: the reference carries identity;
  a hand-written three-piece suit drifts the moment the model reinterprets it.
- Candidate ladder, richest → leanest, for each combination of space/light/
  typography detail. The first candidate inside the gate wins, and every attempt
  is recorded. If none fits, it throws instead of cutting canon to hit a number.
- Typography: verbatim text, or a three-word treatment with the exact text still
  travelling in the plate image, or plate-only.

## Stage 4 — FlowJobBuilder: references, one per class

- `VISIBLE_ATTRIBUTES` per camera plane decides what travels. What the plane
  does not show (feet in a medium shot) is recorded as `not_sent` with the
  reason, so nobody reads it as an oversight.
- A pose reference travels **first** (it places the subject) and only for planes
  that show a body; in a close-up it is reported as omitted.
- Dedupe by class: two files of the same reference class add nothing and eat
  reference budget.
- The space plate goes first — it is what fixes the set. A framing with no plate
  is blocking; the prompt cannot describe the set and the package will not
  invent the image.
- The bridge receives **bare filenames**, because it resolves by name inside
  its own `insumos/`. The staging step copies from the canon folders and fails
  loudly when the origin is missing.

## Two-file-universe rule

Masters deliver silhouette/suit/body; atomic crops deliver a single attribute
with no accompanying gesture. The registry that declares each crop's source
file and crop coordinates is the reason a crop is trustworthy — a crop without a
declared master is a loose file and is not used. `build` and `footwear` are only
legible in a full-body master; eyes, face and the watch are only legible in a
close-up crop.

## Verdict criteria live outside the code

The generation script never judges the image. The approval file carries the
criteria and their evidence anchors: identity (face, eyes, wardrobe), world
(materials, lighting, city-as-background), production (9:16, free space at top
and sides for subtitles, no invented text). Identity failures are fatal even
when the rest is perfect; world deviations are recorded as lock drift and fixed
in the lock, not in the prompt.
