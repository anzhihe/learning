#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    string_operator.py
 @Function:    
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/24
"""


"""一、使用加法运算符操作字符串"""

"""
1、使用加法运算符操作字符串
    可以使用加法运算符将两个字符串连接后生成一个新字符串
"""

print('Hello,' + 'World!')  # Hello,World!

# 把多个字符串常量放在一起就会自动连接然后生成一个新的字符串
s = 'Hello' ',' 'World' '!'
print(s)    # Hello,World!

# 如果想把多个字符串常量写在多行中，可以在每行的末尾添加一个反斜杠
s = 'Hello' ',' \
    'World' \
    '!'
print(s)    # Hello,World!

"""
2、使用乘法运算符操作字符串
    可以使用乘法运算符将字符串中的所有字符重复n次后生成一个字符串
"""

print('Hello' * 3)  # HelloHelloHello


"""二、字符串的"查"操作"""

"""
    因为字符串可以看作是字符的列表，所以字符串与列表的"查"操作是类似的，区别在于：
    当获得字符串中指定子串的索引时，除了调用方法index，还可以调用方法find、rfind、rindex
    其中，子串的索引指的是子串中第一个字符的索引
"""

"""
    当字符中存在多个被查找的子串时，方法index和find返回第一个子串的索引
    方法rindex和rfind返回最后一个子串的索引
"""

s = '5739182186'

print(s.index('18'))    # 4
print(s.find('18'))     # 4

print(s.rindex('18'))   # 7
print(s.rfind('18'))    # 7

"""
    当字符串中不存在指定的子串时，方法index和rindex抛出ValueError，方法find和rfind返回-1
"""

# print(s.index('18', 1, 5))   # ValueError: substring not found
# print(s.rindex('18', 1, 5))  # ValueError: substring not found

print(s.find('18', 1, 5))   # -1
print(s.rfind('18', 1, 5))  # -1


"""二、字符串是不可变类型"""

"""
    字符串没有"改"操作，"增"操作和"删"操作，因为字符串是不可变类型
"""

s = 'Hello,World'
# s[5] = '!'  # TypeError: 'str' object does not support item assignment
print(s[:5] + '!' + s[6:])  # Hello!World


"""三、使用比较运算符比较两个字符串"""

"""
    除了使用比较运算符对两个列表或元组进行比较，还可以使用如下比较运算符对两个字符串进行比较：
    (1) >、>=、
    (2) <、<=
    (3) ==、!=
    比较规则为：
    首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，依次比较下去，
    直到两个字符串中的字符不相等时其比较结果就是两个字符串的比较结果，两个字符串中的所有后续字符将不再被比较
    两个字符进行比较时，比较的是其ordinal value。调用内置函数ord可以得到指定字符的
    ordinal value。与内置函数ord对应的是内置函数chr，调用内置函数chr时指定ordinal value
    可以得到其对应的字符。
"""

print(ord('a')) # 97
print(chr(97))  # a

print(ord('b')) # 98
print(chr(98))  # b

print(ord('A')) # 65
print(chr(65))  # A

print('a' < 'b')    # True
print('a' > 'A')    # True

print('cbadf' > 'cbAeg')    # True

"""
    还可以使用is对两个字符串进行比较
    ==与is的区别：
    ==是"相等性"测试，is是"同一性"测试
    
    字符串常量会被缓存和重用
"""

a = b = 'Hello'
c = 'Hello'

print(a == b)   # True
print(a == c)   # True

print(a is b)   # True
print(a is c)   # True
