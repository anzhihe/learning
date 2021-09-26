#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    instance_methods.py
 @Function:    python实例方法
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/12
"""


"""实例方法"""

"""
    实例方法指的是只有实例对象才可以调用的方法
    
    在类对象中定义实例方法时，第一个形参表示调用该方法的实例对象，其对应的实参由系统自动传入
    第一个形参的名称通常是self，也可以是其它名称
    
    实例方法只能被实例对象所调用，有两种调用方式：
    1. 在类对象的内部(其它实例方法中)
        语法格式：self.方法名([实参])
    2. 在类对象的外部
        语法格式：实例对象.方法名([实参])
        类对象的所有实例对象都有一个指向类对象的指针，所以类对象的所有实例对象都可以调用类对象中定义的实例方法
        
    调用实例方法时，系统自动将调用该实例方法的实例对象作为实参传递给第一个形参。第一个实参会
    传递给第二个形参，第二个实参会传递给第三个形参，依次类推
"""

class MyClass(object):
    # 在类对象中定义实例方法
    def im1(self, p1, p2):
        print(p1, p2)

    def im2(self):
        # 在类对象的内部(其它实例方法中)调用实例方法
        self.im1(1, 2)

mc = MyClass()

# 在类对象的外部调用实例方法
mc.im1(1, 2)    # 1 2
mc.im2()        # 1 2

"""
    Python是动态语言，所以，在实例对象或类对象创建之后，可以对其动态地绑定实例方法
    
    同一个类对象的不同实例对象所绑定的实例方法是相互独立的。也就是说，给一个实例对象绑定的实例方法，
    对于另一个实例对象是不起作用的
    
    为了能让一个类对象的所有实例对象都能调用某个实例方法，可以给类对象绑定该实例方法
"""

# 定义一个函数作为实例方法
def do_sth(self):
    print("do_sth()被调用了")

# 导入标准库types中的MethodType类
from types import MethodType
# 给实例对象mc动态地绑定实例方法
mc.do_sth = MethodType(do_sth, mc)
# 调用绑定的实例方法
mc.do_sth()     # do_sth()被调用了

mc2 = MyClass()
# mc2.do_sth()    # AttributeError: 'MyClass' object has no attribute 'do_sth'

# 再定义一个函数作为实例方法
def im3(self):
    print("im3()被调用了")

# 给类对象动态地绑定实例方法
MyClass.im3 = im3

# 类对象的所有实例对象都能调用给类对象动态绑定的实例方法
mc.im3()    # im3()被调用了
mc2.im3()   # im3()被调用了