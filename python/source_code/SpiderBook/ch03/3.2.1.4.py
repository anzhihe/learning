#coding:utf-8

'''
Timeout设置超时:更改 Socket 的全局 Timeout 值

import urllib2
import socket
socket.setdefaulttimeout(10) # 10 秒钟后超时
urllib2.socket.setdefaulttimeout(10) # 另一种方式

'''

'''
urlopen函数提供了对Timeout的设置

import urllib2
request=urllib2.Request('http://www.zhihu.com')
response = urllib2.urlopen(request,timeout=2)
html=response.read()
print html

'''