#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    string_operator2.py
 @Function:    string operator
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/24
"""

"""一、字符串的大小写转换"""

"""
    如果想要对字符串中某些字符的大小写进行转换，可以调用字符串的以下方法：
    (1) upper：把所有字符全部转换为大写
    (2) lower：把所有字符全部转换为小写
    (3) swapcase：把所有小写字符转换为大写，把所有大写字符转换为小写
    (4) capitalize：把第一个字符转换为大写，把其余字符转换为小写
    (5) title：把每个单词的第一个字符转换为大写，把每个单词的剩余字符转换为小写
"""

s = 'he is learning PYTHON'

print(s.upper())    # HE IS LEARNING PYTHON
print(s.lower())    # he is learning python
print(s.swapcase()) # HE IS LEARNING python
print(s.capitalize())   # He is learning python
print(s.title())    # He Is Learning Python

"""
    如果想要判断字符串中某些字符的大小写，可以调用字符串的以下方法：
    (1) isupper：是否所有字符全为大写
    (2) islower：是否所有字符全为小写
    (3) istitle：是否每个单词的第一个字符为大写并且每个单词的剩余字符为小写
"""

print(s.isupper())  # False
print(s.upper().isupper())  # True

print(s.islower())  # False
print(s.lower().islower())  # True

print(s.istitle())  # False
print(s.title().istitle())  # True


"""二、字符串的对齐"""

"""
    如果想要设置字符串的对齐方式，可以调用字符串的以下方法：
    (1) center：中心对齐
    (2) ljust：左对齐
    (3) rjust：右对齐
    这三个方法都可以接收两个参数，其中，
    第1个参数指定字符串的宽度，如果指定的宽度小于等于字符串的长度，返回字符串本身
    第2个参数指定填充字符，且第2个参数是可选的，其默认值是空格
"""

print('HelloWorld'.center(18, '*')) # ****HelloWorld****
print('HelloWorld'.center(18))      #     HelloWorld
print('HelloWorld'.center(8))       # HelloWorld

print('HelloWorld'.ljust(18, '*')) # HelloWorld********
print('HelloWorld'.ljust(18))      # HelloWorld
print('HelloWorld'.ljust(8))       # HelloWorld

print('HelloWorld'.rjust(18, '*')) # ********HelloWorld
print('HelloWorld'.rjust(18))      #         HelloWorld
print('HelloWorld'.rjust(8))       # HelloWorld

"""
    zfill：右对齐，左边用0填充
    该方法只接收一个参数，用于指定字符串的宽度。如果指定的宽度小于等于字符串的长度，返回字符串本身
"""

print('578'.zfill(6))       # 000578
print('-578'.zfill(6))      # -00578

print('578'.zfill(2))       # 578
print('-578'.zfill(3))      # -578


"""三、字符串的子串替换"""

"""
    如果想将字符串中的某个子串替换为指定的字符串，可以调用方法replace
    该方法的第1个参数指定被替换的子串，第2个参数指定替换子串的字符串
    该方法返回替换后得到的字符串，替换前的字符串不发生变化
"""

s = 'Hello-Hello-Hello'
print(s.replace('Hello', 'hi'))     # hi-hi-hi
print(s)    # Hello-Hello-Hello

# 调用该方法时可以通过第3个参数指定最大替换次数
print(s.replace('Hello', 'Hi', 2))  # Hi-Hi-Hello
print(s)    # Hello-Hello-Hello


"""四、字符串的字符转换"""

"""
    如果想对字符串中的某些字符进行转换，可以调用方法maketrans和translate
    首先调用方法maketrans创建一个转换表，然后把创建的转换表作为参数传给方法translate
"""

table = str.maketrans('bcd', '234')
# table = str.maketrans({'b': '2', 'c': '3', 'd': '4'})
# table = str.maketrans({98: 50, 99: 51, 100: 52})
print(table)    # {98: 50, 99: 51, 100: 52}

print(ord('b')) # 98
print(ord('2')) # 50

print(ord('c')) # 99
print(ord('3')) # 51

print(ord('d')) # 100
print(ord('4')) # 52

s = 'incredible'
print(s.translate(table))   # in3re4i2le

"""
    在调用方法maketrans创建转换表时，还可以指定要删除的所有字符
"""

table = str.maketrans('bcd', '234', 'ie')
print(table)    # {98: 50, 99: 51, 100: 52, 105: None, 101: None}
print(s.translate(table))   # n3r42l

# 不转换，只指定要删除的所有字符
table = str.maketrans('', '', 'ie')
print(table)    # {105: None, 101: None}
print(s.translate(table))   # ncrdbl