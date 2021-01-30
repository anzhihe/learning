#coding:utf-8
'''
使用ProxyHandler在程序中动态设置代理

import urllib2
proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib2.build_opener([proxy,])
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.zhihu.com/')
print response.read()
'''

'''
直接调用 opener 的 open方法代替全局的 urlopen方法

import urllib2
proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
opener = urllib2.build_opener(proxy,)
response = opener.open("http://www.zhihu.com/")
print response.read()

'''