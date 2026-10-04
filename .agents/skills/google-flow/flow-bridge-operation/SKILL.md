---
name: flow-bridge-operation
description: "Use when generating Flow images via extension + bridge."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [flow, bridge, extension, manifest, locks, images]
    related_skills: [flow-image-generation, flow-batch-generation, flow-cdp-operation]
---

# Flow via extension + bridge (no CDP)

The class of task: turn a **shot manifest** into Flow images, where the prompt,
the references and every visual fact come from JSON locks, and the browser work
is delegated to the **Flow I2I Assistant extension** through a local WebSocket
bridge. No DOM injection, no Playwright, no CDP.

Use this instead of the CDP skills whenever the deliverable is "manifest/locks →
image" and a portable package exists. The CDP route is the fallback for projects
that have no such package.

## When to use

Any task of the shape "a manifest / prompt package + reference images → images
generated in Flow, via the extension and the local bridge":

- generating a shot, a beat, or a batch from a portable package or an in-project
  prompt package;
- diagnosing a generation that produced files but closed in an unexpected way
  (`file_watch` instead of `job_done`, a stale result file, an unexplained
  `state: N`);
- deciding whether a reference **provably** reached the generation
  (binding evidence) rather than whether the image merely looks right.

Not for the CDP route (no extension) — see `flow-cdp-operation`.

## Read the package's START.md FIRST — completely

Portable Flow packages ship a `START.md` that is the **route index**, and its
route changes between versions (this one went "generate by CDP" → "generate by
extension" during development; following the stale version cost two full work
phases). Read it before integrating anything, and re-read it if the file
changed. `README.md` is reference only. When a doc and the code disagree, the
**code** wins: read it and fix the doc.

Layout that matters: `tools/` (commands), `src/flow/` (manifest→scene→prompt→job),
`src/characters/` (attribute→source hierarchy), `src/integrations/` (bridge client
+ quota guard), `src/validators/`, `knowledge/` (all the locks), `02 IMAGENES ANCLA/`
(masters), `02 REFERENCIAS ATOMIZADAS/` (atomic crops), `insumos/` (what the
bridge reads), `salidas/`, `out/`, `.state/runs.jsonl`.

## Three commands, in this order

```bash
cd "<package folder>"
npm run verify     # portability proof: no absolute paths, no hand-written relative paths
npm run status     # free: bridge up? extension connected? cooldown? folders exist?
npm run shot       # free dry run: resolves the manifest to the full job, writes out/plan.json
npm run generate   # COSTS QUOTA. One attempt, never auto-retries
python scripts/bridge.py   # the bridge daemon itself; prints the endpoint it bound to
python scripts/bping.py    # ping + status against a running bridge
node tools/pre-generation-gate.js   # FREE barrier: canon intact, contracts hold, plate generable
```

`status` before everything: it is free and it predicts whether the generation
will be wasted. `shot` before every new shot: it is the only safe way to iterate
on prompt/references without the extension open. The gate before any authorized
run: it is the check that stops a doomed generation before it costs anything.

## Hard rules (from the package, non-negotiable)

- **Model: only `Nano Banana 2`** — the string must match the Flow menu exactly.
- **Quality: only 1K (`preview`)**. Flow offers 2K/4K for images; **1080p does
  not exist for images** (it is a video-only label). A config asking for 1080p
  image quality is wrong.
- **One generation at a time.** The bridge has a serial queue; parallel submits
  are the fastest way to get flagged.
- **Confirm with the user before spending quota.** Every generation costs.
- **On "actividad inusual": STOP TOTAL**, set a 60–120 min cooldown, never retry
  in a loop. A retry after that signal is exactly what the guard forbids.
- The bridge is the truth for termination: **a new, stable file in the downloads
  folder** is the real end of a job, not the `job_done` message. Missing
  `job_done` is normal; 18 min with no file and no notice is the real timeout.
  Every status field can agree and still be a zero-delivery run: `flow status:
  completed`, `resolver: terminal=completed` and `ok: true` are the extension
  reporting its own loop finished, not that a file exists. When `files` is
  empty, the job failed at delivery whatever the status says. Compare the
  download's **mtime against the job's own timestamp** before citing it — a
  file whose name matches the prompt slug is often left over from an earlier
  run and reads as this run's evidence. Two close-metadata fields that are
  mutually exclusive (`note: fin por archivo` together with `finished_by:
  job_done`) mean the close path is nondeterministic; treat the pair as
  contradictory evidence, not as a fact. One cause is a stale process: if that
  pair contradicts the current source, the bridge that wrote it predates the edit.
- **`completed != SUCCESS`, and the terminal verdict must be derived from the
  artifact list, not asserted beside it.** When the resolver builds a success
  envelope unconditionally, `ok: true` with `files: []` is the default output of a
  zero-delivery run and every consumer reads it as a win. Derive the verdict from
  the harvested files: an empty list means the close is a delivery failure, whatever
  the extension's own status message said. Fix it where the envelope is built, not
  in the consumers that read it — a consumer patched to distrust `ok` is a third copy
  of the same rule and the first to drift. Ship a delivery-evidence record alongside
  it (`job_id`, `started_at`, `finished_at`, `file_path`, `file_mtime`,
  `file_hash`) so the verdict cites a re-checkable file instead of an unverifiable
  status. This is the failure a restart does **not** fix: it survives every reload and
  only closes when the envelope is derived from the artifacts.
