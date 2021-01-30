#coding;utf-8
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.phantomjs import webdriver

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)
driver = webdriver.PhantomJS()#desired_capabilities=dcap)
driver.get("http://www.google.com")
driver.quit()
