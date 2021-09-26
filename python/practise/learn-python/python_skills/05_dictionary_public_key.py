#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    05_dictionary_public_key.py
 @Function:    找到多个字典中的公共键
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/22
"""

"""快速找到多个字典中的公共键(key)"""

"""
实际案例：
    西班牙足球甲级联赛,每轮球员进球统计:
    第一轮: {'苏亚雷斯':1, '梅西':2, '本泽马':1,'C罗':3, ...}
    第二轮: {苏亚雷斯':2, 'C罗':1, '格里兹曼':2, '贝尔':1, ...}
    第三轮: {'苏亚雷斯':1, '托雷斯':2, '贝尔':1, '内马尔':1, ...}
    统计出前N轮，每场比赛都有进球的球员.
"""

"""
常规方法：使用多次迭代
"""

from random import randint, sample

# 使用字典解析和sample构建三轮联赛，abcdefg七个球员中的进球数
s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
print(s1)
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
print(s2)
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
print(s3)

# 使用多次迭代找出公共键，执行效率不高
res = []
for k in s1:
    if k in s2 and k in s3:
        res.append(k)

print(res)

"""
解决方案：
    利用集合(set)的交集操作：
    1.使用字典的keys()方法，得到一个字典keys的集合
    2.使用map函数，得到所有字典的keys的集合
    3.使用reduce函数，取所有字典的keys的集合的交集
"""

from functools import reduce

print(s1.keys())
print(s2.keys())
print(s3.keys())
print(s1.keys() & s2.keys() & s3.keys())

# 统计前N轮联赛，以3轮联赛为例，依次添加即可
print(map(dict.keys, [s1, s2, s3]))

res = reduce(lambda x, y: x & y, map(dict.keys, [s1, s2, s3]))
print(res)

