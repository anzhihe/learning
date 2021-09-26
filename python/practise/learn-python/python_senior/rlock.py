#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    rlock.py
 @Function:    多线程、多进程同步之RLock
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/30
"""


"""一、多线程同步之RLock"""

"""
    在同一线程中，当调用了Lock的方法acquire()之后，如果在调用方法release()之前再次调用了
方法acquire()，也会导致死锁。
"""

"""
from threading import Lock

lock = Lock()

lock.acquire()
print('获得锁')

lock.acquire()
print('获得锁')

lock.release()
print('释放锁')

lock.release()
print('释放锁')
"""

"""
    标准库模块threading中还提供了一个用于表示锁的类对象RLock(Reentrant Lock，可重入锁)。
与Lock相同的是：RLock也提供了用于获得锁的方法acquire()和用于释放锁的方法release()。
与Lock不同的是：在同一个线程中，当调用了RLock的方法acquire()之后，可以在调用方法release()之前
多次调用方法acquire()而不会导致死锁。
"""

from threading import RLock

rlock = RLock()

rlock.acquire()
print('获得锁')

rlock.acquire()
print('获得锁')

rlock.release()
print('释放锁')

rlock.release()
print('释放锁')

"""
    在RLock的内部维护了一个Lock和一个计数器counter。counter记录了锁被acquire的次数。
    
    当线程第一次调用方法acquire()获得锁时，锁的拥有者被保存，同时计数器counter被初始化为1；
当再次调用方法acquire()时，首先判断调用者是否是锁的拥有者，如果是，计数器counter加1。
    方法acquire()的定义如下：
    def acquire(self, blocking=True, timeout=-1):
        me = get_ident()
        if self._owner == me:
            self._count += 1
            return 1
        rc = self._block.acquire(blocking, timeout)
        if rc:
            self._owner = me
            self._count = 1
        return rc
        
    当调用方法release()时，首先判断调用者是否是锁的拥有者，如果是，计数器counter减1；
如果计数器counter减1后变为0，则将锁的拥有者设置为None，然后释放锁。
    方法release()的定义如下：
    def release(self):
        if self._owner != get_ident():
            raise RuntimeError("cannot release un-acquired lock")
        self._count = count = self._count - 1
        if not count:
            self._owner = None
            self._block.release()
    
    RLock相当于一个门可以上多把锁，上多少锁就得开多少把锁。
    因此，方法acquire()和release()必须成对出现。如果在某个线程中调用了n次acquire()，必须
调用n次release()才能释放该线程所占用的锁。
"""

"""二、多进程同步之RLock"""

"""
    RLock也遵守了上下文管理协议，所以可以使用with语句对代码进行简化。
"""

'''
from threading import Thread, RLock

numa = 0
numb = 0

rlock = RLock()

def do_sth():
    """
    rlock.acquire()
    try:
        adda()
        addb()
    finally:
        rlock.release()
    """
    with rlock:
        adda()
        addb()

def adda():
    global numa
    """
    rlock.acquire()
    try:
        numa += 1
    finally:
        rlock.release()
    """
    with rlock:
        numa += 1

def addb():
    global numb
    """
    rlock.acquire()
    try:
        numb += 1
    finally:
        rlock.release()
    """
    with rlock:
        numb += 1

if __name__ == '__main__':

    tlist = []

    for i in range(10):
        t = Thread(target=do_sth)
        tlist.append(t)
        t.start()

    for item in tlist:
        item.join()

    print(numa)
    print(numb)
'''


"""二、多进程同步之RLock"""

"""
    RLock也遵守了上下文管理协议，所以可以使用with语句对代码进行简化。
"""

from multiprocessing import Process, Value, RLock


def do_sth(numa, numb, rlock):
    """
    rlock.acquire()
    try:
        adda(numa)
        addb(numb)
    finally:
        rlock.release()
    """
    with rlock:
        adda(numa)
        addb(numb)

def adda(numa):
    """
    rlock.acquire()
    try:
        numa += 1
    finally:
        rlock.release()
    """
    with rlock:
        numa.value += 1

def addb(numb):
    """
    rlock.acquire()
    try:
        numb += 1
    finally:
        rlock.release()
    """
    with rlock:
        numb.value += 1

if __name__ == '__main__':

    numa = Value('i', 0)
    numb = Value('i', 0)

    rlock = RLock()

    plist = []

    for i in range(10):
        p = Process(target=do_sth, args = (numa, numb, rlock))
        plist.append(p)
        p.start()

    for item in plist:
        item.join()

    print(numa.value)
    print(numb.value)