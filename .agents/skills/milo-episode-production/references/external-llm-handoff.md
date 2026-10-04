# External LLM handoff — delivering the design master to third-party models

When the user runs the episode design master in external chat LLMs (one file,
several models, results pasted back for Hermes-side audit), two mechanics decide
whether the models obey constrained-delivery modes. Both failed in production
before being encoded here.

## 1. Attachments are reference, chat text is orders

A model receiving the master as an attached file treats it as background
material and under-weights in-file gates and stop conditions — the binding
instruction must ALSO travel in the chat message body. Rule: the mode/trigger
line always goes in the message text; the file rides along as the spec.
Additionally, line 1 of the deliverable .md must declare itself the principal
instruction when received as an attachment (not reference), and fence any
operator-only sections (trigger catalogs, usage notes) as human-only so the
model does not self-trigger the wrong mode from inside the file.

## 2. Mode gates go first, never last

A conditional gate buried at the end of a prompt loses to an autonomous
delivery instruction at the top — the model anchors on the first order and
treats the late gate as optional. Any mode that restricts output (competition
gates, stop-after-X, format locks) belongs in a gate block BEFORE §0, stating
it overrides everything below. Appending 'UPDATE: actually stop after…' under
an existing full-delivery order does not work; move the gate, do not annotate
around it.

## 3. Prove which copy the model received before blaming wording

When a model disobeys, hash (md5) the on-disk master against the user's local
copy before rewriting a single rule. Twice the delivered file turned out to be
a stale upload predating the hardening — no wording change can fix a copy that
never contained it. Paste-back content that matches neither on-disk copy is
stale by definition; re-upload current + trigger-in-message closes the variable.
