#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    lock.py
 @Function:    多进程、多线程同步之Lock
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/30
"""


"""一、多进程同步之Lock"""

"""
    为了保证多个进程能安全地操作共享数据，必须确保一个进程在操作共享数据时，其它进程都不能操作。
    与上厕所同理，一个进程A在操作共享数据前必须先试图获得锁从而给相关代码上锁，进程A获得了锁之后，
锁的状态变为"locked"。如果另外一个进程B试图获得锁，进程B的状态会变为"blocked"并且被添加到锁等待池，
只能等待获得锁的进程A释放之后，锁的状态变为"unlocked"，进程调度程序再从锁等待池中处于状态"blocked"
的进程中选择一个来获得锁，获得锁之后该进程的状态变为"running"。由于只有一把锁，无论有多少个进程，
同一时刻最多只有一个进程能获得该锁，这样，就确保了操作共享数据的相关代码只能由一个进程从头到尾
完整地执行，从而确保了多个进程操作共享数据总是安全的。
    但是，包含锁的相关代码只能以单进程模式执行，因此效率大大降低了。
"""

"""
    标准库模块multiprocessing中提供了一个类对象Lock，用于表示锁，以实现多进程之间的同步。
简单地说，同步就意味着"阻塞和等待"。

    为了保证获得锁的进程用完后一定要释放锁，可以将操作共享数据的相关代码放在try语句块中，
把释放锁的代码放在finally语句块中。

    由于类对象Lock遵守了上下文管理协议，所以可以使用with语句进行简化，这样，在进行运行时上下文时
会自动调用方法acquire()，在离开运行时上下文时会自动调用方法release()。
"""

from multiprocessing import Process, Lock, Value


def do_sth(num, lock):
    for i in range(10000):
        """
        lock.acquire()
        try:
            num.value += 1
        finally:
            lock.release()
        """
        with lock:
            num.value += 1

if __name__ == '__main__':

    num = Value('i', 0)
    lock = Lock()

    p1 = Process(target=do_sth, args=(num, lock))
    p2 = Process(target=do_sth, args=(num, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(num.value)


"""二、多线程同步之Lock"""

"""
    为了保证多个线程能安全地操作共享数据，必须确保一个进程在操作共享数据时，其它线程都不能操作。
    与上厕所同理，一个线程A在操作共享数据前必须先试图获得锁从而给相关代码上锁，线程A获得了锁之后，
锁的状态变为"locked"。如果另外一个线程B试图获得锁，进程B的状态会变为"blocked"并且被添加到锁等待池，
只能等待获得锁的线程A释放之后，锁的状态变为"unlocked"，线程调度程序再从锁等待池中处于状态"blocked"
的线程中选择一个来获得锁，获得锁之后该线程的状态变为"running"。由于只有一把锁，无论有多少个线程，
同一时刻最多只有一个线程能获得该锁，这样，就确保了操作共享数据的相关代码只能由一个线程从头到尾
完整地执行，从而确保了多个线程操作共享数据总是安全的。
    但是，包含锁的相关代码只能以单线程模式执行，因此效率大大降低了。
"""

"""
    标准库模块threading中提供了一个类对象Lock，用于表示锁，以实现多线程之间的同步。
简单地说，同步就意味着"阻塞和等待"。

    为了保证获得锁的进程用完后一定要释放锁，可以将操作共享数据的相关代码放在try语句块中，
把释放锁的代码放在finally语句块中。

    由于类对象Lock遵守了上下文管理协议，所以可以使用with语句进行简化，这样，在进行运行时上下文时
会自动调用方法acquire()，在离开运行时上下文时会自动调用方法release()。
"""

from threading import Thread, Lock

num1 = 0
lock = Lock()

def do_sth1():
    global num1
    for i in range(10000):
        """
        lock.acquire()
        try:
            num.value += 1
        finally:
            lock.release()
        """
        with lock:
            num1 += 1

if __name__ == '__main__':

    t1 = Thread(target=do_sth1)
    t2 = Thread(target=do_sth1)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(num1)