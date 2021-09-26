#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    11_iterator_slice.py
 @Function:    对迭代器做切片操作
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/29
"""

"""如何对迭代器做切片操作?"""

"""
实际案例：
    有某个文本文件，我们想读取其中某范围的内容
    如100 ~ 300行之间的内容，python中文本文件是
    可迭代对象，我们是否可以使用类似列表切片的
    方式得到一个100 ~ 300行文件内容的生成器?
    f = open('/var/log/dmesg')
    f[100:300] #可以么?
"""

"""
解决方案：
    使用标准库中的itertools.islice，它能返回一个迭代对象切片的生成器
"""

from itertools import islice

with open('/tmp/dmesg', 'r') as f:
    lines = islice(f, 10, 30)
    # lines = islice(f, 20)   # 前20行
    # lines = islice(f, 20, None)   # 20到末尾
    # lines = islice(f, 20, -20)   # 去掉前20行的后20行，报错
    # ValueError: Indices for islice() must be None or an integer: 0 <= x <= sys.maxsize.
    # 没读完文件前，不知道整个文件是多少行，无法判断

    for l in lines:
        print(l)

l = range(20)
t = iter(l)
# islice(t, 5, 10)生成器对象会消耗t生成器
for x in islice(t, 5, 10):
    print(x, end=' ')   # 5 6 7 8 9

for x in t:
    print(x, end=' ')   # 10 11 12 13 14 15 16 17 18 19