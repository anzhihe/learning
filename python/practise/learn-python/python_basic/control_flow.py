#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    control_flow.py
 @Function:    python control flow
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/30
"""

"""一、流程控制的概述"""

"""
    1996年，计算机科学家证明了这样的事实：任何简单或复杂的算法都可以由顺序结构、选择结构和
    循环结构这三种基本结构组合而成。
    顺序结构指的是：程序从上到下顺序地执行代码，中间没有任何判断和跳转，直到程序结束
    选择结构指的是：程序根据判断条件的布尔值选择性地执行部分代码
    循环结构指的是：程序根据循环条件反复执行某段代码，直到不满足循环条件为止
"""


"""二、顺序结构"""

"""
    顺序结构指的是：程序从上到下顺序地执行代码，中间没有任何判断和跳转，直到程序结束
"""

print('-------开始-------')

print('第1步：把冰箱门打开')
print('第2步：把大象装进冰箱')
print('第3步：把冰箱门关上')

print('-------结束-------')


"""三、选择结构"""

"""
    选择结构指的是：程序根据判断条件的布尔值选择性地执行部分代码
    python语言提供的实现选择结构的语句是if语句
"""


"""四、代码块的缩进"""

"""
    代码块是一组相关语句的集合
    
    在有的编程语言中，代码块开始和结束于某个特殊字符，比如：以{开始，以}结束
    在python中，代码块开始于冒号，代码块中的所有行(不包括子代码块)都要缩进相同数量的空格
    通常缩进4个空格
    不要忘记缩进，也不要添加不必要的缩进
"""

score = 88
if score >= 60:
    print('及格了')

print('Hello')
#    print('World')  # IndentationError: unexpected indent


"""五、对象的布尔值"""

"""
    所有的对象都有一个布尔值，可以调用内置函数bool(类bool的构造方法)得到对象的布尔值
    
    以下对象的布尔值为False：False、数值零、None、空字符串、空列表、空元组、空字典、空集合
    >>> bool(False)
    False
    >>> bool(0)
    False
    >>> bool(0.0)
    False
    >>> bool(None)
    False
    >>> bool('')
    False
    >>> bool("")
    False
    >>> bool([])
    False
    >>> bool(list())
    False
    >>> bool(())
    False
    >>> bool(tuple())
    False
    >>> bool({})
    False
    >>> bool(dict())
    False
    >>> bool(set())
    False
    >>> bool(frozenset())
    False
    >>> bool(18)
    True
    >>> bool('Python')
    True
    >>> bool('     ')
    True
    >>> bool([1, 2, 3, 4])
    True
    >>> bool((1, 2, 3, 4))
    True
    >>> bool({'a': 18, 'b': 56})
    True
    >>> bool({1, 2, 3, 4})
    True
"""

"""
    所有对象都可被直接用作布尔值，解释器会自动调用内置函数bool进行转换
"""

if 18:
    print(18, True) # 18 True

if 'Python':
    print('Python', True)   # Python True



