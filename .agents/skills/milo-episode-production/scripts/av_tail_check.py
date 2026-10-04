#!/usr/bin/env python3
"""Check whether a rendered master's picture actually covers its narration.

Usage:
  python av_tail_check.py RENDER.mp4 [--master AUDIO_MASTER.mp3] [--fps 30]

Why: timeline-driven renderers (scene specs, Remotion) set the picture length
from the scene sum minus transition overlaps and then trim the audio to it.
A scene sum shorter than `last_word_end + breathing tail` ships a master whose
closing words are cut mid-sound, and every duration still "adds up".

Reports per file: container duration, video frame count, last audible sample
(RMS gate), RMS of the final 300 ms (loud tail = clipped speech), and, when
--master is given, the alignment lag between the render's audio and the take
that proves which master the render actually carries.

Verdicts:
  TAIL_OK            speech ends >= 0.25 s before EOF (there is breathing air)
  NO_BREATHING_TAIL  speech runs to the last frame (closing beat has no air)
  CLIPPED_NARRATION  the master still has audible content past the render's EOF

Stdlib only (array/math/subprocess); needs ffmpeg + ffprobe on PATH.
"""

import argparse
import array
import json
import math
import subprocess
import sys

try:
    from array import array as _arr
except ImportError:  # pragma: no cover
    _arr = None

SR = 16000
WIN = int(SR * 0.02)          # 20 ms RMS windows
SIL_RMS = 0.010              # ~-40 dBFS: anything above counts as audible
TAIL_MIN_S = 0.25


def probe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries",
         "format=duration", "-show_entries",
         "stream=codec_type,width,height,nb_frames", "-of", "json", path],
        capture_output=True, text=True, check=True).stdout
    meta = json.loads(out)
    dur = float(meta.get("format", {}).get("duration", 0.0) or 0.0)
    nframes = wh = None
    for st in meta.get("streams", []):
        if st.get("codec_type") == "video":
            nframes = int(st.get("nb_frames") or 0)
            wh = (st.get("width"), st.get("height"))
    return dur, nframes, wh


def decode(path):
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path, "-f", "s16le", "-ac", "1",
         "-ar", str(SR), "-"], capture_output=True, check=True).stdout
    a = _arr("h")
    a.frombytes(raw[: len(raw) - (len(raw) % 2)])
    if sys.byteorder == "big":
        a.byteswap()
    return a


def envelope(a):
    n = len(a) // WIN
    env = []
    for i in range(n):
        chunk = a[i * WIN:(i + 1) * WIN]
        s = 0.0
        for v in chunk:
            s += float(v) * float(v)
        env.append(math.sqrt(s / WIN) / 32768.0)
    return env


def last_audible(env, thr=SIL_RMS):
    for i in range(len(env) - 1, -1, -1):
        if env[i] > thr:
            return (i + 1) * WIN / SR
    return 0.0


def lag_seconds(env_a, env_b, span=3.0):
    """Lag L minimising |a[t] - b[t-L]|; positive L means b starts later."""
    step = 0.02
    best = None
    for k in range(int(-span / step), int(span / step) + 1):
        if k >= 0:
            x, y = env_a[k:], env_b[:len(env_a) - k or None]
        else:
            x, y = env_a[:k], env_b[-k:]
        n = min(len(x), len(y))
        if n < 100:
            continue
        err = sum(abs(x[i] - y[i]) for i in range(n)) / n
        if best is None or err < best[1]:
            best = (k * step, err)
    return best if best else (None, None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("render")
    ap.add_argument("--master", default=None,
                    help="audio master / take the render should carry")
    ap.add_argument("--fps", type=float, default=30.0)
    args = ap.parse_args()

    rdur, rframes, rwh = probe(args.render)
    renv = envelope(decode(args.render))
    rlast = last_audible(renv)
    tail300 = sum(renv[-int(0.3 / 0.02):]) / max(1, len(renv[-int(0.3 / 0.02):]))

    print(f"render      : {args.render}")
    print(f"  container : {rdur:.3f} s   frames: {rframes}   "
          f"implied: {rframes / args.fps:.3f} s   size: {rwh}")
    print(f"  last audible sample : {rlast:.3f} s")
    print(f"  RMS final 300 ms    : {tail300:.4f} "
          f"({'LOUD -> speech runs into EOF' if tail300 > SIL_RMS else 'silence ok'})")

    verdict = "TAIL_OK"
    if rlast >= rdur - TAIL_MIN_S:
        verdict = "NO_BREATHING_TAIL"

    if args.master:
        mdur, _, _ = probe(args.master)
        menv = envelope(decode(args.master))
        mlast = last_audible(menv)
        lag, err = lag_seconds(menv, renv)
        print(f"master      : {args.master}")
        print(f"  duration  : {mdur:.3f} s   last audible: {mlast:.3f} s")
        print(f"  lag vs render: {lag:+.2f} s (mean |env| err {err:.4f}) -> "
              f"{'render carries this take' if abs(lag or 9) < 0.3 else 'DIFFERENT take/offset'}")
        if mlast > rlast + 0.05:
            verdict = "CLIPPED_NARRATION"
            print(f"  master has {mlast - rlast:.3f} s of audible content past the render's EOF")

    print(f"VERDICT     : {verdict}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
