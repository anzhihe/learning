from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048')
htmlElem = browser.find_element_by_tag_name('html')

while True:
    htmlElem.send_keys(Keys.DOWN) # scrolls to bottom
    htmlElem.send_keys(Keys.RIGHT) # scrolls to top
    htmlElem.send_keys(Keys.UP) # scrolls to bottom
    htmlElem.send_keys(Keys.LEFT) # scrolls to bottom
