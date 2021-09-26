#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    15_string_format_join.py
 @Function:    调整字符串中文本的格式与字符串拼接
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/9/4
"""

"""一、如何调整字符串中文本的格式？"""

"""
实际案例：
    某软件的log文件,其中的日期格式为'yyy-mm-dd':
    ......
    2016-05-23 10:59:26 status unpacked python3-pip:all
    2016-05-23 10:59:26 status half-configured python3-pip:all
    2016-05-23 10:59:26 status installed python3-pip:all
    2016-05-23 10:59:26 configure python3-wheel:all 0.24.0-1
    ......
    
    我们想把其中日期改为美国日期的格式'mm/dd/yyy'.
    '2016-05-23' => '05/23/2016',应如何处理?
"""

"""
解决方案：
    使用正则表达式re.sub()方法做字符串替换，利用正则表达式的捕获组，
    捕获每个部分内容，在替换字符串中调整各个捕获组的顺序
"""

import re

with open('test.log', 'r') as f:
    log = f.read()
    # str_format = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', log)
    # 给每个分组取个别名
    str_format = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', log)
    print(str_format)


"""二、如何将多个小字符串拼接成一个大的字符串？"""

"""
实际安全：
    在设计某网络程序时，我们自定义了一个基于UDP的网络协议，
    按照固定次序向服务器传递一系列参数:
    hwDetect:       "<0112>"
    gxDeptRBits:    "<32>"
    gxResolution:   "<1024x768>"
    gxRefresh:      "<60>"
    fullAlpha:      "<1>"
    lodDist:        "<100.0>"
    DistCull:       "<500.0>"
    
    在程序中我们将各个参数按次序收集到列表中:
    ["<0112>", "<32>", "<1024x768>", "<60>", "<1>", "<100.0>", "<500.0>"]
    最终我们要把各个参数拼接成一个数据报进行发送.
    "<0112><32><1024x768><60><1><100.0><500.0>"
"""

"""
解决方案：
    方法一：迭代列表，连续使用'+'操作依次拼接每一个字符串(拼接量小时使用)
    方法二：使用str.join()方法，更加快速的拼接列表中所有字符串(推荐)
"""

s1 = 'abcdefg'
s2 = '12345'

print(s1 + s2)  # abcdefg12345

# 实际上调用的是str运算符重载的__add__()方法
print(str.__add__(s1, s2))  # abcdefg12345
print(str.__gt__(s1, s2))   # True

pl = ["<0112>", "<32>", "<1024x768>", "<60>", "<1>", "<100.0>", "<500.0>"]
s = ''

for p in pl:
    s += p

print(s)    # <0112><32><1024x768><60><1><100.0><500.0>

"""
 使用str.join()方法
"""

print(''.join(pl))

l = ['abc', 123, 45, 'xyz']
# 以字符串方式拼接,生成器表达式比列表解析效率高
# print(''.join([str(x) for x in l]))
print(''.join(str(x) for x in l))   # abc12345xyz