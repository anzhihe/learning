#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    set_operator2.py
 @Function:    set operator
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/29
"""

"""一、集合的"查"操作"""

"""
    可以使用运算符in(not in)检查集合中是否存在(不存在)指定的元素
"""

s = {3, 4, 5, 6, 7}

print(5 in s)   # True
print(8 in s)   # False

print(5 not in s)   # False
print(8 not in s)   # True


"""二、集合的"增"操作"""

"""
如果想要往集合中添加元素，常见的方式有两种：
1、调用方法add(一次只添加一个元素)
"""

s = {3, 4, 5, 6, 7}
s.add(8)
print(s)    # {3, 4, 5, 6, 7, 8}

# 集合中已经存在的元素不会被添加
s.add(8)
print(s)    # {3, 4, 5, 6, 7, 8}

"""
2、调用方法update(一次至少添加一个元素)
"""

s = {3, 4, 5, 6, 7}
# s.update({2, 8})
# s.update([2, 8])
s.update((2, 8))

print(s)    # {2, 3, 4, 5, 6, 7, 8}

# 集合中已经存在的元素不会被添加
s.update({2, 8})
print(s)    # {2, 3, 4, 5, 6, 7, 8}


"""三、集合的"删"操作"""

"""
如果想要删除集合中的元素，常见的方式有四种：
1、调用方法remove(一次只删除一个指定的元素)
"""

s = {3, 4, 5, 6, 7}

s.remove(5)
print(s)    # {3, 4, 6, 7}

# 如果指定的元素在集合中不存在，抛出KeyError
# s.remove(8) # KeyError: 8

"""
2、调用方法discard(一次只删除一个指定的元素)
"""

s = {3, 4, 5, 6, 7}

s.discard(5)
print(s)    # {3, 4, 6, 7}

"""
    与方法remove不同的是：如果指定的元素在集合中不存在，不会抛出KeyError
"""

s.discard(8)
print(s)    # {3, 4, 6, 7}

"""
3、调用方法pop(一次只删除一个任意的元素)
"""

s = {3, 4, 5, 6, 7}

# 该方法返回被删除的元素
print(s.pop())  # 3
print(s)    # {4, 5, 6, 7}

"""
4、调用方法clear清空集合
"""

s = {3, 4, 5, 6, 7}
s.clear()
print(s)    # set()


"""四、不可变集合frozenset"""

"""
1、什么是frozenset？
    顾名思义，frozenset的意思是"被冻结的set"，也就是不可变的set
    frozenset之于set就好比tuple之于list
    
    因为frozenset是不可变类型，所以frozenset类型的对象：
    (1) 存在哈希值
    (2) 可以作为字典的key
    (3) 可以作为set中的元素
"""

"""
2、frozenset对象的创建
    可以调用内置函数frozenset(类frozenset的构造方法)创建frozenset对象
"""

print(frozenset())  # frozenset()
print(frozenset(range(1, 6)))       # frozenset({1, 2, 3, 4, 5})
print(frozenset([3, 5, 9, 2, 6]))   # frozenset({2, 3, 5, 6, 9})
print(frozenset((3, 5, 9, 2, 6)))   # frozenset({2, 3, 5, 6, 9})
print(frozenset('35926'))           # frozenset({'2', '6', '3', '9', '5'})
print(frozenset({3, 5, 9, 2, 6}))   # frozenset({2, 3, 5, 6, 9})