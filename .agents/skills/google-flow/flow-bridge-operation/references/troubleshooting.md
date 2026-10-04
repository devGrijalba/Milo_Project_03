# Troubleshooting — extension + bridge route

Reference for `flow-bridge-operation`. Read the symptom, act in the order given.
Never retry a generation blindly: quota and Google's activity detection are the
expensive failure, not the script.

## Before anything else

```bash
npm run status
```

It is free and answers: is the bridge alive, is the extension connected, is there
a cooldown, do the canon folders exist. If it reports a problem, do not run
`generate` — the generation would be paid for and lost.

## Symptom table

| Symptom | Cause | Action |
|---|---|---|
| `worker: false` | extension side panel closed | user opens or reloads the side panel inside a Flow project with a Google session. Not automatable from outside. |
| `worker_count > 1` / `worker_conflict: true` | a second client registered — often your own probe | read `worker_count` ONCE (never in a poll loop) and compare with `netstat -ano \| grep 127.0.0.1:<port> \| grep -c ESTABLISHED`; if the two disagree the surplus is yours |
| worker connects from the wrong browser | the extension is loaded in more than one Chromium browser | map each ESTABLISHED socket's PID to a process name. Two copies (Chrome + Brave, or two profiles) means two workers; the user closes one. Never close a browser the user marked off-limits. |
| `EXPECTED_PROJECT_NOT_UNIQUE_OR_OPEN` | no Flow tab with `/project/<id>` open, or more than one | user opens exactly ONE Flow tab on that project UUID and closes any other Flow tab. The check is `matches.length !== 1`, so a duplicate tab fails just as hard as a missing one. |
| port is occupied by another project's bridge | two projects, one default port | do not kill the foreign process. Give each project its own resolvable port and identify by protocol, not port. See the endpoint section in SKILL.md. |
| bridge not responding | daemon not running | `python scripts/bridge.py` in the package root; expect `BRIDGE :8765 listo`. Keep it in its own terminal. |
| bridge alive but from another project copy | a second copy of the package is listening on the port | confirm the owning process; its `insumos/` is the only folder the bridge reads. Stop it and start the bridge from the copy you are generating from. |
| `Flow no listo` | project tab not loaded | user reloads the Flow project tab (F5). |
| job carries no images | references did not reach the bridge | the staging folder is the one inside the OWNING package; check its `insumos/` is populated. |
| no end-of-job notice | normal | the bridge resolves the end by watching the downloads folder. Only 18 min with no file AND no notice is a real timeout. |
| `busy: true` stuck | a hung job | look at the Flow window, then `bping.py` → `job_logs` for the phase messages. |
| traceback / `EOFError` in the bridge log | harmless TCP probe (port checks open and close the socket) | judge health with `bping.py`, not with the log. |
| "actividad inusual" toast | Google throttling automation | **STOP.** Cooldown 60–120 min, no retries, not even a different prompt. |
| generation refused: unknown key | manifest/lock mismatch | read the valid values printed in the error; fix the manifest or declare the lock entry. |
| generation refused: framing has no space plate | the lock does not cover that combination | declare the plate in the world lock. Never substitute a lookalike image. |
| reference not found in staging | the file is not in the canon folders | add the declared file, or point `attribute_sources` at one that exists. The package refuses lookalikes because a close reference causes silent drift. |
| prompt too long / no candidate fits | canon exceeds the word budget | shorten in the locks, not in the code. The adapter will not drop canon to hit a number. **Cut the `compact` projection of the light or space entry for that framing, never the `full` one** — see the word-gate note in SKILL.md. Count words per contribution first so you know which projection is bloated. |
| generation aborted, exit non-zero, message names a vetoed plate | the pre-generation barrier did its job | fix the lock or the plate classification. This is not a bug to work around. |
| gate exits 0 but prints nothing | ESM CLI guard failed on the Windows drive-letter case | gate the CLI on `pathToFileURL(process.argv[1]).href === import.meta.url`. Exit 0 with no output reads as success upstream and is the most dangerous gate failure. |
| gate rejects references it should accept | tri-state collapsed: unmeasured treated as violated | unmeasured traits warn; only measured-and-present blocks; a missing `verified` block blocks |
| gate message says "no plate in the lock" for a plate that exists | a test used an invented framing id | enumerate ids from the lock before using one, so a failure means what its message claims |
| two identical files in the downloads folder, different names | the extension wrote the same image twice | dedupe by SHA-256, keep the oldest, move the rest to a quarantine subfolder. Do not delete: the user never saw those files, and disk space is not the problem. |
| cooldown still active | a previous run set it | wait it out. Clearing the file by hand re-triggers the same Google response. |
| downloads folder does not exist | first run, or the browser downloads elsewhere | it is created on the first generation; override with the package's download env var if the browser is configured elsewhere. It is the only path that cannot be package-relative, because the OS decides it. |
| generation succeeded but the image is a different scene than the one requested | the wrapper accepted `--manifest` and the inner script ignored it, resolving a hardcoded one | resolve the flag in BOTH layers; the plan file must be named for the requested shot and the wrapper must read back THAT file. A response reporting another job's prompt is the tell. See the routing pitfall in SKILL.md. |
| `response.json` reports `ok: true` with a prompt from another shot | the wrapper reads a fixed plan filename while the generator writes per-shot plans | a verdict read from a stale file is not a verdict. Name the plan by shot id on both sides. |
| selector warnings appear inside what looks like one run | two channels interleave in the bridge log: the job's `job_*`/`hermes_*` ids and the extension's autonomous loop under the constant group `live` | count messages per `groupId` before attributing anything. Sequential reading makes `live`'s failures look like the job's |
| a fix pack arrives describing a bug you already fixed on disk | the pack was written from an old artifact, not from the source | open each named function and check whether the fix is present. Report which proposed items are already satisfied — re-implementing them creates a duplicate gate that drifts from the first. |
| an artifact still shows behaviour you fixed in the source | the running process predates the edit; Python does not hot-reload | compare process start time against the file mtime, then restart. An artifact state no reachable code path can emit is the tell. |
| a run reports `flow status: completed` + `resolver: ok` but `files: []` | delivery failed; the status only reports that the extension's loop finished, and the envelope hardcodes `ok: true` | verify a file exists with an mtime after the job timestamp. The fix goes where the envelope is built (derive the verdict from the file list) — a restart does not close this one. See the termination rule in SKILL.md. |
| downloads folder holds a file whose slug matches the prompt | it may be an earlier run's output | compare mtime to the job's own timestamp; identical-looking evidence with an older timestamp is not this job's |
| bridge dies at ~18 min with `BridgeUnavailableError`, and `job_logs` names a UI element it could not find | Flow re-rendered that screen; the extension's selector is stale | user reloads the Flow tab (F5) and the side panel. Do NOT retry first: the same submit spends quota on the same failure. |
| submitted prompt does not match the shot you asked for | see the two rows above | check `.state/runs.jsonl` BEFORE looking at the image: the submit line is the ground truth for what was sent. |
| character looks right but legs/footwear/proportions are invented | identity was resolved by output framing, so hidden zones fell back to partial crops | framing decides what is shown, the reference decides who it is. Resolve identity from the declared full-body master. See `references/identity-resolution.md`. |
| plan's not-sent list says "not visible in medium" for an attribute you consider part of identity | the visibility filter is still driving identity | exempt declared complements (expression/view) and never filter the master itself; add frame-hidden zones before adding the master, not after. |
| a contract test passes immediately after being written | it read the wrong field name and matched nothing | assert the fixture actually contained the expected rows. A green test that loaded zero items validates nothing. |

## Portability

```bash
npm run verify
```

Checks two failure modes, and both matter: machine-absolute paths (break when
the folder moves) and **hand-written relative paths** (work until someone runs
the command from another directory, then fail silently reading the wrong file).
System paths (`C:/Program Files`, `AppData`) are reported but are not failures —
Windows decides those. A `PORTABLE` verdict means the folder can be moved,
renamed or zipped as a unit.

## What this route does NOT do

- No script writing, no corpus analysis, no video render, no audio. Those live
  in other stages/projects.
- No judge of the produced image. It reports that a file arrived; the verdict
  criteria are applied by a human/agent looking at the file.
- No CDP. The CDP replica in the package is kept only as documentation of why
  the extension route exists: Google detects CDP automation, the extension
  route does not have that failure mode.
