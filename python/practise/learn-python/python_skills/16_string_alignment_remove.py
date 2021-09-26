#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    16_string_alignment_remove.py
 @Function:    字符串对齐与字符串元素去除
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/9/4
"""

"""一、如何对字符串进行左、右、居中对齐？"""

"""
实际案例：
某个字典存储了一系列属性值，
{
    "lodDist": 100.0,
    "SmallCull": 0.04,
    "DistCull": 500.0,
    "trilinear": 40,
    "farclip" :477
}

在程序中，我们想以以下工整的格式将其内容输出，如何处理?
SmallCull : 0.04
farclip   : 477
lodDist   : 100.0
DistCull  : 500.0
trilinear : 40
"""

"""
解决方案：
    方法一：使用字符串的str.ljust()，str.rjust()，str.center()进行左，右，居中对齐
    方法二：使用format()方法，传递类似'<20', '>20', '^20'参数完成同样任务
"""

s = 'abc'

# 左对齐
print(s.ljust(20))      # abc
print(s.ljust(20, '=')) # abc=================

# 右对齐
print(s.rjust(20))      #                  abc
print(len(s.rjust(20))) # 20

# 居中对齐
print(s.center(20))     #         abc

"""
    使用内置format()方法
"""

# 左对齐
print(format(s, '<20')) # abc

# 右对齐
print(format(s, '>20')) #                  abc

# 居中对齐
print(format(s, '^20')) #         abc

d = {
    "lodDist": 100.0,
    "SmallCull": 0.04,
    "DistCull": 500.0,
    "trilinear": 40,
    "farclip" :477
}

# 找到长度最长的key
w = max(map(len, d.keys()))

for k in d:
    print(k.ljust(w), ':', d[k])


"""二、如何去掉字符串中不需要的字符？"""

"""
实际案例：

    1.过滤掉用户输入中前后多余的空白字符:
    ' nick2008@gmail.com '
    
    2.过滤某windows下编辑文本中的^\r':
    'hello world\r\n'
    
    3.去掉文本中的unicode组合符号(音调):
    u'nǐ hǎo, chī fàn'
"""

"""
解决方案：
    方法一：字符串strip()，lstrip()，rstrip()方法去掉字符串两端字符
    方法二：删除单个固定位置的字符，可以使用切片 + 拼接的方式
    方法三：字符串的replace()方法或正则表达式re.sub()删除任意位置字符
    方法四：字符串translate()方法，可以同时删除多种不同字符
"""

s = '    abc    123    '

# 删除两端字符
print(s.strip())    # abc    123
print(s.lstrip())   # abc    123
print(s.rstrip())   #     abc    123

# 删除指定字符
s = '---abc+++'
print(s.strip('+-'))    # abc

"""
 使用切片 + 拼接的方式
"""

s = 'abc:123'
print(s[:3] + s[4:])    # abc123

"""
    字符串的replace()方法或正则表达式re.sub()删除任意位置字符
"""

s = '\tabc\t123\txyz'
print(s.replace('\t', ''))  # abc123xyz

# 去除多个指定字符用正则

import re

s = '\tabc\t123\txyz\ropq\r'
print(re.sub('[\t\r]', '', s))  # abc123xyzopq

"""
    字符串translate()方法，可以同时删除多种不同字符
"""

# 将abc和xyz相互转换
s = 'abc123456xyz'
print(s.translate(str.maketrans('abcxyz', 'xyzabc'))) # xyz123456abc

# 不转换，只指定要删除的所有字符
s = 'abc\refg\n123\t'
print(s.translate(str.maketrans('', '', '\t\r\n')))   # abcefg123

import sys
import unicodedata

s = 'nǐ hǎo, chī fàn'

remap = {
 # ord返回ascii值
 ord('\t'): '',
 ord('\f'): '',
 ord('\r'): None
 }

# 去除\t, \f, \r
a = s.translate(remap)

"""
　　通过使用dict.fromkeys()方法构造一个字典，每个Unicode 和音符作为键，对于的值全部为None
　　然后使用unicodedata.normalize()将原始输入标准化为分解形式字符
　　sys.maxunicode: 给出最大Unicode代码点的值的整数，即1114111（十六进制的0x10FFFF）
　　unicodedata.combining: 将分配给字符chr的规范组合类作为整数返回。 如果未定义组合类，则返回0
"""

cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))

b = unicodedata.normalize('NFD', a)

#调用translate 函数删除所有重音符
print(b.translate(cmb_chrs))    # ni hao, chi fan

# print(unicodedata.normalize('NFKD', u).encode('ascii','ignore'))    # b'ni hao, chi fan'