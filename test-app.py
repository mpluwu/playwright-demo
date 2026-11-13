from playwright.sync_api import sync_playwright, expect
import re

print("🤖 Starting the Playwright Robot...")

with sync_playwright() as p:
    print("🌐 Opening Chromium...")
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    
    # 1. Create a "Context" (a blank browser session) and START RECORDING
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    
    # Open the actual tab inside our recording context
    page = context.new_page()
    
    print("🎯 Navigating to the ML App...")
    page.goto("http://localhost:8501")
    expect(page).to_have_title(re.compile("Streamlit"))
    
    print("⌨️ Typing house size: 2000...")
    size_input = page.get_by_label("House Size (Square Feet)")
    size_input.fill("2000")
    
    print("🖱️ Clicking 'Estimate Price'...")
    estimate_button = page.get_by_role("button", name="Estimate Price")
    estimate_button.click()
    
    print("⏳ Waiting for the ML prediction to render...")
    output_text = page.get_by_text("Estimated Price:")
    expect(output_text).to_be_visible(timeout=10000)
    
    # 2. STOP RECORDING and save the report as a zip file
    print("📁 Saving the Playwright Report...")
    context.tracing.stop(path="trace.zip")
    
    print("✅ Success! Closing down.")
    browser.close()
