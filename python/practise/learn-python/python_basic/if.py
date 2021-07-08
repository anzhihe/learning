#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    if.py
 @Function:    python if statement
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/30
"""

"""一、if语句"""

"""
if语句的语法格式：
    if 判断条件:
        条件执行体
    其中，条件执行体对应的代码块必须缩进

if语句的执行流程：
    如果判断条件的布尔值为True，执行条件执行体对应的代码块，执行完之后继续执行if语句后面的代码；
    否则，不会执行条件执行体对应的代码块，而是直接执行if语句后面的代码
"""

score = 88
if score >= 60:
    print('及格了')

"""
可以在if语句的后面添加else从句，其语法格式为：
    if 判断条件：
        条件执行体1
    else:
        条件执行体2
    之所以称为else从句，是因为它并不是一个独立的语句，而是if语句的一部分

添加else从句后的执行流程：
    如果判断条件的布尔值为True，执行条件执行体1对应的代码块，执行完之后继续执行if语句后面的代码；
    否则，执行条件执行体2对应的代码块，执行完之后继续执行if语句后面的代码
"""

score = 58

if score >= 60:
    print('及格了')
else:
    print('没及格')

"""
如果if语句存在两个以上的分支，可以在if语句中添加若干个elif从句(elif是else if的简写)，其语法格式为：
    if 判断条件1:
        条件执行体1
    elif 判断条件2:
        条件执行体2
    elif 判断条件3:
        条件执行体3
    ......
    elif 判断条件n-1:
        条件执行体n-1
    [else:
        条件执行体n]
    其中，else从句是可选的
    
添加elif从句后的执行流程：
    如果判断条件1的布尔值为True，执行条件执行体1对应的代码块，执行完之后继续执行if语句后面的代码；
    否则，执行条件执行体2对应的代码块，执行完之后继续执行if语句后面的代码
    否则，执行条件执行体3对应的代码块，执行完之后继续执行if语句后面的代码
    ......
    否则，执行条件执行体n-1对应的代码块，执行完之后继续执行if语句后面的代码
    [否则，执行条件执行体n对应的代码块，执行完之后继续执行if语句后面的代码]
"""

score = 88
if score < 60:
    print('没过60')
elif score < 70:
    print('过60啦')
elif score < 80:
    print('过70啦')
elif score < 90:
    print('过80啦')
else:
    print('过90啦')
# 上面的代码等价：
score = 88
if score < 60:
    print('没过60')
else:
    if score < 70:
        print('过60啦')
    else:
        if score < 80:
            print('过70啦')
        else:
            if score < 90:
                print('过80啦')
            else:
                print('过90啦')


"""二、条件表达式"""

"""
    条件表达式是包含if-else语句的表达式，它类似于C语言中的三目条件运算符
    条件表达式的语法格式：
    x if 判断条件 else y
    对应的运算规则：
    如果判断条件的布尔值为True，条件表达式的返回值为x；否则，条件表达式的返回值为y
"""

score = 88
result = '及格了' if score >= 60 else '没及格'
print(result)   # 及格了

# 以上代码相当于：
if score >= 60:
    result = '及格了'
else:
    result = '没及格'
print(result)   # 及格了

"""
    在一个条件表达式内可以嵌套另一个条件表达式
"""

a = 6
b = 8
print('a大于b' if a > b else ('a小于b' if a < b else 'a等于b'))   # a小于b
