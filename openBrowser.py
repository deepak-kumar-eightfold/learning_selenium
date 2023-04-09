# This program opens the Chrome browser, go to google.com and perform a search. Different methods can be used to perform search.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://www.google.com/")
print("browser opened")
search = browser.find_element('name', 'q')
search.send_keys("What is selenium?")
# search.send_keys(Keys.RETURN)  // since by default pressing return submits the search, no need to submit() again using the below line.
search.submit()
# time.sleep(1) // Button was not clickable because it didn't load, so sleep for 1 sec and it'll load probably. This is for searching using button click.
# btn = browser.find_element('name', 'btnK')
# btn.click()
time.sleep(5)
browser.close()
