# Skool Community Scraping — Full Worked Example

Target: `https://www.skool.com/sqxtraders` (SQX Traders, 460 members, 1,342 posts)

## Tech Stack

- **Next.js** SSR + client-side navigation
- **AWS WAF** (CloudFront + `aws-waf-token` cookie/header, rotates periodically)
- **Auth**: JWT in httpOnly `auth_token` cookie (1-year expiry on refresh)
- **Backend API**: `api2.skool.com` (CloudFront-backed, CORS to `*.skool.com`)
- **Media CDN**: `https://assets.skool.com/f/{groupId}/{fileId}`

## Setup: Getting Auth

The `auth_token` cookie is **httpOnly** — you CANNOT read it from `document.cookie`. Extract it from a network request header instead:

```
mcp_chrome_devtools_list_network_requests(resourceTypes=["xhr","fetch"])
mcp_chrome_devtools_get_network_request(reqid=N)
# Look at Request Headers → cookie: auth_token=eyJ...
```

The `aws-waf-token` IS readable from `document.cookie` and `localStorage('awswaf_session_storage')`. It rotates periodically (every ~30-60 min), so batch jobs should extract a fresh token before each batch.

Required cookies for direct API calls:
```
auth_token=eyJ...        (httpOnly, from network headers)
aws-waf-token=...        (from document.cookie)
```

Required headers for direct API calls:
```
User-Agent: Mozilla/5.0 ...
x-aws-waf-token: <same as cookie value>
Origin: https://www.skool.com
Referer: https://www.skool.com/
```

## Feed Endpoint (All Posts)

```
GET https://www.skool.com/_next/data/{buildId}/{group}.json?c=&fl=&p={N}&group={group}
```

- `buildId`: from `__NEXT_DATA__.buildId` (e.g. `1779392430956`)
- `group`: URL path segment (e.g. `sqxtraders`)
- `c`: category filter UUID (empty = all)
- `fl`: text search filter
- `p`: page number (1-indexed)
- **33 posts per page**
- **~41 pages for 1,342 total posts**

### Response Structure

```json
{
  "pageProps": {
    "total": 1342,
    "postTrees": [
      {
        "post": {
          "id": "post-uuid",
          "name": "url-slug",
          "metadata": {
            "title": "Post Title",
            "content": "Post body in Skool markup",
            "upvotes": 42,
            "comments": 50,           // comment COUNT (not data)
            "pinned": 0 | 1,
            "labels": "category-uuid",
            "attachments": "uuid1,uuid2",     // comma-separated IDs
            "videoLinksData": "[{\"url\":\"...\",\"provider\":3,\"video_id\":\"...\"}]",
            "imagePreview": "https://assets.skool.com/f/{groupId}/{hash}-md.png",
            "lastComment": 1779310150348855000,
            "noComment": true | false,
            "contributors": "[{\"userId\":\"...\",\"name\":\"...\"}]",
            "myVote": "up" | null
          },
          "createdAt": "2026-05-19T10:48:08.640702Z",
          "userId": "author-uuid",
          "postType": "generic",
          "rootId": "same-as-id",
          "labelId": "category-uuid",
          "user": { /* full user profile object */ }
        }
      }
    ]
  }
}
```

### Key fields inside `user` object

```json
{
  "id": "author-uuid",
  "name": "username-1234",
  "firstName": "Miguel",
  "lastName": "Jiménez",
  "email": "",
  "metadata": {
    "bio": "Trader algo...",
    "location": "Málaga",
    "pictureProfile": "https://assets.skool.com/f/{userId}/{hash}.jpg",
    "pictureBubble": "https://assets.skool.com/f/{userId}/{hash}-sm.jpg",
    "linkYoutube": "https://youtube.com/...",
    "linkInstagram": "https://instagram.com/...",
    "linkTwitter": "https://x.com/...",
    "linkWebsite": "https://...",
    "spData": "{\"pts\":5787,\"lv\":7,\"pcl\":2015,\"pnl\":8015,\"role\":2}",
    "myersBriggs": "ENFJ",
    "mrrStatus": "liftoff",
    "lastOffline": 1779409277343778800
  }
}
```

Note: `email` is always `""` in the feed — real emails require admin-level access.

## Comments API

Discovered endpoint (not rendered in feed data):

```
GET https://api2.skool.com/posts/{postId}/comments?group-id={groupId}&limit=25&pinned=true
GET https://api2.skool.com/posts/{postId}/comments?group-id={groupId}&tail=true&limit=25  (page 2+)
```

Response shape:
```json
{
  "post_tree": {
    "children": [
      {
        "post": {
          "id": "comment-uuid",
          "parent_id": "post-uuid",
          "root_id": "post-uuid",
          "post_type": "comment",
          "created_at": "2026-05-05T10:57:39.361236Z",
          "metadata": {
            "content": "Comment text",
            "upvotes": 9
          },
          "user": { /* same shape as feed user object */ }
        },
        "children": [ /* nested replies — same shape */ ]
      }
    ],
    "meta": {
      "has_more": false | true
    }
  }
}
```

