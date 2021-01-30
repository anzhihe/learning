#coding:utf-8
'''
实现一个完整的请求与响应模型:GET
import requests
r = requests.get('http://www.baidu.com')
print r.content

'''

'''
实现一个完整的请求与响应模型:POST

import requests
postdata={'key':'value'}
r = requests.post('http://www.xxxxxx.com/login',data=postdata)
print r.content
'''

'''
带参数的GET请求

import requests
payload = {'Keywords': 'blog:qiyeboy','pageindex':1}
r = requests.get('http://zzk.cnblogs.com/s/blogpost', params=payload)
print r.url

'''

