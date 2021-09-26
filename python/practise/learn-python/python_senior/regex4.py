#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    regex4.py
 @Function:    使用模块re实现字符串的替换与劈分
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/1
"""


"""一、使用模块re实现字符串的替换"""

"""
    当在字符串中替换指定的子串时，借助模块re并通过正则表达式指定被替换的子串可以实现功能更加强大
的替换功能。
    模块re提供了两个用于实现字符串替换的方法：
1、sub(pattern, repl, string[, count][, flags])
    该方法会将参数string指定的字符串中所有匹配参数pattern的子串替换为参数repl指定的字符串。
    其中，参数count用于指定最大替换次数；默认值是0，表示替换所有的匹配。
    方法的返回值是替换后得到的字符串。
"""

import re

print(re.sub(r'\d+', '888', '-123-56-89-'))     # -888-888-888-
print(re.sub(r'\d+', '888', '-123-56-89-', 2))  # -888-888-89-

"""
    参数repl除了可以指定为替换的字符串之外，还可以指定为一个函数。通过该函数，可以把每次匹配
对应的Match对象作为函数的输入(参数)，在函数体中对匹配到的子串进行处理，函数的输出(返回值)
作为替换的字符串。
"""

def add1(match):
    val = match.group()
    num = int(val) + 1
    return str(num)

print(re.sub(r'\d+', add1, '-123-56-89-'))  # -124-57-90-

"""
    当替换字符串为空字符串时，可以实现字符串中子串的删除。
"""

print(re.sub(r'[aeiou]', '', 'HELLO World', flags=re.I))    # HLL Wrld

"""
2、subn(pattern, repl, string, [, count][, flags])
    返回值是包含两个元素的元组：(对应的方法sub()的返回值，替换次数)
"""

print(re.subn(r'\d+', add1, '-123-56-89-')) # ('-124-57-90-', 3)

"""
    除了直接调用模块re的方法sub( )和subn()之外，也可以调用模块re的方法compile()的返回值的方法: .
    sub(repl, string[, count])
    subn(repl, string[, count])
    模块re的方法sub()和subn()中的参数pattern和flags被转移到了方法compile()中。
"""

pattern = re.compile(r'\d+')

# -888-888-888-
print(pattern.sub('888', '-123-56-789-'))

# -124-57-790-
print(pattern.sub(add1, '-123-56-789-'))

# ('-124-57-790-', 3)
print(pattern.subn(add1, '-123-56-789-'))


"""二、使用模块re实现字符串的劈分"""

"""
    当对字符串进行劈分时，借助模块re并通过正则表达式指定劈分符可以实现更强大的劈分功能。
模块re提供了实现字符串劈分的方法:
    split(pattern, string[, maxsplit][, flags])
    该方法会根据参数pattern指定的劈分符对参数string指定的字符串进行劈分。
    其中，参数maxsplit用于指定最大劈分次数；默认值是0,表示不限制劈分次数。
    方法的返回值是劈分后的所有子串组成的列表。
"""

import re

# ['a', 'b', 'c', 'd']
print(re.split(r'\s+', 'a b     c   d'))

# ['a', 'b', 'c   d']
print(re.split(r'\s+', 'a b     c   d', 2))

# ['a', 'b', 'c', 'd', 'e']
print(re.split(r'[\s\,\;]+', 'a,  b;; c , ;d,e'))

"""
    除了直接调用模块re的方法split()之外,也可以调用模块re的方法compile()的返回值的方法:
    split(string[, maxsplit])
    模块re的方法split()中的参数pattern和flags被转移到了方法compile()中。
"""

pattern = re.compile(r'\s+')

# ['a', 'b', 'c', 'd']
print(pattern.split('a  b    c   d'))

# ['a', 'b', 'c   d']
print(pattern.split('a  b    c   d', 2))