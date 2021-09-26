#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    pipe.py
 @Function:    进程间通信之管道
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/31
"""


"""一、管道的概述"""

"""
python中的管道有两种工作方式：
    (1) 单向(半双工)
        一端只能发送数据，另一端只能接收数据。
    (2) 双向(全双工)
        两端都既能发送数据又能接收数据，一端发送的数据只能由另一端接收。
        
    标准库模块multiprocessing中提供了一个函数Pipe()，其返回值是一个元组，元组中包含两个对象，
分别表示管道两端的连接。
    调用函数Pipe()时，如果不传入参数或传入的参数为True，管道的工作方式为双向(全双工)；
    如果传入的参数为False，管道的工作方式为单向(半双工)，其中，对于返回的元组，第一个连接对象只能接收
数据，第二个连接对象只能发送数据。

对于管道两端的连接对象，主要有两个方法：
    (1) send(self, obj)
        用于将参数obj指定的对象发送到管道。
    (2) recv(self)
        用于从管道中接收对象。
"""


from multiprocessing import Pipe

conn1, conn2 = Pipe()

conn1.send('conn1第1次发送的数据')
conn1.send('conn1第2次发送的数据')

conn2.send('conn2第1次发送的数据')
conn2.send('conn2第2次发送的数据')

print(conn1.recv()) # conn2第1次发送的数据
print(conn1.recv()) # conn2第2次发送的数据

print(conn2.recv()) # conn1第1次发送的数据
print(conn2.recv()) # conn1第2次发送的数据

c1, c2 = Pipe(False)

c2.send('c2发送的数据')
print(c1.recv())    # c2发送的数据

# c1.send('c1发送的数据')  # OSError: connection is read-only


"""二、进程间通信之管道"""

"""
    如果想要实现进程之间的通信，管道是常见的实现方式之一。
"""


from multiprocessing import Process, Pipe
import os, time, random

# 发送数据的子进程执行的代码
def send_data(conn):
    print('发送数据的子进程%d启动' % os.getpid())

    for obj in list(range(1, 10)):
        print('发送数据：%s' % obj)
        conn.send(obj)
        time.sleep(random.random() * 3)

    print('发送数据：None')
    conn.send(None)

    print('发送数据的子进程%d结束' % os.getpid())

# 接收数据的子进程执行的代码
def recv_data(conn):
    print('接收数据的子进程%d启动' % os.getpid())

    while True:
        item = conn.recv()
        if item is None:
            print('接收数据：None')
            break
        print('接收数据：%s' % item)
        time.sleep(random.random() * 3)

    print('接收数据的子进程%d结束' % os.getpid())

if __name__ == '__main__':

    print('父进程%d启动' % os.getpid())

    cr, cs = Pipe(False)

    ps = Process(target=send_data, args=(cs, ))
    pr = Process(target=recv_data, args=(cr, ))

    ps.start()
    pr.start()

    ps.join()
    pr.join()

    print('父进程%d结束' % os.getpid())
