#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    semaphore.py
 @Function:    多线程、多进程同步之Semaphore
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/31
"""


"""一、多线程同步之Semaphore"""

"""
    标准库模块threading中提供了一个类对象Semaphore，用于表示信号量，它可以帮助我们控制并发线程的
最大数量，从而实现多线程之间的同步。

    Semphore也遵守了上下文管理协议，所以可以使用with语句对代码进行简化。
"""
'''
from threading import Thread, Semaphore
import time, random

sem = Semaphore(3)

class MyThread(Thread):
    def run(self):
        # sem.acquire()
        with sem:
            print('%s获得资源' % self.name)
            time.sleep(random.random() * 10)
        # sem.release()

for i in range(10):
    MyThread().start()

"""
    如果调用release()的次数比调用acquire()的次数多，计数器的当前值就会超过它的初始值。
为了确保能够及时检测到程序中的这种bug，可以使用BoundedSemaphore替代semaphore，这样，
一旦程序中出现这种bug，就会抛出异常ValueError
"""

from threading import BoundedSemaphore

bsem = BoundedSemaphore(3)
bsem.acquire()
bsem.release()
# bsem.release()  # ValueError: Semaphore released too many times
'''

"""二、多进程同步之Semaphore"""

"""
    标准库模块multiprocessing中提供了一个类对象Semaphore，用于表示信号量，它可以帮助我们控制并发进程的
最大数量，从而实现多进程之间的同步。

    Semphore也遵守了上下文管理协议，所以可以使用with语句对代码进行简化。
"""

from multiprocessing import Process, Semaphore
import time, random

sem = Semaphore(3)

class MyProcess(Process):
    def run(self):
        # sem.acquire()
        with sem:
            print('%s获得资源' % self.name)
            time.sleep(random.random() * 10)
        # sem.release()

if __name__ == '__main__':
    for i in range(10):
        MyProcess().start()

"""
    如果调用release()的次数比调用acquire()的次数多，计数器的当前值就会超过它的初始值。
为了确保能够及时检测到程序中的这种bug，可以使用BoundedSemaphore替代semaphore，这样，
一旦程序中出现这种bug，就会抛出异常ValueError。
    但是，官方文档中提到: On Mac OS X, this is indistinguishable from Semaphore。
"""

from multiprocessing import BoundedSemaphore

bsem = BoundedSemaphore(3)
bsem.acquire()
bsem.release()
bsem.release()  # 在MacOS平台没有抛出异常ValueError