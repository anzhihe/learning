#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    built-in_function1.py
 @Function:    python获取对象信息的内置函数
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/14
"""


"""一、内置函数issubclass()和isinstance()"""

"""
    内置函数issubclass()用于判断类对象与类对象之间的关系
    内置函数isinstance()用于判断实例对象与类对象之间的关系
"""

"""
    内置函数issubclass接收两个实参，
    第一个实参是类对象
    第二个实参是类对象或由类对象组成的元组
    
    当第二个实参是类对象时，如果第一个实参是第二个实参的子类，那么返回True
    当第二个实参是类对象组成的元组时，如果第一个实参是第二个实参中任意一个类对象的子类，返回True
"""

class A(object):
    pass

class B(object):
    pass

class C(object):
    pass

class D(A):
    pass

print(issubclass(D, A)) # True
print(issubclass(D, B)) # False

print(issubclass(D, (B, A, C))) # True
print(issubclass(D, (B, C)))    # False

print(issubclass(bool, (str, int, dict)))   # True
print(issubclass(bool, (str, list, dict)))  # False

"""
    内置函数isinstance接收两个实参，
        第一个实参是实例对象
        第二个实参是类对象或由类对象组成的元组
        
    当第二个实参是类对象时，如果第一个实参是第二个实参的实例对象，或者第一个实参是第二个实参的
    子类的实例对象，那么返回True
    当第二个实参是类对象组成的元组时，如果第一个实参是第二个实参中任意一个类对象或其子类的实例对象，
    那么返回True
"""

print(isinstance(D(), D))   # True
print(isinstance(D(), A))   # True

print(isinstance(D(), (D, B, C)))   # True
print(isinstance(D(), (B, A, C)))   # True


"""二、内置函数type()"""

"""
    内置函数type()用于获得指定对象的类型
"""

"""
    实例对象的类型是其对应的类对象
"""

class MyClass(object):
    pass

mc = MyClass()

# mc的类型是MyClass，mc是MyClass的一个实例对象
print(type(mc)) # <class '__main__.MyClass'>

# 整数对象18的类型是int，整数对象18是int的一个实例对象
print(type(18)) # <class 'int'>

# 字符串对象'abc'的类型是str，字符串对象'abc'是str的一个实例对象
print(type('abc'))  # <class 'str'>

"""
    类对象的类型是type，也就是说，类对象是type的一个实例对象
"""

# 类对象MyClass的类型是type，类对象MyClass是type的一个实例对象
print(type(MyClass))    # <class 'type'>

# 类对象int的类型是type，类对象int是type的一个实例对象
print(type(int))        # <class 'type'>

# 类对象str的类型是type，类对象str是type的一个实例对象
print(type(str))        # <class 'str'>

"""
    自定义函数对象的类型是function
    内置函数对象的类型是builtin_function_or_method
"""

def do_sth():
    pass

print(type(do_sth)) # <class 'function'>

print(type(print))  # <class 'builtin_function_or_method'>

"""
    可以使用运算符==判断某个对象的类型是否是指定的类型
    对于基本数据类型，可以直接使用其对应的类名；如果不是基本数据类型，需要使用标准库中的模块types
    中定义的变量
"""

print(type(18) == int)      # True
print(type('abc') == str)   # True

# print(type(do_sth) == function)
# print(type(print) == builtin_function_or_method)

import types
print(type(do_sth) == types.FunctionType)   # True
print(type(print) == types.BuiltinFunctionType) # True


"""三、内置函数dir()"""

"""
    对于制定的类对象或实例对象，可以调用内置函数dir()获得其所有可以访问的属性和方法
    (包括从父类中继承的属性和方法)的列表
    类对象与实例对象的结果是有区别的，类对象的结果中不包括实例属性
"""

class MyClass(object):
    ca = "ca"

    def __init__(self):
        self.ia = "ia"

    def im(self):
        pass

    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass

print(dir(MyClass))

print(dir(MyClass()))
