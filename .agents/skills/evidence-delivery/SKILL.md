---
name: evidence-delivery
description: 'Use when handing finished work to the director.'
---

# Evidence-backed delivery

Every handoff must let the director judge and forward the work without
asking follow-ups. Finished work gets a short report (what changed, what is
verified, what is left) plus the artifacts — never a replay of the process.

## Report format: the state, not the journey

Documentation belongs in the bitácora/log, not in the reply. The reply is a
one-page view of the state; if a report must be long to be useful, the real
state is not recorded anywhere readable — fix that instead of writing more.

```
ESTADO: [hecho | en progreso | bloqueado]

QUÉ SE HIZO:
- [one line per completed action, no narrative]

QUÉ SE ENCONTRÓ:
- [finding + its evidence in one line]
- [if it is a defect: what caused it]

QUÉ FALTA:
- [next concrete action]
- [blockers, if any]

DECISIÓN REQUERIDA: [sí/no]
[if yes, the exact question in one line]
```

Rules that make it work:
- **No narrative.** Never "first I verified, then I thought, then I did".
- **No adjectives.** Data only. "Tarda mucho" is useless; "118 s, timeout at
  120 s" is evidence.
- **One finding = one line.** Sub-bullets only when a line cannot carry it.
- **Cifras siempre.**
- **Own errors get one line.** "I declared the wrong task_type" is enough; the
  autopsy goes in the log.
- **10 lines beats 50.** If it does not fit, the detail belongs in the log.

Break the format only for: code/JSON the recipient will review (separate
block), a decision with real trade-offs (a table, not prose), or an unexpected
failure (full detail, because it may be a system fault).

## Every delivery ships

- A `.zip` bundle with the exact deliverables, plus each file's absolute
  path written out (media embed + path line). No zip, no handoff.
- Preview stills/frames inline next to the archive.

## Honesty gates

- `pass:true` only for fully verified claims; anything needing the
director's eye stays `pass:false` with the visual fields marked for them.
- A tool success response is not success: read back the effect (bytes,
  counts, evaluated values) before reporting it.
- Report blockers plainly with the evidence; never fabricate output to
  cover a failed step.

## Freeze the artifact before you certify it

A report is only evidence for the bytes that existed when it was produced. Any
rebuild after the measurement makes the report stale, and a bundle carrying both
a stale report and a fresh artifact ships a self-contradiction that reads as a
lie about the artifact.

- **Re-verify every report against the artifact's final bytes at pack time**, in
  the same command that builds the bundle — never trust a report produced in an
  earlier phase, by an earlier run, or by a delegated agent. Cheap check: re-run
  the measurement and diff the verdict, or assert the report's headline number
  still holds.
- **Ship the raw measurement output, not only its summary.** A report whose
  claims cannot be recomputed from a file in the bundle is an assertion.
- **Audit delegated reports hardest.** A subagent that audited an artifact you
  were still editing produced a correct report about an artifact that no longer
  exists. Two-writer races also corrupt the artifact itself: a rebuild loop
  rewriting a model while you hand-edit the same model yields partial reads
  ("no animations"), not just stale conclusions.
- **Never let a pipeline that rebuilds an artifact run concurrently with a manual
  edit of that same artifact.** Serialize them, or work on a copy.
- When a superseded report has already shipped, regenerate it and repack before
  saying the bundle is done; noting the discrepancy in chat is not a fix.

## Build the bundle with a script, and prove what is in it

- **Stage with a script, not by hand.** A hand-assembled bundle cannot be rebuilt
  and the first thing that breaks after an edit is a file nobody re-copied. The
  script belongs in the repo.
- **Verify a required-file list after staging and exit nonzero** if anything is
  missing. A staging step that swallows errors (`2>/dev/null || true`) reports OK
  while producing a bundle that is missing its index.
- **Confirm the archive's own contents after compressing**, by listing entries and
  asserting the critical paths are present and the excluded ones absent. Name
  comparison must account for whatever prefix the compressor adds, or the check
  passes vacuously.
- **Do not let a required entrypoint live only in the staging folder.** Generate
  the reading guide into a template inside the repo and copy it in the build; a
  guide written straight into staging disappears on the next rebuild.

## Secret exclusion, proved rather than asserted

State "no secrets" only after scanning the staged tree for the ACTUAL values,
not for the pattern of a secret.

- **Scan for each real key value** read from the env file. A pattern scan
  (`sk-`, `gsk_`) false-positives on minified vendor bundles and teaches you to
  ignore the scan's output — which is how a real key ships.
- **Scope the pattern scan to the project's own sources** and exclude vendor and
  generated assets.
- **Distinguish redaction by size from redaction by risk** in the notes: a
  multi-MB raw dataset excluded for size is not a secret, and saying so is what
  makes the rest of the list credible.

## Confirm what exists before packaging it

When the request is "package everything", inventory FIRST — a bundle assembled
without an inventory either omits a subsystem nobody notices until the audit
fails, or carries 500MB of material that was never meant to travel.

