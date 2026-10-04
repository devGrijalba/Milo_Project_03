---
name: milo-voice-casting
description: "Use when casting ElevenLabs voices for MILO characters."
version: 1.0.0
author: Hermes Agent
license: MIT
---

# MILO Voice Casting (proven: Conversation EP001 30s)

## The locked default

**Read the project's voice profile before assuming any voice.** The canon voice
lives in the project, not in this skill, and it changes by director decision. On
the current MILO_DARK_AUTOPILOT tree it is **Erick — Cinematic Storyteller**,
approved as `MILO CANON VOICE v1`, with the identifier resolved from
`ELEVENLABS_VOICE_ID` in the project `.env`.

**`k8cFOyAg7B9qwBlDDNTC` ("Miguel G") is DISABLED and must not be used.** It
synthesizes fine in Spanish and is still in the account — it was disabled on
performance, not on language or timbre, and the project records the previous
take as its worst-rated. A voice that still returns 200 is not a voice that is
still approved: availability and approval are different facts, and treating
availability as approval is how a recast silently reverts.

Three states to distinguish, because they read identically from the API:

- **approved** — a director chose it; it is the character's signature.
- **frozen** — chosen AND sealed: nobody changes voice, model or settings until
  a stated number of real episodes exists. Stronger than approved, not weaker.
- **required** — a variable is expected but the casting is undecided.

Accept `frozen` everywhere you accept `approved`, and make every code path that
refuses an unapproved voice also accept frozen — otherwise the seal breaks the
build the moment it is applied.

Ship neither without reading the profile. A `voice_id` written from memory fails
the call, or worse, generates with a voice nobody approved and nothing surfaces
it until the master. Verify the identifier against `GET /v1/voices` (read-only,
0 quota) and confirm the returned name matches the approved name before writing
it anywhere.

## The voice identifier belongs in the environment, never in a plan file

A plan artifact that carries `voice_id` in plaintext is a copy of a credential:
it ships with the plan, lands in reports, and enters archives. Secret scanners
correctly flag it, and the failure surfaces late — after the plan is written.

Resolve the voice from the environment **at execution time** in the TTS entry
point, and fail closed when it is absent rather than falling back to a value
embedded in the artifact. When an existing plan carries a literal identifier,
the environment wins and the mismatch is warned — this is what stops a plan
authored against a since-disabled voice from quietly producing with it.

Print only a masked form (prefix + length). A voice id is semi-public, but
nothing in a log needs it whole.

## Calibrating voice parameters: the fixture must exercise the property

**Do not tune a voice on text shorter than the metric can resolve.** Words per
minute computed over a 20-word phrase swings wildly on total duration and will
send you chasing a parameter that is not the problem. WPM and pauses-per-30s are
only meaningful over production-length text carrying the project's direction
layer (breaths, pause points, sentence shaping). A bare sentence produces a
delivered-sounding read with almost no perceptible pause — and **no parameter
sweep repairs that**, because the missing input is the direction layer, not the
settings.

The diagnostic that separates the two causes: if every candidate misses the
pause criterion by the same large margin, suspect the fixture, not the settings.

When the acceptance range for a property belongs to the **channel** rather than
the voice, hold the range fixed and adjust the text. Retuning the range to clear
a calibration sample makes the metric unfalsifiable.

**If every candidate fails the acceptance criteria, the honest verdict is NOT
APPROVED — not "the least-bad one".** Report the measured spread, name which
candidate is best on the one property that IS measurable, state plainly which
criteria you cannot evaluate (perceived emotion, whether it reads as the
character), deliver the samples for a human call, and leave the parameters
marked uncalibrated. Choosing among failures converts a measurement into a
fabricated pass.

A parameter name from a spec is not proof the API accepts it. ElevenLabs takes
`style`; a request carrying `style_exaggeration` is ignored **in silence**, and
the run looks like it tested something it never did. Check the field name in the
engine that actually issues the request before spending a sample.

The same discipline applies to a parameter you cannot spell correctly: before
spending a sample on a new setting, confirm the field name against the code path
that builds the request, not against the order's prose. A mistyped key is
ignored silently and the sample reads as a verdict on the wrong variable.

## A preflight that predicts must predict from measurements

A pre-generation gate is worth building only if its predictions come from
observed data. A gate that hardcodes an assumed pace constant and prints
`READY TO GENERATE` is worse than no gate: it manufactures false confidence, and
the false pass is discovered only after the money is spent.

Keep the measurements as a first-class artifact (e.g. an observed-rhythm
registry) and have the predictor average the comparable observations for the
same voice + model + settings. Mark every prediction as a prediction, print the
pace used and its provenance, and derive an explicit confidence: `ALTA` when a
measurement backs it, `BAJA` when it fell back to a constant. When no
measurement exists for the settings under test, **say so in the gate output**
rather than quietly using the fallback.