- **Correlate the log by `groupId`, never by reading it top to bottom.** The
  bridge prints every extension message as `EXT <groupId>: <message>`, and two
  independent execution paths interleave in that one stream: the Hermes job
  channels (`job_<epoch_ms>`, `hermes_<epoch_ms>`, one per submission) and the
  extension's own autonomous automation loop, which logs everything under the
  constant group `live`. Sequential reading makes the `live` channel's selector
  warnings look like the submitted job's fault, because the job's messages sit
  between them in the file. Count messages per `groupId` before attributing any
  warning to a job — a run can show a dozen `configureImage` failures and zero
  on the job's own channel, which inverts the conclusion.
- **Check whether the running process predates the source edit before diagnosing
  a bug from its own output.** A daemon loads its code once at start; Python does
  not hot-reload. Edit a source file while its bridge is still running and every
  artifact that process produces afterwards still exhibits the OLD behaviour —
  so the artifact looks like proof your fix failed. Compare the process start time
  against the file's mtime (`Get-Process -Id <pid> | Select StartTime` against
  `ls -la --time-style=full-iso <file>`). When a produced artifact contains a
  state the current code **cannot emit** — a field combination no reachable code
  path builds — that is a stale-process signal, not a mystery. It reclassifies the
  finding from "live bug" to "already fixed, needs restart", which changes what
  the next action is: a restart, not a patch.
- **Audit a delivered fix pack against the code before implementing any of it.**
  A pack written from an artifact describes that artifact's symptoms, not the
  current source, and by the time it arrives the code may already have changed. For
  each proposed item, open the function in the source and check whether the fix is
  already there. Then report which proposed gates are already satisfied — two of
  four were, and re-implementing them would have produced a duplicate gate: a
  second source of truth that drifts from the first and is trusted because it is
  newer.
- **Never derive a hash or a verdict in a second language.** A hash recomputed
  in Node cannot match one produced by Python's `json.dumps(sort_keys=True)`:
  separators, non-ASCII escaping and float formatting all differ, so the check
  can only ever fail. Pick one owner per hash and let the consumer ask it.
  The same applies to field access — a `KeyError` usually means the field
  moved to a different nested block, and a silent `None` on a status field
  usually means you parsed an older output shape.
- **Report generation, delivery, resolution and binding separately.**
  `generation: SUCCESS|FAILED`, `delivery: SUCCESS|FAILED`,
  `resolution: job_done|file_watch|timeout|error`, `binding: <state> + reason`.
  One `state: N` code collapses these and makes "Flow produced nothing"
  indistinguishable from "identity cannot be proven".
- **When an event handler fires per state change, guard on terminal state
  before any read or delete.** A resolver invoked on `queued` as well as
  `completed` destroys its correlation mapping on the first event, then reports
  "no mapping" for the real close. Translate first, clean up second: cleaning
  first makes a lost send unrecoverable.
- **Binding evidence must be observed at the transport boundary.** Self-asserted
  evidence is not evidence. Full layer model, the interception requirement, the
  producer/consumer contract traps and the `PARTIAL`-as-honest-ceiling rule:
  `references/binding-evidence.md`.
- **Dedupe downloads by content hash, not by name.** The extension sometimes
  writes the same image twice under two filenames (the prompt slug and a suffixed
  variant). Group the harvested files by SHA-256, keep the **oldest** of each
  group, and move the rest to a quarantine subfolder — do not delete them.
  Deleting a file the user never saw is an irreversible loss, and disk space is
  not the problem being solved. Note it was non-repeating across several runs, so
  it is not systematic; it still has to be handled before any batch, because in
  batch the duplicates become operational noise. Test the dedupe function against
  the real accumulated download folder before trusting it.

## The lock chain (why the package is not "just a prompt builder")

```
manifest → Catalog (valid keys, blocks unknowns) → SceneResolver (resolves locks,
never invents) → PromptMapper (English, inside a word gate) → FlowJobBuilder
(references by attribute class + space plate) → FlowBridgeClient.generateImage()
```

- **Manifest contract**: `character`, `base_space`, `emotion`, `message` required;
  at least one of `shot` | `framing`, and if both are present they must agree.
  An **unknown key is blocking** — a typo'd field that is ignored produces a
  poorer scene than was asked for, and that is invisible in the image.
- **Every resolved value carries provenance** (file + path). A value without
  provenance is an invention and must not exist.
- **No defaults in the adapter**: a missing material, light or typography entry
  blocks the shot. Fix the lock, not the prompt.
- **Word gate**: `character_focused` = 20–30 words, `environment_focused` =
  40–50. The mapper walks a candidate ladder (richer → leaner) and the first
  candidate inside the gate wins; if none fit it throws rather than dropping
  canon. The prompt stays in English because the locks carry the English
  projection; the adapter never translates.

  **Where to cut when the gate overflows.** A `PromptBuildError` is a lock defect,
  not a prompt defect. Before editing anything, count the words per contribution
  (space + light + render + action): the shortest candidate's overage tells you
  which projection is bloated. The cut belongs in the **`compact`** projection of
  the light (or space) entry for that specific framing — never in the `full`
  projection, which is what `environment_focused` reads and which must keep its
  richer text. `compact` means **one idea, 3–6 words**; an entry carrying two
  clauses is what broke the contract in the first place. Real case: one space's
  `light_en.compact` held 12 words where its sibling held 4, pushing a 30-word
  gate to 35. Trimming it restored the shot with no change to canon, no change to
  the plate, and no change to reference order.
- **Image carries identity, text carries event**: Flow is image-to-image. A
  prompt that repeats what the reference already shows competes with the
  reference and burns the word budget.

## The reference principle (the reason the package is shaped this way)

> **A reference transmits everything visible in it.**

So there are two file universes:

