# SCORM / Legacy LMS Automation

Patterns for automating legacy enterprise learning management systems (LMS) built on framesets, SCORM 1.2/2004, and form-based login — common in oil & gas, chemical, and industrial training portals (WorKingbird, OverNite Software, etc.).

## Characteristics of Legacy LMS Platforms

- **Frameset-based rendering**: The page structure uses `<table>` layouts and legacy HTML. `document.documentElement.outerHTML` may return `<html><head></head><body></body></html>` (empty DOM) even though the accessibility tree shows content. This happens because the frame content isn't accessible via the parent document's DOM.
- **Custom combobox widgets**: Company/tenant selection uses native `<select>` elements inside complex table layouts. CDP's `DOM.getBoxModel` fails on the popup options.
- **Form-based login**: No API endpoints — all authentication is POST form submission.
- **SCORM launch via new window**: The "Run Course" button submits a hidden form with `target='_new'`, opening the SCORM player in a popup window.
- **Session tied to frameset**: Navigating away (e.g., typing a new URL) may log you out because the session is maintained within the frameset context.

## Login Flow

### Problem: CDP can't click combobox options

```javascript
// browser_click on dropdown option returns:
// CDP error (DOM.getBoxModel): Could not compute box model.
```

### Solution: JS injection via browser_console

**Step 1 — Discover form fields:**
```javascript
(function() {
  const f = document.forms[0];
  return {
    action: f.action,
    method: f.method,
    elements: Array.from(f.elements).map(e => ({
      name: e.name, type: e.type, id: e.id
    }))
  };
})()
```

**Step 2 — Find the company/tenant select values:**
```javascript
(function() {
  const sel = document.querySelector('select[name="cid"]');
  return Array.from(sel.options).map(o => ({
    text: o.text, value: o.value, selected: o.selected
  }));
})()
```

**Step 3 — Set all values and submit via JS:**
```javascript
(function() {
  document.querySelector('select[name="cid"]').value = '7367'; // company ID
  document.querySelector('input[name="UsrLoginID"]').value = 'username';
  document.querySelector('input[name="UsrPassword"]').value = 'password';
  document.querySelector('input[type="submit"]').click();
  return 'Login submitted';
})()
```

**Step 4 — Verify:** After submission, take a snapshot to confirm the dashboard loaded.

> **Pitfall**: Navigating to a URL after login (e.g., `browser_navigate("https://example.com/")`) may redirect back to the login page because the session is linked to the frameset context. To maintain the session, interact within the current page rather than navigating away.

## SCORM Course Launch

### Problem: "Run Course" opens a new window

The SCORM launch uses a hidden form with `target='_new'` and `window.open()`:
```javascript
// From Cell_Launch.RunCourse('SCORM', 1):
document.cell_launch_form.target = '_new';
var content_window = window.open("", "_new");
document.cell_launch_form.submit();
```

Our browser tools cannot access the popup window. Clicking "Run Course" with `browser_click` navigates the page to `about:blank`.

### Solution: Override the form target to _self before submitting

**Step 1 — Inspect the form fields to understand what's being submitted:**
```javascript
document.cell_launch_form
  ? Array.from(document.cell_launch_form.elements).map(function(e) {
      return {name: e.name, value: e.value, type: e.type};
    })
  : 'n/a'
```

**Step 2 — Modify target and submit in the same window:**
```javascript
(function() {
  // Find the URL builder function
  // Or use the known pattern: index.pl?pg=Launch&cmd=Scorm
  document.cell_launch_form.action = URL.Page('Launch', 'Scorm');
  document.cell_launch_form.target = '_self';
  document.cell_launch_form.submit();
  return 'Submitting in same window...';
})()
```

The `URL.Page('Launch', 'Scorm')` function resolves to the SCORM launcher endpoint. If that function is unavailable, the pattern is typically `https://lms.example.com/index.pl?pg=Launch&cmd=Scorm`.

### Step 3 — Interact with the SCORM player

After the form submits in the same window, the SCORM player loads inside an iframe structure. The accessibility tree shows:

```
- Iframe [ref=e1]
- Iframe [ref=e2]
  - generic "Course Title"
    - generic
      - button "Resume" [ref=e5]
      - button "Restart" [ref=e4]
- Iframe [ref=e3]
```

Click "Resume" to continue from where you left off, or "Restart" to begin from the start.

## SCORM Player Navigation

Once inside the player, the interface typically has:

### Sidebar (course menu)
- **Tree view** of lessons/modules, each expandable via `expanded` state
- **Tabs**: "Menu" (table of contents) and "Narration" (transcript)
- Each treeitem shows visited/not-visited status

### Playback controls
- **Pause/Replay** buttons
- **Next** button to advance slides
- **Volume** slider
- **Slide progress** slider

### Top bar
- **HELP**, **RESOURCES**, **GLOSSARY** buttons

