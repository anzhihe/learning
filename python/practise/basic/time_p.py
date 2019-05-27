#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time

print(time.time())
print(time.mktime(time.localtime()))

print(time.gmtime()) #可加时间戳参数
print(time.localtime()) #可加时间戳参数
print(time.strptime('2018-11-11','%Y-%m-%d'))

print(time.strftime('%Y-%m-%d'))  #默认当前时间
print(time.strftime('%Y-%m-%d',time.localtime())) #默认当前时间
print(time.asctime())
print(time.asctime(time.localtime()))
print(time.ctime(time.time()))




