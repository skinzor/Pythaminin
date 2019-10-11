from selenium import webdriver
import time as mirror

# Ask User For input
ask = input("Enter Site To Visit: ")
url = 'https://www.' + ask + '.com/'
print("Visiting Site:" + url)
# Drive Url
driver = webdriver.Chrome("/Users/User/Downloads/chromedriver")
driver.get(url)
# Notify
mirror.sleep(3)
print("Viewing Site:" + url)

