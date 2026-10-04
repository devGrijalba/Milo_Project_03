"""DeepSeek provider: one LLM call per invocation.

Interface contract (same shape as src/provider.py::call, which orchestrator and
multiagent already call through runtime.cached_call):

    call(command, payload, timeout, role=None) -> dict

`command` is ignored here on purpose. The DeepSeek route has no argv: the browser
is the transport, so the provider reads its own settings from config/engine.json.
Keeping the parameter means orchestrator/multiagent need no changes at all.

Layering (deliberate, do not collapse):
    src/ds_provider.py   ONE call. build prompt, inject, extract, validate.
    tools/ds_session.py  ONE tab: open, reuse, close, per-tab websocket.
    tools/ds_pool.py     N tabs, bounded concurrency, lifecycle.

This module owns NO tab lifecycle and NO parallelism. If you find yourself adding a
thread pool here, it belongs in ds_pool instead.

Failure contract, matching src/provider.py:
    - a stub payload is refused BEFORE any browser work (validate_payload)
    - a blocked worker propagates as an exception, never as a candidate
    - a malformed model reply raises; it is never returned as a half-result
"""
from __future__ import annotations

import json
import pathlib
import re

from src.common import config, read

# ---------------------------------------------------------------- payload guard

BASE_PACKAGE_KEY = "base_package"
CANDIDATE_ROLES = ("script_critic",)


def validate_payload(role, payload):
    """Return the list of missing required keys. Empty means executable.

    Copied in spirit from src/provider.py so a bad payload is rejected locally,
    before a browser tab is spent on it.
    """
    if not isinstance(payload, dict):
        return ["payload must be an object"]
    if role == "script_synthesizer":
        missing = [k for k in ("base_package", "specialist_reports")
                   if not isinstance(payload.get(k), dict) or not payload[k]]
        if not missing and len(payload["specialist_reports"]) != 5:
            missing.append("five_specialist_reports")
        return missing
    if role in CANDIDATE_ROLES:
        return [k for k in ("candidate", "candidate_hash")
                if payload.get(k) is None or k not in payload]
    return [k for k in (BASE_PACKAGE_KEY,) if not payload.get(k)]


# ---------------------------------------------------------------- prompt build

def build_prompt(role, payload, instructions, config_path=None):
    """Render the prompt actually typed into the composer.

    The model reads prose plus a JSON blob. The JSON goes last and is fenced so a
    reply can be parsed back out of the assistant text without ambiguity.
    """
    c = config(config_path)
    head = instructions.strip()
    body = json.dumps(payload, ensure_ascii=False, indent=2)
    return (
        f"{head}\n\n"
        "--- PAYLOAD JSON ---\n"
        "Responde EXCLUSIVAMENTE con un objeto JSON valido, sin texto antes ni "
        "despues, sin bloques de codigo markdown.\n\n"
        "```json\n"
        f"{body}\n"
        "```\n"
    )


# ---------------------------------------------------------------- json extract

_FENCE = re.compile(r"```(?:json)?\s*(.*?)```", re.S)


def extract_json(text):
    """Pull one JSON object out of a model reply.

    Order matters: fenced block first (most explicit), then a brace-balanced scan
    that tolerates prose around it. Returns the parsed object or None -- never a
    partial dict, because a half-parsed contract is worse than a clean failure.
    """
    if not text:
        return None
    text = text.strip()

    # 1. fenced block
    for m in _FENCE.finditer(text):
        try:
            obj = json.loads(m.group(1).strip())
            if isinstance(obj, dict):
                return obj
        except json.JSONDecodeError:
            continue

    # 2. bare object, brace-balanced from the first '{'
    start = text.find("{")
    if start == -1:
        return None
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(text)):
        ch = text[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                try:
                    obj = json.loads(text[start:i + 1])
                    if isinstance(obj, dict):
                        return obj
                except json.JSONDecodeError:
                    return None
                return None
    return None


# ---------------------------------------------------------------- transport

def call(command=None, payload=None, timeout=300, role=None, config_path=None,
         session_name=None):
    """Execute one DeepSeek call. `command` is accepted for interface parity and
    ignored: the browser is the transport, not an argv.

    Lifecycle is explicit and ordered:
        acquire -> send -> extract -> validate -> reset_session -> release

    `session_name` is optional. When omitted it is DERIVED from the role, so a
    specialist gets a stable logical session without the caller having to widen
    the invoke signature to pass one.
    """
    from tools.ds_session import DSSession           # imported late: tests stub it
    from tools.ds_extract import extract_from_tab
    from tools.ds_pool import pool as get_pool

    if role:
        missing = validate_payload(role, payload)
        if missing:
            raise ValueError(
                "HERMES_TASK_BLOCKED:MISSING_SCRIPT_REQUEST_CONTEXT:" + ",".join(missing))

    c = config(config_path)
    ds = c.get("ds") or {}
    prompt = build_prompt(role, payload, _instructions_for(role), config_path)

    owner = session_name or ("specialist_" + role if role else None)
    if owner:
        tabpool = get_pool(ds)
        session = tabpool.acquire(owner)
        owned_by_pool = True
    else:
        session = DSSession(ds)
        owned_by_pool = False

    try:
        reply = extract_from_tab(session, prompt, ds)
    finally:
        if owned_by_pool:
            # fresh chat before handing the tab on: reuse must never carry context
            try:
                tabpool.reset_session(owner)
            finally:
                tabpool.release(owner)
        else:
            session.close()

    if not reply or not reply.strip():
        raise ValueError("DEEPSEEK_EMPTY_REPLY:" + str(role))
    result = extract_json(reply)
    if result is None:
        raise ValueError("DEEPSEEK_NO_JSON_IN_REPLY:" + str(role))
    if isinstance(result, dict) and result.get("status") in (
            "HERMES_TASK_BLOCKED", "HERMES_CAPABILITY_BLOCKED"):
        raise ValueError("HERMES_TASK_BLOCKED:" + str(result.get("reason") or "unknown"))
    return result


def _prompt_for(role, c):
    mapping = {
        "script_synthesizer": "writer.md",
        "script_critic": "critic.md",
    }
    return mapping.get(role, "writer.md")


def _instructions_for(role):
    root = pathlib.Path(__file__).resolve().parents[1]
    name = _prompt_for(role, None)
    p = root / "prompts" / name
    return p.read_text(encoding="utf-8") if p.exists() else ""