# Rabbit Hole Messenger Bot

This Python script uses Playwright to automate sending messages from a Rabbit Hole journal entry to a Facebook Messenger contact. 

## Prerequisites

* **Python:** Make sure you have Python installed ([https://www.python.org/downloads/](https://www.python.org/downloads/)).
* **Playwright:** Install it using pip: `pip install playwright`
* **Python dotenv:** Install it using pip: `pip install python-dotenv`

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/glovergaytan-fs/rabbitWrighter.git
   cd your-repo-name
Install Playwright Browsers:

playwright install 
Create a .env file: Create a file named .env in the root directory of the project.

```import os
import time
from dotenv import load_dotenv  # Import load_dotenv
from playwright.sync_api import sync_playwright

# Load environment variables from .env file
load_dotenv()  # Load environment variables 

# Access environment variables
your_username = os.getenv("YOUR_USERNAME")
your_password = os.getenv('YOUR_PASSWORD')
fb_email = os.getenv("FB_EMAIL")
fb_password = os.getenv('FB_PASSWORD')

# ... rest of your code ... ```
Explanation:

Import load_dotenv:

from dotenv import load_dotenv imports the necessary function to load environment variables from a .env file.
Call load_dotenv():

This line is crucial. It reads the .env file (if it exists in the same directory as your script) and loads the key-value pairs as environment variables.
Access Variables with os.getenv():

os.getenv("VARIABLE_NAME") is used to retrieve the values of environment variables.
In your code, it gets the username, password, Facebook email, and password from the loaded environment variables.
How .env Files and python-dotenv Work:

.env File: You create a file named .env in your project's root directory. Inside this file, you store sensitive information or configuration settings as key-value pairs, like this:
YOUR_USERNAME=your_actual_username
YOUR_PASSWORD=your_secret_password
FB_EMAIL=your_facebook_email@example.com
FB_PASSWORD=your_facebook_password
Security: It's important to never commit your .env file to version control (like Git). This keeps your sensitive data out of your repository.
Environment Variables: When load_dotenv() is called, it takes the contents of the .env file and sets them as environment variables within your Python program's current process.
Access: You can then access these environment variables using os.getenv().
Benefits:

Security: Keeps sensitive data like passwords and API keys out of your codebase.
Configuration Management: Easily change configurations without modifying your code.
Portability: Makes it simple to run your application in different environments (development, testing, production) by using different .env files.

Add your credentials and configuration to .env:

YOUR_USERNAME=your_rabbit_hole_username
YOUR_PASSWORD=your_rabbit_hole_password
FB_EMAIL=your_facebook_email
FB_PASSWORD=your_facebook_password 

How it Works

Login: The script logs into your Rabbit Hole account.
Journal Entry: It navigates to your journal details page and continuously checks for new entries that start with "message".
Facebook Messenger: If a new message entry is found, the script opens Facebook Messenger in a new tab and sends the message content to the specified Facebook contact.
Running the Script
Start the script:

python fb_messenger.py

Important Notes

If you're using node then use https://www.npmjs.com/package/dotenv instead

Security: Be cautious about storing sensitive information like passwords directly in your code or .env file. Consider more secure alternatives for production environments.
Facebook's Terms of Service: Ensure that your automation activities comply with Facebook's terms and conditions.

Playwright Documentation: https://playwright.dev/python/docs/intro
Rabbit Hole: https://hole.rabbit.tech/
Facebook Messenger: https://www.messenger.com/
