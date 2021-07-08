#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    list_def.py
 @Function:    list definition
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/22
"""

"""一、列表的概述"""

"""
1、什么是列表？
    为了使程序能方便地存储和操作数据，python语言提供了一些内置的数据结构
    例如：列表、元组、字典和集合等。所谓"内置"，指的是它们是python语言的一部分，因此在程序中可以直接使用它们
    
    列表的示意图：
    列表相当于其它编程语言中的数组
"""

"""
2、列表的特点
    (1) 列表中的所有数据都是按顺序有序排列的，也就是说，列表属于序列类型
    (2) 列表中的所有数据都有两个整数类型的索引，通过指定的索引总能映射到唯一指定的数据
    (3) 列表中可以存在重复的数据
    (4) 列表中可以保存任何类型的数据，多种类型的数据可以混合存储在一个列表中
    (5) 列表可以根据需要动态地伸缩，也就是说，系统会根据需要动态地分配和回收内存，因此，在使用前无须预先声明列表的容量
"""

"""二、列表的创建"""

"""
创建列表的常见方式有两种：
1、使用中括号
    当把列表赋值给变量时，变量名不要取名为list或l，因为list是列表对应的类名，l容易被误读或误写为阿拉伯数字1
"""

L = ['Python', 18, True]
print(L)    # ['Python', 18, True]

# 空列表
print([])   # []

"""
2、调用内置函数list(类list的构造方法)
"""

print(list(range(1, 6)))    # [1, 2, 3, 4, 5]
print(list(['Python', 18, True]))   # ['Python', 18, True]

# 空列表
print(list())   # []

"""三、列表的查操作"""

"""
1、列表元素的索引
    列表中的每个元素都有两个整数类型的索引
    (1) 第1个元素的索引是0，后面元素的索引依次递增1
    (2) 最后一个元素的索引是-1，前面元素的索引依次递减1
"""

"""
2、获取列表中指定元素的索引
"""

# 如果想要获得列表中指定元素的索引，可以调用index，该方法只返回两个整数索引中大于0的那个
L = [5, 3, 7, 9, 2, 1, 7, 6]
print(L.index(9))   # 3

# 如果列表中存在多个指定元素，方法index只返回第1个指定元素的索引值
print(L.index(7))   # 2

# 如果列表中不存在指定的元素，方法index抛出ValueError
# print(L.index(8))   # ValueError: 8 is not in list

# 调用方法index时还可以指定起始索引start和结束索引stop这两个参数
# 只指定起始索引start(不能只指定结束索引)
print(L.index(7, 3))    # 6
# 指定起始索引start和结束索引stop
# print(L.index(7, 3, 5)) # ValueError: 7 is not in list


"""四、使用索引一次只获得一个元素"""

"""
1、可以使用索引获得列表中的元素，但是，一次只获得一个元素
"""

L = [5, 3, 9, 4, 0, 6, 8, 1, 7, 2]

print(L[0])     # 5
print(L[-10])   # 5

print(L[6])     # 8
print(L[-4])    # 8

print(L[9])     # 2
print(L[-1])    # 2

"""
2、如果指定的索引在列表中不存在，会抛出IndexError
"""

# print(L[10])    # IndexError: list index out of range


"""五、使用切片一次获得多个元素"""

"""
1、使用切片一次获得多个元素
    可以使用切片获得列表中的元素，一次可以获得多个元素
    切片的语法格式：[start:stop:step]，其中
    (1) 得到的切片仍然是列表，是原始列表的片段的一份拷贝
    (2) 得到的切片不包括索引stop对应的元素
    (3) 如果不指定step，其默认值是1，此时语法格式可以简化为[start:stop]
    (4) 当step为正数时：
        如果不指定start，切片的第一个元素默认是列表的第一个元素
        如果不指定stop，切片的最后一个元素默认是列表的最后一个元素
        从索引start开始往后计算切片
        当step为负数时：
        如果不指定start，切片的第一个元素默认是列表的最后一个元素
        如果不指定stop，切片的最后一个元素默认是列表的第一个元素
        从索引start开始往前计算切片
    (5) 切片操作是允许索引越界的
"""

L= [5, 3, 9, 4, 0, 6, 8, 1, 7, 2]
print(L[1:7:2]) # [3, 4, 6]

print(L[1:7:])  # [3, 9, 4, 0, 6, 8]
print(L[1:7])   # [3, 9, 4, 0, 6, 8]

print(L[::])    # [5, 3, 9, 4, 0, 6, 8, 1, 7, 2]
print(L[::-1])  # [2, 7, 1, 8, 6, 0, 4, 9, 3, 5]

print(L[6:0:-2])    # [8, 0, 9]
print(L[0:6:-2])    # []
print(L[6::-2])     # [8, 0, 9, 5]
print(L[:5:-2])     # [2, 1]

print(L[:100])      # [5, 3, 9, 4, 0, 6, 8, 1, 7, 2]
print(L[-100:])     # [5, 3, 9, 4, 0, 6, 8, 1, 7, 2]

"""
2、内置函数slice使用
    可以调用内置函数slice(类slice的构造方法)创建slice类型的对象
    内置函数slice有三种调用方式：
    (1) slice(stop)
    (2) slice(start, stop)
    (3) slice(start, stop, step)
    start、stop和step的默认值都是None
    slice(start, stop, step)与start:stop:step是等价的
"""

L= [5, 3, 9, 4, 0, 6, 8, 1, 7, 2]

print(L[1:7:2])             # [3, 4, 6]
print(L[slice(1, 7, 2)])    # [3, 4, 6]

print(L[::])                        # [5, 3, 9, 4, 0, 6, 8, 1, 7, 2]
print(L[slice(None, None, None)])   # [5, 3, 9, 4, 0, 6, 8, 1, 7, 2]

print(L[1:7])               # [3, 9, 4, 0, 6, 8]
print(L[slice(1, 7)])       # [3, 9, 4, 0, 6, 8]
print(L[slice(1, 7, None)]) # [3, 9, 4, 0, 6, 8]

print(L[:7])                    # [5, 3, 9, 4, 0, 6, 8]
print(L[slice(7)])              # [5, 3, 9, 4, 0, 6, 8]
print(L[slice(None, 7, None)])  # [5, 3, 9, 4, 0, 6, 8]


"""
    可以使用运算符in(not in)检查列表中是否存在(不存在)指定元素
    对于in，如果存在，返回True;如果不存在，返回False
    对于not in，如果不存在，返回True；如果存在，返回False
"""

L = [3, 4, 5, 6, 7]

print(5 in L)   # True
print(8 in L)   # False

print(5 not in L)   # False
print(8 not in L)   # True