### Interacting with the player

```javascript
(function() {
  var all = document.querySelectorAll('[onclick]');
  var results = [];
  all.forEach(function(el) {
    var txt = el.textContent.trim().substring(0, 100);
    results.push({tag: el.tagName, text: txt, onclick: el.getAttribute('onclick')});
  });
  return results;
})()
```

The snapshot ref IDs change on each snapshot, so always take a fresh snapshot before clicking.

## Extracting Course Narration / Transcript Text from Articulate Storyline SCORM

When a SCORM course is built with Articulate Storyline, the narration/transcript text is stored in data files within the SCORM package. This technique extracts the full narrative content without playing through the entire course.

### Step 1 — Find the content URL from the frameset

After launching the SCORM course, inspect the page structure:

```javascript
document.documentElement.outerHTML.substring(0, 4000)
```

Look for the `<frameset>` and the `content` frame:

```html
<frameset frameborder="0" framespacing="0" cols="0,*,1">
  <frame name="menu" src="...">
  <frame name="content" src="https://lms.example.com/ext/evt/000/000/051/502/scorm/index_lms.html">
  <frame name="code" src="...">
</frameset>
```

Also check the JSON suspend data embedded in the page for course structure:

```javascript
// In the parent page's JavaScript:
aTemp[0] = {
  status: "incomplete",
  suspend: "...",
  lnk: "/ext/evt/000/000/051/502/scorm/index_lms.html",
  ttl: "Course Title"
};
```

### Step 2 — Read the content frame

Since the frames are same-origin, you can access the content frame directly:

```javascript
// Get the content frame document
var doc = window.frames['content'].document;
var text = doc.body.textContent;

// Or check the full HTML
doc.documentElement.outerHTML;

// List loaded scripts to find data files
var scripts = doc.querySelectorAll('script[src]');
var srcs = [];
for(var i=0; i<scripts.length; i++) {
  srcs.push(scripts[i].src);
}
srcs.join(', ');
```

Typical script URLs in an Articulate Storyline SCORM:

```
.../scorm/lms/scormdriver.js
.../scorm/html5/lib/scripts/frame.desktop.min.js
.../scorm/html5/data/js/frame.js          ← THE DATA FILE
.../scorm/html5/lib/scripts/slides.min.js
.../scorm/story_content/triggers.js
.../scorm/story_content/user.js
.../scorm/html5/lib/scripts/bootstrapper.min.js
```

### Step 3 — Fetch the frame.js data file (contains narration text)

The `frame.js` file in `html5/data/js/` contains the slide data including all narration text. Fetch it directly:

```
web_extract(urls=["https://lms.example.com/.../scorm/html5/data/js/frame.js"])
```

The file is JavaScript that calls `window.globalProvideData('frame', '{...}')` with a JSON string argument. The JSON includes several key sections:

| JSON key | Contents |
|----------|----------|
| `notesData` | **The narration/transcript text** — an array of slide objects, each with `content` (the full slide text/narration) and `slideId`. This IS the transcript equivalent of the course audio. |
| `glossaryData` | Glossary terms with `title` and `content` (definitions). |
| `outline` | Course menu tree with slide titles, scenes, and hierarchy. |

The JSON is minified and the content text uses markdown-like formatting (`**bold**`, `*italic*`, bullet lists). Parse the JSON programmatically rather than scanning the raw text:

```python
import json, re

# Extract JSON from the JS wrapper
match = re.search(r"window\.globalProvideData\('frame',\s*'(.*?)'\)", js_text, re.DOTALL)
raw = match.group(1).replace("\\'", "'").replace('\\n', '\n')
data = json.loads(raw)

# Get all narration text per slide
for slide in data['notesData']:
    print(f"--- {slide['slideId']} ---")
    print(slide['content'])
```

> **Quiz note**: Knowledge Check and Final Test questions/answers are NOT stored as structured quiz data in `frame.js`. They appear as **inline text** within the `notesData` slide content (e.g. "Select the correct answer and click SUBMIT."). The actual correct/incorrect answer mappings and scoring logic are in the binary SCORM communication layer, not accessible from the data files. Use the narration text as a study guide; the Final Test answers must be inferred from it.

### Step 4 — Parse the narration text from the response

The `frame.js` file contains the course content as plain text embedded in JavaScript object literals. Key text patterns to look for:

- **Welcome/introduction**: "Welcome to the [Course Title] course..."
- **Slide content**: Text paragraphs after each slide title
- **Knowledge checks**: "Select the correct answer and click SUBMIT."
- **Lesson transitions**: "Click on each [topic] to learn more."
- **Glossary**: Definitions of key terms (Accident, Hazard, Risk, etc.)

The narration text is the voice-over script — what the course narrator says on each slide. Extract it by scanning the raw file content for complete paragraphs between known slide boundaries.