Exclude contaminated takes from the registry (`comparable: false`) and say why in
the record — a take whose input contained markup is not evidence about the
voice. After the registry exists, a run at production settings should be able to
**block with zero quota** on a predicted out-of-range result; that is the payoff.

Corollary: when several clean takes all miss the same metric, the cause is the
**input**, not the parameters. Sweeping `stability` across a wide range moved
WPM by ~3 (noise) while shortening the script moved it by ~50. Exhaust the text
and the direction layer before blaming a voice, and re-measure the axis you
propose to change before spending a sample on it.

Corollary for ordering investigations: **isolate variables before changing the
voice.** A voice swap discards the isolation — once you recast, you can no longer
tell whether the problem was the voice, the model, or the writing. Re-run the
historical configuration through the current pipeline first; if that reproduces
the old good number, the writer changed, not the voice. Only recast once the
writing has been ruled out, and say which experiment settled it.

### Reproduce the historical condition before buying a sample

When one historical run worked and the current one does not, the cheapest
decisive test is to reconstruct that run's measurable property and see whether
the failure follows. Do it offline, at zero quota:

- take the metrics of the good take (clause length, pause count, words/second)
- rebuild the current text to match those numbers exactly
- predict the outcome from the registry

If the prediction holds while the reconstructed structure is in place, the
structure is not the lever and you saved the sample. Measured: a rewrite
reproducing the old clause density (13,6 vs 13,2 words/clause) still predicted
165,7 WPM, disproving the clause-length hypothesis for the price of a text
edit. Only after that failure does a model or voice swap become the variable
worth spending on.

Corollary: when the measured cadence makes the acceptance range
**arithmetically unreachable** — the range needs 0,43-0,57 s/word and the voice
delivers 0,362 — that is a finding to report, not a defect to grind on. Two
ranges that do not overlap cannot both be satisfied by writing, so state the
incompatibility and let the director choose the axis to move.

### WPM measures silence, not articulation — and silence is already inside seconds-per-word

The instinct on a fast read is to measure speech rate. Measure the split first,
because it redirects the whole investigation: across five clean takes of the
same voice, speaking time held nearly flat (17.1–20.8 s) while total duration
moved 25.2–36.5 s. What changed was **silence**: 7.8 s (30%) to 15.7 s (43%),
with long-clause text producing twice the number of gaps and gaps of 1.76 s
against 1.28 s. So WPM moved without the voice articulating differently.

```bash
ffmpeg -i take.mp3 -af silencedetect=noise=-45dB:d=0.12 -f null - 2>&1 \
  | grep -o 'silence_duration: [0-9.]*'
```

`silencedetect` prints `silence_start` and `silence_end`/`silence_duration` on
**separate lines** — a single-line regex silently returns zero gaps and you
conclude there is no silence. Parse `silence_duration:` only.

The corollary that saves a wasted debugging cycle: **seconds-per-word measured
end-to-end already contains the silence**, because it is `duration ÷ words`. Do
not add silence on top of a pace figure, and do not "correct" a predictor by
adding a silence term it already includes — measured 71 words at 25,68 s is
0,362 s/palabra *including* 7,81 s of silence, and adding them again predicted
33,5 s. When two modules disagree about the same text, diff their formulas
before trusting either; the arithmetic on real takes decides which is right.

Corollary for counting pauses: a channel asking for "5–9 pauses" means pauses
of **intention**, not every physical gap. Three classes exist — boundary
between blocks and marked dramatic pauses count; breathing inside a long clause
does not. Counting all three inflated a 7-pause script to 11 and failed it
against a 5–9 target. Report both numbers (`silencios_utiles` and
`silencios_fisicos`) so the distinction stays auditable.

### Adding words is not a cadence lever — check the ratio before proposing it

The tempting fix for a too-fast read is to lengthen the script. Verify it is not
a no-op before you offer it. WPM is a **ratio**, so with a constant per-word
cadence it is invariant under padding: measured 71 words → 165,3 WPM and 121
words → 165,3 WPM, with the longer text landing at 43,9 s (outside the duration
window). More words buys more seconds, never a slower rate — and it can push
you out of range on the other axis.

The only lever that moves the ratio is **seconds per word**, and phrase
structure is what sets it: long clauses with concrete detail measured 0,499
s/palabra against 0,355 for short ones on the same voice and settings. So the
actionable statement is a *cadence target with its factor* — "go from 0,363 to
~0,490 s/palabra, factor 0,74, by writing longer clauses" — not "add words". Have
the predictor print the factor; a lever without a number is a guess.

Corollary for the gate: a predictor's remedy list is a claim like any other.
Verify the lever arithmetically before shipping it, and when a proposed remedy
is a no-op, say so in the output rather than leaving it as advice.

