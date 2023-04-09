# This program fetches the meaning of the word entered by the user via a google search.
# This will not fetch meaning if meaning of the word is not found in the google dictionary.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


search_string = input("Enter word to find meaning: ")
browser = webdriver.Chrome()
browser.get(f"https://www.google.com/search?q=define+{search_string}")
meaning_div = browser.find_elements(By.CLASS_NAME, "LTKOO")
for each in meaning_div:
    if each.text.strip() != "":
        print(each.text)

browser.close()
