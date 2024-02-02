from selenium import webdriver
import time

browser =  webdriver.Chrome()

# 访问主页
browser.get("http://www.jd.com")
time.sleep(2)

# 访问登陆页
browser.get("https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F")
time.sleep(2)

# 切换为用户密码登陆
# r = browser.find_element_by_class_name('login-tab-r')
r = browser.find_element_by_xpath('//div[@class="login-tab login-tab-r"]')
browser.execute_script('arguments[0].click()', r)
time.sleep(2)

# 发送要输入的用户名和密码
browser.find_element_by_xpath("//input[@id='loginname']").send_keys("username")
time.sleep(1)
for i in "password":
    browser.find_element_by_xpath("//input[@id='nloginpwd']").send_keys(i)
    time.sleep(1)

# 点击登陆按钮
browser.find_element_by_xpath('//div[@class="login-btn"]/a').click()
time.sleep(2)

# 访问签到页面
browser.get("https://mall.jd.com/index-1000002826.html")
time.sleep(2)

# 签到并领金豆
browser.find_element_by_xpath('//div[@class="jSign"]/a').click()
time.sleep(10)

browser.quit()