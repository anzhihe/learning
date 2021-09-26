#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    oop_def.py
 @Function:    Python Object Oriented Programming
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/11
"""


"""一、面向对象编程概述"""

"""
    面向对象编程(Object Oriented Programming，简称OOP)，是一种编程方式，这种编程方式
    需要使用"对象"来实现
    
    对象具有以下特征：
    (1) 世间万物皆对象
        某个具体的领域也是由对象组成的，例如：
        在学校领域，对象包括学生、教师、课程、教室和成绩单等
        在银行领域，对象包括银行账户、出纳员、支票、现金和验钞机等
        因此，问题领域中的概念和实体都可以被抽象为对象
    (2) 每个对象都是唯一的
        对象的唯一性来自于真实世界中事物的唯一性
        世界上不存在两片一模一样的叶子，因此在软件系统中的对象也具有唯一性
        例如：学校领域的学生小张、学生小王、小张的成绩单和小王的成绩单，这些对象都是唯一的
    (3) 对象具有属性和行为
        例如：小王，性别男，年龄18，身高1.8m，体重70kg，能够学习、唱歌和打乒乓球
        小王的属性包括姓名、性别、年龄、身高和体重，行为包括学习、唱歌和打乒乓球
        再例如：一部手机，品牌是苹果，价格是6000元，黑色，能够拍照、打电话和收发短信
        这部手机的属性包括品牌、价格和颜色，行为包括拍照、打电话和收发短信
        对象的行为包括具有的功能及具体的实现
    (4) 对象具有状态
        状态是指某个瞬间对象的各个属性的取值
        对象的某些行为往往会改变对象自身的状态，即属性的取值
        例如，小王的体重本来为80kg，经过减肥后，体重变为70kg
    (5) 对象分为类对象和实例对象两大类
        类对象是具有相同属性和行为的实例对象的抽象
        类对象就是实例对象的模版，实例对象是由类对象创建出来的
        此外，同一个类对象的所有实例对象如果具有相同的属性，表明它们的属性的含义是相同的，
        但是它们的状态不一定相同，也就是属性的取值不一定相同。例如：学生小张、小王和小李，
        都有姓名、性别、年龄、身高和体重这些属性，但是他们的属性的取值是不同的
"""


"""二、面向对象编程的步骤"""

"""
    面向对象编程的大体步骤：
    (1) 抽象出类对象
    (2) 抽象出类对象的属性
    (3) 抽象出类对象的行为(方法)
    (4) 根据类对象创建实例对象
    (5) 通过实例对象访问属性和方法
"""

class Dog(object):
    def __init__(self, breed, name, age, health):
        self.breed = breed      # 品种
        self.name = name        # 昵称
        self.age = age          # 年龄
        self.health = health    # 健康状况

    # 跑
    def run(self):
        print("Dog is running")

    # 吠
    def bark(self):
        print("Dog is barking")

    # 咬
    def bite(self):
        print("Dog is biting")

dog = Dog("拉布拉多", "旺财", 3, "很好")

print(dog.breed)
print(dog.name)
print(dog.age)
print(dog.health)

dog.run()
dog.bark()
dog.bite()


"""三、定义类对象和创建实例对象"""

"""
1、定义类对象
定义类对象的语法格式：
    class 类名(object):
        # 属性和方法
    其中，
    (1) 类名由一个或多个单词组合而成，每个单词的首字母大写且其余字母全部小写，例如：SomeClass
    (2) (object)表示该类对象继承自python内置的类对象object，python中所有的类对象都继承自一个统一的基类：object
"""

class SomeClass(object):
    pass

"""
2、创建实例对象
    根据类对象创建实例对象的语法格式为：类名([实参])
    
    为了在创建实例对象后对其进行初始化(例如：给实例对象绑定一些属性)，可以在类对象中定义一个
    名为__init__的特殊方法(以双下划线__开头和结尾的方法)。这样，创建实例对象后就会自动调用特殊方法__init__
    
    方法就是定义在类对象中的函数。方法与函数的区别在于：
    (1) 定义方法时，方法的第一个形参表示该方法的实例对象，第一个形参的名称通常是self，也可以是其它名称(不建议)
    (2) 调用方法时，系统自动将调用该方法的实例对象作为实参传递给第一个形参。第一个实参会传递给第二个形参，
    第二个实参会传递给第三个形参，依次类推
    
    如果没有定义特殊方法__init__，或者定义了特殊方法__init__但是没有定义除self之外的形参，
    那么根据类对象创建实例对象时就不需要传入实参
"""

sc = SomeClass()
print(sc)   # <__main__.SomeClass object at 0x107ecbee0>

class SomeClass1():
    def __init__(self):
        self.data = 18

sc1 = SomeClass1()
print(sc1)  # <__main__.SomeClass1 object at 0x1086f0d00>

"""
    如果在类对象中定义了特殊方法__init__，那么对于"类名([实参])"，会执行两大步：
    (1) 创建实例对象
    (2) 自动调用创建的实例对象的特殊方法__init__(创建的实例对象会作为实参被自动传递给特殊方法
    __init__的第一个形参self)
"""

class SomeClass2(object):
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

sc2 = SomeClass2(5, 8)
print(sc2)  # <__main__.SomeClass2 object at 0x10c6fabb0>