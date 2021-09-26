#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    regex1.py
 @Function:    单个字符的匹配、正则表达式与原始字符串
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/1
"""


"""一、单个字符的匹配"""

import re

print(re.match(r'...', 'c-8'))          # <re.Match object; span=(0, 3), match='c-8'>
print(re.match(r'...', 'c\n8'))         # None
print(re.match(r'...', 'c\n8', re.S))   # <re.Match object; span=(0, 3), match='c\n8'>

print(re.match(r'\d\d\d', '123abc'))    # <re.Match object; span=(0, 3), match='123'>
print(re.match(r'\D\D\D', 'a-b123'))    # <re.Match object; span=(0, 3), match='a-b'>

print(re.match(r'\w\w\w', 'c_8###'))    # <re.Match object; span=(0, 3), match='c_8'>
print(re.match(r'\W\W\W', '@-#c_8'))    # <re.Match object; span=(0, 3), match='@-#'>

# <re.Match object; span=(0, 6), match=' \t\r\n\x0c\x0b'>
print(re.match(r'\s\s\s\s\s\s', ' \t\r\n\f\vabc'))
# <re.Match object; span=(0, 3), match='c-3'>
print(re.match(r'\S\S\S', 'c-3 \t'))

print(re.match(r'[abc]', 'b'))      # <re.Match object; span=(0, 1), match='b'>
print(re.match(r'[^abc]', 'f'))     # <re.Match object; span=(0, 1), match='f'>
print(re.match(r'[a-zA-Z]', 'M'))   # <re.Match object; span=(0, 1), match='M'>
print(re.match(r'[a-n&h-t]', 'k'))  # <re.Match object; span=(0, 1), match='k'>


"""二、正则表达式与原始字符串"""

"""
    通常用原始字符串来表示正则表达式，因为在原始字符串中，包含哪些字符就表示哪些字符，而无需考虑
转义字符。
"""

import re

# 在原始字符串r'\d'中，包含了一个反斜杠和一个d
# 在正则表达式中，用一个反斜杠和一个d匹配任意一个数字
print(re.match(r'\d', '8')) # <re.Match object; span=(0, 1), match='8'>

"""
    如果不用原始字符串来表示正则表达式，而是用普通字符串来表示，则需要考虑转义字符。
"""

# 在普通字符串中，要用两个\\表示一个反斜杠
# 所以，'\\d'表示的是：一个反斜杠和一个d
# 在正则表达式中，用一个反斜杠和一个d匹配任意一个数字
print(re.match('\\d', '8')) # <re.Match object; span=(0, 1), match='8'>

"""
    在正则表达式中，某些字符具有特殊含义，例如： \.^$? +*{}[]()|。如果想要使用这些字符的字面值，
必须使用反斜杠进行转义。
"""


# 被匹配的字符串'a\\b'是一个普通字符串
# 在普通字符串中，要用两个\\表示一个反斜杠
# 所以，'a\\b'表示的是: a、一个反斜杠、b
# 在正则表达式中，反斜杠是具有特殊含义的，如果要表示反斜杠的字面值，必须使用反斜杠进行转义
# 因此，原始字符串r'a\\b'表示的是: a、一个反斜杠、b
print(re.match(r'a\\b', 'a\\b'))    # <re.Match object; span=(0, 3), match='a\\b'>

# 如果用普通字符串表示上面的正则表达式
# 前两个\\表示一个反斜杠，后两个\\表示一个反斜杠
# 在正则表达式中，反斜杠是具有特殊含义的，如果要表示反斜杠的字面值，必须使用反斜杠进行转义
# 因此，前面两个\\表示的反斜杠，要对后面两个\\表示的反斜杠进行转义，从而表示一个反斜杠(反斜杠的字面值)
print(re.match('a\\\\b', 'a\\b'))    # <re.Match object; span=(0, 3), match='a\\b'>