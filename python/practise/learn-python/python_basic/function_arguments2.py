#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    function_arguments2.py
 @Function:    python function arguments
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/4
"""


"""一、函数的定义之带默认值的形参"""

"""
    定义函数时，可以给形参设置默认值，这样，调用函数时如果不传递对应的实参，就会使用设置的默认值初始化形参
    给形参设置默认值的语法格式为：形参 = 默认值
    给形参设置默认值之后，可以简化函数的调用，只有与默认值不符的形参才需要传递额外的实参
"""

def f1(a, b = 5):
    print('a =', a, 'b =', b)

f1(2, 6)    # a = 2 b = 6
f1(2)       # a = 2 b = 5

def f2(a, b = 5, c = 8):
    print('a =', a, 'b =', b, 'c =', c)

f2(2, 6, 9) # a = 2 b = 6 c = 9
f2(2)       # a = 2 b = 5 c = 8
f2(2, 6)    # a = 2 b = 6 c = 8
f2(2, c = 9)# a = 2 b = 5 c = 9

"""
    定义函数时，没有设置默认值的形参必须位于设置了默认值的形参之前。否则，无法根据位置来匹配
    位置实参和对应的形参
"""

# def f(b = 5, a):
#     print('a =', a, 'b =', b)   # SyntaxError: non-default argument follows default argument
# 假设上面的定义是合法的，对于调用f(2)，你可能想把实参2传递给形参a，但是实参2是位置实参，
# 因此，实参2会传递给形参b，从而导致形参a存在实参缺失

"""
    当函数有多个形参时，把变化大的形参放在前面，把变化小的形参放在后面，变化小的形参就可以设置默认值
"""

"""
    给形参设置默认值之后，调用函数时就存在多种调用方式
"""

def fun(a, b = 5):
    print('a =', a, 'b =', b)

fun(3)      # a = 3 b = 5
fun(a = 3)  # a = 3 b = 5
fun(3, 6)   # a = 3 b = 6
fun(a = 3, b = 6)   # a = 3 b = 6
fun(b = 3, a = 6)   # a = 3 b = 6
fun(3, b = 6)   # a = 3 b = 6

"""
    定义函数时，给形参设置的默认值就被计算出来了。因此，如果给形参设置的默认值是可变类型的对象，
    并且前一次调用函数时在函数体内修改了形参的默认值，那么修改后的值将作为下一次调用函数时形参的默认值
"""

def fun1(L = []):
    L.append(18)
    print(L)

fun1()  # [18]
fun1()  # [18, 18]
fun1()  # [18, 18, 18]

"""
    不要把形参的默认值设置为可变类型的对象
"""

def fun2(L = None):
    if L is None:
        L = []
    L.append(18)
    print(L)

fun2()  # [18]
fun2()  # [18]
fun2()  # [18]


"""二、函数的定义之使用*定义关键字形参"""

"""
    定义函数时，可以在所有形参的某个位置添加一个*，这样，*后面的所有形参都被定义为
    只能接收关键字实参的关键字形参
"""

def f(a, b, *, c, d):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d)

f(1, 2, c = 3, d = 4)   # a = 1 b = 2 c = 3 d = 4
# f(1, 2, 3, 4)   # f() takes 2 positional arguments but 4 were given