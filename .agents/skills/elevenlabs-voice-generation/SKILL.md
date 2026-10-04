---
name: elevenlabs-voice-generation
description: "Use when generating voice audio with ElevenLabs TTS."
version: 1.1.0
author: Hermes Agent
license: MIT
---

# ElevenLabs Voice Generation

Core principle: API-first generation with measured QA — script generates, ffprobe measures, human ear decides. The agent never declares a take good sounding.

## When to Use

- User asks for voiceover, narration, note-de-voz, or character takes via ElevenLabs.
- Any task ending with "N validated audio files + manifest".
- Diagnosing ElevenLabs 401/quota/voice issues.

## Hard Constraints

- Keys live in project `.env` (`ELEVENLABS_API_KEY`, `ELEVENLABS_API_KEY_2`), git-ignored, edited by the user directly. Never paste key values into chat, prompts, or docs — refer by label ("clave 1/2") and fingerprint (`primeros6...últimos4`) only.
- Quota costs real money: probe cheap first, batch only after probe passes. Report characters consumed per key per batch.
- Master spec declared up front (recommended: WAV PCM 16-bit, 44.1 kHz, mono, peak ≤0.89). MP3 from API is the source; WAV derives via ffmpeg, never a second API request.

## Core Pattern

Before: paste prose + context into TTS box, one take, sounds fine to me → context read aloud, 20s takes vs 7s target, overwritten files, letter-vs-spoken mismatches.

After: validate keys → cheap probe → 3 directed takes (same voice, varied direction) → measure proxies → human picks → assemble master → manifest.

## Workflow

1. **Keys.** Fingerprint each key (unique values only — duplicate `.env` lines collapse to the last). Probe: `GET /v1/user` (validity + quota) + `GET /v1/voices`. Then minimal TTS probe per key (`"Hola."`, ~5 chars): 401 `detected_unusual_activity` with green `/v1/user` = free-tier generation disabled → rotate/promote working keys, comment out dead ones, re-validate. Never retry dead keys in a loop.
2. **Text prep (v3 rule).** In `eleven_v3` everything outside `[brackets]` IS SPOKEN. Direction tags (`[whisper]`, `[pause]`, `[fearful whisper]`, etc.) are not pronounced — but ONLY on v3. On `eleven_multilingual_v2` brackets are read aloud literally: strip them or switch to v3. Never paste direction prose into the TTS text. Review text length before spending.
3. **Generate.** `POST /v1/text-to-speech/{voice_id}` (audio) or `.../with-timestamps` (audio + alignment JSON). Baseline: `stability` 0.30–0.40, `similarity_boost` 0.80–0.90, `style` 0.40–0.50 + inline tags + expressive punctuation. Method: 3 takes, same voice, 3 directions (A contained / B confidential-whisper / C urgency), varying stability/style — never the voice. Versioned filenames (`take02_v001`, anti-overwrite guard).
4. **Timestamps (only `with-timestamps`).** Response shape is URL-determined: standard endpoint = raw audio bytes; `/with-timestamps` = JSON `{audio_base64, alignment}` where alignment keys are `characters`, `character_start_times_seconds`, `character_end_times_seconds` (SECONDS, no `_ms` keys — inspect `list(alignment.keys())` first). Fold chars→words on whitespace; save `*_words.json` + raw alignment next to audio. SRT: phrase-boundary blocks, min ~3 words/block, merge orphans, cap ~10 words; times from word start/end.
5. **Measure (never ear).** Per take: duration, peak (`volumedetect`), silence ratio (<−40 dBFS), per-segment dynamics, F0 mean/std (70–400 Hz). Reference: good short takes ~5–7s, pauses 40–58%. Verify no `[tag]` leaked into spoken words via alignment. Write `*_VOICE_COMPARISON.md`: data table + hypotheses labeled as hypotheses + empty scorecard per take. Agent never picks the winner — human ear on phone decides.
6. **Assemble.** Master = chosen take (+ textures) with phone post if needed (highpass 300 / lowpass 3400 / comp 3:1 / peak ≤0.89), WAV PCM16 44.1k mono. Delete invalid intermediates (generator script is the source, not files).
7. **Manifest.** One entry per delivered file: id, filename, voice_id, model, text_hash (never full key), duration measured, sample_rate, channels, sha256, created_at. Invariant: manifest entries == files on disk.

