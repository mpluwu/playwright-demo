import re
from playwright.sync_api import Page, expect

def test_house_price_prediction(page: Page):
    # 1. Go to the local Streamlit app
    page.goto("http://localhost:8501")
    
    # 2. Make sure the app actually loaded
    expect(page).to_have_title(re.compile("Streamlit"))
    
    # 3. Find the number box by its label and type "2000" into it
    size_input = page.get_by_label("House Size (Square Feet)")
    size_input.fill("2000")
    
    # 4. Click the "Estimate Price" button
    estimate_button = page.get_by_role("button", name="Estimate Price")
    estimate_button.click()
    
    # 5. Wait to see if the "Estimated Price:" text shows up on the screen
    output_text = page.get_by_text("Estimated Price:")
    expect(output_text).to_be_visible(timeout=10000)