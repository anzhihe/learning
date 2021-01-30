#coding:utf-8

'''
请求头headers处理

import requests
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
r = requests.get('http://www.baidu.com',headers=headers)
print r.content

'''

'''
响应码code和响应头headers处理

import requests
r = requests.get('http://www.baidu.com')
if r.status_code == requests.codes.ok:
    print r.status_code#响应码
    print r.headers#响应头
    print r.headers.get('content-type')#推荐使用这种获取方式，获取其中的某个字段
    print r.headers['content-type']#不推荐使用这种获取方式
else:
    r.raise_for_status()

'''