A calibration variant that intentionally departs from approved parameters must
be **declared in the name of the canon it writes** (e.g. a canon id containing
`CALIBRATION`), and the gate that enforces production parameters must exempt
only that named case while saying out loud that it is not the production canon.
That is a declared exemption with a trail, not a bypass.

## Length is a first-class output constraint

A short-form reel has a hard duration window (typically 15-25s). An off-vo script
written for cadence overshoots it every time, because explicit `[pause]` tags plus
a full CTA are expensive: measured takes landed at 28.7s, then 25.8s, before
trimming the text to 21.9s.

- Measure `ffprobe duration` on the first take and iterate on the TEXT, not the
  audio. Re-generating the same text with different settings does not converge.
- Remove whole clauses rather than speeding up delivery: a rushed intimate voice
  loses the tone the piece depends on.
- Count silence separately (`silencedetect -40dB`) — long gaps are usually the
  `[pause]` tags, not the words, and they are the cheapest thing to cut.
- Keep a `v001/v002/v00N` version per attempt; never overwrite, and record the
  measured duration of each so the next session starts from the last known length.
- Sanity-check characters before spending: ~0.35-0.6s per word in Spanish, plus
  the pause budget, predicts the take well enough to catch an overshoot.

## Pipeline

```text
GET /v1/shared-voices (filtered) → shortlist by metadata → Spanish TTS previews → PRIMARY/BACKUP/ALT → emotional range gate → VOICE_BIBLE_LOCK.json → full-dialogue production
```

## Search

Filter `language=es + gender + age` (e.g. male/young for Milo, female/middle_aged for mother), `page_size=100`. Compact to name, voice_id, accent, age, descriptive, use_case, es-verified. Require 5+ candidates per role. Prefer latin/mexican/colombian accents for neutral-LatAm; reject broadcaster/upbeat/advertisement profiles for intimate roles (they read as announcers).

## Key scoping pitfall

A 401 on `GET /v1/user` does NOT mean a dead key — that endpoint needs account scope. Validate the key against the endpoint you actually need (`/v1/models`, `/v1/shared-voices`, TTS). Never discard a working key over the wrong probe.

## Verify quirk

`GET /v1/voices/{shared_id}` can 400 on valid shared voices. TTS synthesis is the real verification — a voice that renders clean Spanish audio is usable regardless of the lookup result.

## Previews

Generate with the character's OWN lines (`eleven_multilingual_v2`, stability ~0.45, similarity ~0.75), never generic sample text. Deliver previews + bible as the casting gate; production starts only after approval.

## Emotional range gate (mandatory before series lock)

A 5-second preview cannot lock a series voice. Each PRIMARY must render 3 distinct states (e.g. defense → explanation → vulnerability) holding one identity without sounding acted. Lock only on 3/3 PASS.

## Production rule

Range proven means direction by conversational context and punctuation, NOT one emotion tag per line — per-line acting tags produce audible character-switching. Keep takes contained; the range is already in the voice.

## Narration format: tags are NOT text

`eleven_v3` does **not** read `[tags]` as direction. On the TTS endpoint it
reads them **aloud, literally**, as words — measured, not inferred: a 71-word
take sent with 7 tags came back with `[curious]`, `Hay`, `un` in the alignment,
and sync blew out to 957 ms against a 50 ms tolerance. Check
`GET /openapi.json` → `POST /v1/text-to-speech/{voice_id}` before assuming a
syntax works: the body accepts `text`, `model_id`, `language_code`,
`voice_settings`, `seed`, `previous_text`/`next_text`, and **no audio-tag
field**. An `expressive_mode` parameter exists in the spec but belongs to the
conversational schema, not TTS — do not send it blind to "see if it helps".

Consequence: performance direction travels as **metadata beside the text** (a
plan field such as `voice_direction: {emotion, intensity, tone, pace, tag}`),
and what you POST is `text` with no brackets. Keep a generator that returns both
artifacts, plus a guard that fails closed when a bracket reaches the request
body. A tag in the text is not a style choice; it is audible contamination, and
the alignment is where you catch it.

Direction that DOES reach the model without brackets: **ellipses** for a
dramatic beat. Measured on the same voice, same script, only ellipses added:
pauses-per-30s dropped 11.6 → 8.3 into range, and the delivery audibly stopped
sounding read. Not every beat deserves a pause — classify them (`dramatica` /
`respiratoria` / `continuidad`) and mark only the first, or the pauses become
artificial.

Use `/with-timestamps` when captions must be aligned: it returns
`{audio_base64, alignment}` with `character_start_times_seconds` and
`character_end_times_seconds` (seconds, no `_ms` keys). The MP3 is the source;
derive WAV with ffmpeg rather than spending a second API call.
