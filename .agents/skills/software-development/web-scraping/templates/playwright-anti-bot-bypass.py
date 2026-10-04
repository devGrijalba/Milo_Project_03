#!/usr/bin/env python3
"""
Playwright anti-bot bypass template for sites using disable-devtool (theajack).

This script demonstrates how to:
1. Intercept JS bundles via Playwright route() API
2. Patch disable-devtool's about:blank redirect
3. Override window.open/close to prevent redirect hijacking
4. Mock native bridge checks (St() function)

Target: any site that uses the disable-devtool library to block automation.

Usage:
    pip install playwright
    playwright install chromium
    python bypass_playwright.py
"""

import asyncio
import json
from playwright.async_api import async_playwright

TARGET_URL = "https://example.com"
PHONE = ""
PASSWORD = ""

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-automation",
                "--no-sandbox",
                "--window-size=1920,1080",
            ]
        )
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                       "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            locale="es-CO",
            timezone_id="America/Bogota",
        )
        page = await context.new_page()
        
        console_logs = []
        page.on("console", lambda msg: console_logs.append(f"[{msg.type}] {msg.text[:200]}"))
        page.on("pageerror", lambda err: console_logs.append(f"[PAGE_ERROR] {err}"))

        # --- JS Interception: patch anti-bot code at network level ---
        async def intercept_js(route):
            url = route.request.url
            if any(kw in url for kw in ["diLS-A9T", "main.", "app.", "bundle"]):
                response = await route.fetch()
                body = await response.text()
                
                # Patch 1: disable-devtool redirect to about:blank
                body = body.replace(
                    'window.location.href=w.timeOutUrl||"https://theajack.github.io',
                    'void(0)'
                )
                # Patch 2: window.open("about:blank","_self")
                body = body.replace(
                    'window.open("about:blank","_self")',
                    '({location:{href:""}})'
                )
                # Patch 3: window.close()
                body = body.replace(
                    'window.close()',
                    'void(0)'
                )
                # Patch 4: native bridge check St()
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
        
        # --- Init script: override window.open/close at document level ---
        await page.add_init_script("""
            const _origOpen = window.open;
            window.open = function(url, target, features) {
                if (url === 'about:blank' || !url) {
                    return { location: { href: '' } };
                }
                return _origOpen.call(window, url, target, features);
            };
            window.close = function() {};
        """)
        
        # --- Navigate ---
        print(f"[*] Navigating to {TARGET_URL}")
        try:
            await page.goto(TARGET_URL, wait_until="domcontentloaded", timeout=60000)
        except Exception as e:
            print(f"[!] Nav warning: {e}")
        
        await page.wait_for_timeout(10000)
        
        url = page.url
        print(f"[*] URL: {url}")
        print(f"[*] Title: '{await page.title()}'")
        
        if "about:blank" not in url:
            print("[+] SUCCESS: Page loaded!")
            await page.screenshot(path="bypass_success.png", full_page=True)
            
            # Try to find login elements
            for selector in ["text=Entrar", "text=Login", "button", "input"]:
                els = await page.query_selector_all(selector)
                for el in els[:5]:
                    try:
                        text = await el.inner_text()
                        if text.strip():
                            print(f"  [{selector}]: {text[:60]}")
                    except:
                        pass
        else:
            print("[-] Page still at about:blank")
            state = await page.evaluate("""() => ({
                url: window.location.href,
                readyState: document.readyState,
                bodyLen: document.body ? document.body.innerHTML.length : 0,
            })""")
            print(f"  State: {json.dumps(state)}")
        
        print(f"\n[*] Console logs (last 20):")
        for log in console_logs[-20:]:
            print(f"  {log}")
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
