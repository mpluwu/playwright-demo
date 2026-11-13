from playwright.sync_api import sync_playwright, expect
import re

print("🤖 Starting the Playwright Robot...")

# This starts Playwright directly without needing PyTest
with sync_playwright() as p:
    
    # 1. Launch the browser visibly (headless=False) and slowly (slow_mo=1000)
    print("🌐 Opening Chromium...")
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    page = browser.new_page()
    
    # 2. Go to the Streamlit app
    print("🎯 Navigating to the ML App...")
    page.goto("http://localhost:8501")
    expect(page).to_have_title(re.compile("Streamlit"))
    
    # 3. Type the house size
    print("⌨️ Typing house size: 2000...")
    size_input = page.get_by_label("House Size (Square Feet)")
    size_input.fill("2000")
    
    # 4. Click the button
    print("🖱️ Clicking 'Estimate Price'...")
    estimate_button = page.get_by_role("button", name="Estimate Price")
    estimate_button.click()
    
    # 5. Wait for the ML model result
    print("⏳ Waiting for the ML prediction to render...")
    output_text = page.get_by_text("Estimated Price:")
    expect(output_text).to_be_visible(timeout=10000)
    
    print("✅ Success! The ML prediction appeared. Closing down.")
    browser.close()
