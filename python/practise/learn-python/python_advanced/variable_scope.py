#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    variable_scope.py
 @Function:    python变量的作用域、内置函数locals()和globals()
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/23
"""


"""一、变量的作用域"""

"""
变量的作用域指的是变量起作用的范围。变量的作用域是由定义变量的位置决定的。

变量的作用域有4种：
1. 局部作用域(Local)
    每次调用函数时都会创建一个局部作用域
    局部作用域(函数)中定义的变量称之为局部变量
    局部变量的作用域为：从定义变量处开始到函数结束
    函数调用结束后，其对应的局部作用域中的所有变量都会被销毁
2. 嵌套作用域(Enclosing)
    每次调用嵌套函数中的外函数时都会创建一个嵌套作用域
    当在外函数内定义变量时，该变量的作用域为：从定义变量处开始到函数结束
    外函数调用结束后，其对应的嵌套作用域中的所有变量都会被销毁(闭包除外)
3. 全局作用域(Global)
    每次运行模块时都会创建一个全局作用域
    全局作用域(模块)中定义的变量称之为全局变量
    全局变量的作用域为：从定义变量处开始到模块结束
    程序运行结束后，全局作用域中的所有变量都会被销毁
4. 内置作用域(Built-in)
    每次启动python解释器都会自动加载内置模块，从而创建一个内置作用域
    内置模块中的函数(内置函数)，可以在程序中直接使用
    停止解释器后，内置使用域中的所有变量都会被销毁
"""

def do_sth(a):
    print(a)
    b = 3
    print(b)

do_sth(2)
# print(a)    # NameError: name 'a' is not defined
# print(b)    # NameError: name 'b' is not defined

def outer():
    m = 5
    def inner():
        print(m)
    inner()

outer()     # 5
# print(m)    # NameError: name 'm' is not defined

# print(g)    # NameError: name 'g' is not defined
g = 18

"""
    当在某个作用域中访问变量时，会按照LEGB的顺序依次搜索该作用域及其后面的所有作用域，
只要找到了则停止搜索，如果没找到则抛出NameError。因此，如果不同的作用域中定义了同名的变量，
根据LEGB的搜索顺序，前面作用域中的变量会屏蔽掉后面作用域中定义的同名变量。
"""

print(id(123))
id = "Global"

def outside():
    id = "Enclosing"
    def inside():
        id = "Local"
        print(id)
    inside()

outside()   # 按照LEGB的顺序依次注释id，查看结果

i = 11
def fun1():
    i = 22
    print(i)
fun1()      # 22
print(i)    # 11

j = 0
def fun2():
    # print(j)    # UnboundLocalError: local variable 'j' referenced before assignment
    j = 5
fun2()

"""
    在默认情况下，在局部作用域或嵌套作用域中不能修改全局变量所引用的对象(如果引用的对象是
可变类型的，可以修改对象的内容)
"""

def f1():
    # 重新定义了一个局部变量g，把全局变量g给屏蔽了
    # g = 19

    # 相当于：g = g + 1，重新定义了一个局部变量g，把全局变量g给屏蔽了
    # 当计算等号右边的g + 1时，新定义的局部变量还没有被赋值，因此程序报错
    # g += 1  # UnboundLocalError: local variable 'g' referenced before assignment

    pass

g2 = [3]

def f2():
    # 重新定义了一个局部变量g，把全局变量g给屏蔽了
    # g2 = [1]

    # 全局变量g2引用的对象是可变类型的，可以修改对象的内容
    g2[0] = 8

"""
    如果想在局部作用域或嵌套作用域中修改全局变量所引用的对象，可以在局部作用域或嵌套作用域中
使用关键字global对变量进行声明，从而表明在局部作用域或嵌套作用域中不会再重新定义一个新的同名变量，
而是使用该名称的全局变量。
"""

def f3():
    global g
    g = 19
    print(g)

f3()    # 19

"""
    流程控制语句和异常处理语句不会创建对应的作用域，因此，对于流程控制语句和异常处理语句中定义的
变量，在语句执行结束后仍然是可用的。
"""

if True:
    temp = 18
print(temp)     # 18

for item in [1, 2, 3]:
    print(item)
print(item) # 3

try:
    result = 5
except:
    pass
print(result)   # 5


"""二、内置函数locals()和globals()"""

"""
    命名空间指的是某个作用域内所有名字和值的映射，用字典来表示。
    
    内置函数locals()可以返回其所有局部作用域的命名空间。
    内置函数globals()可以返回其所有局部作用域的命名空间。
"""

def outer(a):
    b = 8
    def inner(c):
        d = 3
    print(locals()) # {'a': 5, 'b': 8, 'inner': <function outer.<locals>.inner at 0x1021194c0>}

outer(5)

g = 2

class MyClass(object):
    pass

print(globals())

"""
    locals()并没有返回实际的命名空间，而是返回值的拷贝，所以，通过locals()修改某个名字对应的值，
对于实际的命名空间是没有影响的；但是，可以通过locals()向实际的命名空间中添加一个名字和值的映射。
"""

def f():
    x = 8
    print(locals()) # {'x': 8}

    locals()['x'] = 9
    locals()['y'] = 10

    print(locals()) # {'x': 8, 'y': 10}

f()

"""
    globals()返回的是实际的命名空间，所以，对globals()所做的任何修改，其实就是对实际命名空间
的修改。
"""

globals()['g'] = 6
globals()['gg'] = 66

print(globals())

"""
    可以在局部作用域或嵌套作用域中通过globals()访问全局作用域中被屏蔽的全局变量。
"""

def do_sth():
    g = 123
    print(globals()['g'])

do_sth()    # 6

"""
    对于内置函数vars()，查看其帮助信息可以：
    
    vars([object]) -> dictionary
    
    Without arguments, equivalent to locals(),
    With an argument, equivalent to object.__dict__。
"""