## API Reference (self-contained)

- Base: `https://api.elevenlabs.io`. Headers: `xi-api-key: <KEY>` + `Content-Type: application/json`. Key fingerprint for logs: `primeros6...últimos4`, label `clave 1/2`.
- Models: `eleven_v3` = understands `[tags]`; `eleven_multilingual_v2` = brackets read aloud (strip tags or switch to v3). Default `output_format = "mp3_44100_128"`.
- Request example:

```json
POST /v1/text-to-speech/{voice_id}
{
  "model_id": "eleven_v3",
  "text": "[whisper] Hola mundo",
  "output_format": "mp3_44100_128",
  "voice_settings": { "stability": 0.35, "similarity_boost": 0.85, "style": 0.45 }
}
```

`curl`: `curl -s -X POST "$BASE/v1/text-to-speech/$VOICE" -H "xi-api-key: $KEY" -H "Content-Type: application/json" -d @body.json -o take01_v001.mp3`. With-timestamps variant: `POST /v1/text-to-speech/{voice_id}/with-timestamps` → JSON `{audio_base64, alignment}`; decode `audio_base64` to mp3 (the MP3 is the source; WAV derives via ffmpeg).

## Measure Commands (copy-paste)

```bash
ffprobe -v error -show_entries stream=sample_rate,channels -show_entries format=duration -of default=noprint_wrappers=1 file.mp3
ffmpeg -i file.mp3 -af volumedetect -vn -sn -dn -f null /dev/null   # peak + mean volume
ffmpeg -i file.mp3 -af silencedetect=noise=-40dB:d=0.3 -f null - 2>&1 | grep silencedetect
ffmpeg -i in.mp3 -ar 44100 -ac 1 -c:a pcm_s16le out.wav            # MP3→WAV master
ffmpeg -i out.wav -af "highpass=f=300,lowpass=f=3400,acompressor=threshold=-18dB:ratio=3" out_phone.wav
sha256sum *.wav | tee manifest.sha256
```

Windows (git-bash): replace `/dev/null` with `NUL`, `sha256sum` available in git-bash.

## Voice & Quota Rules

- Voice choice: fixed `voice_id` per project (documented in batch header); 3 takes vary direction (stability/style/tags), never the voice. New voice only on explicit user request.
- Quota report per batch (one line per key): `clave 1 (abc123...wxyz): probe 5 chars + batch N chars = TOTAL chars; /v1/user remaining: X`. Report BEFORE assembling master.
- Micro-takes (<2s, e.g. single "Hola mundo"): reference 5–7s / pauses 40–58% does NOT apply. Thresholds: duration ≥ text length sanity (`~0.35–0.6s per word` ES), peak ≤ 0dB (target −6..−2dB), no clipped samples, alignment covers 100% of non-tag chars, no `[tag]` in spoken words. SRT for micro-takes = single block.

## Quick Reference

| API | Purpose |
|-----|---------|
| `GET /v1/user` | validity + quota (green ≠ TTS works) |
| `GET /v1/voices` | voice list |
| `POST /v1/text-to-speech/{id}` | audio bytes |
| `POST /v1/text-to-speech/{id}/with-timestamps` | `audio_base64` + alignment (seconds) |

| Param | Baseline |
|-------|----------|
| stability | 0.30–0.40 |
| similarity_boost | 0.80–0.90 |
| style | 0.40–0.50 |

## Common Mistakes

- Context paragraph in TTS text → spoken aloud, take ruined. Frase + tags only.
- Tags sent to v2 → read aloud. v3 or strip.
- `alignment['*_ms']` → KeyError after a 200 with audio written. Keys are `_seconds`.
- Whisper tag assumed quiet → measure peak; tags don't guarantee gain.
- Same filename twice → silent overwrite. Version everything.
- Agent choosing prettiest take → only criterion is a real person recorded this on their phone; human decides.

## Red Flags

- Key value printed in logs/chat.
- Batch started without `Hola.` probe.
- Take judged by agent ear instead of measured proxies + human verdict.
- WAV requested from API instead of derived via ffmpeg.
