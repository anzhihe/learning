#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    break_continue.py
 @Function:    python break & continue statements
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/1
"""

"""一、循环语句中的break-else结构"""

"""
    在执行while语句或for-in语句时，如果循环正常结束，也就是说，如果没有执行循环体中的break
    语句从而提前退出循环，有时可能想在循环正常结束后执行某些操作
    为了判断循环是否正常结束，可以使用一个布尔变量，在循环开始前将布尔变量的值设置为False，
    如果执行了循环体中的break语句从而提前退出循环，那就将布尔变量的值设置为True
    最后，在while语句或for-in语句的后面使用if语句判断布尔变量的值，以判断循环是否是正常结束的
"""

is_break = False
n = 0
while n < 5:
    if n == 6:
        is_break = True
        break
    n += 1
if not is_break:
    print('循环正常结束，没有执行循环体中的break语句')

is_break = False
for n in range(5):
    if n == 6:
        is_break = True
        break
if not is_break:
    print('循环正常结束，没有执行循环体中的break语句')

"""
    上述的解决方案还有更好的替代。python为循环语句提供了break-else结构，也就是说，
    可以在while语句或for-in语句的后面添加else从句，这样，如果没有执行循环体中的break语句
    从而提前退出循环，就会执行else从句
"""

n = 0
while n < 5:
    if n == 6:
        break
    n += 1
else:
    print('循环正常结束，没有执行循环体中的break语句')

for n in range(5):
    if n == 6:
        break
    n += 1
else:
    print('循环正常结束，没有执行循环体中的break语句')


"""二、循环语句中的break和continue"""

"""
    在while语句或for-in语句的循环体中，除了可以使用break语句之外，还可以使用continue语句，
    两者的区别在于：
    break表示"断路"，用于结束整个循环
    continue表示"短路"，用于结束整个循环中的当前迭代，继续下一个迭代
"""

for i in range(1, 5):
    if i == 3:
        break
    print('i =', i)

for i in range(1, 5):
    if i == 3:
        continue
    print('i = ', i)

"""
    在嵌套的循环语句中，break和continue默认作用于当前循环
"""

for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            break
        print('i =', i, 'j =', j)

for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            continue
        print('i =', i, 'j =', j)