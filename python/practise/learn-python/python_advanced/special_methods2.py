#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    special_methods2.py
 @Function:    python类对象的特殊方法
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/17
"""


"""一、类对象的特殊方法之__str__()和__repr__()"""

"""
类对象的特殊方法之__str__()和__repr__()用于自定义并返回实例对象的字符串表示形式

1. 当在交互式命令行中直接打印一个实例对象时，
    如果在实例对应的类对象中实现了特殊方法__repr__()，会自动调用该方法；
    否则，会打印实例对象对应的类对象和实例对象在内存中的地址
    
2. 当调用内置函数print打印一个实例对象时，
    如果在实例对象对应的类对象中实现了特殊方法__str__()，会自动调用该方法
    否则，如果在实例对象对应的类对象中实现了特殊方法__repr__()，会自动调用该方法；
    否则，会打印实例对象对应的类对象和实例对象在内存中的地址

3. 当调用内置函数str创建字符串并且实参是一个实例对象时，
    如果在实例对象对应的类对象中实现了特殊方法__str__()，在内置函数str的内部会自动调用该方法；
    否则，如果在实例对象对应的类对象中实现了特殊方法__repr__()，在内置函数str的内部会自动调用该方法；
    否则，会打印实例对象对应的类对象和实例对象在内存中的地址
    
4. 当调用内置函数repr创建字符串并且实参是一个实例对象时，
    如果在实例对象对应的类对象中实现了特殊方法__repr__()，在内置函数repr的内部会自动调用该方法；
    否则，会打印实例对象对应的类对象和实例对象在内存中的地址
"""

"""
>>> class MyClass(object):
...     pass
... 
>>> mc = MyClass()
>>> mc
<__main__.MyClass object at 0x103f41550>
>>> print(mc)
<__main__.MyClass object at 0x103f41550>
>>> str(mc)
'<__main__.MyClass object at 0x103f41550>'
>>> repr(mc)
'<__main__.MyClass object at 0x103f41550>'
"""

"""
>>> class MyClass(object):
...     def __str__(self):
...         return "__str__被调用"
... 
>>> mc = MyClass()
>>> mc
<__main__.MyClass object at 0x103e5c588>
>>> print(mc)
__str__被调用
>>> str(mc)
'__str__被调用'
>>> repr(mc)
'<__main__.MyClass object at 0x103e5c588>'
"""

"""
>>> class MyClass(object):
...     def __repr__(self):
...         return "__repr__被调用"
... 
>>> mc = MyClass()
>>> mc
__repr__被调用
>>> print(mc)
__repr__被调用
>>> str(mc)
'__repr__被调用'
>>> repr(mc)
'__repr__被调用'
"""

"""
>>> class MyClass(object):
...     def __str__(self):
...         return "__str__被调用"
...     def __repr__(self):
...         return "__repr__被调用"
... 
>>> mc = MyClass()
>>> mc
__repr__被调用
>>> print(mc)
__str__被调用
>>> str(mc)
'__str__被调用'
>>> repr(mc)
'__repr__被调用'
"""

"""
    通常情况下，类对象的特殊方法__str__()和__repr__()的实现代码是一样的，因此，
    当实现了其中一个后，可以把其方法名赋值给另一个的方法名
"""

class MyClass(object):
    def __str__(self):
        return "xxx"

    __repr__ = __str__

"""
    内置函数str()和repr()都返回对象的字符串表示，其区别在于：
    str()的返回值是给用户看的，对用户更加友好
    repr()的返回值是给程序开发者看的，是为了调试服务的
    >>> str("Hello,\nWorld!")
    'Hello,\nWorld!'
    >>> repr("Hello,\nWorld!")
    "'Hello,\\nWorld!'"
"""


"""二、类对象的特殊方法之__new__()"""

"""
当使用"类名([实参])"创建实例对象时，python解释器的主要处理过程包括两大步：
1. 调用特殊方法__new__()创建实例对象
    首先会查找该类对象是否实现了特殊方法__new__()，如果没有实现，则去其父类中依次查找，
    直到类对象object
    特殊方法__new__()会返回创建的实例对象
2. 调用特殊方法__init__()对创建的实例对象进行初始化
    __new__()返回的实例对象会作为实参被自动传递给__init__()的第一个形参self
"""

class Parent(object):
    def __new__(cls, *args, **kwargs):
        # 父类的__new__()被调用，其形参cls对应实参的id：140398668516112
        print("父类的__new__()被调用，其形参cls对应实参的id：%s" % id(cls))
        obj = super().__new__(cls)    # object的特殊方法__new__()知道如何创建实例对象
        print("创建的实例对象的id：%s" % id(obj))    # 创建的实例对象的id：4430051744
        return obj

class Child(Parent):
    def __init__(self, name):
        # 子类的__init__()被调用，其形参self对应实参的id：4430051744
        print("子类的__init__()被调用，其形参self对应实参的id：%s" % id(self))
        self.name = name

print("父类的id：%s" % id(Parent))  # 父类的id：140398668515168
print("子类的id：%s" % id(Child))   # 子类的id：140398668516112

child = Child("Mike")
print("创建的实例对象的id：%s" % id(child))  # 创建的实例对象的id：4430051744
