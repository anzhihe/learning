#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    lambda.py
 @Function:    lambda表达式
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/22
"""


"""lambda表达式"""

"""
定义函数的语法格式：
    def 函数名([形式参数1, 形式参数2, ..., 形式参数n]):
        函数体
        
    当函数体中只有一行return语句时，函数的定义可以用一个lambda表达式来代替，其语法格式为：
    lambda [形式参数1, 形式参数2, ..., 形式参数n]: 关于形式参数的表达式
    
    与定义函数的语法格式相比，lambda表达式：
    (1) 没有函数名
    (2) 没有关键字def
    (3) 没有小括号
    (4) 关于形式参数的表达式相当于函数的返回值
    
    lambda表达式就是匿名简化版的函数
"""

def add(num1, num2):
    return num1 + num2

print(add(1, 2))    # 3

print((lambda num1, num2: num1 + num2)(1, 2))   # 3

"""
    在python中，一切皆为对象。所以，lambda表达式也是对象，从而lambda表达式可以被赋值给变量
"""

le = lambda num1, num2: num1 + num2
print(le(1, 2)) # 3

"""
    因为lambda表达式是匿名简化版的函数，所以，lambda表达式可以作为函数的实参
"""

result = map(lambda x: x * x, [1, 2, 3, 4])
print(list(result)) # [1, 4, 9, 16]

"""
    因为lambda表达式是匿名简化版的函数，所以，lambda表达式可以作为函数的返回值
"""

def do_sth():
    return lambda num1, num2: num1 + num2

print(do_sth()(1, 2))   # 3