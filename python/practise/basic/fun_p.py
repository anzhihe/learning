#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
0.定义函数时,需确定函数句和参数个数.如果有必要,可以先对参数的数据类型做检查
1.函数体内部的语句在执行时,一时执行到return时,函数就执行完毕,并将结果返回.如果没有return语句,函数执行完毕返回None
2.如果想定义空函数(一个什么事也不做的函数),可以用pass语句
3.函数可以同时返回多个值,其实就是一个tuple
'''

import math

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type!')
    if x > 0:
        return x
    else:
        return -x

print(my_abs(-99))
# print(my_abs('A'))

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 默认参数: 简化函数的调用.
# 注意: 1.改造参数在前,默认参数在后; 2.当函数有多个参数时,把变化大的参数放前面,变化小的参数放后面.变化小的参数就可以作为默认参数.
# 当不按顺序提供部分默认参数时,需要把参数名写上.