- `pinned=true` fetches pinned (highlighted) comments first
- `tail=true` fetches the next page (replace `pinned=true` with `tail=true`)
- `limit=25` is max per page
- Nested replies are in `children[].children[]` (2 levels)
- Each comment has a full `user` object identical to post authors

### Comment count vs actual

The `metadata.comments` field in the feed is the **top-level comment count only**. Nested replies are NOT counted in this number. Total interaction count per post = `comments` (top-level) + sum of all `children[].children.length`.

## Attachments

### Critical: attachment ID ≠ download URL

The `metadata.attachments` field in the feed contains **opaque UUIDs** that are **NOT the actual file keys**. Direct access to `https://assets.skool.com/f/{groupId}/{attachmentId}` returns HTTP 403 (S3 AccessDenied).

The **actual download URLs** live inside `attachmentsData` on the individual post page, under two fields:
- `read_url` → the processed/optimized copy (preferred for images)
- `src_read_url` → the original uploaded file (preferred for non-image files)

These use a completely different hash than the attachment ID and **DO return HTTP 200 with the file**.

### Download technique

1. Get `attachmentsData` from the individual post endpoint:
```
GET https://www.skool.com/_next/data/{buildId}/{group}/{postSlug}.json
```
This endpoint requires `auth_token` cookie + `x-aws-waf-token` header — same as feed.

2. For each attachment entry, extract `metadata.read_url` (fall back to `metadata.src_read_url`):
```python
dl_url = meta.get('read_url') or meta.get('src_read_url')
# e.g. https://assets.skool.com/f/{groupId}/ea8e13a4bbcf4772a2bbcb5fd829f19a2... 
```

3. Download directly via Python requests with auth cookie:
```python
resp = requests.get(dl_url, cookies={"auth_token": "..."})
# HTTP 200, Content-Type matches the file type
```

4. No special `x-aws-waf-token` header needed for the CDN download — just the `auth_token` cookie suffices.

### File metadata available in attachmentsData

Each entry in `attachmentsData` contains:
```json
{
  "id": "7a867289...",          // opaque ID, NOT the download hash
  "metadata": {
    "content_type": "image/png",
    "file_name": "image.png",
    "file_size": 123456,           // via src_content_length
    "read_url": "https://...",     // DOWNLOADABLE URL (different hash!)
    "src_read_url": "https://...", // original upload URL (also downloadable)
    "store_key": "f/groupId/hash.ext",
    "src_content_length": 183201,  // real file size in bytes
    "src_content_type": "image/png",
    // For images only:
    "image_md_url": "https://...",  // medium thumbnail (720px)
    "image_sm_url": "https://...",  // small thumbnail (240px)
    "image_md_width": 720,
    "image_md_height": 217,
    "image_sm_width": 240,
    "image_sm_height": 72,
    "src_height": 544,
    "src_width": 1809
  }
}
```

### Batch metadata extraction

`attachmentsData` is NOT present in the feed JSON — you must fetch each post individually. For 500+ posts with attachments, use parallel workers:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

BUILD = "1779392430956"
GROUP = "sqxtraders"
GROUP_ID = "16562bff..."

def get_attachment_meta(post):
    url = f"https://www.skool.com/_next/data/{BUILD}/{GROUP}/{post['slug']}.json"
    resp = session.get(url, timeout=15)
    data = resp.json()
    m = data["pageProps"]["postTree"]["post"]["metadata"]
    raw = m.get("attachmentsData")
    if not raw: return []
    parsed = json.loads(raw) if isinstance(raw, str) else raw
    return [{
        "id": a["id"],
        "file_name": a["metadata"]["file_name"],
        "content_type": a["metadata"]["content_type"],
        "file_size": a["metadata"].get("src_content_length"),
        "download_url": a["metadata"].get("read_url") or a["metadata"].get("src_read_url"),
        "post_slug": post["slug"],
    } for a in parsed]

with ThreadPoolExecutor(max_workers=5) as ex:
    futures = {ex.submit(get_attachment_meta, p): p for p in posts_with_att}
    for f in as_completed(futures):
        all_meta.extend(f.result())
