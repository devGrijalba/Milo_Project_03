---
name: web-scraping
category: software-development
description: Scrape data from web applications using Chrome DevTools MCP — reverse-engineer SPAs, extract structured data, handle pagination, auth, and custom WebSocket binary protocols.
---

# Web Scraping with Chrome DevTools MCP

Use the Chrome DevTools MCP tools to extract data from web applications (SPAs, server-rendered apps, dashboards) that don't offer public APIs.

## When to use this skill

- Data is rendered client-side in a SPA (React, Vue, Angular)
- The site uses auth/sessions (you're already logged in via browser)
- Static `web_extract` fails because content is loaded dynamically
- You need structured data (JSON), not just rendered text
- The target has pagination, infinite scroll, or lazy loading

## General workflow

### 1. Reconnaissance — understand the tech stack

First load the page and inspect:

```
mcp_chrome_devtools_new_page(url="https://example.com/data")
mcp_chrome_devtools_take_snapshot()
mcp_chrome_devtools_list_network_requests()
```

Key patterns to look for in network requests:
- **Next.js**: look for `/_next/data/{buildId}/...json` endpoints
- **GraphQL**: look for `/graphql` POST requests with `__typename` in responses
- **REST API**: look for JSON responses under `/api/`
- **SSR data**: check for `__NEXT_DATA__` script tag in HTML

### 2. Extract SSR payload (fast path)

For **Next.js** sites, the initial page data is embedded:

```javascript
mcp_chrome_devtools_evaluate_script(
  function="() => document.getElementById('__NEXT_DATA__').textContent"
)
```

This returns all props from `getServerSideProps` / `getStaticProps`. Parse it for:
- `pageProps.postTrees` or similar item arrays
- `pageProps.total` for total count
- `pageProps.page` for current page

**Caveat**: `__NEXT_DATA__` is SSR-only. Client-side navigation (pagination, filters) updates the DOM but NOT the script tag.

### 3. Find the data endpoint

For subsequent pages / filtered views, find the actual API:

1. Navigate/interact (click page 2, apply a filter) via `mcp_chrome_devtools_click` / `mcp_chrome_devtools_evaluate_script` 
2. Monitor new network requests: `mcp_chrome_devtools_list_network_requests(resourceTypes=["fetch","xhr"])`
3. Look for the JSON endpoint pattern

**Next.js pattern**: `GET /_next/data/{buildId}/{path}.json?param1=val1&param2=val2`

The response body of this endpoint contains the same shape as `__NEXT_DATA__` but for the requested page/params.

### 4. Extract response body

Once you find the endpoint request:

```
mcp_chrome_devtools_get_network_request(reqid=N)
```

Read the `Response Body` field (may be truncated in display — use `responseFilePath` to save to disk for large payloads).

### 5. Build the full extraction plan

Determine:
- **Total records** from `total` field in first response
- **Records per page** from items array length
- **Total pages** = ceil(total / per_page)
- **Endpoint template**: the URL pattern with page number as variable
- **Query params**: `c=`, `fl=`, sort order, category filters

### 6. Parallel extraction (the fast way)

Once you have the endpoint pattern, you can call it directly via `terminal` with curl if you extract the session cookies, or via Python `requests` with the cookies/headers passed directly.

For large extractions (1000+ items), use `ThreadPoolExecutor` with 5 workers:
```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_page(session, page):
    resp = session.get(endpoint_template.format(page=page))
    return resp.json()

with ThreadPoolExecutor(max_workers=5) as ex:
    futures = {ex.submit(fetch_page, session, p): p for p in range(1, total_pages+1)}
    for f in as_completed(futures):
        results.append(f.result())
```

**auth_token caveat**: The auth cookie may be httpOnly (not readable from `document.cookie`). Extract it from a network request header instead — use `mcp_chrome_devtools_get_network_request(reqid=N)` and copy the `cookie:` header value.

**WAF/Cloudflare**: Sites behind AWS WAF require the `x-aws-waf-token` header in direct API calls, not just the cookie. Include both:
```python
headers = {
    "x-aws-waf-token": "<from browser session>",
    "User-Agent": "...",
    "Origin": "https://example.com",
    "Referer": "https://example.com/",
}
cookies = {"auth_token": "...", "aws-waf-token": "<same as header>"}
```

### 7. Handle pagination controls

Two approaches:

**A) Pagination buttons** — find them via snapshot and click:
```
// Find page buttons
mcp_chrome_devtools_evaluate_script(
  function="() => document.querySelectorAll('button').forEach(b => { if(b.textContent === '2') b.click() })"
)
```

