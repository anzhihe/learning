#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    none_and_range.py
 @Function:    python None & range
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/21
"""

"""一、对象None"""

"""
1、什么是对象None
    对象None用于表示数据值的不存在
    对象None是占据一定的内存空间的，它并不意味着"空"或"没有定义"
    也就是说，None是"something"，而不是"nothing"
"""

# 调用内置函数id查看对象None的内存地址
print(id(None)) # 4485465520

"""
2、对象None的使用场景
    对象None经常用于变量的初始化，或将变量重置为"数据值不存在"的状态
"""

a = None
print(a)    # None

b = 18
print(b)    # 18
b = None
print(b)    # None


"""二、序列类型range"""

"""
1、什么是range?
    range是一种序列类型，range类型用于表示不可变的整数序列
    
    可以调用内置函数range(类range的构造方法)创建range类型的对象，有三种调用方式：
    (1) range(stop)
    (2) range(start, stop)
    (3) range(start, stop, step)
    其中，整数序列的起始值的默认值是0，可以使用参数start指定
    可以使用参数stop指定整数序列的结束值，创建的range对象不包含stop
    整数序列的步长的默认值是1，可以使用参数step进行指定
    
    内置函数range的返回值是一个迭代器对象。为了清楚地表示返回的迭代器对象所表示的整数序列，可以将其转换成列表
    
    range类型的优点在于：不管range对象表示的整数序列有多长，所有range对象占用的内存空间都是相同的，
    因为仅仅需要存储start、stop和step。只有当用到range对象时，才会去计算序列中的相关元素
"""

print(range(5))     # range(0, 5)

print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(0, 5, 1)))     # [0, 1, 2, 3, 4]

print(list(range(1, 5)))     # [1, 2, 3, 4]
print(list(range(1, 5, 1)))  # [1, 2, 3, 4]

print(list(range(0, 20, 4)))    # [0, 4, 8, 12, 16]
print(list(range(0, -20, -4)))    # [0, -4, -8, -12, -16]

"""
2、判断range对象中是否存在(不存在)指定的整数
    可以使用运算符in(not in)检查range对象表示的整数序列中是否存在(不存在)指定的整数
"""

print(3 in range(5))    # True
print(8 not in range(5))    # True
