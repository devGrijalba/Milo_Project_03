---
name: chrome-extension-forensics
description: "Use when identifying installed Chrome extensions on disk."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [windows]
metadata:
  hermes:
    tags: [chrome, extensions, forensics, sessions]
    category: devops
---

# Chrome Extension Forensics

Identify an installed Chrome extension from disk and recall what prior
sessions established about it, answering from evidence rather than memory.

## Procedure

1. **Recall first.** Run `session_search` with the extension name
   (vary phrasing: product name, `extension`, `flow`). If a match names
   an extension ID or folder, treat it as a lead, not a conclusion.
2. **List installed IDs.** List `C:/Users/<user>/AppData/Local/Google/Chrome/User Data/Default/Extensions/` (per-profile: `Default`, `Profile 1`, ...). Folder names are opaque IDs.
3. **Confirm by manifest.** Read `<ID>/<version>/manifest.json` and trust
   `name` + `description` + `content_scripts.matches`, never the folder
   name. Report ID, version folder, description, and matched hosts.
4. **Re-verify before claiming.** Re-list the ID folder in the current
   session — extensions auto-update (version folder changes) or disappear
   per profile.

## Pitfalls

- Folder name alone proves nothing — two profiles can hold different
   versions of the same ID; the manifest is the identity.
- Large `session_search` scroll results spill to a file path instead of
   inline JSON — parse that file with `terminal` + python (`json.load`,
   filter by message id) because `read_file` truncates the single-line
   JSON and `execute_code` fails to parse it.
