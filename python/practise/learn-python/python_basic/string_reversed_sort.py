#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    string_reversed_sort.py
 @Function:    string rerversed & sort
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/24
"""

"""一、字符串的反转"""

"""
    与列表不同的是，字符串是不可变类型，因此，如果想对字符串中的所有字符进行反转，
    不存在方法reverse，只能调用内置函数reversed
"""

s = '12345'

iterator = reversed(s)
print(iterator)         # <reversed object at 0x10d3d2e20>
print(list(iterator))   # ['5', '4', '3', '2', '1']

print(s)    # 12345


"""二、字符串的排序"""

s = 'DBeFac'
print(sorted(s))                    # ['B', 'D', 'F', 'a', 'c', 'e']
print(sorted(s, reverse = True))    # ['e', 'c', 'a', 'F', 'D', 'B']
print(sorted(s, key = str.lower))   # ['a', 'B', 'c', 'D', 'e', 'F']

L = ['Python', 'java', 'Swift']
print(sorted(L, key = len))         # ['java', 'Swift', 'Python']
print(sorted(L, key = str.lower))   # ['java', 'Python', 'Swift']

L = ['Python', 'java', 'Swift']
L.sort(key = len)
print(L)                            # ['java', 'Swift', 'Python']
L.sort(key = str.lower)
print(L)                            # ['java', 'Python', 'Swift']
