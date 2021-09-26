#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    polymorphism.py
 @Function:    python面向对象编程之多态
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/13
"""

"""多态"""

"""
    除了封装和继承，多态也是面向对象编程的三大特征之一
    简单地说，多态就是"具有多种形态"，它指的是：即便不知道一个变量所引用的对象到底是什么类型，
    仍然可以通过这个变量调用方法，在运行过程中根据变量所引用对象的类型，动态地决定引用哪个对象中的方法
    
    如果子类中不存在指定名称的方法，回到父类中去查找，如果在父类中找到了，则调用父类中的方法
"""

class ParentClass(object):
    def do_sth(self):
        print("do_sth() in ParentClass")

class ChildClass1(ParentClass):
    def do_sth(self):
        print("do_sth() in ChildClass1")

class ChildClass2(ParentClass):
    def do_sth(self):
        print("do_sth() in ChildClass2")

class ChildClass3(ParentClass):
    pass

class SomeClass(object):
    def do_sth(self):
        print("do_sth() in SomeClass")

def f(parent):
    parent.do_sth()

f(ParentClass())    # do_sth() in ParentClass
f(ChildClass1())    # do_sth() in ChildClass1
f(ChildClass2())    # do_sth() in ChildClass2
f(SomeClass())      # do_sth() in SomeClass

f(ChildClass3())    # do_sth() in ParentClass

"""
    python是动态语言，在调用函数时不会检查参数的类型，从而导致与静态语言(例如Java)的多态
    是有区别的。对于静态语言，实现多态有三个必要条件
    (1) 继承
    (2) 重写
    (3) 父类类型的变量引用父类或子类类型的实例对象
        因此，对于静态语言，在上面的程序中，要限定形参parent的类型是ParentClass，传入的实参只能是
        ParentClass、ChildClass1和ChildClass2的实例对象
        
    动态语言的多态崇尚"鸭子类型"：当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，
    那么这只鸟就可以被称为鸭子
    在鸭子类型中，我们并不关心是什么类型，到底是不是鸭子，只关心对象的行为
    在上面的程序中，我们并不关心变量parent所引用的对象是什么类型，到底是不是ParentClass或
    其子类类型，只关心变量parent所引用的对象是否有do_sth()这个方法
"""
