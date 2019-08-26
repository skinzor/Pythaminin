#Requires selenium. install using pip
from selenium import webdriver
import time

# Ask User for input
username = input("Enter Your Facebook Email ID Or Phone Number: ")
password = input("Enter Your Facebook Password: ")
print("Automation Has Been Injected")

url = 'https://www.facebook.com/'

# Need driver & Path to driver. https://chromedriver.chromium.org/downloads
# Check chrome version and download correct driver. chrome://settings/help
driver = webdriver.Chrome("/Users/User/Downloads/chromedriver")

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)

time.sleep(2)

driver.find_element_by_id('loginbutton').click()
