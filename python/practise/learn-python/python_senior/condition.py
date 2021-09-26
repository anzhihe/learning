#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    condition.py
 @Function:    多线程、多进程同步之Condition
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/31
"""


"""一、多线程同步之Condition"""

"""
    标准库模块threading中提供了一个类对象Condition，用于表示带触发条件的锁，以帮助我们处理
多线程间复杂的同步问题。Condition允许一个或多个线程等待触发条件，直到收到另外一个线程的通知。
"""

from threading import Thread, Condition
import time


class MyThread1(Thread):
    def __init__(self, name, cond):
        super().__init__(name=name)
        self.cond = cond

    def run(self):
        cond.acquire()

        print('%s说：1' % self.name)
        cond.notify()
        cond.wait()

        # 思考两秒之后再说
        time.sleep(2)
        print('%s说：11' % self.name)
        cond.notify()
        cond.wait()

        time.sleep(2)
        print('%s说：111' % self.name)
        cond.notify()

        cond.release()

class MyThread2(Thread):
    def __init__(self, name, cond):
        super().__init__(name=name)
        self.cond = cond

    def run(self):
        time.sleep(1)
        cond.acquire()

        # 思考两秒之后再说
        time.sleep(2)
        print('%s说：2' % self.name)
        cond.notify()
        cond.wait()

        time.sleep(2)
        print('%s说：22' % self.name)
        cond.notify()
        cond.wait()

        time.sleep(2)
        print('%s说：222' % self.name)

        cond.release()

if __name__ == '__main__':

    cond = Condition()

    MyThread1('Thread1', cond).start()
    MyThread2('Thread2', cond).start()



"""二、多进程同步之Condition"""

"""
    标准库模块multiprocessing中提供了一个类对象Condition，用于表示带触发条件的锁，以帮助我们处理
多进程间复杂的同步问题。Condition允许一个或多个进程等待触发条件，直到收到另外一个进程的通知。    
"""

"""
from multiprocessing import Process, Condition
import time

cond = Condition()

class MyProcess1(Process):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        cond.acquire()

        print('%s说：1' % self.name)
        cond.notify()
        cond.wait()

        # 思考两秒之后再说
        time.sleep(2)
        print('%s说：11' % self.name)
        cond.notify()
        cond.wait()

        time.sleep(2)
        print('%s说：111' % self.name)
        cond.notify()

        cond.release()

class MyProcess2(Process):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        time.sleep(1)
        cond.acquire()

        # 思考两秒之后再说
        time.sleep(2)
        print('%s说：2' % self.name)
        cond.notify()
        cond.wait()
        
        time.sleep(2)
        print('%s说：22' % self.name)
        cond.notify()
        cond.wait()

        time.sleep(2)
        print('%s说：222' % self.name)

        cond.release()

if __name__ == '__main__':

    MyProcess1('Process1').start()
    MyProcess2('Process2').start()
"""