**B) URL-based pagination** — navigate directly:
```
mcp_chrome_devtools_navigate_page(type="url", url="https://...?p=2")
```
Then extract the new `__NEXT_DATA__` or wait for client-side render.

### 8. Extract attachments/files

For content with attached files:
- File URLs typically follow CDN patterns: `https://assets.domain.com/f/{groupId}/{fileId}`
- **WARNING**: the `attachmentId` in the feed metadata is often an opaque UUID that is NOT the actual S3 file key. Direct access may return 403.
- **Look for `attachmentsData`** in individual item pages (not the list/feed view). This field contains the REAL download URLs under `read_url` / `src_read_url` — which use a different hash and typically work with auth.
- Test accessibility: if the feed gives attachment IDs, fetch one individual item page to check for `attachmentsData`, then try the `read_url` directly.
- Download via Python `requests` with the auth cookie:
  ```python
  resp = requests.get(read_url, cookies={"auth_token": "..."})
  ```
- The CDN download typically only needs `auth_token` cookie, NOT the WAF token header.
- For batch file-type analysis, fetch individual item pages in parallel (ThreadPoolExecutor, 5 workers) extracting only `attachmentsData` from each.

## WebSocket-Based SPAs

Some modern SPAs use WebSocket for ALL server communication instead of HTTP REST. The browser connects to a WS endpoint on page load and sends/receives binary or JSON messages for auth, data fetching, and updates.

### Detecting WebSocket Communication

1. **Network tab**: `mcp_chrome_devtools_list_network_requests(resourceTypes=["websocket"])` shows WS connections
2. **Look for WS libraries in HTML source**: `hxws`, `socket.io`, `SockJS`, `ws` — often loaded as blocking `<script>` in `<head>`
3. **Config patterns**: Search for `wsURL`, `websocket`, `wss://` in the HTML payload or config files
4. **No REST endpoints**: If you find zero `/api/` fetch/XHR requests but the page functions, it's WS-only

### Reverse-Engineering Custom Binary WebSocket Protocols

When the SPA uses a custom binary protocol (not JSON over WS), you must reverse-engineer from the JS bundles:

#### Step 1: Find command/subcommand constants

Search the main JS bundle for patterns like:

```bash
# Find command enums — pattern: CMD_NAME:NUMBER
grep -oP 'MDM_[A-Z_]+:\d+' bundle.js

# Find sub-command enums
grep -oP 'SUB_[A-Z_]+:\d+' bundle.js
```

Common patterns (from real-world casino SPAs):
- Main command: `MDM_MB_LOGON:1`
- Sub-commands: `SUB_MB_LOGON_ACCOUNTS:2`, `SUB_MB_LOGON_MOBILE_EX:7`

#### Step 2: Extract packet structure

Search for where these commands are defined with field types:

```bash
# Find packet structure definitions
grep -oP 'MDM_MB_LOGON\].{100,600}' bundle.js
```

Field type patterns:
- `uint8_t`, `uint16_t`, `uint32_t`, `int64_t` — fixed-width integers
- `char16_t` — UTF-16 string with length prefix
- `utf8` — UTF-8 string
- `time_t` — Unix timestamp

Each field has `t:` (type), `k:` (key/field name), and optionally `s:` (string length) or `array:` (array length).

#### Step 3: Find the send function

```bash
# Find where the send function is called with specific commands
grep -oP 'send\(l\.MDM_[A-Z_]+,\s*l\.SUB_[A-Z_]+' bundle.js
```

This reveals the data objects being sent. Common fields:
- `moduleID`, `plazaVersion`, `deviceType` — device/platform info
- `machineID` — device fingerprint
- `accounts` — username/phone with format `{tag}00{callingCode}{phone}`
- `logonPass` — MD5(password)
- `ipAddr` — client IP
- `channelName` — traffic source
- `spreadBindID` — affiliate tracking

#### Step 4: Find response structures

The response parsers often reveal what data comes back:

```bash
# Find response handlers
grep -oP 'SUB_MB_LOGON_SUCCESS\].{100,500}' bundle.js
```

### Handling WS-Only Auth

When login happens entirely via WebSocket:

1. **The WS library matters** — Common WS libraries used in Chinese casino/gaming platforms:
   - **hxws** (`hxws-*.js`) — Binary protocol with WASM-based compression. The `.wasm` file is loaded alongside the JS.
   - **socket.io** — JSON-based protocol, easier to intercept
   - **SockJS** — Fallback-based, multi-transport

2. **You can't POST to log in** — There is no REST login endpoint. You must either:
   - Use the browser (authenticate normally) and extract the session token from WS messages
   - Re-implement the binary protocol in Python (complex — requires understanding the hxws packet structure and WASM)
   - Use Puppeteer/Playwright to automate the browser (avoids protocol reimplementation)