```

### File types found in SQX Traders (531 posts, 1,098 attachments)

| Content-Type | Count | Example files |
|-------------|-------|--------------|
| `image/png` | ~600+ | Screenshots, diagrams |
| `image/jpeg` | ~300 | Photos, config screenshots |
| `application/octet-stream` | ~80 | .cfx (SQX configs), .rar archives |
| `application/pdf` | ~40 | Ebooks, guides, reports |
| `text/html` | ~8 | Tool UIs (SQX Builder Tool.html) |
| `text/plain` | ~8 | Text files |
| `application/vnd.openxmlformats-officedocument...` | ~15 | .docx transcripts |
| `application/x-msdownload` | ~7 | .exe installers |
| `text/csv` | ~6 | Data exports |
| `application/x-compressed` | ~5 | .zip archives |
| `text/x-python` | ~5 | .py scripts |
| `text/markdown` | ~2 | .md docs |
| `audio/x-m4a` | 1 | Audio file |
| `application/json` | 1 | JSON export |

### Compressed files (23 total in SQX Traders, ~33 MB)

| File | Size | Post |
|------|------|------|
| `TranslateBook-Windows.zip` | 28.6 MB | Traductor libros de trading |
| `BuildingBlocks.rar` | 1.7 MB | Compendio Custom Projects |
| `CustomProjects.rar` | 10.4 MB | Compendio Custom Projects |
| `BIAL GUARDIAN.rar` | 3.8 MB | Alertas trading |
| `Calibracion_SQX_revisado...rar` | 1.9 MB | Calibración SQX |
| `CUSTOM_INDICATORS ACTUALIZADOS...rar` | 1.2 MB | Pack indicadores SQX |
| `SQX - Custom Indicators & Building Blocks.zip` | 627 KB | Pack indicadores |
| `Larry_Williams_divisas_EURGBP_H4_LS.zip` | 622 KB | Estrategia Larry Williams |
| `MonkeyTest_v1.0.rar` | 55 KB | Monkey Test |
| `SQX Instrument Extractor.zip` | 112 KB | Extractor MT5 |
| `OverfittingScore.zip` | 62 KB | Overfitting score tab |
| `Analizador Avanzado de Estrategias.zip` | 409 KB | Análisis portfolio |
| `CP_Volatilidad.zip` | 737 KB | Custom Project volatilidad |
| `DAX M5.zip` | 519 KB | Robot DAX template |
| `trading_analyzer_advanced.zip` | 11 KB | Herramienta análisis |
| `RiesgoVariableFijo.rar` | 3 KB | Riesgo variable |
| + 7 small SMC/ICT ZIPs | 24-31 KB each | SMC/ICT con SQX |

Also notable: ~96 non-image files of interest including .cfx (SQX builders), .docx (transcripts), .pdf (ebooks/guides), .exe (installers up to 85 MB), .py, .java, .csv data exports, .xlsx templates.

### Downloading attachments in bulk

All files are downloadable via `auth_token` cookie alone — NO `x-aws-waf-token` header needed for CDN downloads.

### Full pipeline (1,098 files, 962 MB)

```python
# 1. Fetch per-post metadata (attachmentsData) via Next.js endpoint
#    (NOT in feed — each post individually)
with ThreadPoolExecutor(max_workers=5) as ex:
    futures = {ex.submit(fetch_attachment_meta, p): p for p in posts_with_att}

# 2. Download each file — CDN only needs auth_token cookie, not WAF
for a in all_meta:
    url = a['download_url']  # read_url or src_read_url
    resp = requests.get(url, cookies={"auth_token": "..."}, timeout=60)
    with open(fpath, 'wb') as f:
        f.write(resp.content)

# 3. Index files back to parent posts
for p in posts:
    p['downloaded_files'] = [...]  # list of {file_name, content_type, file_size, downloaded, local_path}
