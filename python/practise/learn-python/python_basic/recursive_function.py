#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    recursive_function.py
 @Function:    python recursive function
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/5
"""


"""递归函数"""

"""
1、什么是递归函数？
    在一个函数的函数体内，可以调用其它函数
    如果在一个函数的函数体内调用了该函数本身，该函数就是递归函数
    
    递归函数包含了一个隐式的循环，因此，递归函数必须有一个明确的递归结束条件，也称为递归出口
    
    能用递归来解决的问题必须满足两个条件：
    (1) 可以通过递归调用来缩小问题的规模，且新问题与原问题有着相同的形式
    (2) 存在一种简单情境，可以使递归在简单情境下退出
    
    递归函数的优点是定义简单，逻辑清晰
"""

"""
2、使用递归计算阶乘
    n! = 1 * 2 * 3 ... * n = (n-1)! * n, 且1! = 1
    如果用函数fac(n)表示n!，那么fac(n) = fac(n - 1) * n = n * fac(n -1)，且fac(1) = 1
"""

def fac(n):
    """使用递归计算阶乘"""
    if n == 1:
        return 1
    return n * fac(n -1)

print('fac(6) =', fac(6))   # fac(6) = 720

"""
3、使用递归计算斐波那切数列
    F0 = 0, F1 = 1, Fn = F(n - 1) + F(n -2)(n >= 2)
    如果用函数fib(n)表示Fn，那么fib(n) = fib(n - 1) + fib(n - 2),
    且fib(0) = 0, fib(1) =1
"""

def fib(n):
    """使用递归计算斐波那切数列"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

print('fib(6) =', fib(6))   # fib(6) = 8