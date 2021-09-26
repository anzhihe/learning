#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    02_tuple_element_name.py
 @Function:    给元组中的元素命名
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/20
"""

"""一、为元组中每个元素命名，提高程序可读性"""

"""
学生信息系统中数据为固定格式:
(名字，年龄，性别，邮箱地址，...)

学生数量很大为了减小存储开销，对每个学生信息用元组表示:
('Jim', 16, 'male', 'jim8721@gmail.com')
('LiLei', 17, 'male', 'leile@qq.com')
('Lucy', 16, 'female', 'lucy123@yahoo.com')
......

访问时，我们使用索引(index)访问，大量索引降低程序可读性.
如何解决这个问题?
"""

# 赋值一个学生信息
student = ('Jim', 16, 'male', 'jim8721@gmail.com')

# 使用索引访问元组字段，程序中会出现大量索引的值(0, 1, 2, ...)，可读性差
# 想获得学生的姓名NAME
print(student[0])   # Jim

# AGE
if student[1] >= 18:
    pass

# SEX
if student[2] == 'male':
    pass

"""
解决方式
1、C语言宏定义的方式
// C
#define NAME 0
#define AGE 1

2、使用C语言的枚举类型
enum Student {
    NAME,
    AGE,
    SEX,
}
"""

"""
方案1：定义类似与其他语言的枚举类型，也就是定义一系列数值常量
"""

NAME, AGE, SEX, EMAIL = range(4)

# 通过变量的名字就能知道访问的是元组中的哪个字段
# 如想获得学生的姓名NAME
print(student[NAME])   # Jim

# AGE
if student[AGE] >= 18:
    pass

# SEX
if student[SEX] == 'male':
    pass

"""
方案2：使用标准库中collections.namedtuple替代内置tuple
"""

from collections import namedtuple

# 创建子类Student，传入索引的命名
Student = namedtuple('Student', ['NAME', 'AGE', 'SEX', 'EMAIL'])

# 使用位置传参
s1 = Student('Jim', 16, 'male', 'jim8721@gmail.com')
print(s1)   # Student(NAME='Jim', AGE=16, SEX='male', EMAIL='jim8721@gmail.com')

# 使用关键字传参
s2 = Student(NAME='Anzhihe', AGE=18, SEX='male', EMAIL='anzhihe@gmail.com')
print(s2)   # Student(NAME='Anzhihe', AGE=18, SEX='male', EMAIL='anzhihe@gmail.com')

# 以类对象的方式通过属性访问元组元素
print(s1.NAME, s1.AGE, s1.SEX, s1.EMAIL)    # Jim 16 male jim8721@gmail.com
print(s2.NAME, s2.AGE, s2.SEX, s2.EMAIL)    # Anzhihe 18 male anzhihe@gmail.com

# 创建的内对象为内置元组的子类
print(isinstance(s1, tuple))    # True