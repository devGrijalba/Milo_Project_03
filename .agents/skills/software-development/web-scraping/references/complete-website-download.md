# Complete Website Download for Offline Viewing

## When to use this

The user wants to save a complete web page (`.html` + all assets) that looks **identical** to the live site when opened offline or from another machine. This is NOT data extraction — it's visual preservation.

## Key constraint: Cloudflare Turnstile

Most sites behind Cloudflare Turnstile **cannot** be downloaded by any automated tool:

| Tool | Result |
|------|--------|
| curl / wget / monolith / httrack | 403 / Cloudflare challenge |
| requests + cf_clearance cookie | 403 — JA3 TLS fingerprint mismatch |
| curl_cffi / cloudscraper | 403 |
| Playwright headless (any browser + stealth) | Stuck on Turnstile forever |
| Chrome DevTools MCP | Turnstile never resolves |

**The only reliable approach**: Connect to the user's real desktop browser (Chrome/Brave/Edge) via CDP after they've passed the Turnstile challenge.

## Workflow

### Step 1: Launch browser with CDP

Kill all browser instances, then relaunch with debugging enabled:

```bash
# Brave (Windows)
"/c/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" --remote-debugging-port=9222 --remote-allow-origins="*" --no-first-run "https://target-site.com"

# Chrome (Windows)
"/c/Program Files/Google/Chrome/Application/chrome.exe" --remote-debugging-port=9222 --remote-allow-origins="*" --no-first-run "https://target-site.com"
```

Flags explanation:
- `--remote-debugging-port=9222` — enables CDP
- `--remote-allow-origins="*"` — required in modern Chrome/Brave, otherwise WebSocket gets 403
- `--no-first-run` — suppresses welcome tab

### Step 2: User passes Cloudflare

The browser opens as a real, visible window. The user navigates to the target URL and completes the Turnstile challenge (tick the checkbox). Once the page renders, tell the user "ya está, avísame".

### Step 3: Connect via CDP and get page resources

```python
import asyncio, json, websockets

# Find the tab
import urllib.request
tabs = json.loads(urllib.request.urlopen('http://localhost:9222/json').read())
tab = next(t for t in tabs if 'target-site' in t.get('url', '') and t.get('type') == 'page')
ws_url = tab['webSocketDebuggerUrl']

async with websockets.connect(ws_url, max_size=100*1024*1024) as ws:
    msg_id = 0
    async def send(method, params=None):
        nonlocal msg_id
        msg_id += 1
        msg = {'id': msg_id, 'method': method}
        if params: msg['params'] = params
        await ws.send(json.dumps(msg))
        while True:
            raw = await asyncio.wait_for(ws.recv(), timeout=30)
            resp = json.loads(raw)
            if 'id' in resp and resp['id'] == msg_id:
                return resp

    await send('Page.enable')
```

**Important**: Filter responses by `resp['id'] == msg_id` — CDP sends events (without `id`) interleaved with responses.

### Step 4: Inline ALL CSS via document.styleSheets

Run this JavaScript *inside* the page. It captures ALL styles (internal, external, dynamically injected) and replaces `<link>` with `<style>` tags:

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

`try/catch` handles cross-origin CSS (Google Fonts, CDN FontAwesome) which throw SecurityError on `cssRules` access — those keep their original `<link>` tags.

### Step 5: Convert ALL images to data URIs via fetch()

Run this as an async function with `awaitPromise: True`. It downloads same-origin images and replaces them as data URIs:

