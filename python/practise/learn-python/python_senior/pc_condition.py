#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    pc_condition.py
 @Function:    经典生产者消费者问题(多线程、多进程Condition版)
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/31
"""


"""一、经典生产者消费者问题(多线程Condition版)"""

"""
    经典生产者消费者问题：
    假设有一群生产者(Producer)和一群消费者(Consumer)通过一个市场来交换产品。
    生产者的策略是：如果市场上剩余的产品少于20个，那么就生产4个产品放到市场上；
    消费者的策略是：如果市场上剩余的产品多于10个，那么就从市场上消费3个产品。
"""


from threading import Thread, Condition
import time

cond = Condition()
count = 0

class Producer(Thread):
    def run(self):
        global count, cond
        while True:
            cond.acquire()
            if count < 20:
                count += 4
                print('%s：生产者生产了4个产品，当前总共%d个产品' % (self.name, count))
                cond.notify()
            else:
                print('%s：不生产，等待' % self.name)
                cond.wait()
            cond.release()
            time.sleep(2)

class Consumer(Thread):
    def run(self):
        global count, cond
        while True:
            cond.acquire()
            if count > 10:
                count -= 3
                print('%s：消费者消费了3个产品，当前总共%d个产品' % (self.name, count))
                cond.notify()
            else:
                print('%s：不消费，等待' % self.name)
                cond.wait()
            cond.release()
            time.sleep(2)

for i in range(3):
    Producer().start()

for i in range(3):
    Consumer().start()



"""二、经典生产者消费者问题(多进程Condition版)"""

"""
from multiprocessing import Process, Value, Condition
import time

cond = Condition()
count = Value('i', 0)

class Producer(Process):

    def run(self):
        global count, cond
        while True:
            cond.acquire()
            if count.value < 20:
                count.value += 4
                print('%s：生产者生产了4个产品，当前总共%d个产品' % (self.name, count.value))
                cond.notify()
            else:
                print('%s：不生产，等待' % self.name)
                cond.wait()
            cond.release()
            time.sleep(2)

class Consumer(Process):
    def run(self):
        global count, cond
        while True:
            cond.acquire()
            if count.value > 10:
                count.value -= 3
                print('%s：消费者消费了3个产品，当前总共%d个产品' % (self.name, count.value))
                cond.notify()
            else:
                print('%s：不消费，等待' % self.name)
                cond.wait()
            cond.release()
            time.sleep(2)

if __name__ == '__main__':

    for i in range(3):
        Producer().start()

    for i in range(3):
        Consumer().start()
"""
