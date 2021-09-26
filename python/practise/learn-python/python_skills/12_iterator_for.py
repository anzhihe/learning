#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    12_iterator_for.py
 @Function:    一个for语句中迭代多个可迭代对象
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/29
"""

"""如何在一个for语句中迭代多个可迭代对象？"""

"""
实际案例：
1.某班学生期末考试成绩，语文，数学，英语分别存储在3个列表中，
同时迭代三个列表，计算每个学生三科的总分. (并行)

2.某年级有4个班，某次考试每班英语成绩分别存储在4个列表中，
依次迭代每个列表，统计全学年成绩高于90分人数. (串行)
"""

from random import randint


chinese = [randint(60, 100) for _ in range(40)]
math = [randint(60, 100) for _ in range(40)]
english = [randint(60, 100) for _ in range(40)]

# 比较局限，只适用支持索引的可迭代对象，比如生成器
# for i in range(len(chinese)):
#     print(chinese[i] + math[i] + english[i])

"""
解决方案：
    并行：使用内置函数zip，它能将多个可迭代对象合并，每次迭代返回一个元组
    串行：使用标准库的itertools.chain，它能将多个可迭代对象连接
"""

# 内置函数zip可以将多个可迭代对象合并起来
print(list(zip([1, 2, 3, 4], ('a', 'b', 'c', 'd'))))    # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# [(1, 'a', 'f'), (2, 'b', 5), (3, 'c', 'e'), (4, 'd', 6)]
print(list(zip([1, 2, 3, 4], ('a', 'b', 'c', 'd'), {5, 6, 'e', 'f'})))

# 长度不一致，取较小的合并
print(list(zip([1, 2, 3, 4], ('a', 'b', 'c')))) # [(1, 'a'), (2, 'b'), (3, 'c')]

total = []

for c, m, e in zip(chinese, math, english):
    total.append(c + m + e)

print(total)

from itertools import chain

for i in chain([1, 2, 3, 4], ['a', 'b', 'c']):
    print(i, end=' ')   # 1 2 3 4 a b c

c1 = [randint(60, 100) for _ in range(41)]
c2 = [randint(60, 100) for _ in range(42)]
c3 = [randint(60, 100) for _ in range(43)]
c4 = [randint(60, 100) for _ in range(44)]

count = 0

for s in chain(c1, c2, c3, c4):
    if s > 90:
        count += 1

print(count)