```javascript
async function toDataUrl(url) {
    try {
        const r = await fetch(url, { credentials: 'include', cache: 'force-cache' });
        if (!r.ok) return null;
        const blob = await r.blob();
        return await new Promise((res, rej) => {
            const reader = new FileReader();
            reader.onloadend = () => res(reader.result);
            reader.onerror = rej;
            reader.readAsDataURL(blob);
        });
    } catch(e) { return null; }
}

// Convert <img> tags (strip Joomla fragments with .split('#')[0])
const imgPromises = [];
document.querySelectorAll('img').forEach(img => {
    const src = img.getAttribute('src') || '';
    if (src && !src.startsWith('data:') && src.startsWith('http')) {
        imgPromises.push(toDataUrl(src.split('#')[0]).then(d => {
            if (d) { img.setAttribute('src', d); imgCount++; }
        }));
    }
});
await Promise.all(imgPromises);

// Convert CSS background images in style="" attributes
const bgPromises = [];
document.querySelectorAll('[style]').forEach(el => {
    const s = el.getAttribute('style') || '';
    const matches = [...s.matchAll(/url\(["']?([^"')]+)["']?\)/g)];
    matches.forEach(m => {
        const url = m[1].split('#')[0];
        if (url && !url.startsWith('data:')) {
            bgPromises.push(toDataUrl(url).then(d => {
                if (d) el.style.cssText = el.style.cssText.replace(m[0], 'url("' + d + '")');
            }));
        }
    });
});

// Convert CSS background images inside <style> tags
document.querySelectorAll('style').forEach(styleTag => {
    const text = styleTag.textContent || '';
    const matches = [...text.matchAll(/url\(["']?([^"')]+)["']?\)/g)];
    matches.forEach(m => {
        const url = m[1].split('#')[0];
        if (url && !url.startsWith('data:')) {
            const resolved = url.startsWith('http') ? url : new URL(url, window.location.origin).href;
            bgPromises.push(toDataUrl(resolved).then(d => {
                if (d) styleTag.textContent = styleTag.textContent.replace(m[0], 'url("' + d + '")');
            }));
        }
    });
});
await Promise.all(bgPromises);
```

Send with: `{'awaitPromise': True, 'returnByValue': True}`

**Key details:**
- `fetch()` preserves original image format (JPEG stays JPEG, unlike canvas which re-encodes as PNG, making files 3-5x larger)
- `split('#')[0]` strips Joomla `#joomlaImage://local-images/...` fragments from URLs
- `credentials: 'include'` ensures cookies are sent (required for same-origin auth)
- Cross-origin images (CDN flags, third-party) cannot be fetched — they'll load from the original domain via `<base>` tag when online

### Step 6: Get the modified HTML

```python
resp = await send('Runtime.evaluate', {
    'expression': 'document.documentElement.outerHTML',
    'returnByValue': True
})
html = resp['result']['result']['value']
```

### Step 7: Add <base> tag

```python
html = html.replace('<head>', '<head><base href="https://original-site.com/">')
full = '<!DOCTYPE html>\n' + html
```

The `<base>` tag makes remaining external URLs (CDN images, Google Fonts) resolve to the live site when online.

### Step 8: Serve locally (CRITICAL)

**Do NOT open the .html file directly** (via double-click or `file://` protocol). Chrome/Brave blocks external resources from `file://` even with `<base href="...">` due to CORS/security policy.

```bash
# Save as index.html in a directory
python -m http.server 8080
# Access via http://localhost:8080/
```

### Alternative: Page.captureSnapshot (MHTML)

If the `document.styleSheets` approach is too complex, use MHTML:

```python
resp = await send('Page.captureSnapshot', {'format': 'mhtml'})
# In modern Chrome, the data is PLAIN TEXT, NOT base64
mhtml_text = resp['result']['data']
with open('page.mhtml', 'w', encoding='utf-8') as f:
    f.write(mhtml_text)
```

Open `.mhtml` via `Ctrl+O` in Chrome/Brave. Note: Some Chrome versions don't render MHTML reliably.

### Fallback: minimal approach (just HTML + base tag)

For Joomla/WordPress sites where CSS inlining is complex or breaks relative paths, a simpler fallback works when the user has internet:

