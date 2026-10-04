# Designing a pre-generation barrier

A validator that someone must remember to run is documentation. A barrier runs
unconditionally before the quota is spent and aborts on failure. This is the
design, so a future session can build one instead of rediscovering it.

## The five checks, in order

Stop at the first failure. Each one closes a different hole:

1. **The canon index exists.** A production package that references assets by
   path + hash declares what is canonical. Without it, nothing downstream can
   tell whether the run is using the approved assets.
2. **Every declared hash still matches.** Re-hash each referenced file. A
   mismatch means the asset changed and must be re-audited; the package is no
   longer valid. This converts silent modification into a detectable event.
3. **Attribute contracts hold.** Delegate to the validator's exported function —
   never a second implementation. Remember the tri-state rule: missing `verified`
   blocks, measured-present blocks, individual unmeasured traits warn.
4. **The plate for this framing is generable.** Resolve the framing through the
   catalog to its plate, then look up the plate's audited classification. This is
   the check that prevents feeding a burned-text plate into a generation. Also
   consider the separate `environment_anchor` / `environment_inspiration`
   distinction — those are different questions.
5. **Nothing superseded is in the generative canon.** Historical evidence is
   kept, but must be marked so it can never be sent. The check states which
   files are excluded, so the exclusion is visible rather than assumed.

## Wiring it in

Spawn the gate as a **separate process**:

```js
const gate = spawnSync(process.execPath,
  [join(ROOT, 'tools', 'pre-generation-gate.js'), MANIFEST],
  { cwd: ROOT, encoding: 'utf-8' });
process.stdout.write(gate.stdout ?? '');
if (gate.status !== 0) {
  console.log('\nABORTED por el gate. NO se ha enviado nada y NO se ha gastado cuota.');
  process.exit(1);
}
```

Two reasons it must be spawned, not imported:

- An import that throws is indistinguishable from a gate that passed, and the
  generation proceeds on a check that never ran.
- Exit codes across a process boundary are a contract you can rely on; a thrown
  exception inside the same process can be swallowed by a broad `catch` upstream.

Run it in **both** modes. Informational on dry run, blocking on authorized. The
point is that the authorized path has no branch that skips it.

## Proving the barrier blocks

A gate that has only ever returned PASS is untested. Verify it end to end:

1. Back up the real manifest.
2. Repoint it at a known-invalid target (a plate already audited as unusable).
3. Run the **authorized** path.
4. Confirm all three: the message names the true reason, exit code is non-zero,
   and the download count is **unchanged**.
5. Restore the manifest, re-hash every reference, confirm no temp files remain.

An unchanged download count is the only proof quota was not spent. Assert on it.

## Failure modes of the barrier itself

| Symptom | Cause | Rule |
|---|---|---|
| Exits 0, prints nothing | ESM CLI guard failed (Windows drive-letter case) | use `pathToFileURL(process.argv[1]).href === import.meta.url`, then verify the output actually appears |
| Rejects every input | tri-state collapsed: unmeasured treated as violated | unmeasured warns, only measured-present blocks |
| Says "no plate in the lock" for a real plate | test used an invented id | enumerate ids from the lock; make the message trustworthy |
| Approved an asset with no `verified` | approved by default when the field was missing | missing `verified` blocks |

The silent-exit case is the dangerous one: exit 0 with no output reads as
success to every wrapper script upstream.

## Changing the rules revokes every standing authorization

A package validated under ruleset `abc…` is **not** validated when the rules
are now `def…`. The gate must compare the ruleset hash recorded in the
artifact against the current one and refuse, naming both:

```
BLOCKED: el QA vigente no autoriza este paquete.
  status guardado: PASS | QA vigente: PASS
  STALE_VALIDATION: validado con ruleset b17e50038311… actual 02b4a5ddc946…
```

This looks like a bug — both sides say PASS — and it is the gate working. Any
edit to the rule definitions (a new hard fail, a reworded constraint, a new
required field) invalidates every prior PASS. Design the check so a
score-based PASS cannot survive a rules change.

Revalidating is cheap and is the correct response to the block: re-run the
current engine, rewrite the recorded `ruleset_hash`/`validated_at` alongside
`result`/`score` in the artifact, then re-run the gate. Do not relax the
comparison to make a stale package pass — that is the one change that turns
the gate into decoration.

A score of 100 does not override a hard fail, and a current PASS does not
retroactively bless an artifact written under old rules. Score and
authorization are separate fields, and the gate reads both.

## Reporting shape

Print per-check lines with `OK` / `FALLA`, the resolved scene, and a single
verdict line. On failure the message must state the concrete reason and the
consequence (`NO generar`), because this text is what a person reads to decide
what to fix. Never print a summary that requires re-running with another flag to
understand.
