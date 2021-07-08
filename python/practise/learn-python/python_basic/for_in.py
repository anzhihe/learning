#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    for_in.py
 @Function:    python for in statement
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/1
"""

"""一、for-in语句"""

"""
1、什么是for-in语句？
    for-in语句专门用于遍历序列、字典和集合等类型的对象
    其中，遍历指的是：把对象的所有元素依次访问一遍。每访问一个元素，称之为一次迭代。因此，
    可以使用for-in语句遍历的对象又被称为可迭代对象
    
for-in语句的语法格式：
    for 自定义的变量 in 要遍历的可迭代对象:
        循环体
    其中，循环体对应的代码块必须要缩进
    如果循环体内不需要访问自定义的变量，可以将自定义的变更替代为下划线_
    
for-in语句的执行流程：
    反复判断是否遍历完可迭代对象中的所有元素：
    如果已经遍历完可迭代对象中的所有元素，则终止循环
    如果没有遍历完可迭代对象中的所有元素，则自定义的变量自动被赋予当前迭代的元素值，然后执行循环体，
    执行完循环体后再次判断是否遍历完可迭代对象中的所有元素
    
    当迭代次数已知时，推荐使用for-in语句；当迭代次数未知时，推荐使用while语句
"""

"""
2、使用for-in语句遍历range、列表、元组和字符串等序列
"""

for number in range(1, 4):
    print(number)

for _ in range(1, 4):
    print('Hello')

for number in [1, 2, 3]:
    print(number)

for number in (1, 2, 3):
    print(number)

for char in '123':
    print(char)

"""
    在遍历序列的过程中，如果需要对序列进行修改，最好先通过切片操作生成一份序列的拷贝
"""

words = ['Java', 'Python', 'Kotlin', 'Swift', 'Go']
for word in words[:]:
    if len(word) < 5:
        words.remove(word)
print(words)    # ['Python', 'Kotlin', 'Swift']

"""
3、使用for-in语句遍历集合和字典
"""

s = {2, 3, 1}
for number in s:
    print(number)
for number in sorted(s):
    print(number)

d = {'Fruits': 86, 'Books': 88, 'Videos': 83}
# "自定义的变量自动被赋予当前迭代的元素值"中的"元素值"指的是字典的key
for elem in d:
    print(elem)
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
for key, value in d.items():
    print(key, '→', value)