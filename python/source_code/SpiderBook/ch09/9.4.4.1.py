#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("file:///e:/test.html")
username = driver.find_element_by_name('username').get_attribute()
password = driver.find_element_by_xpath(".//*[@id='loginForm']/input[2]")
login_button = driver.find_element_by_xpath("//input[@type='submit']")

username.send_keys("qiye")
password.send_keys("qiye_pass")
login_button.click()

# username.clear()
# password.clear()

# select = driver.find_element_by_xpath("//form/select")
# all_options = select.find_elements_by_tag_name("option")
# for option in all_options:
#     print("Value is: %s" % option.get_attribute("value"))
#     option.click()

from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_xpath('//form/select'))
select.select_by_index(2)

