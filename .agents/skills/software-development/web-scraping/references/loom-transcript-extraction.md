# Loom Video Transcript Extraction

Extract transcriptions/captions from Loom videos embedded in course platforms (Skool, etc.).

## Video Provider: Loom

Loom provides two formats of transcripts:
1. **VTT** (WebVTT): `cdn.loom.com/mediametadata/captions/{video_id}-{n}.vtt` — standard subtitle format
2. **JSON** (Structured, preferred): `cdn.loom.com/mediametadata/transcription/{video_id}-{n}.json` — `phrases[].ts` + `phrases[].value`

Both URLs are **time-limited** (signed with Policy + Signature) and expire ~1 hour after generation. They must be extracted from the live Loom embed page.

## Detection

When a page embeds a Loom video, look for an iframe with `src` containing `loom.com/embed/{video_id}`:

```javascript
document.body.innerHTML.match(/loom\.com\/embed\/([a-f0-9]+)/)
```

## Extraction Workflow

### 1. Navigate to Loom embed page
```
https://www.loom.com/embed/{video_id}
```

### 2. Extract transcription URL
```javascript
const scripts = Array.from(document.querySelectorAll('script'));
const allText = scripts.map(s => s.textContent).join(' ');

// JSON format (preferred):
const transMatch = allText.match(
  /https:\/\/cdn\.loom\.com\/mediametadata\/transcription\/[a-z0-9-]+\.json[^"]*/
);

// VTT fallback:
const vttMatch = allText.match(
  /https:\/\/cdn\.loom\.com\/mediametadata\/captions\/[a-z0-9-]+\.vtt[^"]*/
);
```

### 3. Fetch transcription data
```javascript
// JSON format — returns {phrases: [{ts: number, value: string}, ...]}
fetch(transMatch[0])
  .then(r => r.json())
  .then(d => console.log(JSON.stringify({
    "phrases": d.phrases.map(p => ({ts: p.ts, value: p.value}))
  })));

// VTT format — returns standard WebVTT text
fetch(vttMatch[0])
  .then(r => r.text())
  .then(text => console.log(text));
```

## VTT Parsing (Python)

```python
import re

def parse_vtt(vtt_text):
    segments = []
    lines = vtt_text.strip().split("\n")
    i = 0
    if lines and lines[0].strip() == "WEBVTT":
        i = 1
    while i < len(lines):
        line = lines[i].strip()
        # Skip empty lines and standalone segment counters
        if not line or line.isdigit():
            if line.isdigit() and i + 1 < len(lines):
                if not re.match(r"\d+:\d+:\d+\.\d+\s+-->", lines[i + 1].strip()):
                    i += 1; continue
            i += 1; continue
        # Parse timestamp line: 00:01.700 --> 00:06.980
        ts_match = re.match(
            r"(\d+):(\d+):(\d+)\.(\d+)\s+-->\s+(\d+):(\d+):(\d+)\.(\d+)", line
        )
        if ts_match:
            groups = [int(g) for g in ts_match.groups()]
            h1, m1, s1, ms1 = groups[:4]
            h2, m2, s2, ms2 = groups[4:]
            start = h1*3600 + m1*60 + s1 + ms1/1000
            end = h2*3600 + m2*60 + s2 + ms2/1000
            text_parts = []; i += 1
            while i < len(lines):
                nl = lines[i].strip()
                if not nl: i += 1; break
                if nl.isdigit() and i+1 < len(lines) and re.match(r"\d+:\d+:\d+\.\d+\s+-->", lines[i+1].strip()): break
                if re.match(r"\d+:\d+:\d+\.\d+\s+-->", nl): break
                cleaned = re.sub(r"<[^>]+>", "", nl).strip()
                if cleaned: text_parts.append(cleaned)
                i += 1
            if text_parts:
                segments.append({"text": " ".join(text_parts), "start": round(start, 2), "duration": round(end - start, 2)})
        else: i += 1
    return segments
```

## JSON Transcription Format (direct conversion)

The JSON format maps directly to the RAG pipeline's segment format:

```python
segments = [{"start": p["ts"], "text": p["value"]} for p in data["phrases"]]
```

No parsing needed — it's already structured with timestamps.

## Skool Course Integration

When the videos are inside a Skool course, each module has an `md` parameter:

```
https://www.skool.com/sqxtraders/classroom/{course_id}?md={module_id}
```

To find which modules have Loom videos:
1. Navigate to each module page
2. Check for Loom video ID in the HTML
3. Some modules are text-only (descriptions, no video)

Output format compatible with the RAG pipeline:

```python
{
    "video_id": "loom_video_id",
    "md_param": "skool_module_id",
    "title": "Module Title",
    "source": "loom",
    "language": "es",
    "segments": [{"start": 1.5, "text": "..."}, ...]
}
```

## Pitfalls

- **Signed URLs expire**: The transcription JSON/VTT URLs have time-limited policies (~1 hour). Extract and fetch in the same browser session.
- **Rate limiting**: Loom doesn't rate-limit caption fetches, but Skool's AWS WAF may block rapid page loads. Add 1-2s delay between module navigations.
- **Some modules lack videos**: Not every module has a Loom embed. Text-only modules have no iframe.
- **Language detection**: Loom auto-captions detect the spoken language. Spanish videos produce Spanish VTT, English produce English VTT. No language selection available.
- **VTT segment counter lines**: VTT lines that are just numbers (segment counters) must be skipped. Peek at the next line to distinguish counters from actual content.