3. **WASM analysis approach**: When the binary protocol uses a WASM module (like hxws), the key encoding functions (`allocSendBuffer`, `getSendBufferSize`, `sendNetData`) are C++ class methods registered via **embind** at runtime — NOT direct WASM exports. Attempting to call them from Python requires running the full WASM environment with all 44+ emscripten/emval imports implemented. This is generally not feasible without a real browser runtime. Focus efforts on browser automation or token extraction instead.

4. **Token extraction**: After successful WS login, the token is typically stored in:
   - `localStorage` (readable via browser console)
   - A global JS variable
   - A cookie set by the server
   - Check network request headers for `Authorization` or `token` fields in subsequent HTTP calls

### Cloudflare Turnstile and Headless Browsers

Sites behind Cloudflare Turnstile (or similar WAFs) **block ALL automated tools** — no exceptions. The challenge is a client-side JS execution test that detects headless browsers via multiple fingerprint vectors (WebGL, canvas, timing, Chrome runtime features).

**Verified: every HTTP-level and headless-browser tool fails:**

| Tool | Result | Notes |
|------|--------|-------|
| `monolith` | 403 / HTML challenge page |
| `cloudscraper` | 403 / HTML challenge page |
| `curl_cffi` impersonation | 403 / HTML challenge page |
| Playwright Chromium + stealth | Stuck on challenge, never resolves |
| Playwright Firefox | Stuck on challenge, never resolves |
| Chrome DevTools MCP | Turnstile shows "Verificando..." forever |
| **SingleFile extension** | **✓ Works** | Must use a real browser with human interaction |

**See `references/cloudflare-turnstile-bypass-matrix.md` for the full test matrix.**

#### Turnstile-specific symptoms

| Symptom | Likely Cause |
|---------|-------------|
| Network requests all 200 but DOM is empty | JS challenge not completing |
| `about:blank` in JS context but accessibility tree has content | JS injection page loaded, challenge failed |
| `document.querySelectorAll('*').length` returns ~45 with challenge div only | Turnstile rendered but never resolved |
| Console shows CSP 'eval' warnings | Turnstile script partially loaded, interaction blocked |
| Turnstile checkbox visible but clicking does nothing | Bot detection, challenge never completes |

#### The ONLY reliable solutions for Turnstile sites

**Option A: SingleFile browser extension (recommended for end users)**