- **Enumerate top-level folders with sizes before deciding scope.** The size
  distribution is the decision: a single reference-asset folder can outweigh the
  entire engine tree, and it is the one folder a reader will not open.
- **Read the artifact rather than the folder name.** A folder that looks like
  third-party reference material may be a required input; one that looks like a
  core motor may be a duplicate. Hash-compare suspected duplicates instead of
  assuming — "these are the same image" is a claim that needs bytes behind it.
- **Keep duplicates and retired material in an audit bundle, and declare why in
  the index.** An auditor must be able to VERIFY the duplication, not take it on
  faith; and deleting a retired artifact or a superseded tool is what makes the
  same solution get proposed again. Exclude only what is genuinely not content:
  VCS binary internals (ship the readable log instead), interpreter caches,
  reinstallable dependency trees.
- **Ship the gate runs as evidence, not as a claim that gates pass.** Put the
  captured output of every verifier in the bundle. "All green" asserted in an
  index is an assertion; eight exit codes with their tails is evidence.
- **Write the index as a MAP, not a list.** The auditor's first need is not a
  file listing (they have one) but the architecture: what each subsystem does,
  which contract governs what, which gate checks which claim, and the order to
  read in. An index that only enumerates files makes the reader rediscover the
  system — which is the work you were paid to save them.
- **Verify the archive itself before delivering it.** List entries after
  compressing, assert the index and each critical subsystem's entry point are
  present, assert the excluded paths are absent, and run a CRC check. Report the
  size and a checksum so the recipient can prove the transfer was intact.
- State plainly which scope decisions you made without asking, so the recipient
  can widen them trivially rather than re-request the whole bundle.

## Exclusion list, and what each entry costs

Secrets, dependency trees, browser profiles and session cookies, work-in-progress
copies, and oversized raw corpora. For the oversized one, leave a placeholder
file in its place saying what it was, how big, and how to regenerate it — a
missing folder reads as an oversight, an explained one reads as a decision.

## Answer "is it secured?" with the split, not a verdict

When asked whether a system is secured, never answer yes or no flat. Report the
two levels separately, because they fail differently and only one of them is
usually broken:

- **The rules hold** — verified by real execution (a gate aborted, hashes intact,
  contracts satisfied). This does not decay; it is not infrastructure.
- **A live dependency is up** — bridge process, service, worker connection. This
  dies on its own when the session ends and is trivially restorable.

The first is the design; the second is a running process. Conflating them makes
a dead bridge read as a broken system, and the fix for one is unrelated to the
fix for the other.

**Restoring a stopped local process in the user's own project is not a
confirmation-worthy action.** Starting a bridge, a dev server, or a worker that
the project already declares is ordinary repair: do it, then report `worker:
true`. Asking "shall I start it?" for something the project is designed to have
running trains the user to approve the obvious. Reserve questions for external
cost, irreversible deletion, and conflicting instructions.

## Where files may be written

The user's project folder is the boundary. Before creating, copying, or
restoring anything, decide whether it belongs inside the project root or in an
explicitly approved scratch location.

- **A stale path in a skill or config is a finding to report, not an
  instruction to materialise it.** When a skill points at a directory that does
  not exist, do not create that directory tree to satisfy the pointer. Copying
  data to make a broken pointer look valid converts a visible bug into an
  invisible one. Report the broken pointer and ask where the data belongs.
- **Search the project before searching the wider disk.** A report naming a file
  "in `OLD/`" is not proof that `OLD/` is the only copy. The project's own data
  folder is the first place to look; an external `OLD`/`archive` directory is
  often a stale duplicate of something that already lives inside the project.
- **Never run a whole-disk recursive glob to confirm a path you were handed.**
  It costs minutes and, on a large tree, returns directories the user has to
  think about. Search the project, then the one referenced path.
- **A directory you created this session is yours to clean up** — and deleting
  it needs no permission, because you own it. State plainly what was created and
  that it is gone.

## Read the thing before you accept the premise

When a request carries a factual premise ("this is the only copy", "the data
isn't in the project", "the file is at X"), verify it before acting on it. This
session's premise came from the user and was wrong twice over: the file was
archived outside the project AND the project's own data folder held a better,
larger version of the same research.

- Verify with a real check, and report what the check found — including when
  the check contradicts the premise. Correcting the premise is more useful than
  complying with it.
- Prefer the artifact inside the project root over a duplicate outside it, even
  when the outside one is what was named. Say which you used and why.

## Scope discipline

- Stop at the defined deliverable set (STOP gate); never extend into the
next phase uninvited.
- When two instructions conflict on creative direction, halt and ask with
both options stated — do not guess which one wins.
- When the strategy is declared FAIL, stop its renders immediately instead
of finishing doomed work.
- **Deliver one flat folder, not a nested tree, when the recipient is a person
  or a system with no nested-view UI.** A folder-per-topic layout is good
  engineering and unusable as a handoff. One directory, an index file naming
  each artifact and its priority, and the minimum viable subset called out
  explicitly ("if you read only five files, these").
