#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    tuple_def.py
 @Function:    tuple definition
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/23
"""

"""一、元组的概述"""

"""
1、什么是元组？
    除了列表，元组也是python语言提供的内置数据结构之一
    
    元组与列表的主要区别：
    (1) 元组用小括号表示(列表用中括号表示)
"""

t = ('Python', 18, True)
print(t)    # ('Python', 18, True)

# 小括号是可以省略的
t = 'Python', 18, True
print(t)    # ('Python', 18, True)

# 空元组的两种表示方式
print(())       # ()
print(tuple())  # ()

"""
    (2) 元组是不可变类型(列表是可变类型)
    为什么要设计元组这样的不可变类型呢？因为一旦创建了不可变类型的对象，对象内部的所有数据
    就不能被修改了，这样就避免了由于修改数据导致的错误。此外，对于不可变类型的对象，在多任务环境下
    同时操作对象时不需要加锁。因此，在程序中尽量使用不可变类型的对象
"""

t = ('Python', 18, True)
# t[1] = 20   # TypeError: 'tuple' object does not support item assignment

"""
    对于元组中可变类型的数据，元组中存储的是其引用(在内存中的地址)，因此，
    存储的引用是不能被改变的，也就是说，不能再引用任何其它对象。
    但是，引用所指向的可变类型的数据是可以改变的
"""

t = (5, [1, 3], 8)
# t[1] = 7    # TypeError: 'tuple' object does not support item assignment
t[1][0] = 7
print(t)    # (5, [7, 3], 8)

"""
2、只包含一个元素的元组
    元组中至少要包含一个逗号，即使元组只有一个元素，
    否则，小括号会被看做是数学公式中的小括号
"""

t = (18)
print(t)    # 18
print(type(t))  # <class 'int'>

t = (18,)
# t = 18,
print(t)    # (18,)
print(type(t))  # <class 'tuple'>
