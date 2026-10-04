# Web-app release E2E — prove the UI works in a real browser

API-green is not UI-green. Service and HTTP-level tests cannot catch dead
client interactivity (unhydrated pages, blocked scripts, broken redirects).
Every release gate needs at least one real-browser pass over the critical
auth-gated flow, separate from the API suite.

## 1. Browser login proof (Playwright/Chromium)

Drive a real browser; assert the full chain, not just the POST status:

- Attach three listeners before navigating: `console` (flag CSP violations
  as their own category), `pageerror` (uncaught exceptions), `request`/
  `requestfailed` (confirm the auth POST actually fires; catch blocked or
  failed resource loads).
- Fill credentials, click submit, await the post-login URL.
- Assert: redirect happened, session cookie exists, home shows the identity
  via `innerText` — never `textContent`, which includes script payloads and
  produces false matches.
- Assert zero CSP errors and zero relevant JS errors (filter out known
  dev-only noise such as React `unsafe-eval` warnings, explicitly).

## 2. Server-log diagnostic for dead forms

When a form 'does nothing', check the server access log BEFORE blaming
credentials: clicks arriving as `GET /login?` with NO corresponding auth
POST means the client handler never ran (dead hydration), not a wrong
password. A wrong password always leaves a 401 POST in the log.

## 3. Next.js + CSP hydration rule

`script-src 'self'` WITHOUT `'unsafe-inline'` blocks Next.js's own inline
bootstrap scripts (`__next_f`, `__next_r`) → ZERO hydration on every page,
silent in production builds. Symptoms: native form submits (bare `?` URLs),
stuck loading placeholders, no console errors a user would notice.

- Fix: add `'unsafe-inline'` to `script-src` and document WHY inline; keep
  React auto-escaping plus server-side output escaping as the stated XSS
  defense, with tests pinning it.
- Never allowlist the bootstrap by hash — its contents change per request.
- Record a nonce/hash-based CSP as explicit follow-up debt; do not block
  the release on it once the escape tests hold.

## 4. Login UX must distinguish 401 from 429

A login form reporting every failure as 'invalid credentials' turns a
rate-limit lockout into an undiagnosable retry loop (each retry extends the
lockout while the message blames the password). Surface 429 with its own
message telling the user to wait. When guiding a HUMAN through a suspected
lockout: forbid retries for a full window (2 min), then one careful manual
attempt with autofill disabled — rapid re-clicking renews the block
indefinitely, so 'try again' is the worst advice.

## 5. Scratch E2E/debug scripts vs the production build

Keep throwaway browser/debug scripts OUT of the build's tsconfig `include`
(or delete them before `next build`): one scratch file with a type error
fails the production type-check and blocks the release.

## 6. Rate-limited systems

See `validation-recipes.md` §9 (unique client identity per run) — not
repeated here. Browser E2E runs need it too: repeated logins from one IP
trip login rate limits and masquerade as product failures.
