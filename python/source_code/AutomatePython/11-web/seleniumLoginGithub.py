from selenium import webdriver

account = 'your_account'
pwd = 'your_password'

browser = webdriver.Firefox()
browser.get('https://github.com')
loginElem = browser.find_element_by_link_text('Sign in')
loginElem.click()
emailElem = browser.find_element_by_id('login_field')
emailElem.send_keys(account)
pwdElem = browser.find_element_by_id('password')
pwdElem.send_keys(pwd)
pwdElem.submit()