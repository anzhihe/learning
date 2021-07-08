#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    string_operator3.py
 @Function:    string operator
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/25
"""

"""一、字符串的劈分和合并"""

"""
1、调用方法split和rsplit劈分字符串
    方法split从字符串的左边开始劈分，方法rsplit从字符串的右边开始劈分
    默认的劈分符是空格字符串，这两个方法的返回值都是一个列表
"""

s = 'Python    Swift    Kotlin'

print(s.split())    # ['Python', 'Swift', 'Kotlin']
print(s.rsplit())   # ['Python', 'Swift', 'Kotlin']

# 可以通过参数sep指定劈分字符串时的劈分符

s = 'Python|Swift|Kotlin'

print(s.split(sep = '|'))    # ['Python', 'Swift', 'Kotlin']
print(s.rsplit(sep = '|'))   # ['Python', 'Swift', 'Kotlin']

"""
    可以通过参数maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分后，剩余的子串
    会单独作为一部分。此时，方法split和rsplit就有区别了
"""

s = 'Python    Swift    Kotlin    Java'

print(s.split(maxsplit=2))   # ['Python', 'Swift', 'Kotlin    Java']
print(s.rsplit(maxsplit=2))  # ['Python    Swift', 'Kotlin', 'Java']

"""
2、调用方法partition或rpartition劈分字符串
    方法partition从字符串的左边开始劈分，方法rpartition从字符串的右边开始劈分
    调用这两个方法时都必须指定劈分符
    方法partition在指定的劈分符第一次出现的地方(方法rpartition在指定的劈分符最后一次出现的地方)，将字符串劈分为三个部分
    (1) 劈分符前面的部分
    (2) 劈分符
    (3) 劈分符后面的部分
    这两个方法的返回值都是一个元组
"""

s = 'Hello-World-!'
print(s.partition('-'))      # ('Hello', '-', 'World-!')
print(s.rpartition('-'))     # ('Hello-World', '-', '!')

s = 'HelloWorld-'
print(s.partition('-'))      # ('HelloWorld', '-', '')
print(s.rpartition('-'))     # ('HelloWorld', '-', '')

"""
    如果字符串中不存在指定的劈分符，方法partition返回的元组中的三个元素依次为：
    (1) 字符串本身
    (2) 空字符串
    (3) 空字符串
    
    如果字符串中不存在指定的劈分符，方法rpartition返回的元组中的三个元素依次为：
    (1) 空字符串
    (2) 空字符串
    (3) 字符串本身
"""

s = 'HelloWorld'
print(s.partition('-'))     # ('HelloWorld', '', '')
print(s.rpartition('-'))    # ('', '', 'HelloWorld')

"""
3、调用方法join合并多个字符串
"""

# 字符串之间用'|'进行合并
s = '|'.join(['Python', 'Swift', 'Kotlin'])
# s = '|'.join(('Python', 'Swift', 'Kotlin'))
print(s)    # Python|Swift|Kotlin

s = ''.join(['Python', 'Swift', 'Kotlin'])
print(s)    # PythonSwiftKotlin

# 可以把字符串看作是字符的列表
s = '|'.join('Python')
print(s)    # P|y|t|h|o|n


"""二、以is开头的字符串方法"""

"""
字符串的很多方法是以is开头的：
1、isidentifier：判断指定的字符串是否是合法的标识符
"""

print('abc'.isidentifier()) # True
print('123'.isidentifier()) # True

"""
    可以调用模块keyword中的方法iskeyword判断一个字符串是否是关键字
"""

import keyword
print(keyword.iskeyword('if'))  # True
print(keyword.iskeyword('iF'))  # False

"""
2、isspace：判断指定字符串是否全部由空白字符组成
3、isalpha：判断指定字符串是否全部由字母组成
4、isdecimal：判断指定字符串是否全部由十进制的数字组成
5、isnumeric：判断指定字符串是否全部由数字组成
6、isalnum：判断指定字符串是否全部由字母和数字组成
"""

print('\t  \r     \n'.isspace())    # True

print('abc'.isalpha())   # True
print('abc1'.isalpha())  # False

print('123'.isdecimal())        # True
print('123六Ⅵ'.isdecimal())     # False

print('123六Ⅵ'.isnumeric())     # True
print('123六Ⅵa'.isnumeric())    # False

print('abc123六Ⅵ'.isalnum())    # True
print('abc123六Ⅵ!'.isalnum())   # False


"""三、去除字符串的前导字符串或后续字符串"""

"""
    如果想去除字符串的前导字符串或后续字符串，可以调用以下方法：
    (1) lstrip：去除字符串的前导字符串
    (2) rstrip：去除字符串的后续字符串
    (3) strip：去除字符串的前导字符串和后续字符串
    其中，默认的前导字符串和后续字符串都是空格字符串
"""

s = '    Hello World       '
print(s.lstrip())   # Hello World
print(s.rstrip())   #     Hello World
print(s.strip())    # Hello World

"""
    调用以上三个方法时可以指定一个字符串，这样,
    前导字符串指的是：从左边第1个字符串开始依次往后，直到某个字符不在指定的字符串中
    后续字符串指的是：从右边最后1个字符开始依次往前，直到某个字符不在指定的字符串中
"""

s = 'www.example.com'
print(s.lstrip('cmowz.'))   # example.com
print(s.rstrip('cmowz.'))   # www.example
print(s.strip('cmowz.'))    # example