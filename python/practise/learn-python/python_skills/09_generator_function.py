#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    09_generator_function.py
 @Function:    使用生成器函数实现可迭代对象
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/28
"""

"""如何使用生成器函数实现可迭代对象？"""

"""
实际案例：
实现一个可迭代对象的类，它能迭代出给定范围内所有素数:
    pn = PrimeNumbers(1, 30)
    for k in pn:
        print(k,)
    输出结果:
    2 3 5 7 11 13 17 19 23 29 
"""

"""
解决方案：将该类的__iter__方法实现成生成器函数，每次yield返回一个素数
"""

class PrimeNumbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_prime_num(self, n):
        if n < 2:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True

    def __iter__(self):
        for i in range(self.start, self.end + 1):
            if self.is_prime_num(i):
                yield i

if __name__ == '__main__':

    for i in PrimeNumbers(1, 100):
        print(i, end=' ')

