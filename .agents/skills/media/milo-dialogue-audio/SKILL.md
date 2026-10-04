---
name: milo-dialogue-audio
description: "Use when producing dialogue audio for MILO episodes."
version: 1.0.0
author: Hermes Agent
license: MIT
---

# MILO Dialogue Audio (proven CONV EP001 30s, 9.6/10)

Two locked voices carry the episode; the mix must sound like one overheard conversation, not alternating narrators.

## Voice casting (ElevenLabs shared-voices API)

1. Search `GET /v1/shared-voices` per role (language=es, gender, age; page_size=100) — demand 5+ candidates each.
2. Shortlist by metadata: latin-american/mexican/colombian accent, conversational/narrative use-case; reject broadcaster/upbeat/ad delivery and adult-imitating-teen.
3. Verify with `GET /v1/voices/{id}`, but treat 400s as inconclusive — shared voices intermittently reject lookup while TTS works. The TTS preview itself is the real verification; never discard a candidate on lookup failure alone.
4. Generate Spanish previews with the character's actual lines (eleven_multilingual_v2, stability ~0.45, similarity ~0.75).
5. PRIMARY + BACKUP + ALT per role, recorded in `VOICE_BIBLE_LOCK.json` with voice_ids and direction notes.

## Emotional range gate (mandatory before series lock)

A 5-second preview cannot lock a series voice. Generate 3 state-distinct lines per PRIMARY (e.g. defense → explanation → vulnerability) and pass the gate only when identity holds across all three without sounding acted. Lock only after the gate passes.

## Production assembly

- Generate PER LINE (one TTS call each), never one emotional instruction per line — over-direction makes voices act. Carry emotion through punctuation and context; keep voice_settings constant across the episode.
- Assemble with explicit silence gaps (ffmpeg `adelay` + `amix`): short processing gaps (0.3–0.5 s) between turns, long narrative silences (1.5–2 s) at scripted beats. Compute offsets from measured line durations and verify the total lands in the target window (28–32 s for 30s format) BEFORE rendering.
- Micro-timing pass: add 200–400 ms processing air around the emotional peak lines; re-verify the window afterwards.
- Master: loudnorm to -16 LUFS (TP ≤ -1.5), SHA + durations recorded; Whisper word timestamps after lock feed the caption pipeline (`milo-caption-narrative`).

## Keys

ElevenLabs key lives in `10_CADENA/.env` (`ELEVENLABS_API_KEY`), passed via env, never logged. A 401 on `/v1/user` with 200 on `/v1/models` means restricted scope, not a dead key — test the endpoints the workflow actually needs before rotating.