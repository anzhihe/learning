from selenium import webdriver
import time

browser =  webdriver.Chrome()

browser.get("http://www.jd.com")

# 等待10秒
time.sleep(10)

content = browser.page_source
print(content)

browser.quit()