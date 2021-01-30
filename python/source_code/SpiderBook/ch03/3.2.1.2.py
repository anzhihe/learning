#coding:utf-8
'''
请求头headers处理:设置一下请求头中的User-Agent域和Referer域信息

import urllib
import urllib2
url = 'http://www.xxxxxx.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
referer='http://www.xxxxxx.com/'
postdata = {'username' : 'qiye',
           'password' : 'qiye_pass'}
# 将user_agent,referer写入头信息
headers={'User-Agent':user_agent,'Referer':referer}
data = urllib.urlencode(postdata)
req = urllib2.Request(url, data,headers)
response = urllib2.urlopen(req)
html = response.read()


'''
'''
请求头headers处理:add_header来添加请求头信息

import urllib
import urllib2
url = 'http://www.xxxxxx.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
referer='http://www.xxxxxx.com/'
postdata = {'username' : 'qiye',
           'password' : 'qiye_pass'}
data = urllib.urlencode(postdata)
req = urllib2.Request(url)
# 将user_agent,referer写入头信息
req.add_header('User-Agent',user_agent)
req.add_header('Referer',referer)
req.add_data(data)
response = urllib2.urlopen(req)
html = response.read()

'''
