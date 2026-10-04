# Browser Automation: Form Interaction Troubleshooting

When the built-in browser tools (`browser_click`, `browser_type`) fail on form elements — especially select/combobox dropdowns — fall back to JavaScript injection via `browser_console`.

## Problem

`browser_click` on a dropdown option returns:
```
CDP error (DOM.getBoxModel): Could not compute box model.
```

This happens when the element is inside a `MenuListPopup` that CDP can't compute a bounding box for. The click is registered (the combobox expands) but the option element itself can't be targeted.

## Solution: JS Injection via browser_console

### Step 1 — Discover form field names

```javascript
// Inspect all form elements
(function() {
  const f = document.forms[0];
  return {
    action: f.action,
    method: f.method,
    elements: Array.from(f.elements).map(e => ({
      name: e.name,
      type: e.type,
      id: e.id
    }))
  };
})()
```

### Step 2 — Find the select's option values

```javascript
// Get all options with their text + value
(function() {
  const sel = document.querySelector('select[name="cid"]');
  return Array.from(sel.options).map(o => ({
    text: o.text,
    value: o.value,
    selected: o.selected
  }));
})()
```

### Step 3 — Set all form values and submit via JS

```javascript
(function() {
  // Set company/select value
  document.querySelector('select[name="cid"]').value = '7367';
  // Set text/password fields
  document.querySelector('input[name="UsrLoginID"]').value = 'username';
  document.querySelector('input[name="UsrPassword"]').value = 'password';
  // Click submit
  document.querySelector('input[type="submit"]').click();
  return 'Form submitted via JS';
})()
```

### Step 4 — Verify login success

Navigate to the root URL or dashboard to confirm:
```
browser_navigate(url="https://example.com/dashboard")
```

Look for the user's name or dashboard elements in the snapshot title or content.

## Variations

**If browser_type on a field seems to work but doesn't persist:**
The form may reset on certain events. Use JS to set values directly instead:

```javascript
document.querySelector('input[name="fieldName"]').value = 'value';
```

**If clicking the submit button also fails:**
Use JS to submit the form instead of clicking:

```javascript
document.forms[0].submit();
// OR
document.querySelector('input[type="submit"]').click();
```

**If the page is inside an iframe:**
Access the iframe content first:

```javascript
document.querySelector('iframe').contentDocument.querySelector('...')
```

**Check for CSRF tokens:**
Hidden fields like `csrf_token` or `resetpwd` are usually auto-populated by the server form. JS-based submission preserves these naturally — don't try to remove them.

## Why this works

CDP's `DOM.getBoxModel` requires the element to be rendered in the layout tree. Some popup/overlay elements (especially native `<select>` options in `MenuListPopup`) are rendered by the browser's internal UI layer, not the page DOM layout — CDP can't compute their box model. JavaScript DOM manipulation bypasses CDP entirely and interacts with the browser's rendering engine directly.

## Limitations

- Some SPA frameworks use synthetic events — calling `.click()` on the element may not trigger the framework's event listeners. Try `.dispatchEvent(new Event('submit', {bubbles: true}))` or fire the framework-specific event.
- If the site has a CSP that blocks inline script execution, `browser_console` may be the only way (it runs in the page context, not via `<script>` injection).
- httpOnly cookies set during login won't be readable from JS but are automatically attached to subsequent requests.
