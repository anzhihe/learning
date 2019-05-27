#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

'''
# 1.match(pattern,string,flags=0)
从起始位置开始根据模型去字符串中匹配指定内容,只匹配单个
 - 正则表达式
 - 要匹配的字符串
 - 标志位,用于控制正则表达式的匹配方式

# flags
I = IGNORECASE = sre_compile.SRE_FLAG_IGNORECASE # ignore case
L = LOCALE = sre_compile.SRE_FLAG_LOCALE # assume current 8-bit locale
U = UNICODE = sre_compile.SRE_FLAG_UNICODE # assume unicode locale
M = MULTILINE = sre_compile.SRE_FLAG_MULTILINE # make anchors look for newline
S = DOTALL = sre_compile.SRE_FLAG_DOTALL # make dot match newline
X = VERBOSE = sre_compile.SRE_FLAG_VERBOSE # ignore whitespace and comments
'''

t1 = re.match('\d+','123anzereffdb33')
if t1:
    print(t1.group())

##############################################

'''
# 2.search(pattern,string,flags=0)
根据模型去字符串中匹配指定内容,匹配单个
'''

t2 = re.search('\d+','w343feufd94343ksdfdf')
if t2:
    print(t2.group())

##############################################

'''
# 3.group和groups
'''

t3 = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)",t3).group())

print(re.search("([0-9]*)([a-z]*)([0-9]*)",t3).group(0))
print(re.search("([0-9]*)([a-z]*)([0-9]*)",t3).group(1))
print(re.search("([0-9]*)([a-z]*)([0-9]*)",t3).group(2))
print(re.search("([0-9]*)([a-z]*)([0-9]*)",t3).group(3))

print(re.search("([0-9]*)([a-z]*)([0-9]*)",t3).groups())


##############################################

'''
# 4.findall(pattern,string,flags=0)
匹配到字符串中所有符合条件的元素
'''

t4 = re.findall('\d+','343fdfdfer-k3434?')
print(t4)

##############################################

'''
5.sub(pattern,repl,string,count=0,flags=0)
用于替换匹配的字符串,比str.replace功能更加强大
'''

t5 = "12345abcde678"
new_t5 = re.sub('\d+','T',t5)
new_t5_1 = re.sub('\d+','T',t5,1)

print(new_t5)
print(new_t5_1)

##############################################

'''
6.split(pattern,string,maxsplit=0,flags=0)
根据指定匹配进行分组,比str.split更加强大
'''

# content = "'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"
# new_content = re.split('\*', content)
#  new_content = re.split('\*', content, 1)
# print(new_content)

# content = "'1 - 2 * ((60-30+1*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2) )'"
# new_content = re.split('[\+\-\*\/]+', content)
# # new_content = re.split('\*', content, 1)
# print(new_content)


inpp = '1-2*((60-30 +(-40-5)*(9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2))'
inpp = re.sub('\s*','',inpp)
new_content = re.split('\(([\+\-\*\/]?\d+[\+\-\*\/]?\d+){1}\)', inpp, 1)
print(new_content)


