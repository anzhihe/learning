#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    04_dict_values_sorted.py
 @Function:    根据字典中值的大小，对字典中的项排序
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/22
"""

"""根据字典中值的大小，对字典中的项排序"""

"""
实际案例：
    某班英语成绩以字典形式存储为:
    {'LiLei': 79, Jim': 88, 'Lucy':92, ...}
    根据成绩高低，计算学生排名.
"""

"""
解决方案：
    使用内置函数sorted
    1.使用zip将字典数据转化成元组
    2.传递sorted函数的key参数
"""

from random import randint

d = {x: randint(60, 100) for x in 'xyzabc'}
print(d)    # {'x': 94, 'y': 61, 'z': 60, 'a': 73, 'b': 84, 'c': 84}
print(sorted(d))    # ['a', 'b', 'c', 'x', 'y', 'z']

# 默认是按键的值来进行升序排序的
print(iter(d))      # <dict_keyiterator object at 0x101cafae0>
print(list(iter(d)))    # ['x', 'y', 'z', 'a', 'b', 'c']

"""
    使用zip将字典数据转化成元组
"""

print(d.keys())     # dict_keys(['x', 'y', 'z', 'a', 'b', 'c'])
print(d.values())   # dict_values([94, 61, 60, 73, 84, 84])
t1 = zip(d.values(), d.keys())
print(sorted(t1))   # [(60, 'z'), (61, 'y'), (73, 'a'), (84, 'b'), (84, 'c'), (94, 'x')]

"""
   传递sorted函数的key参数 
"""

# dict_items([('x', 94), ('y', 61), ('z', 60), ('a', 73), ('b', 84), ('c', 84)])
print(d.items())

# 每次迭代d.items()，把其中某个项传入给lambda匿名函数，同时根据项中的元素指定比较的键(x[1])
d1 = sorted(d.items(), key=lambda x: x[1])
print(d1)   # [('z', 60), ('y', 61), ('a', 73), ('b', 84), ('c', 84), ('x', 94)]
