#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    set_operator.py
 @Function:    set mathematical operations
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/29
"""

"""集合的数学操作"""

"""
1、两个集合的交集
    调用方法intersection和使用运算符&是等价的
    做交集操作后生成一个新集合，做交集操作的两个集合不变
"""

s1 = {1, 3, 5, 7, 9}
s2 = {2, 3, 6, 7, 10}

print(s1.intersection(s2))  # {3, 7}
print(s1 & s2)  # {3, 7}
print(s1)   # {1, 3, 5, 7, 9}
print(s2)   # {2, 3, 6, 7, 10}

"""
    s1.intersection_update(s2)的执行结果：
    用s1.intersection(s2)的返回值更新s1，s2不变
    方法intersection_update的返回值为None
"""

print(s1.intersection_update(s2))   # None
print(s1)   # {3, 7}
print(s2)   # {2, 3, 6, 7, 10}

"""
2、两个集合的并集
    调用方法union和使用运算符|是等价的
    做并集操作后生成一个新集合，做并集操作的两个集合不变
"""

s1 = {1, 3, 5, 7, 9}
s2 = {2, 3, 6, 7, 10}

print(s1.union(s2))     # {1, 2, 3, 5, 6, 7, 9, 10}
print(s1 | s2)          # {1, 2, 3, 5, 6, 7, 9, 10}
print(s1)   # {1, 3, 5, 7, 9}
print(s2)   # {2, 3, 6, 7, 10}

# 注意：不存在方法union_update()

"""
3、两个集合的差集
    调用方法difference和使用运算符-是等价的
    做差集操作后生成一个新集合，做差集操作的两个集合不变
"""

s1 = {1, 3, 5, 7, 9}
s2 = {2, 3, 6, 7, 10}

print(s1.difference(s2))    # {1, 5, 9}
print(s1 - s2)  # {1, 5, 9}
print(s1)   # {1, 3, 5, 7, 9}
print(s2)   # {2, 3, 6, 7, 10}

"""
    s1.difference_update(s2)的执行结果：
    用s1.difference(s2)的返回值更新s1，s2不变
    方法difference_update的返回值为None
"""

print(s1.difference_update(s2)) # None
print(s1)   # {1, 5, 9}
print(s2)   # {2, 3, 6, 7, 10}

"""
4、两个集合的对称差集
    调用方法symmetric_difference和使用运算符^是等价的
    做对称差集操作后生成一个新集合，做对称差集操作的两个集合不变
"""

s1 = {1, 3, 5, 7, 9}
s2 = {2, 3, 6, 7, 10}

print(s1.symmetric_difference(s2))  # {1, 2, 5, 6, 9, 10}
print(s1 ^ s2)  # {1, 2, 5, 6, 9, 10}
print(s1)   # {1, 3, 5, 7, 9}
print(s2)   # {2, 3, 6, 7, 10}

"""
    s1.symmetric_difference_update(s2)的执行结果：
    用s1.symmetric_difference(s2)的返回值更新s1，s2不变
    方法symmetric_difference_update的返回值为None
"""

print(s1.symmetric_difference_update(s2))   # None
print(s1)   # {1, 2, 5, 6, 9, 10}
print(s2)   # {2, 3, 6, 7, 10}
