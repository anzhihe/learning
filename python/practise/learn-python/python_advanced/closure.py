#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    closure.py
 @Function:    python闭包
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/22
"""


"""闭包"""

"""
    如果在一个函数的内部嵌套定义了另外一个函数(姑且将外部的函数和内部的函数分别称之为外函数和
内函数)，内函数中引用了外函数中的变量，并且外函数的返回值是内函数，这样，就构成了一个闭包。
"""

def outer():
    a = 10
    def inner():
        print(a)
    return inner

"""
    通常情况下，在函数调用结束后，函数内定义的变量将不再可用。
    但是，对于闭包而言，在外函数调用结束后，外函数中被内函数引用的变量仍然是可以用，
因为外函数中被内函数引用的变量会被绑定到内函数的特殊属性__closure__中。
"""

def do_sth():
    temp = 8
    print(temp)

do_sth()
# print(temp)

outer_result = outer()
outer_result()  # 10
outer()()       # 10

print(outer_result.__closure__) # (<cell at 0x106153fa0: int object at 0x105f45a50>,)
print(outer_result.__closure__[0].cell_contents)    # 10

"""
    在默认情况下，在内函数中不能修改外函数中的变量引用的对象(如果引用的对象是可变类型的，
可以修改对象的内容)
"""

def outer2():
    a = 10
    def inner2():
        # 重新定义了一个变量a，把外函数中的变量a给屏蔽了
        # a = 11

        # 相当于a = a + 1
        # 重新定义了一个变量a，把外函数中的变量a给屏蔽了
        # 当计算等号右边的a + 1时，新定义的变量a还没有被赋值，因此程序报警
        # a += 1

        pass
    return inner2

def outer3():
    a = [3]
    def inner3():
        # 重新定义了一个变量a，把外函数中的变量a给屏蔽了
        # a = [1]

        # 变量a引用的对象是可变类型的，可以修改对象的内容
        a[0] = 8

        print(a)
    return inner3

outer3()()  # [8]

"""
    如果想在内函数中修改外函数中的变量所引用的对象，可以在内函数中使用关键字nonlocal对变量
进行声明，从而表明在内函数中并没有重新定义一个新的同名变量，而是使用外函数中该名称的变量。
"""

def outer4():
    a  = 10
    def inner4():
        nonlocal a

        # a = 11
        a += 1

        print(a)
    return inner4

outer4_result = outer4()
outer4_result()     # 11

"""
    对于内函数中引用的外函数中的变量，在调用内函数后对该变量的修改，在下一次调用内函数时仍然是
有效的，因为该变量会被绑定到内函数的特殊属性__closure__中。
"""

outer4_result()     # 12