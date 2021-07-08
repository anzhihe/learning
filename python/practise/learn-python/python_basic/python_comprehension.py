#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    python_comprehension.py
 @Function:    list dict set comprehension
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/2
"""

"""一、列表生成式"""

"""
1、什么是列表生成式？
    如果想要生成列表[1, 4, 9, 16, 25, 36]，可以使用for-in循环
"""

L = []
for i in range(1, 7):
    L.append(i * i)
print(L)    # [1, 4, 9, 16, 25, 36]

"""
    上述的解决方案有更好的替代，那就是使用列表生成式
    列表生成式的语法格式：
    [表示列表元素的表达式 for 自定义的变量 in 可迭代对象]
    其中，"表示列表元素的表达式"中通常含"自定义的变量"
    列表生成式的使用场景：凡是可以通过for-in循环创建的列表，都可以使用列表生成式来创建
"""

L = [i*i for i in range(1, 7)]
print(L)    # [1, 4, 9, 16, 25, 36]

"""
2、在列表生成式中使用if语句
    可以在列表生成式的for-in循环后添加if语句
"""

L = [i*i for i in range(1, 7) if not i % 2]
print(L)    # [4, 16, 36]

# 以上代码相当于：
L = []
for i in range(1, 7):
    if not i % 2:
        L.append(i * i)
print(L)    # [4, 16, 36]

"""
3、在列表生成式中使用双重循环
"""

L = [(i, j) for i in range(1, 4) for j in range(1, 4)]
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
print(L)

# 以上代码相当于：
L = []
for i in range(1, 4):
    for j in range(1, 4):
        L.append((i, j))
print(L)

# 既使用双重for-in循环，又使用if语句
L = [(i, j) for i in range(1, 4) for j in range(1, 4) if i != j]
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print(L)

"""
4、列表生成式支持嵌套
    可以在一个列表生成式中嵌套另一个列表生成式
"""

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
L = [[row[i] for row in matrix] for i in range(4)]
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
print(L)

# 以上代码相当于：
L= []
for i in range(4):
    L.append([row[i] for row in matrix])
print(L)

# 以上代码相当于：
L = []
for i in range(4):
    l_row = []
    for row in matrix:
        l_row.append(row[i])
    L.append(l_row)
print(L)


"""二、集合生成式"""

"""
1、什么是集合生成式？
    如果想要生成集合{1, 4, 9, 16, 25, 36}，可以使用for-in循环
"""

s = set()
for i in range(1, 7):
    s.add(i * i)
print(s)    # {1, 4, 36, 9, 16, 25}

"""
    上述的解决方案有更好的替代，那就是使用集合生成式
    集合生成式的语法格式：
    {表示集合元素的表达式 for 自定义的变量 in 可迭代对象}
    其中，"表示集合元素的表达式"中通常包含"自定义的变量"
    集合生成式的使用场景：凡是可以通过for-in循环创建的集合，都可以使用集合生成式来创建
"""

s = {i * i for i in range(1, 7)}
print(s)    # {1, 4, 36, 9, 16, 25}

"""
2、在集合生成式中使用if语句
    可以在集合生成式的for-in循环后添加if语句
"""

s = {i * i for i in range(1, 7) if not i % 2}
print(s)    # {16, 4, 36}

# 以上代码相当于：
s = set()
for i in range(1, 7):
    if not i % 2:
        s.add(i * i)
print(s)

"""
3、在集合生成式中使用双重循环
"""

s = {(i, j) for i in range(1, 4) for j in range(1, 4)}
# {(1, 2), (2, 1), (3, 1), (1, 1), (2, 3), (3, 3), (2, 2), (3, 2), (1, 3)}
print(s)

# 以上代码相当于：
s = set()
for i in range(1, 4):
    for j in range(1, 4):
        s.add((i, j))
print(s)

# 既使用双重for-in循环，又使用if语句
s = {(i, j) for i in range(1, 4) for j in range(1, 4) if i != j}
print(s)    # {(1, 2), (2, 1), (3, 1), (2, 3), (3, 2), (1, 3)}


"""三、字典生成式"""

"""
1、什么是字典生成式？
"""

items = ['Fruits', 'Books', 'Others']
prices = [96, 78, 83]

"""
    如果想要生成字典{'FRUITS': 96, 'BOOKS': 78, 'OTHERS': 83}，可以使用for-in循环
"""

d = {}
for item, price in zip(items, prices):
    d[item.upper()] = price
print(d)    # {'FRUITS': 96, 'BOOKS': 78, 'OTHERS': 83}

"""
    上述的解决方案有更好的替代，那就是使用字典生成式
    字典生成式的语法格式：
    {表示字典key的表达式：表示字典value的表达式 for 自定义的表示key的变量,自定义的表示value的变量 in 可迭代对象}
    其中，"表示字典key的表达式"中通常包含"自定义的表示key的变量"，"表示字典value的表达式"中
    通常包含"自定义的表示value的变量"
    字典生成式的使用场景：凡是可以通过for-in循环创建的字典，都可以使用字典生成式来创建
"""

d = {item.upper(): price for item, price in zip(items, prices)}
print(d)    # {'FRUITS': 96, 'BOOKS': 78, 'OTHERS': 83}

"""
2、在字典生成式中使用if语句
    可以在字典生成式的for-in循环后添加if语句
"""

d = {item.upper(): price for item, price in zip(items, prices) if price > 80}
print(d)    # {'FRUITS': 96, 'OTHERS': 83}

"""
3、在字典生成式中使用双重for-in循环
"""

d = {i: j for i in range(1, 4) for j in range(1, 4)}
print(d)    # {1: 3, 2: 3, 3: 3}

# 以上代码相当于：
d = {}
for i in range(1, 4):
    for j in range(1, 4):
        d[i] = j
print(d)

# 既使用双重for-in循环，又使用if语句
d = {i: j for i in range(1, 4) for j in range(1, 4) if i != j}
print(d)