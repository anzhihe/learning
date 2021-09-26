#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    partial.py
 @Function:    python偏函数
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/22
"""


"""偏函数"""

"""
    定义函数时，可以给形参设置默认值，从而简化函数的调用，只有与默认值不符的形参才需要传递
额外的实参。
    
    偏函数也可以简化函数的调用。
    可以将某个已有的函数转换为一个新函数，在转换的过程中指定最前面的若干个位置实参以及关键字实参，
这样，当调用新函数的时候，在其内部调用的仍然是转换前的函数，在传递实参时只需要传递剩余的
位置实参和关键字实参就可以了。转换后的新函数被称为转换前的函数的偏函数。
    借助于标准库的模块functools中的partial(func, *args, **kwargs),
可以将某个已有的函数转换为其偏函数。
"""

from functools import partial

def f(a, b = 5):
    print('a = ', a, 'b = ', b)

f_new = partial(f, 2)

f_new()         # a = 2 b = 5
f_new(6)        # a = 2 b = 6
f_new(b = 6)    # a = 2 b = 6
# f_new(a = 3)    # TypeError: f() got multiple values for argument 'a'

def eval_sum(*args):
    s = 0
    for n in args:
        s += n
    return s

eval_sum_new = partial(eval_sum, 20, 30)
print(eval_sum_new(1, 2, 3, 4, 5))  # 65

def f1(a, b = 5, *args, **kwargs):
    print('a =', a, 'b =', b, 'args =', args, 'kwargs =', kwargs)

f1_new = partial(f1, 1, 3, 6, m = 8)
f1_new(2, 4, n = 9) # a = 1 b = 3 args = (6, 2, 4) kwargs = {'m': 8, 'n': 9}

def f2(a, b = 5, *, c, **kwargs):
    print('a =', a, 'b =', b, 'c =', c, 'kwargs =', kwargs)

f2_new = partial(f2, 1, m = 8)
f2_new(3, c = 9)    # a = 1 b = 3 c = 9 kwargs = {'m': 8}