```

### Batch approach (stages)

| Stage | Scope | Time | Workers |
|-------|-------|------|---------|
| 1. Feed pages (post list) | All pages | ~2 min | 1 request at a time |
| 2. Comments | All posts with comments | ~5 min | 5 parallel |
| 3. Attachment metadata | All posts with attachments | ~3 min | 5 parallel |
| 4. Download files | All attachments | ~10-15 min | 1 at a time (CDN rate) |

### CDN download note

The file CDN (`assets.skool.com/f/{groupId}/{hash}`) does NOT check the WAF token — only the `auth_token` cookie is required. This means you can download files even after the WAF token expires mid-job.

### Post-download indexing

After downloading, annotate each post with its files for easy lookup:

```json
{
  "id": "post-uuid",
  "title": "...",
  "downloaded_files": [
    {
      "id": "attachment-uuid",
      "file_name": "MonkeyTest_v1.0.rar",
      "content_type": "application/octet-stream",
      "file_size": 56526,
      "downloaded": true,
      "local_path": "D:/SKOOL/sqxtraders/attachments/MonkeyTest_v1.0.rar"
    }
  ]
}
```

## Categories (Labels)

9 categories found on SQX Traders. Map extracted from the filter chips in the DOM:

| UUID | Name | Post count |
|------|------|-----------|
| `d099fc5ea1de4b1da87da5efdbc288ba` | 🗣️ FeedBack | 452 |
| `f2d861cea5d64e22b26a413be9f2e5c4` | 💬 General | 292 |
| `2047fe6d460440b69c899914afe5c879` | 🏆 Logros | 116 |
| `d9ac3a8d852a4703ad5fae003ae68983` | 🪛 Herramientas | 97 |
| `19f3455ac072409197b4ee092201a8e0` | 🛠️ Configuraciones | 81 |
| `5d1626db46124311954621dad6a25364` | 📰 News | 77 |
| `165d1abfad2c4f22bf7013acf121b387` | 💰 Fondeo | 51 |
| `2cd34956b17b408fad4bca7b8867aea6` | 💼 Proyectos | 51 |
| `a013a042aacd424c92d58511bb0c8570` | 👾 IA | 13 |

Extract via:
```js
// Get all filter chips from the community page
document.querySelectorAll('[id^="chip-filter-chip-"]').forEach(el => {
  console.log(el.id, el.textContent);
});
```

## Extraction Script Architecture (Python)

### Phase 1 — Posts (~2 min, 41 API calls)

```python
# For each page 1..41:
resp = requests.get(
    f"https://www.skool.com/_next/data/1779392430956/sqxtraders.json",
    params={"c": "", "fl": "", "p": page, "group": "sqxtraders"},
    cookies={"auth_token": "..."},
    headers={"x-aws-waf-token": "...", "User-Agent": "...", "Origin": "https://www.skool.com"}
)
```

**Deduplication**: Pinned posts appear on every page. Check by `post.id`:
```python
seen = set()
unique = [p for p in all_posts if p['id'] not in seen and not seen.add(p['id'])]
```

### Phase 2 — Comments (~15-20 min, 1,207 posts)

Use ThreadPoolExecutor for parallel fetches. Each post with comments needs one API call (or two if paginated).

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def fetch_comments(session, post_id):
    resp = session.get(f"https://api2.skool.com/posts/{post_id}/comments",
                       params={"group-id": GROUP_ID, "limit": 25, "pinned": "true"})
    # Check has_more → switch to tail=true for subsequent pages
    ...
```

Rate-limit: 1.0s between batches of 5 parallel requests to avoid 429.

### WAF Token Handling

The `aws-waf-token` expires. Refresh strategy:
1. Extract fresh token from Chrome DevTools before each batch
2. If any API call returns 403, stop, extract new token, retry
3. The `auth_token` is stable (1-year JWT)

## Pitfalls

1. **httpOnly auth_token**: Cannot extract via `document.cookie`. Must capture from network request headers (`mcp_chrome_devtools_get_network_request`).
2. **WAF token rotation**: The `aws-waf-token` in localStorage and cookie changes every 30-60 min. Long-running extractions must handle this.
3. **Scheduled maintenance**: Skool occasionally posts maintenance banners that can interfere.
4. **No `__NEXT_DATA__` on client-navigated pages**: The script tag only contains SSR data. After a client-side navigation, the DOM updates but `__NEXT_DATA__` is stale.
5. **Comment count ≠ total interactions**: `metadata.comments` is ONLY top-level comments. Nested replies add 50-100% more volume.
6. **Attachments 403 with bare ID, but downloadable via `read_url`**: The `metadata.attachments` field contains opaque UUIDs that are NOT the file storage keys. `https://assets.skool.com/f/{groupId}/{attachmentId}` returns 403. **BUT** fetch the individual post page — `attachmentsData[].metadata.read_url` or `src_read_url` contains the REAL download URL (different hash), which returns HTTP 200 with the file when accessed with the `auth_token` cookie. This applies to ALL file types (images, archives, PDFs, executables).
7. **`noComment: true` posts**: Some posts have comments disabled. Check this field before fetching comments to save API calls.
8. **Categories not in feed JSON**: The `labels` field is a UUID. Category display names must be extracted from the DOM chip filters.

## Metrics from SQX Traders (actual extraction)

| Metric | Value |
|--------|-------|
| Total posts (unique) | 1,230 |
| Posts with comments | 1,209 |
| Top-level comments | 9,079 |
| Nested replies | 6,867 |
| Posts with attachments | 531 |
| Attachment IDs (unique) | 1,098 |
| Video links | 86 |
| Unique authors | 376 |
| Post content | 863,653 chars |
| Comment content | 1,724,524 chars |
| Reply content | 1,366,912 chars |
| Pages fetched | 41 |
| Time: posts | ~2 min |
| Time: comments (5 parallel) | ~5 min |

### Extraction scripts (reference)

The full extraction pipeline is in `D:/SKOOL/sqxtraders/`:
- `extract_posts.py` — Phases 1 (feed pages, 41 calls)
- `extract_comments.py` — Phase 2 (comments, parallel, 5 workers)
- `download_previews.py` — Phase 3 (image previews from feed)
- `attachment_meta.json` — full attachment inventory with `read_url` download links
