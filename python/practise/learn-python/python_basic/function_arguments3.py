#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    function_arguments3.py
 @Function:    python function arguments
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/4
"""

"""一、函数的定义之使用*定义个数可变的位置形参"""

"""
    定义函数时，可能无法事先确定传递的位置实参的个数，在这种情况下，可以在形参前添加一个*，
    将形参定义为个数可变的位置形参，从而可以接收0个或任意多个位置实参。这些位置实参会将个数可变的
    位置形参初始化为一个元组
"""

def f(*args):
    print(args)

f()         # ()
f(1)        # (1,)
f(1, 2, 3)  # (1, 2, 3)

"""
    定义函数时，最多只能定义一个个数可变的位置形参
"""

# def fun(*arg1, *arg2):  # multiple * parameters are not allowed
#     print(arg1, arg2)

"""
    很多内置函数都定义了个数可变的位置形参。例如，内置函数print()的定义为：
    def print(self, *args, sep=' ', end='\n', file=None):
"""

print()         #
print(1)        # 1
print(1, 2)     # 1 2
print(1, 2, 3)  # 1 2 3

"""
    通常，把个数可变的位置形参定义为最后一个形参，以便接收所有剩余的位置实参
"""

def fun1(a, b, *c):
    print('a =', a, 'b =', b, 'c =', c)

fun1(1, 2, 3, 4, 5)     # a = 1 b = 2 c = (3, 4, 5)

"""
    如果个数可变的位置形参不是最后一个形参，那么其后面的所有形参都被定义为只能接收关键字实参的
    关键字形参。如果向这些关键字形参传递位置实参，所有的位置实参都会被算作个数可变的，从而导致
    关键字实参的缺失
"""

def fun2(a, *b, c, d):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d)

fun2(1, 2, 3, 4, c = 5, d = 6)  # a = 1 b = (2, 3, 4) c = 5 d = 6

# 可能你想把实参5和6分别传递给形参c和d，
# 但是2、3、4、5、6全被算作了个数可变的位置实参，从而导致形参c和d对应实参的缺失
# fun2() missing 2 required keyword-only arguments: 'c' and 'd'
# fun2(1, 2, 3, 4, 5, 6)


"""二、函数的调用之使用*将序列中的每个元素都转换为位置实参"""

def f(a, b, c):
    print('a =', a, 'b =', b, 'c =', c)

f(1, 2, 3)  # a = 1 b = 2 c = 3

L = [1, 2, 3]
# 列表L整体作为一个位置实参
# f(L)    # f() missing 2 required positional arguments: 'b' and 'c'

f(L[0], L[1], L[2]) # a = 1 b = 2 c = 3

"""
    调用函数时，可以在序列前面添加一个*，从而将序列中的每个元素都转换为一个单独的位置实参
"""
# 相当于：f(L[0], L[1], L[2])：
f(*L)   # a = 1 b = 2 c = 3

"""
    注意和个数可变的位置形参进行区分。个数可变的位置形参是在定义函数时使用，使用*将序列中的
    每个元素都转换为位置实参是在调用函数时使用
"""

def fun(*args):
    print(args)

# 列表L整体作为一个位置实参
fun(L)  # ([1, 2, 3],)

# 先将序列中的每个元素都转换为一个单独的位置实参
# 再用这些位置实参将个数可变的位置形参初始化为一个元组
fun(*L) # (1, 2, 3)


"""三、函数的定义之使用**定义个数可变的关键字形参"""

"""
    定义函数时，可能无法事先确定传递的关键字实参的个数，在这种情况下，可以在形参前添加两个*，
    将形参定义为个数可变的关键字形参，从而可以接收0个或任意多个关键字实参。这些关键字实参会将
    个数可变的关键字形参初始化为一个字典
"""

def f(**kwargs):
    print(kwargs)

f() # {}
f(a = 1)    # {'a': 1}
f(a = 1, b = 2, c =3)   # {'a': 1, 'b': 2, 'c': 3}

"""
    定义函数时，最多只能定义一个个数可变的关键字形参
"""

# def fun(**kwargs1, **kwargs2):  # multiple ** parameters are not allowed
#     print(kwargs1, kwargs2)

"""
    很多内置函数都定义了个数可变的关键字形参。例如，内置函数sorted()的定义为：
    def sorted(*args, **kwargs):
"""

L = ['Python', 'Java', 'Swift']
print(sorted(L)) # ['Java', 'Python', 'Swift']
print(sorted(L, key = len)) # ['Java', 'Swift', 'Python']
print(sorted(L, key = len, reverse = True)) # ['Python', 'Swift', 'Java']

"""
    因为调用函数时位置实参必须位于关键字实参之前，所以个数可变的位置形参必须位于
    个数可变的关键字形参之前
"""

# def fun(**kwargs, *args):   # * parameter after ** parameter
#     print(kwargs, args)

def fun(*args, **kwargs):
    print(kwargs, args)


"""四、函数的调用之使用**将字典中的每个键值对都转换为关键字实参"""

def f(a, b, c):
    print('a =', a, 'b =', b, 'c =', c)

f(a = 1, b = 2, c = 3)  # a = 1 b = 2 c = 3

d = {'a': 1, 'b': 2, 'c': 3}

# 字典d整体作为一个位置实参
# f(d)    # f() missing 2 required positional arguments: 'b' and 'c'

f(a = d['a'], b = d['b'], c = d['c'])   # a = 1 b = 2 c = 3

"""
    调用函数时，可以在字典前添加两个**，从而将字典中的每个键值对都转换为一个单独的关键字实参
"""

# 相当于：f(a = d['a'], b = d['b'], c = d['c'])
f(**d)  # a = 1 b = 2 c = 3

"""
    注意和个数可变的关键字形参进行区分。个数可变的关键字形参是在定义函数时使用，
    使用**将字典中的每个键值对都转换为关键字实参是在调用函数时使用
"""

def fun(**kwargs):
    print(kwargs)

# 先将字典中的每个键值对都转换为一个单独的关键字实参
# 再用这些关键字实参将个数可变的关键字形参初始化为一个字典
fun(**d)    # {'a': 1, 'b': 2, 'c': 3}


"""五、函数的各种参数大总结"""

def f1(a, b = 5, *args, **kwargs):
    print('a =', a, 'b =', b, 'args =', args, 'kwargs =', kwargs)

f1(2, 6, 7, 8, c = 9)   # a = 2 b = 6 args = (7, 8) kwargs = {'c': 9}
f1(2)   # a = 2 b = 5 args = () kwargs = {}

def f2(a, b = 5, *, c, **kwargs):
    print('a =', a, 'b =', b, 'c =', c, 'kwargs =', kwargs)

f2(*(3, 6), **{'c': 8, 'd': 10})    # a = 3 b = 6 c = 8 kwargs = {'d': 10}
f2(3, c = 8, d = 10)    # a = 3 b = 5 c = 8 kwargs = {'d': 10}