### Course structure (common Articulate Storyline pattern)

```
1. Course Title (cover slide)
2. Introduction / Welcome
3. Regulations and Standards
4. Assessing Hazards and Personal Risk
5. Lesson 1: [Topic]
   - Sub-topic A
   - Are You At Risk?
   - Knowledge Check
   - Sources of [Topic]
   - Knowledge Check
   - When Should You...?
   - Knowledge Check
6. Lesson 2: [Topic]
   - Taming Hazards
   - Knowledge Check
   - Hazard Types
   - Knowledge Check
   - Seeing Hazards...
7. Lesson 3: [Topic]
   - What To Do? (scenarios)
   - Use Common Sense
   - The ABCs of Classifying Hazards
   - Neighborly Hazard Hunt (interactive)
   - Reporting
   - In Summary
   - Knowledge Check
8. Final Test
```

### Why this works

Articulate Storyline publishes SCORM packages that bundle all slide data as JavaScript objects in `frame.js`. The narration text is the same text that appears in the "Narration" sidebar tab when viewing the course in a browser. It is the full voice-over script and on-screen text combined, organized by slide.

This technique avoids:
- Clicking through every slide manually
- Trying to access cross-origin iframe content
- Playing through video/audio files
- OCR or screen scraping

### Pitfalls

- The `frame.js` URL is by GUID/ID — each course deployment has a unique path. Find it from the script tags in the content frame.
- The text mixes UI labels ("Rectangle 1", "Group 3") with actual content. Filter those out.
- Knowledge check questions and answer choices are interleaved with the narration text — they are part of the course flow.
- The extracted text is the narrative content, NOT a verbatim transcript of every word in any embedded videos. It's the equivalent of reading the course slides + narrator script.
- This only works for Articulate Storyline courses. Other authoring tools (Adobe Captivate, Lectora, iSpring) store data differently.

## Articulate Storyline Final Test / Quiz Patterns

When a SCORM course built with Articulate Storyline includes a Final Test or Knowledge Checks, the quiz structure has specific characteristics that affect automation.

### Quiz data location

Quiz questions, answer choices, and correct/incorrect mappings are **NOT** stored as structured data in `frame.js`. The `notesData` JSON contains only the narration text, which includes the question text and answer choices as inline content (e.g. "Select the correct answer and click SUBMIT.") but not the scoring logic. The actual answer mapping and scoring is handled by the Storyline player's internal API and communicated via the SCORM runtime API — not accessible from the data files.

### Strategy: read-first-then-answer

Since programmatic quiz submission is unreliable, use a two-phase approach:

**Phase 1 — Extract all course content from frame.js** (see "Extracting Course Narration" section above). This gives you the narrative text that contains the course's key facts, definitions, procedures, and principles — everything needed to deduce correct answers.

**Phase 2 — Navigate the quiz to read each question** via the NEXT button, then compile an answer key from the narration text. This is a study-guide approach, not auto-submission.

### Navigating quiz questions

Once the Final Test screen loads with the START button:

```javascript
// Click START to begin
var f = window.frames[1];
var btns = f.document.querySelectorAll('button');
for(var i=0; i<btns.length; i++) {
  if(btns[i].textContent.trim() === 'START') {
    btns[i].click(); break;
  }
}
```

To advance through questions (reads them without submitting — use for reconnaissance):

```javascript
var f = window.frames[1];
var btns = f.document.querySelectorAll('button');
for(var i=0; i<btns.length; i++) {
  if(btns[i].textContent.trim() === 'NEXT') {
    btns[i].click(); break;
  }
}
```

### Quiz UI structure (from accessibility tree)

**Multiple Choice questions:**
```
- radiogroup
  - radio "button template blue.png" [checked=false, ref=e19]
  - radio "button template blue.png" [checked=false, ref=e20]
  - radio "button template blue.png" [checked=false, ref=e21]
  - radio "button template blue.png" [checked=false, ref=e22]
- paragraph > strong > StaticText "Option 1 text"
- paragraph > strong > StaticText "Option 2 text"
...
- button "SUBMIT" [ref=e18]  ← non-functional via JS
```

**Select All That Apply (checkboxes):**
```
- generic > checkbox "button template blue.png" [checked=false, ref=e19]
- paragraph > strong > StaticText "Option 1 text"
- generic > checkbox "button template blue.png" [checked=false, ref=e20]
...
```

**Matching / Drag & Drop:**
```
- strong > StaticText "First/Second/Third/Fourth"
- strong > StaticText "Elimination/Engineering controls/PPE/etc."
```
These are drag-and-drop interactions that cannot be automated via DOM manipulation.

### Quiz question randomization

Articulate Storyline randomizes the **order** of Final Test questions on each attempt. The same question bank is drawn from, but the sequence changes. Always identify questions by their **content text** (e.g. "Many safety regulations come from:") not by their position in the test.

