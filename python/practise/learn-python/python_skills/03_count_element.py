#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    03_count_element.py
 @Function:    统计序列中元素的出现频度
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/22
"""

"""统计序列中元素的出现频度"""

"""
1、某随机序列，找到出现次数最高的3个元素，统计它们出现的次数
"""

"""
   常规方法：使用字典来给元素计数，再根据字典的值进行排序
"""

from random import randint

data = [randint(0, 10) for _ in range(10)]
print(data) # [10, 3, 9, 1, 4, 5, 9, 10, 5, 3]

d = dict.fromkeys(data, 0)
for x in data:
    d[x] += 1
print(d)    # {10: 2, 3: 2, 9: 2, 1: 1, 4: 1, 5: 2}

# x[0]按字典的键排序，x[1]按字典的值的排序，默认升序
c = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(c)    # [(10, 2), (3, 2), (9, 2), (5, 2), (1, 1), (4, 1)]

"""
    更简洁的方法：使用collections.Counter对象
    (1) 将序列传入Counter的构造器，得到Counter对象是元素频度的字典
    (2) Counter.most_common(n)方法得到频度最高的n个元素的列表
"""

from collections import Counter

d2 = Counter(data)
c2 = d2.most_common(3)
print(c2)   # [(10, 2), (3, 2), (9, 2)]

"""
2、对某英文文章的单词，进行词频统计，找到出现次数最高的10个单词，
统计它们出现的次数
"""
import re

with open('/Users/anzhihe/relay.scpt', 'r') as f:
    txt = f.read()

# 使用非字母元素分割
c3 = Counter(re.split('\W+', txt))
# [('end', 10), ('of', 9), ('tell', 8), ('to', 6), ('repeat', 6), ('listOfShows', 5), ('with', 5), ('current', 5), ('if', 4), ('num_hosts', 4)]
print(c3.most_common(10))