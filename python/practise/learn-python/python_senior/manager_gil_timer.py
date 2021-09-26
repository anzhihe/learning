#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    manager_gil_timer.py
 @Function:    进程间通信之Manager、全局解释器锁GIL、定时器线程Timer
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/31
"""


"""一、进程间通信之Manager"""

"""
    如果想要实现进程之间的通信，Manager也是常见的实现方式之一。
    与共享内存相比，Manager更加灵活，因为它可以支持多种对象类型。此外，Manager还可以通过网络
被不同计算机上的进程所共享。但是，Manager的速度比共享内存慢。
"""

"""
from multiprocessing import Process, Manager


def f(d, l):
    d[1] = 18
    d['2'] = 56
    l.reverse()


if __name__ == '__main__':

    manager = Manager()

    d = manager.dict()

    l = manager.list(range(5))

    p = Process(target=f, args=(d, l))
    p.start()
    p.join()

    print(d)    # {1: 18, '2': 56}
    print(l)    # [4, 3, 2, 1, 0]
"""


"""二、全局解释器锁GIL"""

"""
def do_sth():
    while True:
        pass

do_sth()

    单进程或单线程占满了八核CPU中的其中一核。
"""

"""
from multiprocessing import Process

def do_sth():
    while True:
        pass

if __name__ == '__main__':

    Process(target=do_sth).start()
    Process(target=do_sth).start()

    do_sth()

    三个进程占满了八核CPU中的其中三核。因此，多进程可以实现并行(同时处理多个任务)从而发挥
多核CPU的最大功效。
"""

"""
from threading import Thread

def do_sth():
    while True:
        pass

Thread(target=do_sth).start()
Thread(target=do_sth).start()

do_sth()

    三个线程并没有占满八核CPU中的其中三核，而只占满了其中一核，因此，多线程并不能实现并行
(同时处理多个任务)而只能实现并发(交替处理多个任务)。
"""

"""
    我们编写的python代码是通过python解释器来执行的。通常使用的python解释器是官方提供的CPython。
CPython中有一个GIL(Global Interpreter Lock，全局解释器锁)，其作用相当于Lock，任何线程
在执行前必须先获得GIL，一个线程在获得GIL后其它线程就不能执行，直到线程释放GIL。因此，GIL保证了
同一时刻只有一个线程可以执行，从而导致python中的多线程不能实现并行
"""


"""三、定时器线程Timer"""

"""
    如果想要在指定的时间片段之后再启动子线程，可以使用标准库模块threading提供的类对象Timer,
用于表示定时器线程。Timer是Thread的子类，也是通过调用方法start()来启动线程。
"""

"""
from threading import Timer

def do_sth():
    print('Hello Timer!')

timer = Timer(2, do_sth)
timer.start()
"""

"""
    定时器只执行一次。如果需要每隔一段时间执行一次，则需要在子线程调用的函数的内部再次创建与启动
定时器线程。
"""

from threading import Timer
import time

def do_sth():
    print('Hello Timer!')
    global timer
    timer = Timer(3, do_sth)
    timer.start()

timer = Timer(2, do_sth)
timer.start()

time.sleep(10)
timer.cancel()

