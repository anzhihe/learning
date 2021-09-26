#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    decorator.py
 @Function:    python函数装饰器
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/23
"""


"""装饰器"""

"""
    对于某个函数，如果我们希望在不改变该函数代码的前提下，为该函数增加额外的功能，那么就可以使用
装饰器来装饰该函数。
    装饰器是一个函数，装饰器接收一个函数作为参数(传入的实参是被装饰的函数)，装饰器的内部嵌套定义
另一个函数，内函数中会引用装饰器的参数，并且装饰器的返回值是内函数。这样，就构成了一个闭包。
为了让内函数接收任意类型的参数，将内函数的形参定义为(*args, **kwargs)。在函数中，首先完成
为被装饰函数添加的新功能，然后调用被装饰的函数。
    把装饰器应用到被装饰函数的语法为：在被装饰函数的前面添加"@装饰器的函数名"。在被装饰函数add
的前面添加@log后，相当于执行了语句：add = log(add)，首先，被装饰的函数add会作为实参传递给
装饰器log，然后，返回装饰器的内函数wrapper，最后，将内函数wrapper赋值给名为add(被装饰函数的函数名)
的变量，这样，再调用被装饰的函数add时，其实调用的是装饰器的内函数wrapper。
"""

def log(func):
    def wrapper(*args, **kwargs):
        print("函数%s被调用了" % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def add(sum1, sum2):
    print(sum1, sum2)
    return sum1 + sum2

print(add(1, 2))

print(add.__name__) # wrapper

"""
    如果希望被装饰函数的特殊属性__name__的值为其函数名，而不是装饰器的内函数的函数名，
可以在装饰器的内函数前面添加另外一个装饰器：@functools.wraps(装饰器的参数名)，
其中functools.wraps指的是标准库functools中的函数wraps。
"""

import functools

def log2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("函数%s被调用了" % func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log2
def add2(sum1, sum2):
    print(sum1, sum2)
    return sum1 + sum2

print(add2(1, 2))

print(add2.__name__)    # add2

"""
    把装饰器应用到被装饰函数时,还可以传递额外的参数。此时，需要编写一个3层嵌套的装饰器。
对于@log3('6月', '18日')，相当于执行语句：add3 = log3(6月', '18日')(add3)。
"""

def log3(month, day):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("%s%s, 函数%s被调用了" % (month, day, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log3('6月', '18日')
def add3(sum1, sum2):
    print(sum1, sum2)
    return sum1 + sum2

print(add3(1, 2))