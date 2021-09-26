#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    generator.py
 @Function:    python生成器
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/19
"""


"""生成器"""

"""
    为什么前面的课程中没有讲解元组生成式?因为根本就不存在元组生成式!元组是不可变类型的对象,
无法在代码中动态地创建元组对象。
    但是，将列表生成式的[]改成(),程序并不会报错，而是得到一个generator(生成器)对象。为了
查看生成器对应的所有元素，有两种方式:
    (1) 多次调用内置函数next()，每次调用都返回生成器的下一个元素，直到抛出异常StopIteration时表示
    没有更多元素了。
    (2) 使用for-in语句对生成器进行迭代，这样就不需要关心异常StopIteration了。
    
    生成器中保存的并不是其对应的所有元素，而是如何推算出所有元素的算法。将生成器用于for-in语句时，
元素是在循环的过程中不断被推算出来的。将生成器作为内置函数next()的实参时，返回的下一个元素也是
在调用函数时被推算出来的。因此，生成器是惰性推算的，也就是说，只有当用到生成器中的某个元素时,
才会临时进行推算，而并不会提前推算出来。
    如果需要创建一个元素个数较大的容器，就可以考虑使用生成器，从而节省大量的存储空间。
"""

ge = (i * i for i in range(1, 7))
print(ge)   # <generator object <genexpr> at 0x100a7a3c0>

print(next(ge))     # 1
print(next(ge))     # 4
print(next(ge))     # 9
print(next(ge))     # 16
print(next(ge))     # 25
print(next(ge))     # 36
# print(next(ge))     # StopIteration

ge = (i * i for i in range(1, 7))

for item in ge:
    print(item)

"""
    上面使用类似生成式的语法得到的生成器被称为生成器表达式。此外，当推算的算法比较复杂时，还可以
使用生成器函数得到生成器。
    生成器函数中通过关键字yield返回推算出的元素。生成器函数与普通函数的区别在于:当调用内置函数
next()或使用for-in语句进行迭代时，执行完yield语句就会将生成器函数挂起，下次会从挂起的地方
继续执行。
"""

def fib(n):
    i = 0
    a, b = 1, 1
    while i < n:
        yield a
        a, b = b, a + b
        i += 1

gf = fib(6)
print(gf)   # <generator object fib at 0x10a5633c0>

print(next(gf))     # 1
print(next(gf))     # 1
print(next(gf))     # 2
print(next(gf))     # 3
print(next(gf))     # 5
print(next(gf))     # 8
# print(next(gf))     # StopIteration

gf = fib(6)

for item in gf:
    print(item)