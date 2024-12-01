from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Path to Chrome

# Set up the ChromeDriver Service
service = Service(executable_path='PATH to your downloaded chromedriver.exe file')

# Create the WebDriver instance
driver = webdriver.Chrome(service=service, options=chrome_options)


# Open the YouTube channel videos page
driver.get("Link to the youtube channel you are interested in")
driver.implicitly_wait(10)  # Wait for the page to load


# Scroll through the page to load all videos
last_height = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(20)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


# Extract video titles and URLs
video_elements = driver.find_elements(By.CSS_SELECTOR, 'a#video-title-link')
if video_elements:
    # Write links to a file
    with open('video_links.txt', 'w') as file:
        for video in video_elements:
            file.write(f"Title: {title}\nLink: {link}\n\n")
	   

    print("Links saved to video_links.txt")
else:
    print("No video elements found")


# Close the WebDriver
driver.quit()
