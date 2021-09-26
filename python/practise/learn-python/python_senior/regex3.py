#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    regex3.py
 @Function:    使用模块re实现字符串的查找
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/1
"""


"""使用模块re实现字符串的查找"""

"""
    当在字符串中查找指定的子串时，借助模块re并通过正则表达式指定被查找的子串可以实现更强大的查找功能。
模块re提供了三个用于实现字符串查找的方法：
1、search(pattern, string[, flags])
    该方法会在参数string指定的字符串中查找参数pattern指定的第一个子串。
    其中，参数pattern是一个正则表达式，或对正则表达式预编译之后得到的对象。
    如果有匹配的子串，返回第一个匹配对应的Match对象；如果没有匹配的子串，返回None。
"""

import re

print(re.search(r'\d+', '-123-56-89-'))   # <re.Match object; span=(1, 4), match='123'>

pattern = re.compile(r'\d+')
print(re.search(pattern, '-123-56-89-'))  # <re.Match object; span=(1, 4), match='123'>

print(re.search(r'\d+', '-abc-d-efg-'))   # None

"""
    除了直接调用模块re的方法search()之外，也可以调用模块re的方法compile()的返回值的方法：
    search(string[, pos[, endpos]])
    其中，
        参数pos用于指定被查找字符串的起始位置，默认值是0；
        参数endpos用于指定被查找字符串的结束位置，默认值是字符串的长度。被查找的子串不包括结束位置。
        
        模块re的方法search()中的参数pattern和flags被转移到了compile()中。
"""

print(pattern.search('-123-56-89-'))        # <re.Match object; span=(1, 4), match='123'>
print(pattern.search('-123-56-89-', 4))     # <re.Match object; span=(5, 7), match='56'>

"""
2、findall(pattern, string[, flags])
    该方法会在参数string指定的字符串中查找参数pattern指定的所有子串。
    其中，参数pattern是一个正则表达式，或对正则表达式预编译之后得到的对象。
    如果有匹配的子串，返回所有匹配的子串组成的列表；如果没有匹配的子串，返回空列表。
"""

print(re.findall(r'\d+', '-123-56-89-'))    # ['123', '56', '89']
print(re.findall(r'\d+', '-abc-d-efg-'))    # []

"""
    除了直接调用模块re的方法findall()之外，也可以调用模块re的方法compile()的返回值的方法：
    findall(string[, pos[, endpos]])
    其中，
        参数pos用于指定被查找字符串的起始位置，默认值是0；
        参数endpos用于指定被查找字符串的结束位置，默认值是字符串的长度。被查找的子串不包括结束位置。
        
        模块re的方法findall()中的参数pattern和flags被转移到了方法compile()中。
"""

print(pattern.findall('-123-56-89-'))       # ['123', '56', '89']
print(pattern.findall('-123-56-89-', 4))    # ['56', '89']

"""
3、finditer(pattern, string[, flags])
    该方法会在参数string指定的字符串中查找参数pattern指定的所有子串。
    其中，参数pattern是一个正则表达式，或对正则表达式预编译之后得到的对象。
    如果有匹配的子串，返回所有匹配的子串组成的迭代器；如果没有匹配的子串，返回不包含任何元素的迭代器。
"""

iterator = re.finditer(r'\d+', '-123-56-89-')

# <re.Match object; span=(1, 4), match='123'>
# <re.Match object; span=(5, 7), match='56'>
# <re.Match object; span=(8, 10), match='89'>
for match in iterator:
    print(match)

iterator = re.finditer(r'\d+', '-abc-d-efg-')
for match in iterator:
    print(match)

"""
    除了直接调用模块re的方法finditer()之外，也可以调用模块re的方法compile()的返回值的方法：
    finditer(string[, pos[, endpos]])
    其中,
        参数pos用于指定被查找字符串的起始位置，默认值是0;
        参数endpos用于指定被查找字符串的结束位置，默认值是字符串的长度。被查找的子串不包括结束位置。

        模块re的方法finditer()中的参数pattern和flags被转移到了方法compile()中。
"""

iterator = pattern.finditer('-123-56-89-')

# <re.Match object; span=(1, 4), match='123'>
# <re.Match object; span=(5, 7), match='56'>
# <re.Match object; span=(8, 10), match='89'>
for match in iterator:
    print(match)

iterator = pattern.finditer('-123-56-89-', 4)

# <re.Match object; span=(5, 7), match='56'>
# <re.Match object; span=(8, 10), match='89'>
for match in iterator:
    print(match)
