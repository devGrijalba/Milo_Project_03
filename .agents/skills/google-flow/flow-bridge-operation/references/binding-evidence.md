# Binding evidence: observing identity instead of asserting it

The task: prove that a specific reference image is the one that actually
travelled into the generation. This is a *measurement* problem, not a
feature flag — and the whole file exists because the cheap version of it
(the producer says "I sent it") is not a measurement at all.

## The layer model

Evidence is graded by where it was observed. The layer is a property of the
**observation point**, never of the confidence of whoever reports it.

| Layer | Observation point | Trust |
|---|---|---|
| `L1_DOM` | what is visible on screen | diagnostic only — never authorises |
| `L2_APPLICATION` | what the app's own code confirms it did | medium |
| `L3_NETWORK` | the bytes handed to `fetch` / `XMLHttpRequest.send` / `WebSocket.send` | high |
| `L4_BACKEND` | an entity the backend independently accepted and returned an id for | highest |

## The rule that matters most

> **The source that asserts "I sent it" cannot be the proof that it left.**

A process that builds a payload, logs `layer: L3`, then calls `send()` has
observed only its own intent. That is `L2` wearing an L3 label. The extension
signing its own network evidence is a closed loop — the verifier and the
verifier's input are the same agent.

**L3 requires interception at the transport boundary.** Wrap the real send
and inspect the actual payload:

```js
const origSend = WebSocket.prototype.send;
WebSocket.prototype.send = function (data) {
  // inspect `data` here — this is the last point where "about to send"
  // becomes "did send"
  return origSend.call(this, data);
};
```

Same for `fetch` and `XMLHttpRequest.prototype.send`. If the channel is not
HTTP/WebSocket (an app-internal bus, a postMessage to another context), then
there is no L3 available on that path — say so and stop at L2.

**Never declare a layer the run did not earn.** Declaring `L4` because "the
job completed" is re-stating a `L2` observation one level up: the same
cycle produced both facts. `L4` needs an id the backend minted, not a status
the same caller reported.

## A passing synthetic test proves the shape, never the truth

Feeding the classifier a hand-built evidence object and getting `VERIFIED`
demonstrates only that the classifier accepts that shape. It is
indistinguishable from tuning the input to the answer — and it is the most
tempting way to accidentally disable a gate you were trying to test.

Ask what could make the synthetic pass while reality fails:

- the classifier accepted a field the real producer never sets
- the field name matched but the value is derived, not observed
- the correlation is ordered but not real (see below)

A synthetic suite earns its keep as a **regression** suite: assert the
*negative* cases still fail (wrong id → `MISMATCH`, no id → `PARTIAL`,
name-only → `PARTIAL`). Those prove the gate is not loose. A synthetic
`VERIFIED` proves nothing beyond formatting.

## Temporal correlation is not a timestamp

Sequence numbers prove ordering, not identity. The failure they exist to
prevent: the user selects asset A, switches to B, the UI keeps showing A
while the backend processes B. Ordering alone passes that test.

Correlation is valid only when the observed id at the network boundary is
the **same id** that later appears in the backend's response. Same id, plus
ordering, plus independence of both endpoints.

## Producer/consumer field contracts drift silently

Both real defects in this class were the same shape: the producer emitted a
field, the consumer read a *different path* for it, and evidence degraded to
`PARTIAL` with no error anywhere.

- event sequence emitted at top level, read from inside a nested object
- layer emitted as `L3_NETWORK`, matched with `=== 'L3'`

Neither throws. Both produce a plausible-looking downgrade that reads as
"insufficient evidence" rather than "mismatch in the contract".

Defend explicitly:

- Compare layer names by **prefix**, not equality (`L3_NETWORK` is `L3`).
- Assert the exact path and vocabulary on both sides, with a test that
  carries a real-shaped payload from the real producer.
- When evidence degrades, first suspect the contract, then the evidence.

## Event handlers that fire per state change

