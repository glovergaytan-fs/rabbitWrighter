from playwright.sync_api import sync_playwright
import os
import time
from dotenv import load_dotenv

load_dotenv()
your_username = os.getenv("YOUR_USERNAME")
your_password = os.getenv('YOUR_PASSWORD')
fb_email = os.getenv("FB_EMAIL")
fb_password = os.getenv('FB_PASSWORD')

def open_facebook_messenger(browser, text_content): 
    new_tab = browser.new_page()  # Create a new tab
    new_tab.goto('https://www.messenger.com/t/100025019884233') 
    new_tab.wait_for_load_state('load') 
    new_tab.fill('input[aria-label="Email or phone number"]', fb_email)
    new_tab.fill('input[aria-label="Password"]', fb_password)
    new_tab.click('text="Continue"')
    new_tab.wait_for_load_state('load') 
    # time.sleep(16)
    new_tab.click('div[aria-label="Close"]')
    new_tab.click('text="Don\'t sync"')
    new_tab.wait_for_load_state('load') 
    new_tab.fill('div[aria-label="Message"]', text_content)
    new_tab.press('div[aria-label="Message"]', 'Enter')
    print('i am here')
    
def search_messenger(page, contact_name):
    """Searches for a contact in Messenger and opens the conversation."""
    page.fill('input[aria-label="Search Messenger"]', contact_name)
    # Add logic here to select the correct contact from search results
    # For example, wait for the results to appear and then click on the first one
    page.wait_for_selector('div[role="listbox"]') # Wait for search results
    page.locator('div[role="listbox"] >> div[role="option"]').first.click() 

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) 
        page = browser.new_page()
        logged_in_hole = False 
        previous_text_content = '' 

        while True:
            page.goto('https://hole.rabbit.tech')

            if not logged_in_hole:
                page.fill('input#username', your_username)
                page.fill('input#password', your_password)
                page.click('button[type="submit"][data-action-button-primary="true"]') 
                page.wait_for_load_state('load')
                logged_in_hole = True

            page.goto('https://hole.rabbit.tech/journal/details')
            page.wait_for_load_state('load')
            first_item = page.locator('ul li div.line-clamp-1').first
            first_item.click(timeout=60000) 
            page.wait_for_timeout(5000)
            text_content = page.locator('div.whitespace-pre-wrap.pb-\\[80px\\].text-base.text-white.focus\\:outline-none').inner_text()
            print("Text content:", text_content)

            if 'message' in text_content.lower() and text_content != previous_text_content:
                open_facebook_messenger(browser, text_content)
                print("Action triggered because the message starts with 'message' and is new")
                previous_text_content = text_content 
                print("Pre Text content:", previous_text_content)

            time.sleep(60) 

if __name__ == '__main__':
    main()