#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    encapsulation_inheritance.py
 @Function:    python面向对象编程之封装、继承与重写
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/13
"""

"""一、封装"""

"""
封装是面向对象编程的三大特征之一

封装有两方面的含义：
1. 将数据(属性)和行为(方法)包装到类对象中。在方法内部对属性进行操作，在类对象的外部调用方法。
这样，无需关心方法内部的具体实现细节，从而隔离了复杂度
2. 在类对象的内部通过访问控制把某些属性和方法隐藏起来，不允许在类对象的外部直接访问，而是在
类对象的内部对外提供公开的接口方法(例如getter和setter)以访问隐藏的信息。这样，就对隐藏的信息进行了保护
"""

class Student(object):
    def __init__(self):
        self.__score = 90

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("成绩必须在0~100之间")

s = Student()

s.set_score(88)
print(s.get_score())    # 88

# s.set_score(123)    # ValueError: 成绩必须在0~100之间


"""二、继承的概述"""

"""
1、为什么需要继承？
    在下面的程序中，由于狗和鸟都具有吃饭和喝水的这两个功能，所以，类对象Dog和Bird中都定义了
    eat()和drink()这两个方法，并且这两个方法的代码是完全相同的，这样就导致了程序中存在重复的代码

    class Dog(object):
        def eat(self):
            print("吃饭")
        
        def drink(self):
            print("喝水")
            
        def swim(self):
            print("游泳")

    class Bird(object):
        def eat(self):
            print("吃饭")
        
        def drink(self):
            print("喝水")
            
        def fly(self):
            print("飞翔")
"""

"""
2、什么是继承？
    当几个类对象中有共同的属性和方法时，就可以把这些属性和方法抽象并提取到一个基类中，每个类对象
    特有的属性和方法还是在本类对象中定义，这样，只需要让每个类对象都继承这个基类，就可以访问基类中的
    属性和方法了。继承基类的每个类对象被称为派生类。基类也被称为父类或超类，派生类也被称为子类
    python中的所有类对象都继承自一个统一的基类：object。这就是为什么我们在定义类对象时要在类名后面添加(object)
    
    除了封装，继承也是面向对象编程的三大特征之一。继承是实现代码复用的重要手段
"""

class Animal(object):
    def eat(self):
        print("吃饭")

    def drink(self):
        print("喝水")

class Dog(Animal):
    def swim(self):
        print("游泳")

class Bird(Animal):
    def fly(self):
        print("飞翔")

dog = Dog()
dog.eat()       # 吃饭
dog.drink()     # 喝水
dog.swim()      # 游泳

bird = Bird()
bird.eat()      # 吃饭
bird.drink()    # 喝水
bird.fly()      # 飞翔


"""三、继承应用"""

"""
    子类只有一个直接父类时称为单继承，假设子类和父类分别为ChildClass和ParentClass,
    子类继承父类的语法格式为：
    class ChildClass(ParentClass):
        pass
        
    子类有多个直接父类时称为多继承，假设子类是ChildClass，直接父类是ParentClass1，
    ParentClass2，...，ParentClassn，子类继承父类的语法格式为：
    class ChildClass(ParentClass1, ParentClass2, ..., ParentClassn):
        pass
"""

"""
    子类会继承所有父类(包括所有直接父类和所有间接父类)的所有属性和方法
"""

class ParentClassA(object):
    ca = 18

    def im(self):
        print("im()被调用了")

class ParentClassB(object):
    __pca = 23

    def __pim(self):
        print("__pim()被调用了")

class ParentClassC(ParentClassA, ParentClassB):
    @classmethod
    def cm(cls):
        print("cm()被调用了")

class ParentClassD(object):
    @staticmethod
    def sm():
        print("sm()被调用了")

class ChildClass(ParentClassC, ParentClassD):
    pass

print(dir(ChildClass))

"""
    子类可以添加父类中没有的属性和方法
"""

class BaseClass(object):
    ca_base = 5

    def im_base(self):
        print("im_base()被调用了")

class SubClass(BaseClass):
    ca_sub = 8

    def im_sub(self):
        print("im_sub()被调用了")

print(dir(SubClass))


"""四、重写"""

"""
    如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其进行重写从而提供自定义的实现，
    重写的方式为：在子类中定义与父类中同名的属性或方法(包括装饰器)
    
    子类重写父类的属性后，通过子类或其实例对象只能访问子类中重写后的属性，而无法再访问父类中
    被重写的属性
    
    子类重写父类的方法后，通过子类或其实例对象只能调用子类中重写后的方法，而无法再调用父类中
    被重写的方法
    父类中被重写的名为xxx的方法，在子类重写后的方法中可以通过super().xxx()进行通用
"""

class ParentClass(object):
    ca = "ca(父类)"

    def __init__(self):
        print("__init__()被调用了(父类)")

    def im(self):
        print("im()被调用了(父类)")

    @classmethod
    def cm(cls):
        print("cm()被调用了(父类)")

class ChildClass(ParentClass):
    ca = "ca(子类)"

    def __init__(self):
        super().__init__()
        print("__init__()被调用了(子类)")

    def im(self):
        super().im()
        print("im()被调用了(子类)")

    @classmethod
    def cm(cls):
        super().cm()
        print("cm()被调用了(子类)")

cc = ChildClass()

print(ChildClass.ca)    # ca(子类)
print(cc.ca)            # ca(子类)

cc.im()

ChildClass.cm()
cc.cm()
