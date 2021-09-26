#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    try_except.py
 @Function:    使用try-except语句捕获和处理异常
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/19
"""


"""使用try-except语句捕获和处理异常"""

"""
    程序在运行期间产生异常时，为了让程序能够继续运行，可以对抛出的异常实例对象进行捕获和处理，
这是通过try-except语句实现的：
    把可能会产生异常的代码放在try语句块中以捕获异常实例对象，
    把处理异常的代码放在由若干个except子句组成的except语句块中。
    
try-except语句的语法格式为：
    try:
        可能会产生异常的代码
    except 异常类对象1:
        当前except子句处理异常的代码
    except 异常类对象2:
        当前except子句处理异常的代码
    ...
    except 异常类对象n:
        当前except子句处理异常的代码
"""

try:
    result = 1 / 2
    # result = 1 / 0
    # result = int('abc')
    print(result)
except ImportError:
    print("导入错误")
except ZeroDivisionError:
    print("0不能作为除数")
except TypeError:
    print("类型错误")
print("结束")

"""
    如果抛出的异常实例对象所对应的类对象是except子句中异常类对象的子类，那么该except子句也会被匹配
"""

try:
    result = 1 / 0
    print(result)
except ArithmeticError:
    print("数学错误")

"""
    当try语句块中产生异常时，会从上到下依次查找是否有匹配的except子句，只要找到一个匹配的
except子句，则不会再查找剩余的except子句。因此，要注意各个except子句的顺序
"""

try:
    result = 1 / 0
    print(result)
except ZeroDivisionError:
    print("0不能作为除数")
except ArithmeticError:
    print("数学错误")
print("结束")

try:
    result = 1 / 0
    print(result)
except ArithmeticError:
    print("数学错误")
except ZeroDivisionError:
    print("0不能作为除数")
print("结束")

"""
    当多个异常类对象对应的异常处理代码完全相同时，可以把这些异常类对象以元组的形式放在一个except子句中
"""

try:
    result = 1 / 0
    print(result)
except TypeError:
    print("运行出错了")
except ZeroDivisionError:
    print("运行出错了")
except ValueError:
    print("运行出错了")

try:
    result = 1 / 0
    print(result)
except (TypeError, ZeroDivisionError, ValueError):
    print("运行出错了")

"""
    如果想在匹配到的except子句中访问异常实例对象，可以在except子句中的冒号添加关键字as和一个变量 
"""

try:
    result = 1 / 0
    print(result)
except ZeroDivisionError as err:
    print(type(err))    # <class 'ZeroDivisionError'>
    # 类对象ZeroDivisionError实现了特殊方法__str__()
    print(err)          # division by zero

try:
    result = int('abc')
    print(result)
except (TypeError, ZeroDivisionError, ValueError) as err:
    print(type(err))    # <class 'ValueError'>
    # 类对象ValueError实现了特殊方法__str__()
    print(err)          # invalid literal for int() with base 10: 'abc'

"""
    为了在except语句块中将所有的异常对象尽可能地覆盖到，可以将最后一个except子句中的
异常类对象指定为Exception(内置的异常类对象和自定义的异常类对象都继承自Exception)，
或者在最后一个except子句中不指定异常类对象
"""

try:
    result = 1 / 0
    print(result)
except (TypeError, ValueError):
    print("类型错误或值错误")
# except:
except Exception:
    print("其它错误")