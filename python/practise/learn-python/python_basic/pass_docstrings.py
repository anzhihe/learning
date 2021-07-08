#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    pass_docstrings.py
 @Function:    Python pass statement & Docstrings
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/5
"""


"""一、pass语句"""

"""
    pass语句什么都不做，它只是一个占位符，用在语法上需要语句的地方，例如：
    (1) if语句的条件执行体
    (2) for-in语句的循环体
    (3) 定义函数时的函数体
    
    有时候可能还没有想好上述相关语句该怎么写，就可以先使用pass语句作为占位符，以确保程序可以运行，
    等想好了之后再把pass语句替换掉
"""

age = 23
if age > 18:
    pass

for i in range(8):
    pass

def do_something():
    pass


"""二、函数的定义之文档字符串"""

"""
1、什么是文档字符串？
    对于函数、模块、类或方法，位于其第一行的字符串被称为文档字符串，通常用三个引号表示
    文档字符串用于对函数、模块、类或方法进行解释说明
    之所以称为"文档"字符串，是因为可以使用工具根据文档字符串自动地生成文档
    
    应该养成编写文档字符串的习惯，以提高程序的可读性
    
    通过属性__doc__可以访问文档字符串
    调用内置函数help()得到的帮助信息中会包含文档字符串
"""

print(len.__doc__)
print(help(len))

"""
2、函数的文档字符串的常见内容和格式约定
    (1) 第一行是简明扼要的总结
    (2) 第一行的首字母大写，第一行以句号结尾
    (3) 如果文档字符串包含多行，第二行是空行，从第三行开始是详细的描述
    
    更多关于文档字符串的约定，可参考PEP 257: https://www.python.org/dev/peps/pep-0257
"""

def form_complex(real = 0.0, imag = 0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part(default 0.0)
    imag -- the imaginary part(default 0.0)
    """
    pass


"""三、函数的定义之函数注解"""

"""
1、什么是函数注解？
    定义函数时，为了让形参或返回值的类型或作用更加清晰，可以给形参或返回值添加函数注解，
    从而对形参或返回值做解释说明，以帮助函数文档化
    函数注解是可选的，可以添加也可以不添加
    函数注解可以是任意的表达式
    解释器会忽略函数注解，因此解释器并不会使用函数注解来检查实参的类型的返回值的类型
    
    更多关于函数注解，可参考PEP 3107 https://www.python.org/dev/peps/pep-3107/
"""

"""
2、添加函数注解
    给形参添加函数注解的方式为：在形参后面添加:和任意的表达式
    给返回值添加函数注解的方式为：在)的后面添加->和任意的表达式
"""

def f(a: 'string type', b: int) -> 'join a with b':
    return a + str(b)

print(f('hello', 12.3)) # hello12.3

"""
3、访问函数注解
    通过属性__annotations__可以访问函数注解
    调用内置函数help()得到的帮助信息中会包含函数注解
"""

# {'a': 'string type', 'b': <class 'int'>, 'return': 'join a with b'}
print(f.__annotations__)

print(help(f))
