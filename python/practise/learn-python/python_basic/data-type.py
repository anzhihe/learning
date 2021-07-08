#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    data-type.py
 @Function:    Python Data Types
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/19
"""

"""一、数据类型的概述"""

"""
1、什么是数据类型？
    数据类型是对数据的分类，常用的有：整数类型、浮点类型、字符串类型等等
    任何数据都有明确的数据类型，例如：10 属于整数类型，3.14 属于浮点类型，'Hello' 属于字符串类型
"""

"""
2、怎样获取数据的数据类型？
    通过调用内置函数 type 可以获取数据的数据类型
"""

print(type(10))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type('Hello'))    # <class 'str'>


"""二、整数类型"""

"""
1、整数的不同进制的表示方式
    整数的4种进制表示方式：
    (1) 10进制：默认的进制
    (2) 2进制：以0b开头
    (3) 8进制：以0o开头
    (4) 16进制：以0x开头
"""

print(118)          # 118
print(0b1110110)    # 118
print(0o166)        # 118
print(0x76)         # 118

"""
2、整数转换为不同进制的字符串
    调用内置函数将十进制整数转换为不同进制的字符串：
    (1) bin()：将10进制整数转换为2进制(binary)字符串
    (2) oct()：将10进制整数转换为8进制(octal)字符串
    (3) hex()：将10进制整数转换为16进制(hexadecimal)字符串
"""

print(bin(118))     # 0b1110110
print(oct(118))     # 0o166
print(hex(118))     # 0x76

"""
3、整数的创建
    可以直接创建一个整数，也可以调用内置函数int创建整数
    (1) 不传递任何参数时，返回整数0
    (2) 只传递一个参数时，将传递的参数转换为整数
    (3) 传递两个参数时，第一个参数必须是字符串，第二个参数指定进制
"""

print(int())            # 0

print(int(118))         # 118
print(int(118.1))       # 118
print(int('118'))       # 118

print(int('1110110', 2))    # 118
print(int('0o166', 8))      # 118
print(int('0x76', 16))      # 118


"""三、浮点数类型"""

"""
1、什么是浮点数类型？
    浮点数类型用来表示浮点数，也就是小数
"""

print(0.123456789)  # 0.123456789

"""
2、浮点数的创建
    除了使用小数创建浮点数外，还可以调用内置函数float创建浮点数
    (1) 不传递任何参数时，返回浮点数0.0
    (2) 只传递一个参数时，将传递的参数转换为浮点数
"""

print(float())      # 0.0

print(float(118))   # 118.0
print(float(118.2)) # 118.2
print(float('118')) # 118.0

"""
3、用科学计数法表示浮点数
    很大或很小的浮点数可以用科学计数法来表示：men表示m乘以10的n次方，e不区分大小写(e、E)
"""

print(2.3e8)    # 230000000.0
print(2.3e-4)   # 0.00023

"""
4、浮点数存储的不精确性
    计算机采用二进制存储浮点数时是不精确的，可能会存在误差，因此，对于浮点数的运算需要格外小心
    
    解决方案：导入模块demimal或fractions
    其中，模块decimal用于处理十进制的浮点数，模块fractions用于处理分数
"""

print(1.1 + 2.2 - 3.3)  # 4.440892098500626e-16
print(1.1 + 2.2)        # 3.3000000000000003

from decimal import Decimal
print(Decimal('1.1') + Decimal('2.2') - Decimal('3.3'))     # 0.0

from fractions import Fraction
print(Fraction(11, 10) + Fraction(22, 10) - Fraction(33, 10))   # 0


"""四、布尔类型"""

"""
1、什么是布尔类型？
    布尔类型是一个int的子类，只有两种取值：要么是True(值为1)，要么是False(值为0)
    例如：你吃了吗？今天有没有加班？
"""

print(5 > 3)    # True
print(5 < 3)    # False

print(True == 1)        # True
print(False == 0)       # True
print(True + False + 5) # 6