A completion resolver invoked on **every** state event (`queued`, `running`,
`completed`) will, if it reads-and-deletes its correlation mapping, destroy
the mapping on the *first* event and report "no mapping" for the real close.

```
queued    → deletes the only copy of flowId → bridgeId
running   → nothing to translate
completed → no evidence, forever
```

Two fixes, both required:

1. **Guard on terminal state first**, before any read, log, or delete. Only
   `completed`/`cancelled`/`error` may close a job.
2. **Translate before you clean.** Emit the completion message first, then
   drop the mapping. Cleaning first means a lost send is unrecoverable;
   the reverse worst case is a harmless stale entry.

Signature to watch for in logs: a mapper that reports present on the first
event and absent on every event after, with the job still running.

## Identity translation between namespaces is a single-use table

The worker and the flow app mint **different ids** for the same job. The
mapping table is the only thing that translates them, and it is consumed on
use. A fallback that substitutes one namespace for the other keeps events
flowing while destroying correlation — and it announces itself in the
message (`evidence_source: 'flow_fallback'`). Treat that marker as a defect
report, not a resilience win.

The durable fix is upstream: make the mapping survive the service worker's
lifecycle (see below), and keep the fallback instrumented so its use is
visible.

## Manifest V3 service workers drop memory, and sometimes the table

A MV3 service worker is not a process. Chrome suspends it when idle and
recreates it, so module-level variables reset. Anything that must outlive a
few seconds of idle goes in `chrome.storage.local` (or `.session`) with
explicit recovery.

Do not guess which failure you have — read the storage directly, from the
extension's own `Local Extension Settings/<id>/` LevelDB, before changing
code. The log tells you the symptom (`mapping absent`); only the persisted
bytes tell you the state.

Distinguishing the two, from the log signature alone:

| Signature | Cause |
|---|---|
| present on event 1, present on event 2, absent on event 3 | handler deleted it — not a lifecycle loss |
| absent from event 1 onward | the write never landed, or a different context wrote |

A lifecycle loss would show `absent` immediately on the second event, not
after two healthy ones. Reach for the handler before the platform.

## A cross-language hash can never be verified by the other language

`json.dumps(data, sort_keys=True)` in Python and `JSON.stringify(data)` in
Node order keys similarly and produce **different bytes**: separators,
escaping of non-ASCII, and float formatting all differ. A hash recomputed in
JS against a hash produced by Python is a check that can only ever fail.

Pick one owner for every hash and let it be the only authority: the
revalidating side asks the owner, and compares the owner's answer to itself.
Recomputing in a second language is not verification, it is a coin flip with
extra steps.

## Cross-language checks also fail on names, not just values

A `KeyError` on a field you expected means the field moved between the
section that reports it and the section that consumes it — check which
nested block actually carries it before assuming the value is missing.
Silent `None` on a status/score field usually means you parsed an older
output shape, not that the value is null.

## The honest ceiling

Without an independent network/backend observer there is no demonstrable
L3/L4. In that state the correct verdict is `PARTIAL`/`UNVERIFIED` **with
the reason attached**, and the limitation gets recorded as a known property
of the system rather than chased as a defect.

`PARTIAL` is a legitimate terminal answer, not a failure to report upward.
The alternative — a `VERIFIED` produced from self-asserted evidence — is
worse than no binding at all, because it licenses every later generation on
a false premise.

## Reporting

Every resolution reports **separately**:

```
generation:   SUCCESS | FAILED          ← did Flow produce
delivery:     SUCCESS | FAILED          ← did the files arrive
resolution:   job_done | file_watch | timeout | error   ← how the job closed
binding:      VERIFIED | PARTIAL | UNVERIFIED | MISMATCH + reason
```

One `state: N` code collapses these and makes "Flow produced nothing" look
identical to "we cannot prove identity". The layered form answers "which
layer failed" in one glance, and it is what turns a night of failed
experiments into a single named blocker.