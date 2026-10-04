# Character identity resolution — the full decision table

Depth behind the "framing does not select identity" rule in SKILL.md. Read this
when choosing which reference travels, when a character reference set looks
wrong, or when deciding whether to widen the policy.

## When to use

- Choosing which reference travels for a shot, especially `medium` or `wide`.
- A generated image has the right face but wrong body, invented legs or
  footwear: the identity reference was resolved by framing instead of by
  declaration.
- Adding a character, or extending an existing character's reference policy.
- Deciding whether a second reference is a conflict or a legitimate complement.

## The distinction, in one line each

- **Framing** (medium / wide / close_up / detail_shot): what the audience sees.
  Decides composition and, for the *pose* reference only, whether a
  body-shaped reference is distortive.
- **Identity**: who the character is. Decides which file is authoritative for
  every zone of the subject.

A resolver that lets framing pick identity produces a plausible image of
somebody who is not the character. It fails silently: the plan prints no error,
quota is spent, and the defect is visible only by eye.

## Resolution order

```
1. identity base      declared full-body master        ALWAYS for a lead
2. drop crops         whose contract serves a zone the master also serves
3. drop hidden zones  attributes the framing hides (never the master)
4. add master         once, as the authority for every zone
5. add complements    expression / view, only if the manifest declared them
6. add pose           only if declared, and only when framing shows a posture
7. add space plate    environment: carries no identity, never competes
8. fail closed        any surviving conflict on the same zone blocks the submit
```

Step 3 before step 4 is not stylistic. Add the master first and the generic
visibility filter will delete it — the master key is not in the framing's
visible-attribute table, so the shot ends up with zero character references and
reads as an environment plate.

## What counts as a conflict

Read each crop's served zones from the registry's `attribute_contract`. Two
references conflict when one's allowed zones intersect the other's forbidden
zones, or when both claim the same zone.

Typical pairings, and why they matter:

| Pair | Verdict | Mechanism |
|---|---|---|
| master + torso/wardrobe crop | conflict | crop claims `signature_object`, volume; master owns every zone |
| master + face crop | conflict | two authorities for facial identity |
| master + medium-portrait crop | conflict | two authorities for hair/build |
| master + expression | **complement** | different *state*, same subject; only if declared |
| master + profile/back view | **complement** | different *angle*, same subject; only if declared |
| master + space plate | **complement** | environment defines no identity |
| master + pose | **complement** | posture is not a body zone |

When a value is undeclared, treat it as unknown and fail safe: unknown zones
make the reference claim *more* authority, so it gets dropped. Never default a
master to "no zones" — that is how the master deletes itself.

## Declaring the policy as data

Keep it in a per-character lock (`identity_rules.json`) so the resolver reads
it and no filename is hardcoded:

```json
{
  "primary_identity": { "file": "...MASTER_FRONT.png", "class": "full_body" },
  "supplementary_views": { "...PROFILE_LEFT.png": "giros, lateral" },
  "expressions": { "...NEUTRAL_FACE.png": "narracion normal" },
  "forbidden_with_primary": {
    "...TORSO_WARDROBE.png": "transmite signature_object y prohibe face"
  },
  "attribute_conflict_policy": "FAIL_CLOSED"
}
```

Every entry in `forbidden_with_primary` carries its reason. A prohibition with
no reason is indistinguishable from a typo, and a typo there silently disables
the protection.

## Manifest surface

Expose the complements as **optional declared fields** (`expression`, `view`,
`shot_ref`), never inferred from the framing. Validation:

- value not in the lock → block, name the valid set
- no rules declared for that character → block; declaring an expression with no
  rule is inventing the state
- an expression that breaks canonical identity (wide eyes, open mouth) → block
  unless the manifest carries an explicit exception field

An unknown manifest key is blocking, like any other: a typo'd field that is
ignored produces a poorer scene than was asked for.

## Tests that earn their name

Cover, at minimum:

- a medium shot resolves the master and nothing else identity-bearing
- a walking/turned shot resolves master + the declared view
- master + a forbidden crop → blocked, and the message names the file
- no identity source → blocked
- an expression alone cannot satisfy identity
- every prohibition in the lock declares a reason

**Negative cases matter more than positive ones here**, because the default
failure is silent. Also assert the fixture actually loaded — a test keyed on the
wrong field name in the registry goes green while checking an empty set.

## Shot references: a bounded layer, not a new authority class

A shot reference answers *how the camera frames the subject*, never *who the
subject is*. Declare it as a framing key (`shot_framing_medium`) whose forbidden
set is `scene` / `environment` / `pose`, and always travel it **with** the
master — alone it loses proportions and wardrobe, so it is useless and
misleading.

Build it by cropping the master deterministically with a script, never by asking
the model to crop on the way out: a crop requested in the prompt makes it resolve
a contradiction between its own reference and your words, unreproducibly.

**A crop cannot remove a pose that lives in the master.** If the source shows
hands in pockets, every crop of it does too — the trait is in the source, not
introduced by framing. Before promising a crop will fix a posture, use vision to
establish whether the pose is *inherited* or *introduced*, and check whether the
whole source pack shares it. A pack whose every view carries the same posture has
no open pose to derive from, and the fix is a canon decision or a new source,
not another crop.

Keep the layer bounded on purpose. It exists because the master is a complete
composition and the model obeys it over the prompt. Once the framing, the acting
and the scene are all driven from the prompt, the layer should be deleted rather
than extended — prove it earns its slot with the A/B/C variant comparison in
SKILL.md before adding a second one.

## Recording what was dropped

Every dropped crop goes into the plan's not-sent list with the zone it served
and which authority replaced it. This is the difference between "the system
decided" and "we lost that information and nobody said so" — and it is what lets
a later audit tell a deliberate composition decision from a regression.