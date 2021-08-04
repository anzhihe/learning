#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    list_reverse_sort.py
 @Function:    列表的反转、排序和多维列表
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/23
"""

"""一、列表的反转"""

"""
如果想对列表中的所有元素进行反转，常见的方式有两种：
1、调用方法reverse
"""

L = [1, 2, 3, 4, 5]
L.reverse()
print(L)    # [5, 4, 3, 2, 1]

"""
2、调用内置函数reversed
    内置函数reversed的返回值是一个迭代器对象，且被反转的列表不发生变化
"""

L = [1, 2, 3, 4, 5]

iterator = reversed(L)
print(iterator)     # <list_reverseiterator object at 0x1033dc820>
print(list(iterator))   # [5, 4, 3, 2, 1]

print(L)    # [1, 2, 3, 4, 5]


"""二、列表的排序"""

"""
如果想对列表中的所有元素进行排序，常见的方式有两种：
1、调用方法sort
    调用方法sort后，列表中的所有元素默认按照从小到大的顺序进行排序
"""

L = [5, 3, 8, 1, 6]

L.sort()
print(L)    # [1, 3, 5, 6, 8]

# 调用方法sort时，可以指定参数reverse = True，从而按照逆序进行排序
L.sort(reverse = True)
print(L)    # [8, 6, 5, 3, 1]

"""
2、调用内置函数sorted
    内置函数sorted的返回值是排序后生成的新列表，且被排序的列表不发生变化
"""

L = [5, 3, 8, 1, 6]

print(sorted(L))    # [1, 3, 5, 6, 8]
print(L)    # [5, 3, 8, 1, 6]

# 调用方法sorted时，可以指定参数reverse = True，从而按照逆序进行排序
print(sorted(L, reverse = True))    # [8, 6, 5, 3, 1]
print(L)    # [5, 3, 8, 1, 6]


"""三、多维列表"""

"""
    当列表中的元素也是列表时，就构成了多维列表
    
    例如：
    当列表中的元素是一维列表时，就构成了二维列表
    当列表中的元素是二维列表时，就构成了三维列表
    因此，可以把多维列表看做是特殊的一维列表
    
1、一维列表的操作也适用于多维列表
"""

L = [[3, 4], [1, 5, 2], [6, 8, 9, 7]]

print(L[2][1])  # 8

L[1] = 9
print(L)    # [[3, 4], 9, [6, 8, 9, 7]]

L.append([2, 0])
print(L)    # [[3, 4], 9, [6, 8, 9, 7], [2, 0]]

L.pop(2)
print(L)    # [[3, 4], 9, [2, 0]]

"""
2、多维列表的初始化
"""

# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
print([[0] * 3] * 4)

# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
print([[0 for i in range(3)] for j in range(4)])

# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
print([[0] * 3 for j in range(4)])
