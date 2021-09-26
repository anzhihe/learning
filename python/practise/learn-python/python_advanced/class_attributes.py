#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    class_attributes.py
 @Function:    python类属性
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/12
"""


"""类属性"""

"""
类属性指的是类对象所绑定的属性

绑定类属性(给类对象绑定属性)的方式有两种：
1. 在类对象的内部(方法外)
    语法格式：属性名 = 属性值
2. 在类对象的外部
    python是动态语言，所以，在类对象创建之后，可以对其动态地绑定属性
    语法格式：类对象.属性名 = 属性值
    如果指定名称的类属性已经存在，则是对类属性进行修改
    
访问类属性的方式有两种：
1. 在类对象的内部(方法中)
    语法格式：类对象.属性名
2. 在类对象的外部
    语法格式：类对象.属性名 或：实例对象.属性名
    类对象的所有实例对象都有一个指向类对象的指针，所以，类对象的所有实例对象都可以访问类属性
    
    之所以添加前缀"类对象"，是为了表明类属性被哪个类对象所绑定
"""

class MyClass(object):
    # 在类对象的内部(方法外)绑定类属性
    ca1 = 18

    def do_sth(self):
        # 在类对象的内部(方法中)访问类属性
        print(MyClass.ca1)

    def do_another(self):
        # 在类对象的内部(方法中)访问类属性
        print(MyClass.ca2)

mc = MyClass()

# 在类对象的外部调用方法，使得在类对象的内部(方法中)访问类属性
mc.do_sth() # 18

# 在类对象的外部通过类对象访问类属性
print(MyClass.ca1)  # 18
# 在类对象的外部通过实例对象访问类属性
print(mc.ca1)       # 18

# 在类对象的外部绑定类属性
MyClass.ca2 = 56
# 在类对象的外部通过类对象访问类属性
print(MyClass.ca2)  # 56
# 在类对象的外部通过实例对象访问类属性
print(mc.ca2)       # 56
# 在类对象的外部修改绑定的类属性值
MyClass.ca2 = 73
print(MyClass.ca2)  # 73
print(mc.ca2)       # 73

# 在类对象的外部调用方法，使得在类对象的内部访问类属性
mc.do_another()     # 73

"""
    访问实例属性和类属性都可以通过"实例对象.属性名"的方式。当通过"实例对象.属性名"的方式
    访问属性时，会先查找指定的实例对象中有没有指定名称的实例属性，如果没有，再查找对应的类对象中
    有没有指定名称的类属性。所以，当通过"实例对象.属性名"的方式访问属性时，如果实例属性和类属性同名，
    实例属性会屏幕掉类属性
    当通过"实例对象.属性名 = 属性值"的方式绑定属性时，这里的属性只表示实例属性(因为类属性没有
    这样的绑定方式)，所以，只会查找指定的实例对象有没有绑定指定名称的实例属性，如果没有则进行绑定，
    如果已经绑定了，则对属性值进行修改
"""

class Person(object):
    age = 18

p = Person()

# 在实例对象p中没有找到名为age的实例属性，然后在类对象Person中找到了名为age的类属性
print(p.age)    # 18
# 打印名为age的类属性
print(Person.age)   # 18

# 给实例对象p绑定实例属性
p.age = 19
# 实例属性屏蔽掉了同名的类属性
print(p.age)    # 19
# 打印名为age的类发展
print(Person.age) # 18

# 删除实例对象p绑定的实例属性
del p.age
print(p.age)    # 18

p1 = Person()
p2 = Person()

# p1.age += 2等价于：p1.age = p1.age + 2
# 等号右边是属性访问，整个赋值语句是实例属性的绑定
p1.age += 2
print(Person.age)   # 18
print(p1.age)       # 20
print(p2.age)       # 18

# 等号右边是类属性访问，整个赋值语句是类属性的绑定
Person.age += 3
print(Person.age)   # 21
print(p1.age)       # 20
print(p2.age)       # 21