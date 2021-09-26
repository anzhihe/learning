#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    06_dict_ordered.py
 @Function:    让字典保持有序
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/22
"""

"""如何让字典保持有序？"""

"""
实际案例：
    某编程竞赛系统,对参赛选手编程解题进行计时，选手完成题目后，
    把该选手解题用时记录到字典中，以便赛后按选手名查询成绩.
    (答题用时越短，成绩越优.)
    {LiLei': (2, 43), 'HanMeimei': (5, 52), Jim':(1, 39), ...}
    比赛结束后，需按排名顺序依次打印选手成绩，如何实现?
"""

"""
解决方案：
    使用collections.OrderedDict
    以OrderedDict替代内置字典Dict，依次将选手成绩存入OrderedDict
"""

from time import time
from random import randint
from collections import OrderedDict

# 选手成绩字典
d = OrderedDict()

# 模拟8名选手答题
players = list('ABCDEFGH')

# 记录答题开始时间
start = time()

# 模拟答题
for i in range(8):
    # 通过输入阻塞，输入回车表示答题完毕，记录下时间
    input()
    # 模拟某个选手答题完毕，从选手列表中删除
    p = players.pop(randint(0, 7 - i ))
    # 记录答题结束时间
    end = time()
    # 打印选手排名和成绩
    print(i+1, p, end - start)
    # 使用有序字典存储选手成绩
    d[p] = (i + 1, end - start)

# 打印成绩
print('-' * 20)

for k in d:
    print(k, d[k])

"""
1 A 3.3720529079437256
2 F 10.762058019638062
3 E 14.271024942398071
4 C 16.20379877090454
5 G 17.76311683654785
6 D 21.691321849822998
7 B 31.015563011169434
8 H 31.958091020584106
--------------------
A (1, 3.3720529079437256)
F (2, 10.762058019638062)
E (3, 14.271024942398071)
C (4, 16.20379877090454)
G (5, 17.76311683654785)
D (6, 21.691321849822998)
B (7, 31.015563011169434)
H (8, 31.958091020584106)
"""