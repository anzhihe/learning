#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    iterator.py
 @Function:    python迭代器
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/19
"""


"""迭代器"""

"""
    可以用于for-in语句的对象被称为可以迭代(Iterable)对象。例如：range、列表、元组、字符串、
字典、集合、生成器，都是可迭代对象。
    可以调用内置函数isinstance()判断一个对象是否是可迭代对象。标准库模块collections中的
类Iterable用于表示可迭代对象。
"""

from collections import Iterable

print(isinstance([1, 2, 3], Iterable))  # True
print(isinstance('abc', Iterable))      # True
print(isinstance((i * i for i in range(1, 7)), Iterable))      # True


"""
    如果一个可迭代对象可以作为内置函数next()的实参从而支持惰性推算，那么该对象被称为
迭代器(Iterator)对象。
    对于range、列表、元组、字符串、字典和集合等可迭代对象，都不可以作为内置函数next()的实参，
而生成器可以。所以，生成器是迭代器的一种。
    可以调用内置函数isinstance()判断一个对象是否是迭代器对象。标准库模块collections中的
类Iterator用于表示迭代器对象
"""

from collections import Iterator

L = [1, 2, 3]
s = 'abc'

# next(L) # TypeError: 'list' object is not an iterator
# next(s) # TypeError: 'str' object is not an iterator

print(isinstance(L, Iterator))  # False
print(isinstance(s, Iterator))  # False
print(isinstance((i * i for i in range(1, 7)), Iterator))   # True

"""
    可以调用内置函数iter()把不支持惰性推算的可迭代对象转换为迭代器对象
"""

iter_L = iter(L)
iter_s = iter(s)

print(isinstance(iter_L, Iterator)) # True
print(isinstance(iter_s, Iterator)) # True

print(next(iter_L)) # 1
print(next(iter_s)) # a

"""
    如果一个对象同时实现了特殊方法__iter__()和__next__()，那么该对象也被称为迭代器对象。如果
将该对象用于for-in语句，for-in语句首先会调用特殊方法__iter__()返回一个可迭代对象，然后不断调用
该可迭代对象的特殊方法__next__()返回下一次迭代的值，直到遇到StopIteration时退出循环
"""

class MyIterator(object):
    def __init__(self):
        self.data = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.data > 5:
            raise StopIteration()
        else:
            self.data += 1
            return self.data

for item in MyIterator():
    print(item)

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 50:
            raise StopIteration()
        return self.a

for item in Fib():
    print(item)
