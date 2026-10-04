# Cloudflare Turnstile Bypass via CDP + Real Browser

## The Problem

Cloudflare Turnstile (and similar JS-based challenges) blocks ALL automated HTTP tools and headless browsers:

| Tool | Result |
|------|--------|
| curl / wget | 403 Cloudflare challenge page |
| monolith | 403 Forbidden |
| cloudscraper | 403 |
| curl_cffi (impersonation) | 403 |
| Playwright headless (Chromium/FF) | Stuck on "Just a moment..." |
| Playwright + stealth | Detected as bot |
| Chrome DevTools (standalone) | Turnstile never resolves |
| Python requests + cf_clearance cookie | **Still 403** — TLS fingerprint mismatch |

**Key finding**: Even with a valid `cf_clearance` cookie from the user's real browser, Python `requests` still gets 403 because Cloudflare validates the **TLS fingerprint** (JA3) of the client, not just the cookie.

## The Solution: Real Browser + CDP

The only reliable way is to connect to the user's **real desktop browser** (Chrome/Brave/Edge) via Chrome DevTools Protocol (CDP).

### Step 1: Launch browser with debugging port

Kill all instances, then launch in background:

```bash
# Windows (Brave)
"/c/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" --remote-debugging-port=9222 --remote-allow-origins="*" --no-first-run "https://target-site.com"

# Windows (Chrome)
"/c/Program Files/Google/Chrome/Application/chrome.exe" --remote-debugging-port=9222 --remote-allow-origins="*" --no-first-run "https://target-site.com"
```

**Important flags:**
- `--remote-debugging-port=9222` — enables CDP on port 9222
- `--remote-allow-origins="*"` — allows WebSocket connections from any origin (required in modern Chrome/Edge/Brave, otherwise WebSocket gets 403)
- `--no-first-run` — suppresses welcome tab

### Step 2: Find the page

```bash
curl -s http://localhost:9222/json
```

Returns JSON array of open tabs with `id`, `title`, `url`, and `webSocketDebuggerUrl`.

### Step 3: Connect via websockets

```python
import asyncio, json, websockets

async def main():
    ws_url = "ws://localhost:9222/devtools/page/<PAGE_ID>"
    async with websockets.connect(ws_url, max_size=50*1024*1024) as ws:
        msg_id = 0
        async def send(method, params=None):
            nonlocal msg_id
            msg_id += 1
            msg = {"id": msg_id, "method": method}
            if params: msg["params"] = params
            await ws.send(json.dumps(msg))
            # Read until we find the matching response (filter out events)
            while True:
                raw = await asyncio.wait_for(ws.recv(), timeout=30)
                resp = json.loads(raw)
                if "id" in resp and resp["id"] == msg_id:
                    return resp

        await send("Page.enable")
        # Get full rendered HTML
        resp = await send("Runtime.evaluate", {
            "expression": "document.documentElement.outerHTML",
            "returnByValue": True
        })
        html = resp["result"]["result"]["value"]
```

### Key CDP Methods

| Method | Purpose |
|--------|---------|
| `Page.enable` | Activate Page domain |
| `Page.getResourceTree` | Get all page resources (CSS, JS, images, fonts) with URLs and types |
| `Page.getResourceContent` | Download a specific resource by URL — **works for same-origin resources only** |
| `Runtime.evaluate` | Execute JS in page context and return result |
| `Page.captureSnapshot` | Save entire page as MHTML (returns **plain text**, NOT base64) |
| `Network.getAllCookies` | Get cookies from the browser session |

### Complete End-to-End Workflow (CDP + fetch + CSS inlining)

For a fully self-contained HTML that looks identical to the live site:

1. **Kill** existing browser instances → launch with `--remote-debugging-port=9222 --remote-allow-origins="*"`
2. User navigates to the target URL and passes any Cloudflare challenge
3. **Connect** via CDP WebSocket to the tab with the real page content
4. **Inline CSS** — run JS that iterates `document.styleSheets`, reads `cssRules`, replaces `<link>` with `<style>` tags
5. **Convert images** — run JS that uses `fetch()` to download same-origin images as data URIs, replacing `img.src` and `url()` in `[style]` and `<style>` elements
6. **Wait** for all async fetch promises to resolve (`await Promise.all(...)`)
7. **Get outerHTML** — `document.documentElement.outerHTML` via `Runtime.evaluate`
8. **Add `<base>` tag** — `<base href="https://original-site.com/">` so remaining relative URLs resolve online
9. **Save** as `<!DOCTYPE html>\n` + HTML
10. **Serve locally** — `python -m http.server 8080` and open `http://localhost:8080/`

