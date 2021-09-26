#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    regex.py
 @Function:    正则表达式简介，匹配字符串及预编译
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/1
"""


"""一、正则表达式的简介"""

"""
    正则表达式是字符串处理的利器，它可以用于字符串的匹配、查找、替换和劈分。虽然在前面的课程中
也学习过字符串的查找、替换和劈分，但是借助正则表达式和标准库模块re可以实现更加强大的查找、替换和劈分。
其中，标准库模块re是专门用于支持正则表达式的。

    正则表达式是一个特殊的字符串，该字符串中包含了一些特定字符，这些特定字符都有明确的匹配规则，
因此，正则表达式是一个定义了匹配规则的字符串。如果某个字符串符合正则表达式定义的所有匹配规则，那么
该字符串就与该正则表达式匹配。
    如果想要判断一个字符串是否是合法的Email地址，就可以通过正则表达式来定义合法的Email地址
需要满足的规则，然后把要判断的字符串和定义的正则表达式进行匹配。

    正则表达式在很多编程语言中都是适用的，且绝大部分语法都是通用的。
    在正则表达式中，普通字符用于精确匹配，特定字符具有明确的匹配规则，例如: 
    \d用于匹配任意一一个数字，. 用于匹配除换行符之外的任意一个字符。 因此,
    'ab\d'可以匹配'ab0'、'ab1'、 'ab2'、'ab3'、 'ab4'、 'ab5'、 'ab6'、 'ab7'、'ab8'、 'ab9' ;
    ab.'可以匹配'ab3'、'abc'、'ab#'、等等，但无法匹配'ab\n'。
"""


"""二、使用模块re实现字符串的匹配"""

"""
如果想要判断给定的字符串和正则表达式是否是匹配的，可以使用模块re提供的方法:
    match(pattern，string[, flags])
    该方法会根据参数string指定的字符串与参数pattern指定的正则表达式进行匹配。
    其中，
        参数pattern是一个正则表达式，或对正则表达式预编译之后得到的对象。
        参数flags是一个标志位，用于控制正则表达式的匹配方式，如:是否区分大小写、多行匹配等。
        如果需要同时使用多个标志位，可以使用|对标志位进行分隔。
    该方法会从参数string指定的字符串的开头开始，一直向后尝试匹配参数pattern指定的正则表达式，
在到达pattern的末尾前，如果遇到无法匹配的字符或到达了string的末尾，都表示匹配失败，从而返回None。
否则，当到达pattern的末尾时，如果所有的字符都是匹配成功的，则表示匹配成功，从而终止匹配，不再对
string向后匹配，同时，返回一个Match对象。

    根据方法match()的返回值可知，常见的判断方式为:
    if re.match(正则表达式，被匹配的字符串):
        print('匹配成功')
    else:
        print('匹配失败')
"""

import re

print(re.match(r'...', 'a\nc')) # None
print(re.match(r'...', 'ab'))   # None

print(re.match(r'...', 'abc'))      # <re.Match object; span=(0, 3), match='abc'>
print(re.match(r'...', 'abcdef'))   # <re.Match object; span=(0, 3), match='abc'>

# <re.Match object; span=(0, 7), match='aBCdefG'>
print(re.match(r'[a-z]{7}', 'aBCdefG', re.I))
# <re.Match object; span=(0, 10), match='a\ncaBCdefG'>
print(re.match(r'...[a-z]{7}', 'a\ncaBCdefG', re.I|re.S))


"""三、正则表达式的预编译"""

"""
    当在python中使用正则表达式时，正则表达式会首先被编译。如果一个正则表达式要重复使用多次,
处于效率的考虑，可以预编译该正则表达式，这样，接下来重复使用时就不需要再编译了。

    模块re提供了预编译正则表达式的方法:
    compile(pattern[, flags])
    其中，
        参数pattern是一个正则表达式。
        参数flags是一个标志位，与方法match()中参数flags的含义完全相同。
    该方法会返回对正则表达式预编译之后得到的对象。
"""

import re

obj = re.compile(r'...')
print(obj)  # re.compile('...')

"""
    方法compile()的返回值提供了一些方法，在模块re中都有对应的方法。例如:
除了直接调用模块re的方法match()之外，也可以调用模块re的方法compile()的返回值的方法:
    match(string[，pos[ ，endpos ]])
    其中,
        参数pos用于指定被匹配的字符串的起始位置，默认值是0;
        参数endpos用于指定被匹配的字符串的结束位置，默认值是字符串的长度。被匹配的子串不包括结束位置。
        
    因为在方法compile()中可以指定参数pattern和flags，所以，在调用其返回值的方法时，不需要
再指定参数pattern和flags；而调用模块re中的对应方法时，则需要指定参数pattern和flags。
    模块re的方法match()中的参数pattern和flags被转移到了方法compile()中。
"""

# <re.Match object; span=(0, 3), match='abc'>
# print(re.match(r'...', 'abcdef'))
print(re.compile(r'...').match('abcdef'))

print(re.compile(r'...').match('abcdef', 1, 3)) # None


