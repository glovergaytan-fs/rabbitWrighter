import os
from dotenv import load_dotenv

load_dotenv()
your_username = os.getenv("YOUR_USERNAME")
your_password = os.getenv('YOUR_PASSWORD')

from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # Set headless to False to see the browser in action
        page = browser.new_page()

        page.goto('https://hole.rabbit.tech')

        # Check if already logged in
        if page.locator('div.mb-6.font-light >> text=journal').count() > 0:
            print("Already logged in, skipping.")
            browser.close()
            return

        # Enter username and password
        page.fill('input#username', 'your_username') # Replace 'your_username' with your actual username
        page.fill('input#password', 'your_password') # Replace 'your_password' with your actual password

        # Click the "continue" button
        page.click('button[type="submit"][data-action-button-primary="true"]') 

        # Wait for the page to load
        page.wait_for_load_state()

        # browser.close()

if __name__ == '__main__':
    main()