**Expected results**: 15-35 MB for a typical corporate site (Joomla/WordPress) with all images embedded. CSS inlined (20-40 sheets). Images converted: 30-60. Page renders identically to the live site when served via HTTP.

**Performance notes**:
- `Runtime.evaluate` with `returnByValue=True` and large payloads (30+ MB) may require `max_size=100*1024*1024` on the websocket
- `fetch()` approach preserves original image format (JPEG stays JPEG) unlike canvas which re-encodes as PNG (3-5x larger)
- Some cross-origin images (CDN flags, third-party) cannot be converted — they'll load from the original domain via `<base>` tag when online
- The `awaitPromise: True` parameter with an async function ensures all fetch promises resolve before serialization

#### 1. Inline CSS

**Approach A — Download via Page.getResourceContent (external CSS only)**

```python
resp = await send("Page.getResourceTree")
resources = resp["result"]["frameTree"].get("resources", [])
for r in resources:
    if r.get("type") == "Stylesheet":
        url = r.get("url", "")
        resp = await send("Page.getResourceContent", {"frameId": frame_id, "url": url})
        css_content += f"\n/* {url} */\n{resp['result']['content']}\n"
```

**Approach B — Inline ALL CSS from within the browser (recommended)**

Run this JavaScript *inside* the page via `Runtime.evaluate`. It iterates `document.styleSheets`, reads `cssRules`, replaces `<link>` with `<style>` tags. This captures cross-origin CSS (Google Fonts, CDNs), dynamically injected styles, and avoids manual URL matching:

```javascript
const sheets = document.styleSheets;
let inlineCount = 0, failedCount = 0;
for (let i = 0; i < sheets.length; i++) {
    try {
        const rules = sheets[i].cssRules || sheets[i].rules;
        if (!rules || !rules.length) { failedCount++; continue; }
        let cssText = '';
        for (let j = 0; j < rules.length; j++) cssText += rules[j].cssText + '\n';
        if (cssText) {
            const style = document.createElement('style');
            style.textContent = cssText;
            if (sheets[i].ownerNode && sheets[i].ownerNode.tagName === 'LINK') {
                sheets[i].ownerNode.parentNode.replaceChild(style, sheets[i].ownerNode);
                inlineCount++;
            }
        }
    } catch(e) { failedCount++; }
}
```

The `try/catch` handles cross-origin stylesheets (Google Fonts, CDN FontAwesome) which throw a SecurityError when `cssRules` is accessed — these will keep their original `<link>` tags.

**Important**: CSS files may contain relative paths like `url("../images/bg.jpg")`. With the `<base>` tag (step 5), these resolve to the original domain when served via HTTP. For fully offline, you must also inline background images via `fetch()` (see step 3b).

#### 3b. Inline CSS background images in `<style>` tags

After inlining CSS, `<style>` tags may still contain `url()` references to background images. These need to be converted to data URIs too:

```javascript
async function toDataUrl(url) {
    const resp = await fetch(url, { credentials: 'include', cache: 'force-cache' });
    const blob = await resp.blob();
    return await new Promise((res, rej) => {
        const reader = new FileReader();
        reader.onloadend = () => res(reader.result);
        reader.onerror = rej;
        reader.readAsDataURL(blob);
    });
}

// Convert background images in <style> tags
document.querySelectorAll('style').forEach(async (styleTag) => {
    const text = styleTag.textContent || '';
    const matches = [...text.matchAll(/url\(["']?([^"')]+)["']?\)/g)];
    for (const m of matches) {
        const url = m[1].split('#')[0];  // Strip Joomla fragments
        if (url && !url.startsWith('data:')) {
            // Resolve relative URLs against the page's origin
            const resolved = url.startsWith('http') ? url : new URL(url, window.location.origin).href;
            const dataUrl = await toDataUrl(resolved);
            if (dataUrl) styleTag.textContent = styleTag.textContent.replace(m[0], `url("${dataUrl}")`);
        }
    }
});
```