```python
# Get just the raw HTML, no inlining
resp = await send('Runtime.evaluate', {
    'expression': 'document.documentElement.outerHTML',
    'returnByValue': True
})
html = resp['result']['result']['value']
html = html.replace('<head>', '<head><base href="https://original-site.com/">')
with open('index.html', 'w') as f:
    f.write('<!DOCTYPE html>\n' + html)
```

Serve via local HTTP server — do NOT open via file://:

```bash
python -m http.server 8080
# → http://localhost:8080/
```

This loads ALL resources from the live site. From `http://localhost`, the browser treats it as a secure context and loads HTTPS resources without CORS issues. The page looks identical to the live site.

Use this when:
- The page is JS-heavy (Joomla, WordPress, SPA) and won't render offline anyway
- CSS has complex relative path references (`../fonts/`, `../images/`) that break when inlined
- The user just needs a snapshot that works with internet

Trade-off: Requires internet. Without internet, the page degrades to unstyled HTML.

### Key behavioral notes from real captures

1. **Always verify by opening the page yourself** via the browser tool after generating it. Don't tell the user it works until you've seen it render correctly. The user gets frustrated when you claim success without testing.

2. **`Page.captureSnapshot` MHTML may not render** in some Chrome/Brave versions. It's less reliable than the HTML + base tag approach.

3. **`document.styleSheets[i].cssRules` approach** captures ALL styles but inserts them as `<style>` tags. After this, any `url()` references in those styles still point to the original relative paths — you must also convert those background images via `fetch()` inside the page context.

4. **Clean up external resources** from `localhost` that cause 404s: after inlining CSS, remove remaining `<link rel="stylesheet">` tags that couldn't be inlined, or ensure the `<base>` tag handles them.

5. **Don't kill the browser** while the user is using it. Use `taskkill /f /im brave.exe` only as a last resort.

## Expected results

| Site type | File size | CSS inlined | Images inlined |
|-----------|-----------|-------------|----------------|
| Simple brochure site | 500 KB - 2 MB | 5-15 | 10-30 |
| Joomla/WordPress corporate | 8-15 MB | 20-40 | 30-60 |
| Media-heavy site | 30-50 MB | 10-20 | 80-150 |

## Common pitfalls

1. **"The page doesn't look right"** → You're opening via `file://`. Use `python -m http.server 8080` and access via `http://localhost:8080/`.

2. **"STOP! Edit in Articles" / "Edit Here" visible** → Joomla backend markers hidden by CSS. If CSS was properly inlined, these should be hidden. If visible, some site-specific CSS was cross-origin and couldn't be inlined.

3. **"Images don't load"** → Cross-origin CDN images can't be fetched via CDP. They'll load when online via `<base>` tag. For fully offline, these need alternative handling.

4. **"Black screen / blank page"** → WebSocket message too large. Add `max_size=100*1024*1024` to the websocket connection. Or the page state was modified by a previous script run (images converted to data URIs, etc.) — navigate fresh.

5. **"SingleFile keeps loading forever"** → The page is too complex for SingleFile. Use CDP approach instead.

6. **"The MHTML doesn't open"** → In some Chrome versions, double-clicking `.mhtml` opens it in the downloads bar but doesn't render. Use `Ctrl+O` → select file, or drag into a tab.

7. **WebSocket 403/500 on connect** → Tab was closed. Check `curl -s http://localhost:9222/json` for current tabs. If no target tab exists, the user needs to open the page again.

8. **"Agent is not enabled" error** → Forgot to call `await send('Page.enable')` before other Page methods.

9. **Images still show as external (not data URIs)** → The `fetch()` call requires same-origin. Check if the image URL is on a different domain. Also check for Joomla `#joomlaImage://` fragments that prevent matching.

10. **Canvas toDataURL fails silently** → Cross-origin images taint the canvas. Use `fetch()` instead of canvas for image conversion. `fetch()` preserves original format (PNG → PNG, JPEG → JPEG) AND avoids CORS taint.
