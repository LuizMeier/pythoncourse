import requests
from bs4 import BeautifulSoup

# Step 1: Log in to Medium and get session cookies
login_url = 'https://medium.com/m/signin'
session = requests.Session()

# Replace with your Medium credentials
payload = {
    'email': 'your_email',
    'password': 'your_password'
}

# Perform login
response = session.post(login_url, data=payload)
if response.status_code == 200:
    print("Logged in successfully!")

# Step 2: Use the session to import a story
import_url = 'https://medium.com/p/import'
story_data = {
    'title': 'Your Story Title',
    'content': 'Your story content here...'
}

response = session.post(import_url, data=story_data)
if response.status_code == 200:
    print("Story imported successfully!")
else:
    print("Failed to import story.")



###############################

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests

# Step 1: Automate Medium login and email confirmation
driver = webdriver.Chrome()
driver.get('https://medium.com/m/signin')

# Enter email and submit
email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys('your_email@example.com')
email_input.send_keys(Keys.RETURN)

# Wait for the email confirmation (you might need to adjust the sleep time)
time.sleep(60)

# Step 2: Open email and click the confirmation link
# This part depends on your email provider. Here's an example for Gmail:
driver.get('https://mail.google.com/')
# Log in to Gmail and find the confirmation email
# Click the confirmation link

# Step 3: Use Requests to manage the session
session = requests.Session()
for cookie in driver.get_cookies():
    session.cookies.set(cookie['name'], cookie['value'])

# Now you can use the session to import a story
import_url = 'https://medium.com/p/import'
story_data = {
    'title': 'Your Story Title',
    'content': 'Your story content here...'
}

response = session.post(import_url, data=story_data)
if response.status_code == 200:
    print("Story imported successfully!")
else:
    print("Failed to import story.")

# Close the browser
driver.quit()
