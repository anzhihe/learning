#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    instance_attributes.py
 @Function:    python实例属性
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/11
"""


"""实例属性"""

"""
实例属性指的是实例对象所绑定的属性

绑定实例属性(给实例对象绑定属性)的方式有两种：
1. 在类对象的内部(方法中)
    语法格式：self.属性名 = 属性值
    推荐在特殊方法__init__中进行绑定，这样，在创建实例对象后就会自动调用特殊方法__init__
    对实例对象进行初始化，从而绑定实例属性。如果在其它方法中进行绑定，可能需要手动调用方法后才会绑定
2. 在类对象的外部
    python是动态语言，所以，在实例对象创建之后，可以对其动态地绑定属性
    语法格式：实例对象.属性名 = 属性值
    如果指定名称的实例属性已经存在，则是对实例属性进行修改
    
访问实例属性的方式有两种：
1. 在类对象的内部(方法中)
    语法格式：self.属性名
2. 在类对象的外部
    语法格式：实例对象.属性名
    
之所以添加前缀"self"或"实例对象"，是为了表明实例属性被哪个实例对象所绑定
"""

class MyClass(object):
    def __init__(self):
        # 在类对象的内部(方法中)绑定实例属性
        self.ia1 = 18

    def do_sth1(self):
        # 在类对象的内部(方法中)访问实例属性
        print(self.ia1)

    def do_sth2(self):
        print(self.ia2)

    def do_another(self):
        self.ia2 = 56

    def do_sth3(self):
        print(self.ia3)

mc = MyClass()

# 在类对象的外部调用方法，使得在类对象的内部(方法中)访问实例属性
mc.do_sth1()    # 18

# 在类对象的外部访问实例属性
print(mc.ia1)   # 18

# 如果在其它方法中进行绑定，可能需要手动调用方法后才会绑定
# mc.do_sth2()    # AttributeError: 'MyClass' object has no attribute 'ia2'
# 在类对象的外部访问实例属性
# print(mc.ia2)   # AttributeError: 'MyClass' object has no attribute 'ia2'

# 手动调用方法后才会绑定
mc.do_another()
# 在类对象的外部调用方法，使得在类对象的内部(方法中)访问实例属性
mc.do_sth2()    # 56
# 在类对象的外部访问实例属性
print(mc.ia2)   # 56

# 在类对象的外部绑定实例属性
mc.ia3 = 3.14
# 在类对象的外部访问实例属性
print(mc.ia3)   # 3.14
# 在类对象的外部修改绑定的实例属性值
mc.ia3 = 19
# 在类对象的外部访问实例属性
print(mc.ia3)   # 19
# 在类对象的外部调用方法，使得在类对象的内部(方法中)访问实例属性
mc.do_sth3()    # 19

"""
    同一个类对象的不同实例对象所绑定的实例属性是相互独立的，也就是说，给一个实例对象所绑定的
    实例属性，对于另外一个实例对象是不起作用的
"""

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Student('张三', 98)
s2 = Student('李四', 86)

s1.age = 18

# 访问特殊属性__dict__可以获得实例对象所绑定的所有属性和方法的字典
print(s1.__dict__)  # {'name': '张三', 'score': 98, 'age': 18}
print(s2.__dict__)  # {'name': '李四', 'score': 86}