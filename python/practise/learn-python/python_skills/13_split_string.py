#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    13_split_string.py
 @Function:    拆分含有多种分隔符的字符串
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/9/3
"""

"""如何拆分含有多种分隔符的字符串？"""

"""
实际案例：
    我们要把某个字符串依据分隔符号拆分不同的字段，
    该字符串包含多种不同的分隔符,例如:
    
    s = 'ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'
    
    其中<,>, <;>, <|>, <\t>都是分隔符号，如何处理?
"""

"""
解决方案：
    方法一：连续使用str.split()方法，每次处理一种分隔符号
    方法二：使用正则表达式的re.split()方法，一次性拆分字符串(推荐)
"""

def split_str(s, sep):
    res = [s]

    for d in sep:
        t = []
        list(map(lambda x: t.extend(x.split(d)), res))
        res = t

    return [x for x in res if x]

s = 'ab;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz'

# ['ab', 'cd', 'efg', 'hi', 'jkl', 'mn', 'opq', 'rst', 'uvw', 'xyz']
print(split_str(s, ';,|\t'))


import re

# 同时处理多个正则符
t = re.split(r'[,;\t|]+', s)
print(t)