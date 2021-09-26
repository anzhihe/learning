#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    class_static_methods.py
 @Function:    python类方法、静态方法、访问控制
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/12
"""


"""一、类方法"""

"""
    类方法指的是类对象中使用装饰器@classmethod进行装饰的方法
    
    在类对象中定义类方法时，必须使用装饰器@classmethod进行装饰，此外，第一个形参表示类对象，
    其对应的实参由系统自动传入。第一个形参的名称通常是cls，也可以是其它名称
    
    类方法可以被类对象所调用，语法格式为：类对象.方法名([实参]) 或：cls.方法名([实参])
    
    类方法也可以被实例对象所调用，语法格式为：实例对象.方法名([实参]) 或：self.方法名([实参])
    类对象的所有实例对象都有一个指向类对象的指针，所以，类对象的所有实例对象都可以调用类对象中定义的类方法
    
    调用类方法时，系统自动将类对象作为实参传递给第一个形参。第一个实参会传递给第二个形参，
    第二个实参会传递给第三个形参，依次类推
"""

class MyClass(object):
    # 在类对象中定义类方法
    @classmethod
    def cm1(cls, p1, p2):
        print(p1, p2)

    @classmethod
    def cm2(cls):
        # 通过类对象调用类方法
        MyClass.cm1(1, 2)
        cls.cm1(1, 2)

    def im(self):
        # 通过实例对象调用类方法
        self.cm1(1, 2)

# 通过类对象调用类方法
MyClass.cm1(1, 2)   # 1 2

mc = MyClass()

# 通过实例对象调用类方法
mc.cm1(1, 2)        # 1 2
mc.cm2()

mc.im()


"""二、静态方法"""

"""
    类对象的静态方法只是一个普通函数。把某个普通函数归属于类对象，可能只是为了易于代码管理
    
    在类对象中定义静态方法时，必须使用装饰器@staticmethod进行装饰。静态方法只是一个普通函数，
    因此，第一个形参没有特殊含义和要求
    
    静态方法可以被类对象所调用，语法格式为：类对象.方法名([实参]) 或：cls.方法名([实参])
    
    静态方法也可以被实例对象所调用，语法格式为：实例对象.方法名([实参]) 或：self.方法名([实参])
    类对象的所有实例对象都有一个指向类对象的指针，所以，类对象的所有实例对象都可以调用类对象中定义的类方法
    
    调用静态方法时的参数传递与调用普通函数是一样的
"""

class MyClass(object):
    # 在类对象中定义静态方法
    @staticmethod
    def sm(p1, p2):
        print(p1, p2)

    @classmethod
    def cm(cls):
        # 通过类对象调用静态方法
        MyClass.sm(1, 2)
        cls.sm(1, 2)

    def im(self):
        # 通过实例对象调用静态方法
        self.sm(1, 2)

# 通过类对象调用静态方法
MyClass.sm(1, 2)    # 1 2

mc = MyClass()

# 通过实例对象调用静态方法
mc.sm(1, 2)         # 1 2

MyClass().cm()
mc.im()


"""三、访问控制"""

"""
    访问控制指的是：控制类对象的属性和方法在类对象的外部是否可以直接访问
    如果在类对象的某个属性或方法前添加两个下划线__，那么在类对象的外部就不能直接访问该属性或方法了
"""

class MyClass(object):
    def __init__(self):
        self.__pia = 18

    def __pim(self):
        print("__pim()被调用了")

    def do_sth(self):
        print(self.__pia)
        self.__pim()

mc = MyClass()

# print(mc.__pia) # AttributeError: 'MyClass' object has no attribute '__pia'
# mc.__pim()  # AttributeError: 'MyClass' object has no attribute '__pim'

mc.do_sth()

"""
    之所以不能在类对象的外部直接访问以下划线开头的属性或方法，是因为：Python解释器对外把属性或方法
    __xxx改成了另外一个名字：_类名__xxx。所以，在类对象的外部仍然可以通过_类名__xxx
    访问属性或方法__xxx。但是，强烈建议不要这样访问，因为不同版本的Python解释器可能会把属性或方法
    __xxx改成不同的名字
"""

print(mc._MyClass__pia) # 18
mc._MyClass__pim()      # __pim()被调用了

# 调用内置函数dir()获得指定对象所有可以访问的属性和方法
print(dir(mc))

"""
    仍然可以在类对象的外部动态绑定名为__xxx的属性或方法，这与类对象内部名为__xxx的属性或方法
    是不同的
"""

mc.__pia = "Hi"

print(mc.__pia) # Hi

print(dir(mc))

"""
    除了在类对象的属性或方法前添加两个下划线__，还可以在类对象的属性或方法前添加单下划线_,
    这表示：虽然可以在类对象的外部访问该属性或方法，但是最好不要访问
"""

class SomeClass(object):
    def __init__(self):
        self._pia = 18

    def _pim(self):
        print("_pim()被调用了")

sc = SomeClass()

print(sc._pia)  # 18
sc._pim()       # _pim()被调用了