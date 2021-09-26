#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    regex5.py
 @Function:    边界匹配、Match对象的属性和方法
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/1
"""


"""一、边界匹配"""

"""
    边界匹配主要用于匹配字符串的边界或字符串中单词的边界。
"""

import re

# ['12']
print(re.findall(r'^\d+', '12-3\n45-6\n78-9'))

# ['12', '45', '78']
print(re.findall(r'^\d+', '12-3\n45-6\n78-9', re.M))

# ['12']
print(re.findall(r'\A\d+', '12-3\n45-6\n78-9', re.M))

# ['9']
print(re.findall(r'\d+$', '12-3\n45-6\n78-9'))

# ['3', '6', '9']
print(re.findall(r'\d+$', '12-3\n45-6\n78-9', re.M))

# ['9']
print(re.findall(r'\d+\Z', '12-3\n45-6\n78-9', re.M))

# ['py']
print(re.findall(r'\bpy\b', 'ab py cd'))

# ['py']
print(re.findall(r'\bpy\b', 'ab#py@cd'))

# ['py', 'py']
print(re.findall(r'\bpy\b', 'py cd py'))

# ['pycb']
print(re.findall(r'\Bpy\w+', 'apy apycb pyb'))


"""二、Match对象的属性和方法"""

"""
    模块re的方法match()和search()在匹配成功时都会返回一个Match对象，该对象包含了很多关于
此次匹配的信息，可以通过访问Match对象提供的属性和方法来获取这些匹配信息。
"""

import re

match_obj = re.compile(r'(\d+)-(?P<sec>\d+)').match('025-3456abc', 1, 7)
print(match_obj)    # <re.Match object; span=(1, 7), match='25-345'>

print(match_obj.string)     # 025-3456abc
print(match_obj.re)         # re.compile('(\\d+)-(?P<sec>\\d+)')
print(match_obj.pos)        # 1
print(match_obj.endpos)     # 7
print(match_obj.lastindex)  # 2
print(match_obj.lastgroup)  # sec

print(match_obj.group(2))           # 345
print(match_obj.group('sec'))       # 345
print(match_obj.group())            # 25-345
print(match_obj.group(0))           # 25-345
print(match_obj.group(1, 'sec'))    # ('25', '345')

print(match_obj.groups())           # ('25', '345')

print(match_obj.groupdict())        # {'sec': '345'}

print(match_obj.start('sec'))       # 4
print(match_obj.start())            # 1
print(match_obj.end('sec'))         # 7
print(match_obj.end())              # 7