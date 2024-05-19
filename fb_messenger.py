import os
import time
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()
your_username = os.getenv("YOUR_USERNAME")
your_password = os.getenv('YOUR_PASSWORD')

def open_facebook_messenger(page):
    """Opens Facebook Messenger in a new tab."""
    page.evaluate("window.open('https://www.messenger.com/', '_blank')")  


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless to False to see the browser in action, I suggest keeping the head until out of dev
        page = browser.new_page()
        logged_in = False  # Flag to check if already logged in
        
        previous_text_content = '' 

        while True:
            page.goto('https://hole.rabbit.tech')

            if not logged_in:
                # Enter username and password
                page.fill('input#username', your_username)  # Replace 'your_username' with your actual username
                page.fill('input#password', your_password)  # Replace 'your_password' with your actual password

                # Click the "continue" button
                page.click('button[type="submit"][data-action-button-primary="true"]') 

                # Wait for the page to load
                page.wait_for_load_state('load')
                logged_in = True  # Set the flag to True after logging in

            page.goto('https://hole.rabbit.tech/journal/details')
            page.wait_for_load_state('load')

            first_item = page.locator('ul li div.line-clamp-1').first
            first_item.click(timeout=60000) 

            # Wait for the content to load
            page.wait_for_timeout(5000)  # Adjust the timeout as needed

            

            
            text_content = page.locator('div.whitespace-pre-wrap.pb-\\[80px\\].text-base.text-white.focus\\:outline-none').inner_text()
           
            print("Text content:", text_content)

            if text_content.lower().startswith("message") and text_content != previous_text_content:
                open_facebook_messenger(page)
                messenger_page = browser.contexts[0].pages[-1]  # Get the newly opened tab 
                messenger_page.wait_for_load_state('load')
                messenger_page.fill('input[aria-label="Search Messenger"]', "shala glover")
                print("Action triggered because the message starts with 'message' and is new")
                

                previous_text_content = text_content 
                print("Pre Text content:", previous_text_content)

        time.sleep(5)

if __name__ == '__main__':
    main()