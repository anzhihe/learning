#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    regex2.py
 @Function:    贪婪匹配与勉强匹配
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/1
"""


"""一、贪婪匹配与勉强匹配"""

"""
    贪婪匹配：在匹配正则表达式时，使用尽可能长的子串去匹配。
    勉强匹配：在匹配正则表达式时，使用尽可能短的子串去匹配。
"""

import re

print(re.match(r'ab*', 'abbbbbbc'))     # <re.Match object; span=(0, 7), match='abbbbbb'>
print(re.match(r'ab*?', 'abbbbbbc'))    # <re.Match object; span=(0, 1), match='a'>

print(re.match(r'ab+', 'abbbbbbc'))     # <re.Match object; span=(0, 7), match='abbbbbb'>
print(re.match(r'ab+?', 'abbbbbbc'))    # <re.Match object; span=(0, 2), match='ab'>

print(re.match(r'ab?', 'abbbbbbc'))     # <re.Match object; span=(0, 2), match='ab'>
print(re.match(r'ab??', 'abbbbbbc'))    # <re.Match object; span=(0, 1), match='a'>

print(re.match(r'ab{3}', 'abbbbbbc'))   # <re.Match object; span=(0, 4), match='abbb'>
print(re.match(r'ab{3}?', 'abbbbbbc'))  # <re.Match object; span=(0, 4), match='abbb'>

print(re.match(r'ab{3,}', 'abbbbbbc'))  # <re.Match object; span=(0, 7), match='abbbbbb'>
print(re.match(r'ab{3,}?', 'abbbbbbc')) # <re.Match object; span=(0, 4), match='abbb'>

print(re.match(r'ab{3,5}', 'abbbbbbc')) # <re.Match object; span=(0, 6), match='abbbbb'>
print(re.match(r'ab{3,5}?', 'abbbbbbc'))    # <re.Match object; span=(0, 4), match='abbb'>


"""二、分组匹配"""

"""
    可以使用小括号()将正则表达式中的部分内容括起来，从而将该部分内部作为一个分组。
    从正则表达式的左边往右数，第一个左小括号表示第1个分组，第二个左小括号表示第2个分组，...，
依次类推。因此，可以根据编号对分组进行引用。
"""

import re

matchobj = re.match(r'(\d+)-(\d+)', '025-3456abc')
print(matchobj) # <re.Match object; span=(0, 8), match='025-3456'>

print(matchobj.group(1))    # 025
print(matchobj.group(2))    # 3456
print(matchobj.group(0))    # 025-3456
print(matchobj.groups())    # ('025', '3456')

"""
    可以给某个分组起一个别名，其语法格式为：?P<别名>。这样，就可以通过别名对分组进行引用了。
"""

matchobj = re.match(r'(?P<fir>\d+)-(?P<sec>\d+)', '025-3456abc')
print(matchobj) # <re.Match object; span=(0, 8), match='025-3456'>

print(matchobj.group('fir'))    # 025
print(matchobj.group('sec'))    # 3456

"""
    在正则表达式中，也可以根据编号或别名对分组进行引用，其语法格式分别为：
    \编号
    ?P=别名
    确切地说，是引用分组匹配到的子串。
"""

# <re.Match object; span=(0, 13), match='025-3456-3456'>
print(re.match(r'(\d+)-(\d+)-(\2)', '025-3456-3456'))

# <re.Match object; span=(0, 13), match='025-3456-3456'>
print(re.match(r'(\d+)-(?P<sec>\d+)-(?P=sec)', '025-3456-3456'))


"""三、逻辑匹配"""

"""
    在正则表达式中可以使用|进行逻辑匹配，其匹配规则是：
先尝试匹配左边的表达式，如果匹配成功，则跳过匹配右边的表达式；如果匹配不成功，再匹配右边的表达式。
    如果|没有被包括在()中，则它的作用范围是整个正则表达式。
"""

import re

print(re.match(r'123|12', '123'))   # <re.Match object; span=(0, 3), match='123'>
print(re.match(r'abc|12', '123'))   # <re.Match object; span=(0, 2), match='12'>

print(re.match(r'P(ython|erl)', 'Python')) # <re.Match object; span=(0, 6), match='Python'>
print(re.match(r'P(ython|erl)', 'Perl'))   # <re.Match object; span=(0, 4), match='Perl'>