### The SUBMIT button problem

The Storyline SUBMIT button **cannot be triggered programmatically** via JS. Reasons discovered:

1. **No onclick attribute**: `button.getAttribute('onclick')` returns `null` — event listeners are attached via Storyline's internal event system, not standard DOM APIs.
2. **No addEventListener hooks**: `getEventListeners(button)` (DevTools only) shows the listener is attached to a parent container, not the button itself.
3. **Element covered**: `document.elementFromPoint(x, y)` returns a `.media-loader-container` DIV over the button.
4. **Button at (0,0)**: `getBoundingClientRect()` returns coordinates at (0,0) for the submit button when inside certain view states — the button exists in DOM but is not visually rendered.

```javascript
// Verification — all fail:
button.click()                    // No effect
new MouseEvent('click') dispatch  // No effect
button.dispatchEvent(click)       // No effect
```

**Workaround**: Storyline's internal `GetPlayer()` API does not expose submit or next methods. The player object only has:
```
GetVar, SetVar, object, setVar, getVar, once, addForTriggers, addToTimeline,
emphasis, pointerX, pointerY, slideWidth, slideHeight, hidePointer, showPointer,
update, keyDown, getKeyDown, keydown, keyup
```

No `Submit`, `Next`, or navigation methods are exposed. The only reliable way to submit quiz answers is via physical user interaction (mouse click in a real browser).

### Hidden feedback buttons

The Storyline player DOM contains hidden "Correct" and "Incorrect" buttons that appear/disappear based on answer feedback. Their presence in the DOM does not indicate whether the previous answer was right or wrong — their `display`/`visibility` is controlled by Storyline's internal state:

```
button "Correct"  [index=3]
button "Incorrect" [index=4]
```

These are in the same button list as visible UI controls. Check `window.getComputedStyle(el).display` to determine actual visibility.

### Answer key compilation strategy

Since you cannot submit answers programmatically, compile a reference answer key from the `frame.js` narration text:

1. Extract the full `notesData` array (see "Extracting Course Narration" above)
2. The narration text contains ALL course facts organized by slide
3. Map each quiz question to the corresponding lesson section
4. Produce a written answer key the user can follow while taking the test

Common question patterns in "Field Hazard Recognition" type courses:

| Course Topic | Likely Questions |
|-------------|-----------------|
| Sources of hazards | People, Equipment/Materials, Surroundings |
| Hazard types | Psychological, Physical, Chemical, Biological |
| Hierarchy of controls | Elimination → Engineering → Administrative → PPE |
| When to look for hazards | Planning, While underway, After incident |
| ABC classification | A=Extreme, B=Dangerous, C=Minor |
| Hazard report contents | Time/date, contact, witnesses, location, equipment, description, assessment, recommendations |
| Chemical safety | Communication is critical |
| Biological hazards | Sewage, blood, viruses, mold, animals |
| Psychological hazards | Fatigue, stress, long hours, shift work |

### Pitfalls

- **NEXT vs SUBMIT**: Clicking NEXT advances the slide without recording the answer. The quiz scorer only counts SUBMIT clicks. On the results slide, a score of 7.14% (1/14) means only one answer was registered — the rest were skipped.
- **Question randomization**: Each retake presents a different question order. Cannot rely on "question 3" being the same topic each time.
- **Drag-and-drop questions (Matching type)**: These cannot be automated via JS — they require mouse drag events that Storyline's custom event system processes differently from standard HTML5 drag events. Skip these when possible and answer them manually.
- **SUBMIT & EXIT vs SUBMIT**: The results screen has both "SUBMIT & EXIT" and a separate "SUBMIT" button. The former submits the score and closes the course; the latter may be for retake confirmation.
- **RETAKE TEST vs Restart**: "RETAKE TEST" takes you back to the Final Test instructions (with a START button). "Restart" resets the entire course from the beginning.
- **Button matching**: Storyline buttons in the accessibility tree show truncated/odd text like "Snip Diagonal Corner 2" or "Group 1" for styled buttons. Match by position in the button list or by surrounding text content, not by button label alone.

## Session Persistence

Legacy LMS platforms often use **session-per-frameset** — the session token is embedded in the frameset page and doesn't survive navigation to a fresh URL:

| Action | Session preserved? |
|--------|-------------------|
| Form submit in same frame | Yes |
| `browser_navigate` to other URL | Usually No — redirected to login |
| Refresh via `browser_snapshot` | Yes (works within same page load) |
| JS submit with target=_self | Yes |

**Workflow to maintain session:**
1. Login via JS form submit (not browser_navigate)
2. Click training item via browser_click (stays in frameset)
3. Launch SCORM via JS target=_self modification (stays in frameset)
4. Interact within the SCORM iframe
5. Never call browser_navigate unless you want to re-login
