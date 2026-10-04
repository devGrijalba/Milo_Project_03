#!/usr/bin/env python3
"""Text-grounded frame content probe (for sessions that cannot see images).

Usage:
  python frame_content_probe.py shot01.png shot02.png [...] \
      [--env-file D:/hermes/MILO/10_CADENA/.env] [--out probe.json]

The probe asks a free-tier vision model for ONE compact JSON per frame with a
short description plus NORMALIZED boxes (x, y, w, h; y grows downward) for:
people, hands, glass_of_water, doorway. That is what you need to
  * catch two shots carrying the same composition (child at the threshold
    watching a busy mother, twice) before wiring a timeline, and
  * locate the region a crop/reframe must isolate (glass on the nightstand,
    the mother's busy hands).

Treat every answer as a HYPOTHESIS: cross-check boxes against the real pixel
math before cropping, and never trust its character identification (it
mislabels the round-headed adult as the child). Resemblance scoring of Milo
identity stays with the anchor-based judge, not with this probe.

Key resolution order: OPENROUTER_API_KEY env var, else KEY=value lines in
--env-file. The key is never printed and never written to --out.
"""

import argparse
import base64
import io
import json
import os
import sys
import time
import urllib.request

DEFAULT_MODELS = [
    "inclusionai/ling-3.0-flash-vl:free",
    "qwen/qwen3.8-27b:free",
    "z-ai/glm-5.2:free",
]

PROMPT = (
    "Analyze this storybook illustration frame (vertical 9:16). Answer about CONTENT and "
    "POSITION only. Give bounding boxes in NORMALIZED coordinates (x,y = top-left of box, "
    "w,h = size; 0-1, y grows downward). Reply ONLY compact JSON: "
    '{"describe":"one or two sentences",'
    '"people":[{"who":"child|mother|none","what_doing":"...","box":[x,y,w,h]}],'
    '"hands_visible":true|false,"hands_box":[x,y,w,h]|null,'
    '"glass_of_water_visible":true|false,"glass_box":[x,y,w,h]|null,'
    '"doorway_visible":true|false,"doorway_box":[x,y,w,h]|null,'
    '"text_or_watermark":"none|describe"}'
)


def load_key(env_file):
    key = os.environ.get("OPENROUTER_API_KEY", "").strip()
    if key or not env_file or not os.path.exists(env_file):
        return key
    for line in open(env_file, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            if k.strip() == "OPENROUTER_API_KEY":
                return v.strip()
    return ""


def img_b64(path, width=512, quality=70):
    """Downscale when PIL is available (token economy), else send as-is."""
    try:
        from PIL import Image
        im = Image.open(path).convert("RGB")
        im = im.resize((width, int(im.height * width / im.width)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=quality)
        return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    except Exception:
        with open(path, "rb") as fh:
            return "data:image/png;base64," + base64.b64encode(fh.read()).decode()


def ask(key, model, data_url):
    body = json.dumps({"model": model, "messages": [{"role": "user", "content": [
        {"type": "text", "text": PROMPT},
        {"type": "image_url", "image_url": {"url": data_url}},
    ]}]}).encode()
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions", data=body,
        headers={"Content-Type": "application/json",
                 "Authorization": "Bearer " + key})
    out = json.load(urllib.request.urlopen(req, timeout=180))
    txt = out["choices"][0]["message"]["content"]
    data = json.loads(txt[txt.index("{"):txt.rindex("}") + 1])
    data["judge"] = out.get("model", model)
    return data


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("images", nargs="+")
    ap.add_argument("--env-file", default=None)
    ap.add_argument("--models", nargs="*", default=DEFAULT_MODELS)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    key = load_key(args.env_file)
    if not key:
        print("no OPENROUTER_API_KEY (env or --env-file): nothing sent", file=sys.stderr)
        return 2

    results = {}
    for path in args.images:
        url = img_b64(path)
        for model in args.models:
            try:
                results[os.path.basename(path)] = ask(key, model, url)
                print(os.path.basename(path), "OK via", results[os.path.basename(path)]["judge"])
                print("   ", json.dumps(results[os.path.basename(path)], ensure_ascii=False)[:700])
                break
            except Exception as exc:  # rate limit / retired free id / moderation
                print(os.path.basename(path), model, "failed:", str(exc)[:120], file=sys.stderr)
                time.sleep(4)
        time.sleep(2)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(results, fh, indent=1, ensure_ascii=False)
        print("saved", args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
