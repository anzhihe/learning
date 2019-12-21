import requests
import bs4
from selenium import webdriver

# open browser
browser = webdriver.Firefox()
# open page
browser.get(url)

# get all links: bs4
# download each link and test status code: requests 
