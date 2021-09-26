#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    special_attributes.py
 @Function:    python获取对象的信息之特殊属性
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/16
"""


"""一、特殊属性和特殊方法"""

"""
    调用内置函数dir()后的返回值中，很多属性和方法都是以双下划线__开头和结尾的，这些属性和方法
    中的绝大多数都继承自类object
"""

print(dir(object))

"""
    以双下划线__开头和结尾的属性被称为特殊属性，以双下划线__开头和结尾的方法被称为特殊方法。
    特殊属性和特殊方法都是系统预定义的，我们自定义的属性名和方法名不要以双下划线__开头和结尾。
    在我们自定义类对象时，经常会重写一个或多个特殊方法，例如__init__。特殊方法会在特定的情形下
    被自动调用，很少需要手动调用特殊方法
"""


"""二、特殊属性__dict__"""

"""
    对于指定的类对象或实例对象，可以访问特殊属性__dict__获得该类对象或实例对象所绑定的
    所有属性和方法的字典。其中，字典中的键为属性名或方法名
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

MyClass.ca2 = "ca2"
print(MyClass.__dict__)

mc = MyClass()
mc.ia2 = "ia2"
print(mc.__dict__)  # {'ia': 'ia', 'ia2': 'ia2'}


"""三、特殊属性__doc__"""

"""
调用内置函数dir得到的类对象的所有属性中，有一个特殊属性叫__doc__，用于表示类对象的文档字符串

1、什么是类对象的文档字符串(docstring)?
    与函数的文档字符串类似，位于类对象的第一行的字符串被称为类对象的文档字符串，通常用三个引号表示
    类对象的文档字符串是对类对象的功能简要描述
    
    在PyCharm，类对象的文档字符串用灰色显示
    
    之所以称为"文档"字符串，是因为可以使用工具根据文档字符串自动地生成文档
    
    应该养成编写文档字符串的习惯，以提高程序的可读性
"""

class MyClass(object):
    """这是类对象的文档字符串"""
    pass

"""
2、访问类对象的文档字符串
    通过类对象的特殊属性__doc__可以访问类对象的文档字符串
    调用内置函数help()得到的帮助信息中会包含类对象的文档字符串
"""

print(list.__doc__)
print(MyClass.__doc__)  # 这是类对象的文档字符串

print(help(list))
print(help(MyClass))

"""三、特殊属性__slots__"""

"""
    python是动态语言，所以，在创建对象之后，可以对其动态地绑定属性和方法
    如果想要对实例对象动态绑定的属性和方法的名称进行限制，可以在其对应的类对象中
    定义特殊属性__slots__，并给__slots__赋值一个所有元素都为字符串的列表或元组，
    这样，对实例对象动态绑定的属性和方法的名称就只能来自于__slots__中的元素
"""

class MyClass(object):
    __slots__ = ("attr1", "do_sth1")

mc = MyClass()

mc.attr1 = 18

# mc.attr2 = 56   # AttributeError: 'MyClass' object has no attribute 'attr2'

def do_sth1(self):
    print("do_sth1被调用了")

from types import MethodType
mc.do_sth1 = MethodType(do_sth1, mc)
mc.do_sth1()    # do_sth1被调用了

def do_sth2(self):
    print("do_sth2被调用了")

# mc.do_sth2 = MethodType(do_sth2, mc)
# mc.do_sth2()    # AttributeError: 'MyClass' object has no attribute 'do_sth2'

"""
    默认情况下，访问实例对象的属性是通过访问该实例对象的特殊属性__dict__来实现的。例如：
    访问obj.x其实访问的是obj.__dict__['x']。
    在类对象中定义了特殊属性__slots__后，其实例对象就不会在创建特殊属性__dict__了，
    而是为每个属性创建一个描述器，访问属性时就会直接调用这个描述器。调用描述器比访问__dict__要快，
    因此，在类对象中定义特殊属性__slots__可以提高属性的访问速度。
    此外，在类对象中定义了特殊属性__slots__后，由于其实例对象不再创建特殊属性__dict__，同时，
    特殊属性__dict__是一个字典，字典的本质是哈希表，是一种用空间换取时间的数据结构，
    因此，在类对象中定义特殊属性__slots__可以减少内存消耗。
"""

# AttributeError: 'MyClass' object has no attribute '__dict__'
# print(MyClass().__dict__)

"""
    特殊属性__slots__只对其所在类对象的实例对象起作用，对其所在类对象的子类的实例对象是不起作用的
    如果子类也定义了特殊属性__slots__，那么子类的实例对象可以动态绑定的属性和方法的名称为
    子类的__slots__加上父类的__slots__
"""

class MyChildClass1(MyClass):
    pass

mcc1 = MyChildClass1()
mcc1.attr3 = 56

class MyChildClass2(MyClass):
    __slots__ = ("attr2", "do_sth2")

mcc2 = MyChildClass2()

mcc2.attr1 = 18
mcc2.attr2 = 18
mcc2.do_sth1 = 18
mcc2.do_sth2 = 18

# AttributeError: 'MyChildClass2' object has no attribute 'attr3'
# mcc2.attr3 = 18