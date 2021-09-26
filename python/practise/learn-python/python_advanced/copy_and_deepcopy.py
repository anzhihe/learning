#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    copy_and_deepcopy.py
 @Function:    python 浅拷贝与深拷贝
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/10
"""


"""一、浅拷贝"""

"""
    对于某个对象，如何创建它的拷贝呢？也就是说，如何创建与该对象具有相同值的另一个对象呢？
    
    所谓浅拷贝，指的是：对于某个对象，虽然创建了与该对象具有相同值的另一个对象，但是，这两个对象
    内部嵌套的对应子对象全都是同一个对象。简单地说，外部进行了拷贝，内部没有拷贝
    
    以下方式得到的拷贝都是浅拷贝：
    (1) 切片操作[:]
    (2) 调用列表、字典、集合的方法copy()
    (3) 调用内置函数list()、dict()、set()
    (4) 调用标准库模块copy中的函数copy()
"""

L1 = [[3, 6], 8]
# L2 = L1[:]
# L2 = L1.copy()
# L2 = list(L1)
import copy # 导入标准库模块copy
L2 = copy.copy(L1)  # 调用标准库模块copy中的函数copy()
print(L2)   # [[3, 6], 8]

print('id(L1):%s' % id(L1))         # id(L1):4386649728
print('id(L2):%s' % id(L2))         # id(L2):4386718208

print('id(L1[0]):%s' % id(L1[0]))   # id(L1[0]):4386647808
print('id(L2[0]):%s' % id(L2[0]))   # id(L2[0]):4386647808

print('id(L1[1]):%s' % id(L1[1]))   # id(L1[1]):4384516624
print('id(L2[1]):%s' % id(L2[1]))   # id(L2[1]):4384516624

L1[0][1] = 7
L1[1] = 9
print(L1)   # [[3, 7], 9]
print(L2)   # [[3, 7], 8]

"""
    对于没有嵌套子对象的不可变对象，例如：整数对象、字符串对象和元组对象等，不会进行拷贝，也就是说，
    不会创建另一个对象
"""

i = 18

ic1 = int(i)
print(ic1)  # 18
print('id(i):%s' % id(i))       # id(i):4348980048
print('id(ic1):%s' % id(ic1))   # id(ic1):4348980048

ic2 = copy.copy(i)
print(ic2)  # 18
print('id(i):%s' % id(i))       # id(i):4348980048
print('id(ic2):%s' % id(ic2))   # id(ic2):4348980048

t = (1, 2, 3)

tc1 = tuple(t)
print(tc1)
print('id(t):%s' % id(t))       # id(t):4440932544
print('id(tc1):%s' % id(tc1))   # id(tc1):4440932544


"""二、深拷贝"""

"""
    可以调用标准库模块copy中的函数deepcopy()实现深拷贝
    
    所谓深拷贝，指的是：对于某个对象，创建与该对象具有相同值的另一个对象，同时，这两个对象
    内部嵌套的对应可变子对象全都不是同一个对象。简单地说，外部和内部进行了拷贝
"""

import copy

L1 = [[3, 6], 8]
L2 = copy.deepcopy(L1)  # 调用标准库模块copy中的函数deepcopy()
print(L2)   # [[3, 6], 8]

print('id(L1):%s' % id(L1))         # id(L1):4380346816
print('id(L2):%s' % id(L2))         # id(L2):4380350080

print('id(L1[0]):%s' % id(L1[0]))   # id(L1[0]):4380347072
print('id(L2[0]):%s' % id(L2[0]))   # id(L2[0]):4380349312

print('id(L1[1]):%s' % id(L1[1]))   # id(L1[1]):4378212880
print('id(L2[1]):%s' % id(L2[1]))   # id(L2[1]):4378212880

L1[0][1] = 7
L1[1] = 9
print(L1)   # [[3, 7], 9]
print(L2)   # [[3, 6], 8]

"""
    对于没有嵌套子对象的不可变对象，例如：整数对象、字符串对象和元组对象等，不会进行拷贝，也就是说，
    不会创建另一个对象
"""

i = 18

ic = copy.deepcopy(i)
print(ic)
print('id(i):%s' % id(i))     # id(i):4470414160
print('id(ic):%s' % id(ic))   # id(ic):4470414160

t = (1, 2, 3)

tc = copy.deepcopy(t)
print(tc)
print('id(t):%s' % id(t))     # id(t):4423896960
print('id(tc):%s' % id(tc))   # id(tc):4423896960

"""
    如果不可变对象内部有嵌套的可变子对象，深拷贝之后，会创建一个与该不可变对象具有相同值的另一个对象
"""

t1 = ([3, 6], 8)
t2 = copy.deepcopy(t1)
print(t2)   # ([3, 6], 8)

print('id(t1):%s' % id(t1))     # id(t1):4457890304
print('id(t2):%s' % id(t2))     # id(t2):4457844032

print('id(t1[0]):%s' % id(t1[0]))     # id(t1[0]):4321873664
print('id(t2[0]):%s' % id(t2[0]))     # id(t2[0]):4321874944

print('id(t1[1]):%s' % id(t1[1]))     # id(t1[1]):4315888144
print('id(t2[1]):%s' % id(t2[1]))     # id(t2[1]):4315888144