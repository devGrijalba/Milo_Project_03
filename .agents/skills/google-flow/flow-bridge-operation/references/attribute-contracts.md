# Attribute contracts: verifying a crop before registering it

The rule behind this file: **a filename declares an intention, only vision says
what the file contains.** A crop whose name and contents disagree fails
silently — the plan prints no error, quota is spent, and the output is a
plausible blend of two identities.

## The verification recipe

For each crop, ask the question the crop's `forbidden_attributes` implies, and
nothing else. One vision call per attribute in conflict, on a proxy small enough
to answer fast.

| Crop purpose | Ask | Register when |
|---|---|---|
| `identity_reference` (face) | "Any clothing or shoulders at the edges?" | answer is no |
| `identity_reference` (face) | "Is the mouth visible? Is the iris a distinct color, or a solid white?" | both are yes — the traits you need must be legible |
| `clothing_reference` | "Is any face, eye, mouth or head visible?" | answer is no, with no exception |
| `pose_reference` | "Does the head appear at all?" | answer is no |
| `volume_reference` | "Does the crop reach the waist, or does it cut at the chest?" | it reaches the waist |

A face crop that is clean but **lacks the trait it exists for** is a failure too:
that is how a neutral-expression master becomes a bad identity reference when the
character only shows its mouth during strong expression. If the trait is missing
everywhere in the canon, that is a **canon decision**, not a crop fix.

## Choosing the source master

Do not pick a master by its name or intention ("neutral", "identity", "master").
Verify what the expression actually contains:

- A **neutral** expression often hides small traits (a thin mouth, a half-lidded
  iris) that a **strong** expression shows clearly. For an identity reference,
  the master that makes the traits legible wins, even if the expression is not
  the one you would pick by taste.
- A master carrying a dramatic expression is a poor *identity* reference but the
  right source for a *pose* crop.

## Choosing the crop box

Measure per file, from the master itself, with vision on a light proxy:

1. Ask for the boundary as a **percentage from the left/top edge**, not pixels —
   absolute values from a scaled proxy do not transfer.
2. Convert to pixels **of the original master** and crop.
3. **Verify the new crop with vision** and confirm it contains what you needed.

Step 3 is not optional. A crop box computed from a plausible-sounding number
lands on the wrong region often enough that skipping verification guarantees a
wasted asset. In the real case a crop computed from another master's waist
measurement cut at the chest and was caught only by verifying the result.

## Weight

Crop file size is not a quality signal. The same content as PNG can be 15× the
size of the JPEG, and the generation model rescales the reference anyway. Optimize
for legibility, not for kilobytes — an over-compressed crop loses exactly the
fine detail the crop exists to deliver.

## Recording the result

```json
{
  "id": "..._TORSO_WARDROBE",
  "from": "..._MASTER_FRONT.png",
  "crop": "w=573:h=454:x=225:y=314",
  "attribute_contract": {
    "purpose": "clothing_reference",
    "allowed_attributes": ["wardrobe", "signature_object", "body_shape"],
    "forbidden_attributes": ["face", "eyes", "mouth", "expression"]
  },
  "verified": { "contiene_cara": "NO", "arrastra_ropa": false },
  "why_it_was_rebuilt": "Covered 11%–75% of the master: a near-full body with the complete face inside. It competed with the identity reference and the model blended both."
}
```

Keep `verified` measured and `purpose` declared. A validator that confirms
`purpose` using `purpose` checks nothing.

## `verified` must be complete enough to validate

A `forbidden_attribute` with no corresponding measurement in `verified` cannot be
checked at all, and the gap shows up as a failure the first time a gate runs. When
you add a forbidden attribute, add the field that measures it in the same edit.
Auditing the registry against the gate — rather than against the contract alone —
is what surfaces these.

## Superseding a reference without losing the evidence

When a better reference replaces an older one, keep the old file and mark it
rather than deleting it. A superseded reference is historical evidence for a real
diagnosis, and deleting it means the next session re-derives the same conclusion
from scratch. Mark it as not-for-generation in the index so it can never be sent,
and say which file replaced it and why. Two fields to keep straight:

- `status`: superseded / active
- `send_to_flow`: false / true

They are separate because one is provenance and the other is permission, and
collapsing them makes a vetoed file look merely old.

## Proving separation works across more than one scene

One passing scene does not prove attribute separation works — it proves it worked
there. Once a subject's identity is stable in a single setting, run one test that
changes **only** the environment plate and holds prompt, negative, model, pose,
reference order and attribute content fixed. That answers a different question:
does identity survive when the environment reference changes?

The value is in what stays constant. If identity holds in a second setting, the
per-attribute reference scheme generalizes, and that is worth more than another
good image in the first setting. Do not spend a further test re-checking identity
in the setting that already passed; it cannot add information.

Also record the **cost** of each run honestly. If generation times vary widely
with no controlled explanation, report the numbers as data and explicitly decline
to attribute a cause. An unexplained measurement is fine; an invented cause is
not.

