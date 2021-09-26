#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    mro.py
 @Function:    python方法解析顺序
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/14
"""


"""MRO"""

"""
    MRO的全称是Method Resolution Order(方法解析顺序)，它指的是对于一棵类继承树，当调用
    最底层类对象所对应实例对象的方法时，python解释器在类继承树上搜索方法的顺序
    对于一棵类继承树，可以调用最底层类对象的方法mro()或访问最底层类对象的特殊属性__mro__，
    获得这棵类继承树的MRO
"""

class A(object):
    def f(self):
        print("A.f")

class B(A):
    def f(self):
        print("B.f")

class C(A):
    def f(self):
        print("C.f")

class D(B, C):
    def f(self):
        print("D.f")

# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.mro())

# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.__mro__)

d = D()
d.f()   # D.f

"""
    在子类重写后的方法中通过super()调用父类中被重写的方法时，在父类中搜索方法的顺序基于
    以该子类为最底层类对象的类继承树的MRO
    如果想调用指定父类中被重写的方法，可以给super()传入两个实参：super(a_type, obj)，其中，
    第一个实参a_type是个类对象，第二个实参obj是个实例对象，这样，被指定的父类是：
    obj所对应类对象的MRO中，a_type后面那个类对象
"""

class A(object):
    def f(self):
        print("A.f")

class B(A):
    def f(self):
        print("B.f")

class C(A):
    def f(self):
        print("C.f")

class D(B, C):
    def f(self):
        super().f()     # B.f
        # super(D, self).f()  # B.f
        # super(B, self).f()  # C.f
        # super(C, self).f()  # A.f

d = D()
d.f()   # B.f