Install [SingleFile](https://chrome.google.com/webstore/detail/singlefile/mpiodijhokgodhhofbcjdecpffjipkle) in Chrome/Edge, open the target URL, complete the Turnstile challenge, click the SingleFile icon (📄). Saves one `.html` with ALL assets embedded.

**Option B: CDP Remote Debugging (for automated capture)**

When you need programmatic access to a page behind Cloudflare, connect to the user's real desktop browser via CDP:

1. Launch Chrome/Brave with `--remote-debugging-port=9222 --remote-allow-origins=*`
2. The user navigates and passes the Turnstile challenge
3. Connect via Python `websockets` library to extract content

```python
import asyncio, json, websockets

async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
    # Get rendered HTML
    resp = await send("Runtime.evaluate", {
        "expression": "document.documentElement.outerHTML",
        "returnByValue": True
    })
    html = resp["result"]["result"]["value"]
```

For a self-contained HTML with embedded CSS and images:
1. Get `outerHTML` via `Runtime.evaluate`
2. Download CSS files via `Page.getResourceContent` and inline as `<style>`
3. Convert images to data URIs using canvas `toDataURL()` from within the browser (same-origin only)
4. Add `<base href="https://original-site.com/">` so relative URLs resolve online
5. Alternatively, use `Page.captureSnapshot` to get MHTML format (returns plain text directly)

**Key findings from real captures:**
- `cf_clearance` cookie alone is NOT enough — Cloudflare also checks TLS fingerprint (JA3). Python `requests` still gets 403 even with valid cookies.
- CSS `document.styleSheets[i].cssRules` approach captures ALL styles (including inline, dynamically injected, and cross-origin where accessible), preferred over manual `Page.getResourceContent` downloads.
- Canvas `toDataURL()` fails silently for cross-origin images (CORS) AND re-encodes as PNG (3-5x larger). Prefer `fetch()` from within the browser context (same-origin) which preserves original format.
- After inlining CSS, `<style>` tags may contain `url()` references to background images that must also be converted via `fetch()`.
- Joomla appends `#joomlaImage://local-images/...` fragments to image URLs. Always strip with `.split('#')[0]` before fetching.
- **file:// protocol blocks external resources**: Even with `<base href="...">`, opening a local .html file from the filesystem blocks loading external CSS/JS/images (CORS). Use a local HTTP server: `python -m http.server 8080` and access via `http://localhost:8080/`.
- WebSocket message size: `Runtime.evaluate` responses for pages with data URIs can exceed 30 MB. Set `max_size=100*1024*1024` on the websocket connection.
- MHTML from `Page.captureSnapshot` is **plain text** in modern Chrome, NOT base64 encoded. Just save the response string directly as `.mhtml`.
- JS-heavy sites (Joomla, SPAs) will NOT look identical offline without JS files executing. The DOM captured is the post-JS state but without JS files, interactive elements (sliders, menus, carousels) won't work.
- **file:// protocol blocks external resources**: Even with `<base href="...">`, opening a local .html file from the filesystem blocks loading external CSS/JS/images (CORS). Use a local HTTP server: `python -m http.server 8080` and access via `http://localhost:8080/`.
- **Joomla image fragments**: Joomla appends `#joomlaImage://local-images/...` fragments to image URLs. Always strip with `.split('#')[0]` before fetching.
- **WebSocket message size**: `Runtime.evaluate` responses for pages with data URIs can exceed 30 MB. Set `max_size=100*1024*1024` on the websocket connection.

See `references/cloudflare-cdp-bypass.md` for full CDP workflow, code examples, and pitfalls.

**Do NOT waste time** trying wget, httrack, monolith, cloudscraper, curl_cffi, Playwright, undetected_chromedriver, or cookie injection for Turnstile sites. The challenge requires real JS execution in a non-headless browser environment with a proper TLS fingerprint.

#### For non-Turnstile WAFs (AWS WAF, Cloudflare under较轻配置)

If the site is behind a lighter WAF (not Turnstile), these may help:

1. **Residential proxies** — Browserbase or similar services
2. **Browser profile** — Persisted Chrome profile with real browsing history
3. **User-agent rotation** — Match real browser fingerprints
4. **Viewport + touch** — Emulate mobile device for less aggressive challenges
5. **Cookie injection** — Valid session cookie from a real browser

### TikTok scraping: dedicated CDP browser + hydration-JSON pattern

- **Launch automation Chrome minimized** with a dedicated user-data-dir (e.g. `$LOCALAPPDATA/hermes/chrome-9222`), never the user's regular profile: `powershell -Command "Start-Process 'C:/Program Files/Google/Chrome/Application/chrome.exe' -ArgumentList '--remote-debugging-port=9222','--remote-allow-origins=*','--user-data-dir=...','--no-first-run','--start-minimized','https://tiktok.com/' -PassThru -WindowStyle Minimized"`. Without `--remote-allow-origins=*` the websocket to `webSocketDebuggerUrl` fails with 403 'Rejected an incoming WebSocket'.
- **Search/list view**: navigate the automation tab to `https://www.tiktok.com/search?q=<term>`, sleep ~9s + scroll 1–2x, collect `a[href*="/video/"]` (dedupe by ID, grab nearest-container `innerText` for like counts). Plain DOM — a bare `websocket`-to-CDP Python script suffices, no Playwright.
- **Detail extraction — navigate the SAME main tab, poll for hydration; never one new tab per video.** Fresh tabs repeatedly fail hydration (`nojson`/`noitem`) and dead tabs pile up (9 at once in a real run). `Page.navigate` to `tiktok.com/@x/video/<id>`, then poll `Runtime.evaluate` every ~4s (≤12 tries): a fixed `sleep(7)` reads a half-hydrated page.
- **Parse the hydration JSON, not the DOM**: `__UNIVERSAL_DATA_FOR_REHYDRATION__` → `__DEFAULT_SCOPE__` → key is currently `webapp.video-detail` (lowercase; locate dynamically via `.toLowerCase().includes('video-detail')` — TikTok renames scope keys without notice). Yields `author.uniqueId`, `stats.playCount/diggCount/commentCount/shareCount`, `video.duration`, `video.subtitleInfos`.
- **Transcripts come free**: take the `subtitleInfos` entry with `Format == 'webvtt'`, download via curl with `-H "Referer: https://www.tiktok.com/"` — real timestamped WebVTT, no ASR step.
- For engagement math weight comments+shares above likes: `(likes + 3*comments + 5*shares)/plays`; short-video rates are ~5–15%, so verify decimal placement against a known video before reporting.

### Empty DOM + Populated Accessibility Tree

This phenomenon occurs when the page loads but the JavaScript fails to execute (anti-bot, CSP, or JS error). The browser's accessibility tree may show **stale content from a previous successful render** or from the SSR fallback HTML.

**What it actually means:**
- The SSR HTML was parsed by the accessibility engine
- But the Vue/React app failed to hydrate
- Any JS-driven DOM will be empty
- You cannot extract data via `document.querySelector` or `evaluate_script`
- The last successful snapshot may show content that's no longer live

**Verification:** Check `document.documentElement.outerHTML` — if it's `<html><head></head><body></body></html>`, the JS didn't run.

**Workaround:** Use `mcp_chrome_devtools_list_network_requests` to see what actually loaded (the HTTP responses prove the server delivered content), then extract data at the network level instead of the DOM level.

## Anti-Bot Automation Bypass

Some sites deploy client-side anti-bot libraries that actively block browser automation (Playwright, Puppeteer, Selenium). The most common encountered on Asian gaming/casino platforms is **disable-devtool by theajack**.

### Recognizing disable-devtool

Signs in the JS bundle:
- A `setTimeout` with `window.location.href` redirect to `"about:blank"` or `"https://theajack.github.io/disable-devtool/404.html"`
- Repeating `console.log` + `console.clear` + `console.table` patterns (polling loop detecting DevTools)
- Code referencing `ondevtoolopen`, `ondevtoolclose`, `ondevtoolchange` callbacks
- The `St()` function that checks `window.jsBridge || window.Native?.getMyDeviceId()` (native app bridge check)

### Effect on automation

When disable-devtool detects automation, it:
1. Calls `window.open("about:blank", "_self")` — redirects the current page to blank
2. Calls `window.close()` — attempts to close the window
3. Optionally redirects to the ajack 404 page as fallback

Result: `browser.current_url` returns `about:blank`, DOM is empty, but network requests all succeeded (200s).

### Bypass strategy: Playwright Route Interception + Init Script

**Step 1 — Intercept the main JS bundle and patch the detection code:**

```python
async def intercept_js(route):
    url = route.request.url
    if "diLS-A9T.js" in url or "main" in url:
        response = await route.fetch()
        body = await response.text()
        
        # Patch the about:blank redirect
        body = body.replace(
            'window.location.href=w.timeOutUrl||"https://theajack.github.io/disable-devtool/404.html"',
            'void(0) /* patched */'
        )
        # Patch window.open("about:blank","_self") 
        body = body.replace(
            'window.open("about:blank","_self")',
            '({location:{href:""}})'
        )
        # Patch window.close()
        body = body.replace(
            'window.close()',
            'void(0)'
        )
        # Patch the native bridge check
        body = body.replace(
            'St=()=>{var e;return window.jsBridge||((e=window.Native)==null?void 0:e.getMyDeviceId)}',
            'St=()=>true'
        )
        
        await route.fulfill(
            response=response,
            body=body,
            headers={**response.headers, 'content-type': 'application/javascript'}
        )
    else:
        await route.continue_()

await page.route("**/*.js", intercept_js)
```

**Step 2 — Also inject an init script to override window.open/close:**

```python
await page.add_init_script("""
    const originalOpen = window.open;
    window.open = function(url, target, features) {
        if (url === 'about:blank' || !url) {
            return { location: { href: '' } };
        }
        return originalOpen.call(window, url, target, features);
    };
    window.close = function() {};
""")
```

**Step 3 — Then navigate:**

```python
await page.goto(url, wait_until="domcontentloaded", timeout=60000)
```

**Note**: This strategy may still fail because disable-devtool uses timing-based detection (console.log/clear cycle timing) that Playwright's CDP instrumentation alters even when JS is patched. The library detects DevTools by measuring the time difference between `console.log` and `console.clear` calls — automation adds latency that reveals instrumentation.

### Alternative: CDP Remote Debugging (Undetectable by disable-devtool)

When route interception + init script fail (common with timing-based disable-devtool), launch Chrome with `--remote-debugging-port` and connect via CDP WebSocket directly. The disable-devtool library **cannot detect CDP connections** — it only monitors F12 DevTools UI via window size, debugger timing, and console.log/clear cycle timing.

#### Launch Chrome with CDP

```python
import subprocess
import time

chrome_proc = subprocess.Popen([
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    '--remote-debugging-port=9222',
    '--no-first-run',
    '--disable-blink-features=AutomationControlled',
    'https://target-site.com'
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
time.sleep(5)
```

#### Extract data via CDP WebSocket

```python
import urllib.request, json, websockets

# Get tab WebSocket URL
resp = urllib.request.urlopen('http://127.0.0.1:9222/json')
tabs = json.loads(resp.read())
tab = next(t for t in tabs if 'target' in t.get('url',''))

async with websockets.connect(tab['webSocketDebuggerUrl']) as ws:
    # Get cookies
    await ws.send(json.dumps({"id": 1, "method": "Network.getCookies"}))
    resp = await ws.recv()
    cookies = json.loads(resp)['result']['cookies']
    
    # Get localStorage (useful for WS-only auth)
    await ws.send(json.dumps({"id": 2, "method": "Runtime.evaluate", "params": {
        "expression": "JSON.stringify(window.localStorage)",
        "returnByValue": True
    }}))
    resp = await ws.recv()
    ls = json.loads(resp)['result']['result']['value']
```

The CDP approach also works for sites where the user is already logged in but disable-devtool blocks inspection — launch Chrome pointing at the same user data directory, navigate, and extract.

See the `chrome-devtools-cookie-extraction` skill for the full CDP-based extraction workflow.

### Alternative: undetected_chromedriver

When Playwright fails, try `undetected-chromedriver` (Python package):

```bash
pip install undetected-chromedriver
```

```python
import undetected_chromedriver as uc
driver = uc.Chrome(headless=True, use_subprocess=True)
driver.get(url)
```

**Caveat**: ChromeDriver version must match Chrome version exactly. Mismatch causes `session not created: This version of ChromeDriver only supports Chrome version X`.

### Alternative: Native bridge mocking for mobile-web apps

Some casino SPAs have a dedicated `St()` function that checks if the page is running inside a native mobile app WebView. When running in a browser (not native), these functions redirect to `about:blank`.

Patch target in JS:
```javascript
// Original:
St=()=>{var e;return window.jsBridge||((e=window.Native)==null?void 0:e.getMyDeviceId)}

// Patched to:
St=()=>true
```

This alone doesn't bypass disable-devtool — it only bypasses the native-app check. Both must be patched.

### Decision tree for automation approach

When facing a site with heavy anti-bot:

1. **Direct API/WebSocket first** — If you can understand the protocol from the JS bundles, communicate directly (no browser needed). For WS-only sites with WASM-encoded binary protocols (hxws), key encoding functions (`allocSendBuffer`, `sendNetData`, `getSendBufferSize`) are C++ class methods registered via **embind** at runtime — NOT direct WASM exports. They cannot be called from Python without running the full hxws environment with all 44+ emscripten/emval imports. Focus on browser session extraction instead.
2. **Route interception** — If the protocol is too complex (WASM binary encoding), try Playwright with JS patching. **Expect possible failure** if the site uses timing-based disable-devtool detection (console.log/clear cycle timing).
3. **CDP Remote Debugging** — When Playwright fails, launch Chrome with `--remote-debugging-port` and connect via CDP WebSocket. This is **undetectable** by disable-devtool (it monitors F12 DevTools UI, not CDP protocol connections). Works for both cookie extraction and interacting with the page.
4. **undetected_chromedriver** — Falls back when Playwright fails (different fingerprint). **Caveat**: ChromeDriver version must match Chrome exactly. Mismatch error: `session not created: This version of ChromeDriver only supports Chrome version X`.
4. **Real browser session + filesystem extraction** — Last resort: extract session data from the user's Chrome filesystem (cookies SQLite DB, localStorage LevelDB) without using DevTools at all. See the `chrome-devtools-cookie-extraction` skill for filesystem-level extraction and multi-profile scanning techniques.

## Pitfalls

- **TikTok hydration JSON key is `'webapp.video-detail'` (lowercase)**, not the `VideoDetail` shape other docs show — find the scope key with `Object.keys(scope).find(k => k.toLowerCase().includes('video-detail'))` instead of hardcoding, because the platform renames scope keys without notice. TikTok also hydrates `__UNIVERSAL_DATA_FOR_REHYDRATION__` asynchronously after `Page.navigate`: poll `Runtime.evaluate` every ~3s (up to ~45s) until the item exists — a fixed `time.sleep(7)` reads a half-hydrated page and yields false `nojson`/`noitem` errors.
- **TikTok video subtitle/transcript URLs come from `video.subtitleInfos`** in the same hydration JSON (pick `Format == 'webvtt'`); download with a `Referer: https://www.tiktok.com/` header — real timestamped transcripts without any ASR step.
- **WAF/Cloudflare**: sites behind AWS WAF (like Skool) may require a `aws-waf-token` cookie from the live browser session — curl without it may 403.
- **CSP restrictions**: some endpoints check `x-nextjs-data: 1` header or `referer`. Always mirror browser headers in direct calls.
- **Session expiry**: `auth_token` cookies expire. If calls start 403ing, re-extract from the live browser session.
- **__NEXT_DATA__ staleness**: on client-side navigated pages, `__NEXT_DATA__` still shows the SSR page 1 data. Always check the DOM or network for actual current content.
- **Rate limiting**: many apps throttle rapid pagination. Add 200-500ms delays between requests.
- **Truncated responses**: `mcp_chrome_devtools_get_network_request` may truncate large response bodies. Use `responseFilePath` parameter to save full response to disk.
- **Attachments may have opaque IDs ≠ real S3 keys**: Feed/list APIs often expose a `fileId` or `attachmentId` that is NOT the actual file storage key. Direct access to `https://cdn.example.com/f/{id}` 403s. The real download URL is in a separate `attachmentsData` field on the INDIVIDUAL item page, under `read_url` or `src_read_url`. Fetch individual pages to get these real URLs, then download with the auth cookie.
- **Comment count field may be top-level only**: Some platforms (Skool) only count top-level comments in the feed metadata field. Nested replies add 50-100% more volume not reflected in the count.
- **Check `noComment` / `commentsDisabled`**: Skip comment-fetching API calls for posts that have comments disabled. Saves time and rate-limit budget.
- **Auth cookies may be httpOnly**: Not all cookies are readable from `document.cookie`. For httpOnly cookies, extract from network request headers via `mcp_chrome_devtools_get_network_request`.
- **Individual post page endpoint**: For SPA sites like Skool that hide attachment metadata in per-post pages, the pattern is `/_next/data/{buildId}/{group}/{postSlug}.json` — this contains data NOT available in the feed JSON (e.g. `attachmentsData` with content_type, file_name, and crucially the real download URLs). Fetch in parallel via Python requests for bulk analysis.
- **WAF token expiry mid-job**: Long-running extractions (1,000+ items, 15+ min) will hit WAF token expiry. Strategy: extract fresh token from `document.cookie` via Chrome DevTools before each batch, and on any 403 response, stop the batch, re-extract token, and retry.
- **CDN downloads may not need WAF token**: For file downloads from CDN endpoints (e.g. `assets.skool.com/f/{groupId}/{hash}`), the `auth_token` cookie alone often suffices — the WAF token check only applies to the API/feed endpoints. Test with just the auth cookie first to save the overhead of token management during bulk downloads.
- **Don't re-scrape what you already extracted**: After dumping data to local JSON files, answer questions from your local cache, not by going back to the browser or API. The user will call you out ("por que buscas con el MCP si ya descargaste todo"). Once extraction data is on disk, use `read_file`, `terminal` (Python), or `execute_code` to query it — not Chrome DevTools MCP re-fetches.

## Local Visualization Dashboard

After extracting data to JSON files, create a self-contained HTML file (`index.html`) for browsing:

```
scraped-data/
├── all_items.json         # extracted data
├── all_comments.json      # nested comments
├── attachments/           # downloaded files
├── index.html             # ← open in browser to browse
└── start_server.cmd       # python -m http.server 8080
```

### Dashboard template pattern

```html
<script>
fetch('all_items.json').then(r => r.json()).then(data => {
  // Render search, filter, sort controls
  // Render post cards with comments toggle, attachment links
});
</script>
```

Features to include:
- **Full-text search** across titles and content
- **Category/label filter** populated from the data
- **Sort** by date, popularity, comment count
- **Expand/collapse** for long content
- **Comments section** with nested replies toggle
- **Attachment links** pointing to local files (`attachments/filename`)
- **Count** of visible results

Files are served via `python -m http.server 8080` (CORS requirement for fetch). The attachments directory must be in the same served root.

## Verification

After extraction, verify completeness:

## Complete Website Download for Offline Viewing

When the user wants to save a complete webpage (HTML + CSS + images) that looks **identical** to the live site. The key challenge is Cloudflare Turnstile — it blocks ALL automated tools. The only reliable approach is connecting to the user's real browser via CDP.

**See [references/complete-website-download.md](references/complete-website-download.md) for the full workflow**, including:
- Launching Chrome/Brave with CDP debugging
- Inlining ALL CSS via `document.styleSheets` (captures cross-origin styles)
- Converting images to data URIs via `fetch()` (preserves original format)
- Adding `<base>` tag for remaining external resources
- **CRITICAL**: serving via `python -m http.server 8080` instead of `file://`

**Key finding from real captures:**
- CSS via `document.styleSheets[i].cssRules` is superior to `Page.getResourceContent` — it captures cross-origin styles, dynamically injected CSS, and avoids URL-matching bugs
- `fetch()` preserves original image format (JPEG stays JPEG) unlike canvas `toDataURL()` which re-encodes as PNG (3-5x larger) AND fails silently on CORS
- Joomla appends `#joomlaImage://local-images/...` fragments — always strip with `.split('#')[0]`
- WebSocket `max_size=100*1024*1024` is needed for pages with data URIs (15-35 MB payloads)
- `file://` protocol blocks external resources even with `<base>` tag — ALWAYS serve via local HTTP\n- **Simple fallback for JS-heavy sites**: Just add `<base>` tag to raw HTML + serve via local HTTP — loads all resources live, looks identical (requires internet). Test by opening the URL yourself before reporting success.

## Absorbed Skills

This umbrella skill absorbed four narrower scraping/automation skills:

- **complete-webpage-save** (archived) — complete website download for offline viewing using monolith, cloudscraper, SingleFile, CDP browser connection, COEP handling, CSS inlining, image data URI conversion. All patterns integrated into the "Complete Website Download" section above.
- **skool-content-extraction** (archived) — Skool community content extraction (Next.js SSR, Loom captions, module navigation, placeholder video ID detection). Integrated into the "Real-world example: Skool community scrape" section above. Its `references/loom-caption-extraction.md` is available.
- **chrome-devtools-cookie-extraction** (archived) — CDP remote debugging bypass for disable-devtool sites, filesystem SQLite extraction, multi-profile scanning, WebSocket-only auth sites. Integrated into the "Chrome DevTools Cookie Extraction" subsection.
- **kkbrio-casino-protocol** (archived) — technical analysis of kkbrio.love (oro7777) casino architecture, hxws WebSocket binary protocol, game provider mapping. Valuable as a reverse-engineering reference. Preserved as a reference.

## References

### Browser Form Interaction Troubleshooting
[references/browser-automation-form-troubleshooting.md](references/browser-automation-form-troubleshooting.md)
When `browser_click` fails on select/dropdown elements ("Could not compute box model") — use JS injection via `browser_console` to inspect form fields, set values programmatically, and submit. Covers CSRF tokens, iframe forms, and SPA event listeners.

### SCORM / Legacy LMS Automation
[references/scorm-lms-automation.md](references/scorm-lms-automation.md)
Automating legacy enterprise LMS platforms (WorKingbird, OverNite Software) with frameset-based rendering, custom combobox login, SCORM 1.2/2004 course launch via new-window forms, and session persistence gotchas. Covers form target override (_new to _self) and interaction with iframe-based SCORM players.

### Complete Website Download
[references/complete-website-download.md](references/complete-website-download.md)
Full workflow for saving a complete webpage behind Cloudflare Turnstile.

### Cloudflare Turnstile Bypass via CDP
[references/cloudflare-cdp-bypass.md](references/cloudflare-cdp-bypass.md)
Strategy for extracting content from sites behind Cloudflare Turnstile:
connect to the user's real desktop browser via CDP (`--remote-debugging-port=9222`),
use websockets + Runtime.evaluate to extract resources.
- Count matches the `total` field
- No duplicate IDs
- Date range looks plausible (oldest to newest)
- Spot-check 3-5 posts against live page content

## Real-world example: Skool community scrape

See `references/skool-scraping.md` for a full worked example including:
- Finding the Next.js build ID
- The JSON endpoint pattern: `/_next/data/{buildId}/{group}.json?c=&fl=&p={N}&group={group}`
- Handling the pinned/duplicate post issue
- Extracting attachment URLs
- Cookie/auth requirements

## HXWS WebSocket Binary Protocol Reference

See `references/hxws-websocket-binary-protocol.md` for a complete worked example of reverse-engineering a custom binary WebSocket protocol from a production casino SPA. Covers:
- Command/sub-command structure extraction from minified JS
- Binary packet field type mappings (uint8_t, char16_t, utf8, etc.)
- Login protocol: account format, password hashing (MD5), device fingerprinting
- Response structure decoding
- The hxws library (WASM-based binary encoding)
- Bot detection behavior patterns (empty DOM + populated accessibility tree)
- Game provider ID mappings
- API signing algorithm (signedPost)

This is the go-to reference when you encounter a site that uses WebSocket for ALL communication instead of HTTP REST.

## Templates

See also:
- `templates/hxws-ws-login.py` — Runnable Python template for implementing hxws binary WebSocket login. Customize the protocol constants, field schemas, and credentials for your target.
- `templates/playwright-anti-bot-bypass.py` — Complete Playwright script with JS route interception to bypass disable-devtool and other anti-automation libraries. Includes window.open/close patching and native bridge mocking.

## Loom Transcript Extraction from Courses

See `references/loom-transcript-extraction.md` for extracting captions/transcriptions from Loom videos embedded in Skool (or other) course modules. Covers:
- Loom transcription JSON format (`phrases[].ts` + `phrases[].value`)
- VTT parsing
- Signed URL extraction from the Loom embed page
- Skool course module navigation pattern
- Compatibility with the YouTube RAG pipeline output format