| | Masters (`02 IMAGENES ANCLA/`) | Atomic crops (`02 REFERENCIAS ATOMIZADAS/`) |
|---|---|---|
| Delivers | silhouette, suit, full body | **one** attribute, with no accompanying gesture |
| Irreplaceable for | build, footwear | eyes, face, watch/cufflink |

An attribute points at a file by **class**, not by "the most detailed one", and
every crop declares its source file and crop coordinates in a registry — a crop
without a declared master is a loose file and is not used. Because the prompt
budget leaves no room to describe a posture, the only way to stop a
hand-adjusting-cuff gesture from leaking into every shot is to crop it out of
the image. See `references/manifest-and-locks.md` for the full chain and
`references/troubleshooting.md` for the symptom table.

## Framing does not select identity — one zone, one authority

The two rules that decide which reference travels, and they are separate on
purpose:

> **The framing decides what is shown. The reference decides who the
> character is.**

Selecting identity by output framing is the expensive default: a `medium` shot
does not show feet, so a framing-driven resolver drops `build`/`footwear` and
resolves those attributes from partial crops. The model then completes legs,
footwear and proportions by probability. Visibility is not identity.

For a recurring lead character, resolve identity **from the full-body master**,
declared in the lock — never from a crop. Then:

| Zone | Authority |
|---|---|
| identity base | the declared full-body master, always |
| expression | a declared expression reference, if the manifest asks for one |
| alternate view | a declared profile/back view, if the manifest asks |
| environment | the space plate — carries no identity, so it never competes |

**A zone has exactly one authority.** When the master enters, every crop whose
contract declares a zone the master also transmits is dropped with a recorded
reason — a torso crop that serves `signature_object` is a second authority for
that zone, and the model blends the two. Read each crop's served zones from the
registry's declared contract, not from its filename, and treat a value the
registry does not declare as *unknown* (fail safe) rather than *all zones*.

Three failure shapes this rule prevents, all observed:

- **Retiring the master along with the crops.** If the master is added before
  the visibility filter runs, it is born "not visible" and disappears — a shot
  with zero character references that looks like an environment plate. Order it:
  drop competing crops → drop frame-hidden zones → add the master.
- **Filtering declared complements by framing.** A new attribute key
  (`expression`, `view`) is absent from the framing's visible-attribute table, so
  a generic "drop attributes not visible" loop silently discards what the
  director explicitly asked for. Exempt declared complements from that filter.
- **Reporting a verdict from a stale file.** See the routing pitfall below.
- **Deduplicating declared complements by reference class.** A "one image per
  class" rule is right for body zones — two files of the same class carry the
  same information — and wrong for declared complements: a shot reference and an
  expression are both `medium_portrait` and transmit different things. Dedupe
  only the zone-carrying references and send complements in their own list, or
  the layer you just built silently vanishes from the job.

Declare the policy as data (`identity_rules.json` per character: primary
identity, supplements, expressions, forbidden-with-primary, conflict policy) so
the resolver reads it instead of hardcoding a filename, and make a surviving
conflict **fail closed** with the offending file named — a policy with no
verification is a declaration, not a control. Full decision table, the
conflict/complement matrix, manifest validation rules and the test list:
`references/identity-resolution.md`.

## A master transmits composition, not just identity

Resolving identity from the full-body master fixes the body-invention problem and
creates a second one: the master **is** a complete composition, and the model
obeys the reference over the prompt. Asking for a medium shot and sending the
master returns a full-body, centred, catalogue-pose subject — the prompt's
framing loses to the reference's. Not hallucination: obedience.

So identity and cinematography need separate systems:

| Layer | Answers | Source |
|---|---|---|
| identity | who the character is | the full-body master |
| **shot reference** | how the camera frames them | a crop derived from the master |
| expression | what emotional state | a declared expression reference |
| environment | where they are | the space plate |

A **shot reference** is a crop of the master that bounds framing without
replacing identity. It travels *with* the master, never instead of it: alone it
loses proportions and wardrobe. Declare it in the lock under `shot_references`
with a contract whose `allowed_attributes` is a framing key
(`shot_framing_medium`) and whose forbidden set is `scene`/`environment`/`pose`
— it answers "how", never "who".

Do not ask the model to crop. A crop requested in the prompt makes it resolve a
contradiction between its own reference and your words, unreproducibly. Crop
deterministically with a script, register the crop with its source and
coordinates, and verify it with vision.

**A crop cannot remove a pose that lives in the master.** If the master shows
hands in pockets, every crop of it does too — the trait is in the source, not
introduced by framing. Fixing that needs a pose reference (posture is not a body
zone, so it coexists with the master), or a canon decision. Verify with vision
whether a pose is *inherited* or *introduced* before promising a crop will
remove it.

## Lighting resolves in layers, never by concatenation

