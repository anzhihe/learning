#coding:utf-8
'''
CookieJar函数进行Cookie的管理:获取Cookie值

import urllib2
import cookielib
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open('http://www.zhihu.com')
for item in cookie:
    print item.name+':'+item.value

'''

'''
CookieJar函数进行Cookie的管理:设置Cookie值

import  urllib2
opener = urllib2.build_opener()
opener.addheaders.append( ( 'Cookie', 'email=' + "xxxxxxx@163.com" ) )
req = urllib2.Request( "http://www.zhihu.com/" )
response = opener.open(req)
print response.headers
retdata = response.read()

'''

