
from selenium import webdriver

account = 'your_account'
pwd = 'your_password'

# open browser
browser = webdriver.Firefox()
# open page
browser.get('https://github.com')

# login: get email and pwd element and send keys
loginElem = browser.find_element_by_link_text('Sign in')
loginElem.click()
emailElem = browser.find_element_by_id('login_field')
emailElem.send_keys(account)
pwdElem = browser.find_element_by_id('password')
pwdElem.send_keys(pwd)
pwdElem.submit()
# click create email button
# get recevier element and send keys
# get content element and send keys
# get send button and submit