**Also convert background images from inline styles:**

```javascript
document.querySelectorAll('[style]').forEach(async (el) => {
    const s = el.getAttribute('style') || '';
    const matches = [...s.matchAll(/url\(["']?([^"')]+)["']?\)/g)];
    for (const m of matches) {
        const url = m[1].split('#')[0];
        if (url && !url.startsWith('data:')) {
            const dataUrl = await toDataUrl(url);
            if (dataUrl) el.style.cssText = el.style.cssText.replace(m[0], `url("${dataUrl}")`);
        }
    }
});
```
#### 3. Inline images via fetch() (same-origin only)

Convert `<img>` tag sources and CSS background images to data URIs using `fetch()` from within the browser. This preserves original image format (JPEG stays JPEG):

```javascript
async function toDataUrl(url) {
    const resp = await fetch(url, { credentials: 'include', cache: 'force-cache' });
    const blob = await resp.blob();
    return await new Promise((res, rej) => {
        const reader = new FileReader();
        reader.onloadend = () => res(reader.result);
        reader.onerror = rej;
        reader.readAsDataURL(blob);
    });
}
```

**Note**: Modern Chrome returns MHTML as plain text (not base64 encoded). The format uses `Content-Transfer-Encoding: quoted-printable` for text parts. Some browsers may not open `.mhtml` files reliably.

### Pitfalls

- **file:// protocol blocks external resources (CRITICAL)**: Opening the saved `.html` file directly from the filesystem (double-click, `file://`) **will not load external resources** even with `<base href="...">`. Chrome/Brave blocks CSS, JS, and images from `https://` origins when the page is served via `file://`. Always serve locally: `python -m http.server 8080` from the directory containing the HTML, then access via `http://localhost:8080/`. This is the single most common reason "the page doesn't look right".

- **Page.captureSnapshot** returns the MHTML as a **plain text string**, NOT base64-encoded. Just save the response directly as `.mhtml`. In older Chrome versions it was base64 — check the actual response.
- **CORS limits**: `Page.getResourceContent` only works for same-origin resources. Cross-origin (CDN, Google Fonts, reCAPTCHA, Cloudflare insights JS) returns errors. You cannot download fonts from `fonts.gstatic.com` or analytics scripts from `static.cloudflareinsights.com` via CDP.
- **WebSocket max_size**: MHTML snapshots can be 10+ MB. Set `max_size=50*1024*1024` on the websocket connection to avoid `1009 (message too big)` errors.
- **Response filtering**: CDP sends events (without `id`) interleaved with responses. Always filter responses by matching `resp["id"] == msg_id` to get the right response. Without this, you'll read events instead of command responses.
- **Page.enable** must be called before `Page.getResourceTree` or `Page.getResourceContent`, otherwise you get `"Agent is not enabled"` error.
- **Canvas approach is silent on failure**: When `drawImage` taints the canvas due to CORS, it throws a security error. The try/catch catches it silently — you won't know which images failed unless you check `naturalWidth` after conversion.
- **cf_clearance cookie ≠ Python access**: Even with a valid `cf_clearance` cookie copied from the browser, Python `requests` still gets 403/400. Cloudflare uses JA3 TLS fingerprinting to detect non-browser clients. You MUST use the real browser (via CDP) to fetch resources.
- **JS-heavy pages**: Joomla, WordPress with page builders, and SPA sites use JavaScript for layout. A static HTML snapshot will not look the same without JS executing. The DOM captured by `outerHTML` is the post-JS state, but without the JS files to re-execute, interactive elements (sliders, menus, tabs) won't work offline.
- **SingleFile extension**: If the user has SingleFile installed in their browser, recommend it over programmatic approaches. It produces a perfect self-contained HTML. On Brave/Chrome, it may be hidden under the puzzle icon 🧩 in the toolbar.

### Brave-Specific Notes

- **Path**: `/c/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe`
- **Version reported** as "Chrome/X.Y.Z.W" in CDP (Chromium-based)
- **SingleFile extension** ID: `mpiodijhokgodhhofbcjdecpffjipkle`
- Use `start` or `background=true` to launch in background without blocking
- On fresh launch with `--remote-debugging-port`, Cloudflare Turnstile may auto-pass because it's a real browser with a real user profile
