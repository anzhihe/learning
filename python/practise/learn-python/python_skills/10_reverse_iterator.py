#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    10_reverse_iterator.py
 @Function:    反向迭代
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/28
"""

"""如何进行反向迭代以及如何实现反向迭代？"""

"""
实际案例：
    实现一个连续浮点数发生器FloatRange(和range类似),
    根据给定范围(start, end)和步进值(step)产生一些列连续
    浮点数，如迭代FloatRange(3.0, 4.0, 0.2)可产生序列:
    正向:3.0->3.2->3.4->3.6->3.8->4.0
    反向:4.0->3.8->3.6->3.4->3.2->3.0
"""

"""
解决方案：
    使用迭代器来完成
    正向：实现正向迭代协议的__iter__方法，它返回一个正向迭代器
    反向：实现反向迭代协议的__reversed__方法，它返回一个反向迭代器
"""

class FloatRange:

    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        """实现正向迭代协议"""

        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        """实现反向迭代协议"""

        t = self.end
        while t >= self.start:
            yield t
            t -= self.step

if __name__ == '__main__':

    # 正向迭代
    for i in FloatRange(5, 10, 0.5):
        print(i)

    # 反向迭代
    for i in reversed(FloatRange(5, 10, 0.5)):
        print(i)