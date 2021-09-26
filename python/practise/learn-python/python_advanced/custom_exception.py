#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    custom_exception.py
 @Function:    python自定义异常、异常与函数、获取异常信息
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/20
"""


"""一、自定义异常"""

"""
    尽管python内置的异常类对象可以满足我们绝大部分的需求，但是有时候我们可能想要创建自定义的
异常类对象。
    正如所有内置异常类对象的基类是Exception，自定义异常类对象只需要继承Exception或其子类
"""

class MyException(Exception):
    def __init__(self, msg1, msg2):
        self.msg1 = msg1
        self.msg2 = msg2

try:
    raise MyException("123", "abc")
except MyException as err:
    print(err)


"""二、异常和函数"""

"""
    当函数内发生异常时，异常实例对象会被抛给该函数的调用者，如果该函数的调用者没有捕获和处理，
则继续抛给上一层的调用者，这样一直向上抛，最后会被python解释器捕获。
"""

"""
def f1():
    print(1 / 0)

def f2():
    f1()

def f3():
    f2()

f3()
"""

"""
    在异常实例对象被向上抛的过程中，可以选择在合适的层对异常实例对象进行捕获和处理，而不需要
在每一层进行捕获和处理。
"""

def f1():
    print(1 / 0)

def f2():
    f1()

def f3():
    try:
        f2()
    except ZeroDivisionError as err:
        print(err)

f3()


"""三、获取异常信息"""

"""
    在捕获异常实例对象后，可以调用标准库模块sys中的函数exc_info以获取异常的相关信息。
    该函数的返回值是一个包含三个元素的元组，这三个元素分别表示：
    异常的类型、异常的错误信息和包含异常调用堆栈的跟踪信息的Traceback对象
    为了进一步提取Traceback对象中包含的信息，可以调用标准库模块traceback中的函数extract_tb()
"""

import sys
import traceback

def f1():
    print(1 / 0)

def f2():
    try:
        f1()
    except ZeroDivisionError:
        ex_type, ex_value, ex_traceback = sys.exc_info()

        print('异常的类型: %s' % ex_type)
        print('异常的错误信息: %s' % ex_value)
        print('异常调用堆栈的跟踪信息: %s' % ex_traceback)

        tb = traceback.extract_tb(ex_traceback)
        print(tb)

        for filename, linenum, funcname, source in tb:
            print('文件名: %s' % filename)
            print('行数：%s' % linenum)
            print('函数名：%s' % funcname)
            print('源码：%s' % source)

f2()