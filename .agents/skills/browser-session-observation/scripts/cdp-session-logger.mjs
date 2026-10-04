// cdp-session-logger.mjs — passive DOM+network observer for ONE Chrome instance.
// Usage: node cdp-session-logger.mjs <browserWsUrl> <logPath>
// Appends JSONL: {ts, layer:"user"|"cdp", kind, ...}. Never clicks or navigates.
import fs from 'node:fs';

const [BROWSER_WS, LOG] = process.argv.slice(2);
if (!BROWSER_WS || !LOG) { console.error('usage: node cdp-session-logger.mjs <browserWsUrl> <logPath>'); process.exit(2); }

const out = fs.createWriteStream(LOG, { flags: 'a' });
const log = (obj) => out.write(JSON.stringify({ ts: new Date().toISOString(), ...obj }) + '\n');

const HOOK = `(() => {
  if (window.__ivhook) return; window.__ivhook = true;
  const sel = (el) => { if (!el || !el.tagName) return '';
    if (el.id) return '#' + el.id;
    let p = el.tagName.toLowerCase(); const t = (el.innerText||el.value||'').trim().slice(0,60);
    if (el.className && typeof el.className === 'string') p += '.' + el.className.trim().split(/\\s+/).slice(0,2).join('.');
    return p + (t ? ' "' + t + '"' : ''); };
  const send = (kind, d) => console.log('__HOOK__' + JSON.stringify({ kind, ...d }));
  document.addEventListener('click', (e) => send('click', { sel: sel(e.target), x: e.clientX, y: e.clientY, url: location.href }), true);
  document.addEventListener('input', (e) => { const t = e.target;
    const isPass = t.type === 'password';
    send('input', { sel: sel(t), type: t.type || t.tagName, name: t.name || t.placeholder || '', len: String(t.value ?? '').length, val: isPass ? undefined : String(t.value ?? '').slice(0, 500), url: location.href }); }, true);
  document.addEventListener('change', (e) => send('change', { sel: sel(e.target), url: location.href }), true);
  document.addEventListener('submit', (e) => send('submit', { sel: sel(e.target), url: location.href }), true);
  document.addEventListener('keydown', (e) => { if (e.key === 'Enter') send('enter', { sel: sel(e.target), url: location.href }); }, true);
  let st = null;
  document.addEventListener('scroll', () => { clearTimeout(st); st = setTimeout(() => send('scroll', { y: Math.round(scrollY), url: location.href }), 800); }, true);
})();`;

let msgId = 0;
const pending = new Map();
const attachedTargets = new Set();
let ws = null;

function send(method, params = {}, sessionId) {
  return new Promise((resolve) => {
    const id = ++msgId;
    pending.set(id, resolve);
    const m = { id, method, params };
    if (sessionId) m.sessionId = sessionId;
    ws.send(JSON.stringify(m));
    setTimeout(() => { if (pending.has(id)) { pending.delete(id); resolve(null); } }, 8000);
  });
}

async function attachToTarget(targetId) {
  if (attachedTargets.has(targetId)) return;
  attachedTargets.add(targetId);
  const r = await send('Target.attachToTarget', { targetId, flatten: true });
  if (!r || !r.sessionId) return;
  const s = r.sessionId;
  await send('Page.enable', {}, s);
  await send('Runtime.enable', {}, s);
  await send('Network.enable', {}, s).catch(() => null);
  await send('Log.enable', {}, s).catch(() => null);
  await send('Page.addScriptToEvaluateOnNewDocument', { source: HOOK }, s).catch(() => null);
  await send('Runtime.evaluate', { expression: HOOK }, s).catch(() => null);
  log({ layer: 'cdp', kind: 'attached', target: targetId.slice(0, 8) });
}

function onEvent(method, params) {
  const t = (params && (params.targetInfo || params.target)) || {};
  switch (method) {
    case 'Target.targetCreated':
      if (t.type === 'page') { log({ layer: 'cdp', kind: 'tab-open', title: t.title, url: t.url }); attachToTarget(t.targetId); }
      break;
    case 'Target.targetInfoChanged':
      if (t.type === 'page') log({ layer: 'cdp', kind: 'tab-update', title: t.title, url: t.url });
      break;
    case 'Target.targetDestroyed': log({ layer: 'cdp', kind: 'tab-close', target: (params.targetId || '').slice(0, 8) }); break;
    case 'Page.frameNavigated': { const f = params.frame || {}; if (!f.parentId) log({ layer: 'cdp', kind: 'navigate', url: f.url }); break; }
    case 'Page.loadEventFired': log({ layer: 'cdp', kind: 'loaded' }); break;
    case 'Network.requestWillBeSent': { const r = params.request || {}; if (r.url && !r.url.startsWith('data:')) log({ layer: 'cdp', kind: 'request', method: r.method, url: String(r.url).slice(0, 300) }); break; }
    case 'Network.responseReceived': { const r = params.response || {}; log({ layer: 'cdp', kind: 'response', status: r.status, url: String(r.url || '').slice(0, 300) }); break; }
    case 'Network.loadingFailed': log({ layer: 'cdp', kind: 'load-failed', url: String(params.errorText || '').slice(0, 200) }); break;
    case 'Runtime.consoleAPICalled': {
      const txt = (params.args || []).map((a) => a.value ?? a.description ?? a.type).join(' ');
      if (txt.startsWith('__HOOK__')) { try { log({ layer: 'user', ...JSON.parse(txt.slice(8)) }); } catch { /* noop */ } }
      else if (txt.trim()) log({ layer: 'cdp', kind: 'console', text: txt.slice(0, 500) });
      break;
    }
    case 'Runtime.exceptionThrown': log({ layer: 'cdp', kind: 'page-error', text: String((params.exceptionDetails || {}).text || '').slice(0, 300) }); break;
    case 'Log.entryAdded': { const e = params.entry || {}; log({ layer: 'cdp', kind: 'log', level: e.level, text: String(e.text || '').slice(0, 300), url: String(e.url || '').slice(0, 200) }); break; }
  }
}

function connect() {
  ws = new WebSocket(BROWSER_WS);
  ws.onopen = async () => {
    log({ layer: 'cdp', kind: 'logger-connected' });
    await send('Target.setDiscoverTargets', { discover: true });
    const targets = await send('Target.getTargets');
    for (const t of (targets && targets.targetInfos) || []) if (t.type === 'page') attachToTarget(t.targetId);
  };
  ws.onmessage = (ev) => {
    let m; try { m = JSON.parse(ev.data); } catch { return; }
    if (m.id && pending.has(m.id)) { pending.get(m.id)(m.result); pending.delete(m.id); return; }
    if (m.method) onEvent(m.method, m.params || {});
  };
  ws.onclose = () => { log({ layer: 'cdp', kind: 'logger-reconnect' }); setTimeout(connect, 3000); };
  ws.onerror = () => { try { ws.close(); } catch { /* noop */ } };
}

const stop = () => { log({ layer: 'cdp', kind: 'logger-stopped' }); process.exit(0); };
process.on('SIGINT', stop); process.on('SIGTERM', stop);
connect();
log({ layer: 'cdp', kind: 'logger-started' });