A space plate and an emotion both declare lighting, and they can contradict each
other. Observed: an emotion's `lighting` was `warm side light, soft shadows,
amber tones` while its own `avoid` listed `cold blue light` — and the plate it
was combined with emitted `cold blue window light`. The emotion was asking for
exactly what the space produces.

Substitution by priority ("emotional replaces environment") hides the conflict
and hands the model two opposite instructions. Resolve it in layers instead:

| Layer | Authority | Meaning |
|---|---|---|
| `environment` | the space plate — always preserved | where the light comes from |
| `subject_modifier` | the emotion — only when it does not contradict | how it falls on the character |

Detect the contradiction by testing each `avoid` entry against the plate's
lighting tokens. On conflict: keep the environment, drop the subject modifier,
and **declare the conflict in the resolved scene** with both sources and the
reason — never silently drop either one. The emotion's own `lighting` and
`avoid` stay untouched in the lock; only its application to this shot changes.

Two consequences worth stating: a warm-palette emotion conflicts by definition
with every cold-lit plate, so an emotion that never conflicts with the space
set is itself a signal; and the subject-modifier marker must be cheap. Marking it
with a phrase (`soft X on subject`) added three words and pushed shots that
previously fit over the gate — use one word.

## Deduplicate a light layer that repeats what the space already says

Resolving by layers fixes contradictions, not duplication. The remaining cause
of a gate that will not fit is often two systems describing the *same*
property: the environment already declares warm light, and the emotion's
modifier adds warm light again. Sending both is two instructions for one zone
plus words the director spent.

Generalise the rule that already governs identity and framing — **one visual
zone, one authority** — to lighting:

1. Classify the environment's light and the emotion's modifier into declared
   families: warm, cool, dark, direct, diffuse. Declare the tokens; do not
   approximate with string similarity.
2. If **every** family the modifier carries is already present in the
   environment, drop the modifier. Partial overlap is not redundancy — a warm
   modifier over a warm-and-cool space still adds penumbra the space never
   declared, and travels.
3. Record the removal in the resolved scene: `decision`, `reason`, both family
   sets, the repeated families, and an explicit note that the emotion is still
   expressed through acting, pose, composition and rhythm. A modifier that
   vanishes silently reads as a dropped emotion and gets re-added next session.
4. Leave the emotion's lock fields untouched — only its application to this
   shot changes.

Detect this before reaching for a bigger word gate. A gate raised to make a
duplicate fit converts a design defect into a permanent budget increase.
Conflicting and redundant light are different failures with the same symptom; a
layered resolver needs both paths, and the word budget is fixed render tail
(~11 words) plus your variable contributions, so count per contribution before
deciding which one to cut.

## Every crop declares an attribute contract, and you verify it

> **`asset_name` != `asset_truth`.** A filename declares an intention; only vision
> says what the file contains. Register a crop by what you **measured** it
> holds, never by what its name promises.

A crop whose name and contents disagree is the most expensive defect in this
pipeline, because it fails silently: the plan prints no error, the quota is
spent, and the output is a plausible mix of two characters. Real case: a crop
named `..._TORSO_WARDROBE` covered 11%–75% of its master — a near-full body
**with the complete face inside**. It competed with the face reference and the
model blended both. Three generations were spent isolating it.

So every crop carries, in the registry:

```json
"attribute_contract": {
  "purpose": "clothing_reference",
  "allowed_attributes": ["wardrobe", "signature_object", "body_shape"],
  "forbidden_attributes": ["face", "eyes", "mouth", "expression"],
  "rule": "ZERO faces. Not one, not partial, not a sliver of head at the top edge."
},
"verified": { "contiene_cara": "NO", "arrastra_ropa": false }
```

`verified` is the **measured** truth; `purpose` is only the claim. A validation
gate compares the two and treats a present `forbidden_attribute` as **blocking,
not a warning** — it is the direct cause of a contaminated generation. Keep the
two fields separate: a gate that reads `purpose` to confirm `purpose` validates
nothing, which is exactly the error it was built to catch.

### Every attribute verdict is tri-state, and the three states are not equal

A `forbidden_attribute` resolves to PASS / VIOLATED / **UNMEASURED**, and
collapsing UNMEASURED into either neighbour breaks the gate in opposite ways:

- **A missing `verified` block is blocking.** There is nothing to compare against,
  so approving by default means the gate is decorating, not validating.
- **A single forbidden attribute left unmeasured inside an otherwise-measured
  `verified` block is a warning, not a violation.** Refusing to certify an
  unmeasured trait *is* refusing to invent a verdict. Common case: a face
  reference forbidding `pose` cannot have "no pose" — absence of a pose is not a
  measurable fact about a face crop.
- **Only a measured-and-present attribute blocks.**

Getting this backwards produces a gate that fails on every input, and **a gate
that always fails is a gate people learn to skip** — strictly worse than no gate.
The first implementation of this rule rejected all five references as violations
purely because nothing had been measured; the fix was to count and report
unmeasured traits explicitly instead of failing on them.

### The gate must be able to stop a generation, not describe one

A validator nobody runs is documentation. Wire it in as a **barrier that runs
before the bridge call** and exits non-zero to abort, in both dry-run and
authorized modes.

- **Spawn the gate as a separate process** rather than importing it. An import
  that throws looks identical to a gate that passed, and the generation proceeds
  on a check that never ran.
- **Test the barrier by making it block.** Point the manifest at a deliberately
  invalid target (a known-vetoed plate), run the *authorized* path, and confirm
  three things: the failure message names the real reason, the process exits
  non-zero, and the download count is **unchanged**. Unchanged downloads is the
  only proof that quota was not spent.
- **Exit 0 with no output is the worst possible gate failure** — it reads as
  success. When adding a CLI entry point, verify it actually prints. In ESM, gate
  the CLI on `pathToFileURL(process.argv[1]).href === import.meta.url`; comparing
  raw strings fails on Windows because `import.meta.url` upper-cases the drive
  letter, and the script then exits silently having done nothing.

Full gate design and the refactor pitfall: `references/pre-generation-gate.md`.
Editing locks without losing canon, auditing `compact` projections, and
resolving lighting by layers: `references/lock-editing-discipline.md`.

**Crop coordinates belong to the file, not the concept.** Never carry a
measured offset from one master to another: waist at 47% in one anchor is 69–79%
in another, and reusing it produces a crop that cuts where it should not. Measure
per file, then verify the new crop actually contains what the concept needs.

Verify a new crop with vision before registering it, checking the *forbidden*
attributes first — those are the ones that silently break identity. See
`references/attribute-contracts.md` for the per-attribute verification recipe,
and `references/pre-generation-gate.md` for the barrier that enforces it all
before quota is spent.
## Before spending quota on a diagnostic run: read what the logs already prove

A request to "run one instrumented execution and observe" is a quota request
hiding inside a diagnostic request. When the failure being investigated is
already on disk, reconstruct it from the log first and only run when the
existing evidence cannot distinguish the candidate explanations.

The decisive question is always: **can the evidence separate the candidate
causes?** For "did the UI actually get configured, or did the selector fail to
find an element that was already correct?", the discriminator is a reading of
the **effective** UI state (which value is selected), not a log line saying
`Element not found`. If no run ever captured the effective state before and
after, then no re-run without that capture answers anything — it reproduces the
same ambiguity and spends quota to do it.

Sequence that avoids the waste:

1. **Reconstruct from the existing log first.** Count messages per `groupId`,
   isolate the job's own channel, and read the baseline rate of the same code
   path across earlier runs. A path that succeeds on most runs tells you the
   fault is a window, not a systemic defect — and costs nothing to learn.
2. **Separate the question from the incident.** Report what the evidence
   supports even when it is not the answer you were asked for. A reported
   success with an empty file list is a real delivery failure and outranks the
   question you were sent to investigate; say so rather than only reporting the
   selector warnings.
3. **If a re-run is still needed, state up front what would make it
   informative** — which capture discriminates which cause. If the answer is
   "none", do not run; say what instrumentation is missing instead.
4. **Conclude `INCONCLUSIVE` rather than picking a plausible cause** when the
   discriminating observation does not exist. Naming an unproven cause sends
   the next session to patch the wrong layer, which is worse than an open
   question.

The rule this replaces: a diagnostic that reports a specific failure reads as
decisive, so it gets acted on. Reserve a specific verdict for evidence that
distinguishes it from its neighbours.

## Diagnosing a bad generation: freeze, then bisect

A wrong output is not a prompt problem until proven otherwise. Before touching
the prompt:

1. **Freeze the experiment.** Write down prompt, negative, model, ratio, scene,
   pose, emotion and the exact reference order. Change exactly one thing next
   time, and record the hash of every reference file you send.
2. **Classify the failure** into identity / environment / obedience / render, and
   name which specific traits failed. "The image is wrong" is not a finding.
3. **Check the references before the prompt.** If a trait came out wrong, ask what
   the reference for that trait actually contained. A trait that is absent from
   the reference cannot be preserved by the model, and no prompt wording fixes it.
4. **Look for a second carrier of the same trait.** Two references that both show
   a face, or both show a pose, compete; the model blends them and the result is
   neither. This is the highest-yield check and the most commonly skipped.
5. **One variable per generation.** A test that changes two things cannot attribute
   the result, and you will re-run it.

The prompt is the last place to look, not the first. In the real case the prompt
was never wrong: three crops lied about their contents, and fixing the assets
fixed all three failing traits at once.

## Pitfalls that cost real time

- **A live bridge on :8765 may belong to a DIFFERENT copy of the package.** The
  bridge resolves reference images by name inside **its own** `insumos/`, so a
  bridge started from project A silently cannot see project B's references and
  fails with "imagen no encontrada" (or, worse, picks up A's files). Before
  generating, confirm which folder owns the listening process (PID → start time
  → the working copy whose `insumos/` is populated) and make the package you
  are generating from the one that owns the bridge.
- **The port is configuration, not identity. Verify the protocol, not the port.**
  Two projects sharing one machine will each want a bridge; 8765 is not
  "the Flow bridge port", it is whoever got there first. A foreign bridge on the
  expected port will happily answer a `{action:'status'}` probe with an `ok:true`
  shape close enough to pass a naive readiness check, and the failure then
  surfaces mid-generation as a confusing selector error. Three rules that make
  this deterministic rather than lucky:
  1. **Make the port resolvable, never a literal.** One resolver owns the
     endpoint (process env > `.env` > project config > a default that is NOT
     the popular port). Bridge, client, transport and health check all read it,
     so they cannot drift apart.
  2. **Advertise identity in every status.** The bridge returns
     `project`/`protocol`/`protocol_version`/`bridge_endpoint`, and the client's
     guard compares protocol, project AND the endpoint it was actually called at.
     Keep the older `worker_count==1` guard too and add the identity check
     **after** it — additive, so the original rejection reason still wins
     (`BRIDGE_NOT_READY`) and the new one is distinguishable
     (`BRIDGE_ENDPOINT_MISMATCH`) rather than collapsing into one opaque error.
  3. **Compare endpoints semantically.** `localhost:8766` and `127.0.0.1:8766`
     are the same endpoint; a string compare rejects the first and accepts a
     bridge on a different port. Split host/port, treat the loopback trio as
     equivalent, and require an exact port match.
  The extension cannot read `.env` (MV3 has no filesystem), so do **not** try to
  configure it from a file: let the bridge declare its endpoint in the handshake
  and have the extension adopt and persist that. The bootstrap port is only a
  first guess, and a worker adopting the endpoint of the bridge it actually
  connected to cannot desynchronize from it.
- **Probe the real listener, but with ONE connection — a poll loop can cause the
  fault you are diagnosing.** A bridge that registers workers per socket counts
  every client, so a diagnostic wrapped in `for …; do probe; sleep; done` adds a
  worker per iteration. Once the sockets pile up the status flips to
  `worker_count: 2` / `worker_conflict: true` and the bridge starts rejecting
  real work with `WORKER_CONFLICT_OR_MISSING` — a fault manufactured by the
  instrumentation, not present in the system. Read `worker_count` **once**,
  compare with the `ESTABLISHED` socket count for that port (`netstat -ano |
  grep 127.0.0.1:<port> | grep -c ESTABLISHED`), and if the two disagree the
  surplus is yours. Symmetrically: when the user reports "it worked before you
  started touching it", suspect your own probe before the user's build — and
  say so plainly instead of debugging their extension.
- **`worker_count: 2` is not `worker: false`.** Two different faults with two
  different owners. `worker: false` / `worker_count: 0` means the extension side
  panel is closed — the **user's** action; ask them to open or reload it inside
  a Flow project with the Google session active, and do not try to automate the
  extension from outside. `worker_count > 1` is a conflict, and the usual cause
  is a second client (your probe, a stale daemon, a duplicate extension copy)
  rather than anything the user did.
- **Grep the storage keys the extension actually reads before telling the user
  to clear one.** A key introduced by your own patch cannot pre-exist in
  `chrome.storage.local`, so "delete the stale persisted endpoint" is a silent
  no-op when the endpoint was previously a hardcoded literal in the source —
  and a no-op that appears to fix it manufactures false confidence. Enumerate
  the real keys (`grep -oh "storage.local.get(['\"][^'\"]*" *.js`) and confirm
  the value before recommending a removal. Deleting only a config key is safe;
  wiping storage wholesale destroys the job, sent-image and outbox maps.
- **The generation commands read the FIRST shot only** (`shots[0]`). To produce
  a different shot, replace that entry — do not assume an index flag exists.
- **A missing reference is blocking, by design.** If a reference is not in
  `insumos/`, the pipeline refuses to substitute a similar image: a close
  reference causes silent drift. Fix the lock or add the declared crop.
- **Attributes fall back to a declared class when the declared source does not
  satisfy it**, and the plan prints a warning. Read the warnings in `shot`: a
  "class required vs reserve used" line means a pose/medium image is now
  carrying hair or wardrobe, and that is a decision, not a detail.
- **The bridge's own timeout errors and TCP-probe tracebacks are noise.** Judge
  health with `bping.py`, not with a stray `EOFError` in a log.
- **The scripts never judge the image.** The verdict criteria live in the
  package's approval JSON (identity, eyes, wardrobe, materials, lighting,
  aspect, subtitle space, no invented text). Look at the file and apply them
  yourself; the script only reports that a file arrived.
- **Never re-derive a validator's logic when you make it importable — move it.**
  Rewriting the checks while extracting them into an exported function
  reintroduced field names that did not match the real data, producing veredict
  sets that were all wrong while still looking like the original output. Extract
  the existing body verbatim and leave the CLI as a presentation layer. Two
  copies of a check diverge, and a gate that has silently desynced from the
  validator it replaced is more dangerous than no gate, because it is trusted.
- **A consistency bug in a table you just wrote is real, not cosmetic.** After
  writing per-row classification flags, re-read the emitted file and check each
  row against its own status field. A row whose `generation_safe` disagreed with
  its `asset_status` would have shipped a vetoed plate as generable. Catch it by
  re-reading, not by trusting the write.
- **Test ids against the lock, not from memory.** An invented framing id produced
  a gate failure whose message ("no plate in the lock") was indistinguishable from
  a real lock gap. Enumerate the actual ids in the lock before using one in a
  test, so a test failure always means what its message claims.
- **A test that reads the wrong field name passes while checking nothing.** A
  contract test keyed on `item.file` in a registry whose key is `id`/`output`
  saw no data, so every assertion "passed" on an empty set. When a test goes
  green immediately after being written, suspect that it read nothing: assert
  that the fixture actually contained the expected rows before trusting the
  pass.
- **A CLI wrapper that takes a flag its inner script ignores is a silent
  misroute.** If the wrapper passes `--manifest` down and the script hardcodes
  one, every run generates the wrong image, burns quota, and reports success.
  When adding a routing flag, resolve it in BOTH layers and prove it end to end:
  the plan file must be named for the requested shot, and the wrapper must read
  back *that* file. A response reporting the previous job's prompt is the tell —
  a verdict read from a stale file is not a verdict.
- **Compare requested against resolved just before the submit, and block on
  mismatch.** Write a run record (requested manifest, resolved manifest, shot id,
  prompt hash) *before* the submit. Quota is spent at the submit, so any check
  after it is a post-mortem.
- **Do not hunt the system for the automation when the package documents it.**
  Grepping browser profile folders for the extension wastes the turn and finds
  the wrong add-on — several unrelated Flow extensions may be installed, and the
  log strings come from none of them. The route index and the extension's own
  doc folder in the package name the extension, the bridge contract and the
  known-good state. Read those first, then the system.
- **Never bulk-edit a lock with `json.load` → `json.dump`.** Round-tripping a
  lock rewrites the whole file: it collapses nested arrays onto one line and can
  silently drop entries from arrays that were multi-line, so canon you were not
  editing disappears from `full` descriptions. `git diff` after the write catches
  it (`-` lines that are not the fields you meant to touch). Revert and redo the
  edit as a targeted patch on the exact field. If a script must write the file,
  diff the parsed structures field by field against a backup afterwards and
  report the change count — a formatting rewrite looks like dozens of content
  changes and buries a real one.
- **A full-field read is not a snapshot: `patch` warns and the next write can be
  refused as stale.** Paging a large lock leaves later writes operating on a
  partial view. For a big JSON file, parse it once and edit through a script or
  a patch anchored on a field you have actually read, rather than chaining
  patches across a file you only saw in slices.
- **A `cd` into a system directory persists and silently breaks every relative
  path afterwards.** A diagnostic command that changes the working directory
  leaves the shell there, so the next command's relative paths resolve against
  the wrong root and report "no such file" for files that exist. When a path you
  just used stops resolving, print the cwd before debugging the project —
  `pwd` is the answer more often than the file is missing.
- **Verify a crop's declared purpose with vision before registering it, and
  re-verify after adjusting the box.** A first crop that ran past the waist was
  accepted on measurement and rejected on inspection; the correction needed a
  second crop and a second look. Measure, crop, verify, adjust, verify again —
  and record the rejected intermediate in the audit so the next editor knows
  which boxes were already tried.
- **Compressing `compact` can invert the space's light.** A plate whose
  `composition` says the blue light dominates and whose single warm lamp is
  *distant* cannot be compressed to the warm source alone: the compact then
  contradicts the composition it belongs to. Before cutting a plate's
  `light_en.compact`, read its `composition` — if the space has two light
  sources with different roles, both belong in compact even when that puts it
  over the word budget of a `simple` plate. The ceiling follows *declared*
  lighting complexity: `simple` = one source, `compound` = ambient plus
  differently-roled accent with its `lighting_sources` listed. Audit for
  inversion explicitly: a plate whose composition declares a dominant colour
  must have that colour in compact.
- **Distinguish "the bridge died" from "the extension's page changed".** Read
  `job_logs` from the bridge status: a phase message naming a UI element it
  could not find means Flow re-rendered that screen and the user has to reload
  the tab — retrying the same submit spends quota on the same failure. A bridge
  with no worker is different: the side panel is closed, also user-side.

## Pin `model` when you pin `provider` — `auto` is not a model

Setting `provider` alone looks complete and is not. With `model: null` the
client sends `model=auto`, and a provider that accepts human-facing interactive
chats may reject `auto` outright for programmatic calls:
`HTTP 400: Upstream request failed: Model is unavailable.` The chat works
because the interactive session already had a concrete model resolved; a worker
that inherits nothing gets the literal string `auto`.

So `provider` and `model` are **one** decision. Pin both, and pin `model` to a
concrete id you have seen return a real answer on that provider — read the
provider's own model list rather than guessing (`provider_models_cache.json`
maps provider → live model ids).

**A connectivity probe must exercise the real worker path, not a hand-written
CLI call.** A one-line "reply with this JSON" query passes against a provider
that cannot serve the actual workload: it never touches the tool loop, the
session scaffolding or the file write the worker contract requires. Probe by
invoking the adapter itself with a minimal payload and checking that
`response.json` appeared and `execution.json` shows `returncode: 0` — the audit
stores stdout hashes only, so this never prints a credential. A green probe that
did not take that path proves nothing about the 20 adapters.

## Reference authority: one function per reference

A reference image transmits **everything visible in it**, so a second reference
covering the same zone is a second authority competing with the first. The model
averages them and the Director loses. Measured on DARK project, 2026-10-01:

| layer | who controls it | evidence |
|---|---|---|
| identity | the master reference | exp-a + exp-c |
| expression | the prompt (`action_en`) | exp-a + exp-c |
| pose | the prompt | exp-a + exp-c |
| scene | prompt + environment plate | exp-a + exp-c |
| **framing** | **nobody** | exp-c |

**So "fewer references" is the wrong lesson.** The rule is: remove a reference
when it *competes* for the same authority with a stronger one. Removing an
uncompetitive-but-useless reference is an unmeasured case — do not write it as a
rule from the competitive data.

### A crop derived from its own source does not gain authority

The obvious fix for "the master dominates the composition" is a framing crop
derived from that master. **Measured: it fails.** Sending master + its own crop
left the framing unchanged (still full body, shoes visible). A crop loses
against its own source.

So there is no reference-layer fix for framing. The candidates are architectural
and must be evaluated as such: a *generated* framing master, a local compositor
(crop/scale in post), or planning the shot before generating.

**Before generating, check for a framing reference already marked retired.**
Retired assets stay on disk with their reason; deleting them invites retrying the
same failed approach.

## Prompt budget: count before you build, not after

`character_focused` has a hard 20–30 word gate. The fixed render tail alone costs
~11. That leaves ~19 for action + space + light + camera. When a shot overflows,
count words per contribution *before* editing anything:

- A too-long `action_en` is the Director's, and shortening it is a directed
  choice, not a workaround.
- A bloated `light_en.compact` / `prompt_en.compact` is a **lock defect**.
  Cut it in `compact`, never in `full` — `full` is the canon.

`PromptBuildError` says which, and the shortest candidate's overage tells you
where. Two more traps in the same budget:

- **Compound lighting gets its own declared limit.** A plate whose `composition`
  says "the blue light dominates, the only warm one is far away" cannot be
  compressed to one idea without *inverting* the space. Declare
  `lighting_complexity: "compound"` with `max_words: 8` **and** list
  `lighting_sources` — an exception without declared sources is freedom, not a
  rule. A compact that contradicts its own `composition` is a regression, and
  the audit below catches it.
- **Layered lighting must be resolved, not concatenated.** Environment light and
  the emotional modifier can contradict each other (the emotion's `avoid` may name
  exactly the light the plate emits). Resolve to one string with three possible
  outcomes — `removed_conflict`, `removed_redundant`, `fused` — and always report
  which one and why. Fusing is **not** about saving words; it is about producing
  one authority. And when an emotion declares no light, the environment's is used
  (absence of a modifier is not absence of lighting).

## Preflight: never spend quota on an unverified bridge

A `--go` launched before the bridge finished connecting returned
`GATE_BLOCKED` in 0.5 s. No quota (the guard stops *before* sending), but the run
was lost and it looked like a real motor failure. The block was correct; the
sequence was wrong.

Run the 5 checks first — bridge ping, worker connected, bridge free, manifest
resolves (dry run), prompt hash confirmed — then submit. A gate block with
preflight green is a **real** motor failure worth investigating; a gate block
without preflight is **our** sequencing error.

## Completion: the artifact is the authority, not the message

The package already says the real end of a job is a new stable file in the
downloads folder, not the `job_done` message. Two rules follow:

- If the process runs in the background with completion notification, **do not
  poll in parallel.** Duplicate mechanisms waste turns and can report "still
  working" for a job that already finished.
- Verify the artifact on disk before analysing it. The process message is a
  signal, not proof.

## Lock editing: patch fields, never reserialize

Twice, a script that read a lock, changed one field, and wrote the whole file
back destroyed unrelated canon — it dropped array entries from a `full` block
and reformatted every description. The functional tests still passed; only a
structural diff against git caught it.

**WORLD LOCK PATCH POLICY:** edit world locks with surgical single-field patches,
then diff structurally against `HEAD` and allow changes only to the fields you
meant to touch. A full parse-and-reserialize is not a lock edit.

`git diff` output is not proof of content change — reformatting shows as
removed lines. Compare the parsed structure field by field.

Anchors double as the environment plate for a framing, so each one carries an
audited classification. Audit the plate set as a batch, and record per plate:

```json
"environment_risk": { "text": false, "logos": false,
                      "real_people": false, "human_like_elements": true }
