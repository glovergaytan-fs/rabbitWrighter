from playwright.sync_api import sync_playwright
import time
from datetime import datetime
import re
import os
from dotenv import load_dotenv

load_dotenv()
your_username = os.getenv("YOUR_USERNAME")
your_password = os.getenv('YOUR_PASSWORD')
fb_email = os.getenv("FB_EMAIL")
fb_password = os.getenv('FB_PASSWORD')

def parse_message(text):
    recipient = None
    message = None
    pattern = r"message to (\w+)"
    match = re.search(pattern, text)
    if match:
        recipient = match.group(1)
    else:
        print("The phrase 'message to' was not found in the string.")
    index = text.find("content")
    if index != -1:
        message = text[index + len("content"):].strip()
    else:
        print("The word 'content' was not found in the string.")
    if recipient is None or message is None:
        print("Could not parse recipient or message from the text")
    return recipient, message

def journal():
    today = datetime.now()
    return f"journal-bar-{today.year}-{today.month:02}-{today.day:02}"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        hole_page = browser.new_page()
        discord_page = browser.new_page()
        logged_in_hole = False
        previous_text_content = ''
        logged_in_dc = False

        # Log into hole.rabbit.tech
        hole_page.goto("https://hole.rabbit.tech")
        if not logged_in_hole:
            hole_page.fill('input#username', your_username)
            hole_page.fill('input#password', your_password)
            hole_page.click('button[type="submit"][data-action-button-primary="true"]')
            hole_page.wait_for_load_state('load')
            logged_in_hole = True

        # Log into Discord
        discord_page.goto("https://discord.com/login")
        if not logged_in_dc:
            discord_page.fill('input[name="email"]', your_username)
            time.sleep(1)
            discord_page.fill('input[name="password"]', your_password)
            discord_page.keyboard.press("Enter")
            time.sleep(10)
            logged_in_dc = True

        while True:
            hole_page.goto('https://hole.rabbit.tech/journal/details')
            hole_page.wait_for_load_state('load')
            first_item = hole_page.locator('ul li div.line-clamp-1').first
            first_item.click(timeout=60000)
            hole_page.wait_for_timeout(5000)
            texts = hole_page.locator('div.whitespace-pre-wrap.pb-\\[80px\\].text-base.text-white.focus\\:outline-none').inner_text()
            print("Text content:", texts)

            recipient, message = parse_message(texts.lower())
            print(recipient)
            # recipient = 'r1-general'
            print(message)

            if (recipient and message) and texts != previous_text_content:
                print(f"Recipient: {recipient}, Message: {message}")

                if discord_page.url != "https://discord.com/channels/@me":
                    discord_page.goto("https://discord.com/channels/@me")
                    discord_page.wait_for_load_state('load')
                time.sleep(3)
                discord_page.keyboard.press('Control+K')
                time.sleep(3)

                quick_switcher = discord_page.locator('input[aria-label="Quick switcher"]')
                quick_switcher.wait_for(state='visible', timeout=60000)
                quick_switcher.fill(recipient)
                time.sleep(3)
                discord_page.keyboard.press("Enter")
                time.sleep(1)
                discord_page.fill('div[role="textbox"]', message)
                discord_page.keyboard.press("Enter")
                print("Message sent")
                previous_text_content = texts
                print("Pre Text content:", previous_text_content)
            else:
                print(f"Couldn't parse: {texts}")

            print("Timing out for 20 seconds... Checking again in 20 seconds...")
            time.sleep(20)

if __name__ == '__main__':
    main()
