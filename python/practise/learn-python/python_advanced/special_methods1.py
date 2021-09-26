#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    special_methods1.py
 @Function:    python类对象的特殊方法
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/17
"""


"""一、类对象的特殊方法之__len__()"""

"""
    内置函数len()用于返回对象的长度
"""

print(len([1, 2, 3, 4, 5])) # 5
print(len('abcde'))         # 5
print(len({'a': 1, 'b': 2, 'c': 3}))    # 3

"""
    在上面的例子中，内置函数len()的实参都是内置类对象的实例对象，例如：
    [1, 2, 3, 4, 5]是内置类对象list的一个实例对象；
    {'a': 1, 'b': 2, 'c': 3} 是内置类对象dict的一个实例对象
    
    内置函数len()的实参在默认情况下不能是自定义类对象的实例对象
"""

# class MyClass(object):
#     pass

# print(len(MyClass()))   # TypeError: object of type 'MyClass' has no len()

"""
    如果想让内置函数len()的实参可以是自定义类对象的实例对象，必须在自定义类对象中
    实现特殊方法__len__()。这样，调用内置函数len()时，在其内部会自动调用实参所对应类对象的
    特殊方法__len__()。之所以内置函数len()的实参可以是上述内置类对象的实例对象，
    是因为上述的内置类对象中都实现了特殊方法__len__()
"""

class MyClass(object):
    def __len__(self):
        return 18

print(len(MyClass()))   # 18


"""二、类对象的特殊方法之__iter__()和__next__()"""

L = [1, 2, 3, 4, 5]

for item in L:
    print(item)

"""
    for-in语句在默认情况下不能用于自定义类对象的实例对象
"""

# class MyClass(object):
#     pass

# for item in MyClass():  # TypeError: 'MyClass' object is not iterable
#     print(item)

"""
    如果想让for-in语句可以用于自定义类对象的实例对象，必须在自定义类对象中实现特殊方法
    __iter__()和__next__()。for-in语句首先会调用特殊方法__iter__()返回一个可迭代对象，
    然后不断调用可迭代对象的特殊方法__next__()返回下一次迭代的值，直到遇到StopIteration时退出循环
    只实现了特殊方法__iter__()的类对象，被称为可迭代类对象；同时实现了特殊方法__iter__()和
    __next__()的类对象，被称为迭代器类对象
    之所以for-in语句可以用于某些内置类对象(例如：list、tuple、str等)的实例对象，
    是因为这些内置类对象中都同时实现了特殊方法__iter__()和__next__()
"""

class MyClass(object):
    def __init__(self):
        self.data = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.data > 5:
            raise StopIteration()
        else:
            self.data += 1
            return self.data

for item in MyClass():
    print(item)


"""三、类对象的特殊方法之__add__()和__radd__()"""

"""
    标准算术运算符在默认情况下不能用于自定义类对象的实例对象
"""

class MyClass1(object):
    pass

class MyClass2(object):
    pass

# TypeError: unsupported operand type(s) for +: 'MyClass1' and 'MyClass2'
# print(MyClass1() + MyClass2())

"""
    如果想让标准算术运算符可以用于自定义类对象的实例对象，必须在自定义类对象中实现标准算术运算符
    对应的以下特殊方法：
    (1) +对应的特殊方法是__add__()和__radd__()
    (2) -对应的特殊方法是__sub__()和__rsub__()
    (3) *对应的特殊方法是__mul__()和__rmul__()
    (4) /对应的特殊方法是__truediv__()和__rtruediv__()
    (5) //对应的特殊方法是__floordiv__()和__rfloordiv__()
    之所以可以使用加法和乘法运算符操作列表，是因为列表所对应的类对象list中实现了+和*对应的特殊方法；
    之所以可以使用加法和乘法运算符操作字符串，是因为字符串所对应的类对象str中实现了+和*对应的特殊方法
    
    假设两个运算数obj1和obj2，以+为例，对于obj1 + obj2，需要在obj1对应的自定义类对象中实现
    特殊方法__add__()，或在obj2对应的自定义类对象中实现特殊方法__radd__()（radd中的r是right的缩写，
    因为obj2位于运算符+的右边，所以实现的特殊方法是__radd__()；因为obj1位于运算符+的左边，
    所以实现的特殊方法是__add__()）。
"""

class C1(object):
    def __add__(self, other):
        print("特殊方法__add__被调用")
        return "xxx"
        # return NotImplemented

class C2(object):
    def __radd__(self, other):
        print("特殊方法__radd__被调用")
        return "yyy"
        # return NotImplemented

obj1 = C1()
obj2 = C2()

print(obj1 + obj2)