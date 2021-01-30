#coding:utf-8

'''
Cookie处理:获取cookie

import requests
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
r = requests.get('http://www.baidu.com',headers=headers)
#遍历出所有的cookie字段的值
for cookie in r.cookies.keys():
    print cookie+':'+r.cookies.get(cookie)

'''

'''
Cookie处理:设置cookie

import requests
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
cookies = dict(name='qiye',age='10')
r = requests.get('http://www.baidu.com',headers=headers,cookies=cookies)
print r.text

'''

'''
Cookie处理:自动化

import requests
loginUrl = 'http://www.xxxxxxx.com/login'
s = requests.Session()
#首先访问登录界面，作为游客，服务器会先分配一个cookie
r = s.get(loginUrl,allow_redirects=True)
datas={'name':'qiye','passwd':'qiye'}
#向登录链接发送post请求，验证成功，游客权限转为会员权限
r = s.post(loginUrl, data=datas,allow_redirects= True)
print r.text

'''