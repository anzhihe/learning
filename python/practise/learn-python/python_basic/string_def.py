#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    string_def.py
 @Function:    string definition
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/6/23
"""

"""一、字符串的概述"""

"""
1、什么是字符串？
    在程序中，文本内容用字符串来表示
    字符串由一系列有序的字符组成
    例如：'HelloWorld'，'PythonLanguage'
    字符串与列表和元组一样，都属于序列类型
    可以将字符串看作是字符的列表，列表的很多操作对于字符串也是适用的
    没有单独的字符类型，字符就是只包含一个元素的字符串，例如：'a'、'b'、'c'
"""

"""二、字符串的创建"""

"""
创建字符串的两种方式：
1、使用引号
    创建字符串时既可以使用单引号，也可以使用双引号，通常使用单引号
    当把字符串赋值给变量时，变量名不要取名为str，因为str是字符串对应的类名
"""

"""
>>> s = 'abcd'
>>> s
'abcd'

>>> s = "abcd"
>>> s
'abcd'

# 空字符串
>>> ''
''
>>> ""
''
"""

"""
    可以在单引号中使用双引号，也可以在双引号中使用单引号
    
>>> 'abc"def"'
'abc"def"'
>>> "abc'def'"
"abc'def'"
"""

"""
    不能在单引号中使用单引号，也不能在双引号中使用双引号

# 本来想要打印字符串abc'def'，结果前两个单引号进行了匹配
>>> 'abc'def''
  File "<stdin>", line 1
    'abc'def''
         ^
SyntaxError: invalid syntax

# 本来想要打印字符串abc"def"，结果前两个双引号进行了匹配
>>> "abc"def""
  File "<stdin>", line 1
    "abc"def""
         ^
SyntaxError: invalid syntax
"""

"""
2、调用内置函数str(类str的构造方法)

>>> str('abcd')
'abcd'
>>> str("abcd")
'abcd'

>>> str(123)
'123'
>>> str(12.3)
'12.3'

# 空字符串
>>> str()
''
"""


"""三、转义字符"""

"""
1、使用转义字符表示无法直接表示的特殊字符
    当字符串中包含换行、回车、水平制表符或退格等无法直接表示的特殊字符时，该如何表示呢？
    (1) 换行：newline，光标移动到下一行的开头
    (2) 回车：return，光标移动到本行的开头
    (3) 水平制表符：键盘上的tab键，光标移动到下一组4个空格的开始处
    (4) 退格：键盘backspace键，回退一个字符
    
    可以使用如下转义字符：
    换行：\n
    回车：\r
    水平制表符：\t
    退格：\b
"""

print('abc\ndef')
print('abc\rdef')   # def
print('123456\t123\t45')    # 123456	123	45
print('abc\bdef')   # abdef

"""
2、使用转义字符表示在字符串中有特殊用途的字符
    某些字符在字符串中有特殊用途，比如：反斜杠用于转义，单引号和双引号用于字符串的边界
    因此，不能在字符串中直接包含这些有特殊用途的字符
"""

# 本来想要打印字符串'abc\rdef'，结果反斜杠用于转义了
print('abc\rdef')   # def
# 本来想要打印字符串'abc'def'',结果前两个单引号进行了匹配
# print('abc'def')
# 本来想要打印字符串'abc'def'',结果前两个双引号进行了匹配
# print("abc"def"")

"""
    当字符串中包含反斜杠、单引号和双引号等有特殊用途的字符时，必须使用反斜杠对这些字符进行转义
    反斜杠：\\
    单引号：\'
    双引号：\"
"""

print('abc\\rdef')  # abc\rdef
print('abc\'def\'') # abc'def'
print("abc\"def\"") # abc"def"


"""四、原始字始符"""

"""
1、如果不想让字符串中的转义字符生效，可以在字符串的前面添加r或R，从而将字符串声明为原始字符串
"""

print(r'\tC:\\Program Files')   # \tC:\\Program Files
print(R'\tC:\\Program Files')   # \tC:\\Program Files

"""
2、原始字符串的最后一个字符不能是反斜杠(最后两个字符都是反斜杠除外)
"""

# print(r'HelloWorld\') # SyntaxError: EOL while scanning string literal
print(r'HelloWorld\\')  # HelloWorld\\

# 解释器不会把r'What\'看做是一个原始字符串，因为原始字符串不能以反斜杠结尾
print(r'What\'s your name') # What\'s your name
# 解释器不会把r'What\\'看做是一个原始字符串，因为原始字符串可以以两个反斜杠结尾
# print(r'What\\'s your name') # What\'s your name


"""五、跨越多行的字符串"""

"""
如果想让字符串跨越多行，常见的方式有两种：
1、使用三个引号
"""

print('''我是一个
跨越多行的
字符串''')

print("""我是一个
跨越多行的
字符串""")

# 在三个引号中既可以包含单引号，也可以包含双引号
print('''我是一个
'跨越多行'的
"字符"串''')

print("""我是一个
'跨越多行'的
"字符"串""")

# 可以在三个单引号中嵌套三个双引号，也可以在三个双引号中嵌套三个单引号
print('''我是一个
"""跨越多行"""的
字符串''')

print("""我是一个
'''跨越多行'''的
字符串""")

"""
2、在每行的结尾添加\
"""

print('我是一个\
跨越多行的\
字符串')