import asyncio
from playwright.async_api import async_playwright
import os

async def verify():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        # Create a mobile context
        iphone_12 = p.devices['iPhone 12']
        context = await browser.new_context(**iphone_12)
        page = await context.new_page()

        pages = [
            "index.html",
            "blog.html",
            "skup-aut-porady.html"
        ]

        for p_name in pages:
            url = f"http://localhost:8001/{p_name}"
            print(f"Checking {url}...")
            await page.goto(url)
            await page.wait_for_timeout(1000) # Wait for animations
            screenshot_name = f"final_{p_name.replace('.html', '')}_mobile.png"
            await page.screenshot(path=screenshot_name)
            print(f"Saved {screenshot_name}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify())