```

- `text` / `logos` / `real_people` — presence of burned-in words, marks, or actual
  people. Any of these is disqualifying for generation.
- `human_like_elements` — the **intermediate** category: figures with human faces
  that are not subjects (theatrical masks, framed silhouettes, a classical bust).
  It is neither a human being nor automatic contamination. **It does not block;
  it obliges you to declare it.** A plate degrades to inspiration **only** on
  evidence of burned text or a complete human face inside the character's primary
  zone. Masks flanking a free central seat are a declared risk, not a veto.

Write the reason as prose next to the flag. "Not degraded: the central seat is
empty and the masks are lateral" is what stops the next session from "fixing" a
decision that was deliberate.

**Auditing a plate for burned text — two traps, both hit in one session:**

- **Do not crop-and-rescale to read small text.** Text that reads perfectly at
  ~900px on the full frame was invisible in three separate crops of the supposedly
  correct region. Cropping preserves pixels but rescaling destroys small glyphs.
  Read small text from the full image at high resolution.
- **Locate the region before asking the question.** Asking "is there text?" over a
  frame where the subject sits low returned "no legible text" twice, and a third
  crop-based reading disagreed with both. Get coordinates from a moderate
  full-frame read, convert to absolute, then ask the specific question. A
  mis-aimed crop produces a false negative that reads as a clean bill of health.

Where a plate is unusable, keep it as `environment_inspiration` with its reason
and its still-valid values (lighting, atmosphere, architecture). Degrading is not
deleting; the atmosphere is often still worth citing.

## Adding a new shot / a new character

Before adding any new reference asset, prove it is needed. A derived shot
reference solves one real problem — the master transmitting its own framing — and
then risks solving a problem the model does not have.

**Decide between a new asset and more prompt by controlled comparison, not by
argument.** Build N manifests that differ in exactly one respect and resolve them
all as dry runs first, then spend quota on them together:

| variant | identity | expression | shot ref | prompt carries |
|---|---|---|---|---|
| A | master | — | — | pose, acting, scene |
| B | master | declared | — | pose, acting, scene |
| C | master | declared | declared | pose, acting, scene |

Read the resolved reference lists and confirm each variant differs only by the
layers you are testing, then compare the images against one rubric (identity
match, natural posture, scene fidelity, target expression, no catalogue pose).
If A already resolves pose and framing correctly from the prompt, the shot
reference is a workaround for a non-problem and costs a reference slot forever.

Two budget rules for that comparison:

- **Hold the prompt constant across variants.** If each variant gets its own
  `action_en`, you are measuring two changes at once and the result attributes
  nothing. If the shared prompt does not fit the gate, shorten it once, for all
  variants, before comparing.
- **Check the gate before running the comparison.** Variants that differ only in
  references fail the word gate identically, so the comparison cannot happen at
  all. Resolve every variant to a plan first.

A recurring pose that the prompt cannot reproduce three times in a row is the
evidence that earns a pose reference — not one shot that came out stiff.

When the evidence supports a new asset, add it only if it satisfies the standing
criterion: it carries reusable identity information, not a one-scene direction.
State it, mood, glance and seat are prompt territory; a walk cycle or an
analytical posture that recurs across many shots is canon territory.

1. Write the manifest entry (character, base_space, emotion, message, shot or
   framing, plus `action_en` when the action must reach the prompt).
2. `npm run shot` and read the trace + prompt + reference list + warnings.
3. A new character needs a `knowledge/characters/<id>/` folder with `bible.json`;
   the catalog derives valid ids from the directory listing, so a character
   outside it blocks with an unknown-key error. Its `attribute_sources` must
   point at files that exist in the canon folders.
4. A framing with no space plate blocks generation. That is the package telling
   you the lock does not cover the combination — declare the plate, do not
   improvise one.
