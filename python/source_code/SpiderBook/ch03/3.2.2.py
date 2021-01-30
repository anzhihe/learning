#coding:utf-8

'''
httplib/urllib实现:GET请求

import httplib
conn =None
try:
    conn = httplib.HTTPConnection("www.zhihu.com")
    conn.request("GET", "/")
    response = conn.getresponse()
    print response.status, response.reason
    print '-' * 40
    headers = response.getheaders()
    for h in headers:
        print h
    print '-' * 40
    print response.msg
except Exception,e:
    print e
finally:
    if conn:
        conn.close()


'''

'''
httplib/urllib实现:POST请求

import httplib, urllib
conn = None
try:
    params = urllib.urlencode({'name': 'qiye', 'age': 22})
    headers = {"Content-type": "application/x-www-form-urlencoded"
    , "Accept": "text/plain"}
    conn = httplib.HTTPConnection("www.zhihu.com", 80, timeout=3)
    conn.request("POST", "/login", params, headers)
    response = conn.getresponse()
    print response.getheaders() #获取头信息
    print response.status
    print response.read()
except Exception, e:
    print e
finally:
    if conn:
        conn.close()
'''