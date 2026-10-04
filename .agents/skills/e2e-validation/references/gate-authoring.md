# Authoring inter-stage gates

Depth for the "when you are the one writing the gate" section of SKILL.md, plus
the two recipes that keep recurring when a pipeline's stages disagree with each
other rather than with themselves.

## The self-test must be able to say no

Encode the cases that MUST fail and run them before the gate judges anything.
Four defects make a self-test that looks armed but cannot fire:

1. **Label vs number comparison.** If the case table declares the expected check
   as a number (`check_esp = 3`) and the failure message carries a string prefix
   (`"[check3] …"`), the membership test compares `3` against `"check3"` and
   never matches: every negative case reports as a failure while the gate is
   behaving exactly right. The natural reaction — weakening the gate — is the
   wrong move. Normalize both sides to one form first, and re-read the report
   line by line before believing a mass failure.
2. **Derive the count, never hardcode it.** Print `len(casos)/len(casos)`. A
   literal `10/10` survives adding or removing cases and becomes a false claim
   about coverage.
3. **Inject the root.** If the evaluation function anchors every path to the
   project root, negative cases cannot build fixtures in a temp dir and the
   whole suite collapses onto the happy path. Make the root a parameter with the
   project as default.
4. **A case that cannot execute is decoration.** A fixture pointing at a
   genuinely-retired version will legitimately PASS; it is not testing the
   "unknown source" branch. Make the negative fixture point at something that
   is neither the official version nor a retired one.

## Writing the gate's own text

Failures must name the artifact, the field, and the two values that disagree —
"plan built on V1, official is V2, hashes `628cd7…` vs `9e05d5…`". A gate that
says "inconsistency detected" pushes the diagnosis back to the operator and has
saved nobody a minute. Report the comparison inputs; they are the evidence.

## Recipe: two stages disagree about the same attribute

When two modules compute the same thing by different methods and only one
reaches the consumer:

1. Run BOTH on the same real artifact and tabulate: item count, total, and how
   many violate the threshold. The gap between the two rows is the finding —
   "5 of 6" against "4 of 10" says which one is closer, which a prose claim
   cannot.
2. Check whether the *consumer* actually receives the better one. Often the
   accurate computation exists, emits machine-readable output, and has zero
   callers — grep for callers before assuming it is wired.
3. Do not reconcile them by editing the better one to match the worse. Write the
   policy down as **declared, not applied**, with the reason applying it is a
   multi-contract change, and name the cost that reordering would introduce.

## Recipe: adjacent stages do not share a vocabulary

Before building any bridge, measure the intersection between the producer's
vocabulary and the consumer's enum, and report counts: `n` names on each side
and the intersection (frequently empty). An empty intersection is the finding;
"they may disagree" is not.

- **The translation table is a DATA artifact**, not a constant in the bridge
  code. A table in source is unauditable and the only way to change an
  equivalence is to edit code.
- **The bridge READS the table and aborts when it is missing.** An in-code
  fallback copy is a second source of truth that will diverge without anyone
  noticing — the bridge would keep passing while disagreeing with the catalog
  nobody reads.
- **A value with no entry is REJECTED with a reason.** Substituting "the closest
  match" is an editorial decision disguised as a translation.
- **Declare the fields you do not propagate**, each with its downstream consumer
  and why. A field that vanishes silently is indistinguishable from a field that
  was lost, and the next engine cannot tell which happened.
- If one stage writes free text where the next expects a value (a duration
  embedded in a string), the parse rule belongs in the same data artifact and
  must be declared as parsed — never inferred.

## Recipe: which version of the source is authoritative

When several versions of one source artifact exist and derived artifacts were
built across versions, declare the official one and make a gate prove it.

- **Compare by CONTENT HASH.** Two different paths holding identical bytes are
  the same source; the same path holding different bytes is not. Comparing
  filenames or paths reports SYNC for different content and FAIL for a rename.
- **Absence of a version declaration is not exemption.** An artifact that
  declares nothing is an orphan: it blocks until it declares. This is the rule
  that catches the real gap — a stage that receives the source as an argument
  and never records it.
- **Staleness cascades transitively.** A derivative of a stale derivative is
  stale. Verify it by chaining each declared source, not by trusting a
  hand-written state field, or the cascade is only as good as the field.
- **Follow declared indirection.** An artifact that points at another artifact
  which carries the version IS traceable; so is a *directory* artifact whose
  member files declare it. Read what is there instead of demanding the field on
  the artifact itself.
- **Retire, never delete.** Keep superseded versions on disk marked stale with
  the reason. Deleting them lets the same divergence reappear with no record of
  having been solved once.
- State the scope limit: a per-episode lock leaves other episodes unprotected by
  absence, and that is worth saying out loud rather than implying coverage.

## Editing whitespace-sensitive regions

Code inside a function, nested JSON, YAML — regions where leading whitespace is
semantic. `patch` preserves the indentation you supply rather than the file's,
so a replacement written at the wrong depth lands as a syntactically valid but
wrong-level block, and a second patch on top of it compounds the drift.

- Read the exact current lines before replacing, and replace the **whole block**,
  not a fragment of it.
- When a region has already drifted through one bad patch, stop patching it:
  rewrite the block by line index with a script, then parse-check the file.
  Repeated patch attempts on misaligned indentation converge on nothing.
- Gate it: after editing a Python or JSON file, run a syntax/parse check in the
  same turn. Several wasted round-trips in this class of work come from
  discovering the indentation error on the next unrelated run.