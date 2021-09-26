#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    fork()_mainthread.py
 @Function:    子进程的创建与启动之调用函数fork()与
               自动创建与启动的父线程
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/25
"""

"""一、子进程的创建与启动之调用函数fork()"""

"""
    标准库模块os中提供了一个函数fork()，用于将当前进程复制一份子进程，而后父进程和子进程从
调用fork()处开始分叉(fork的含义)，兵分两路，继续并行运行后面的程序。
    与普通函数不同的是，函数fork()会返回两次，分别在父进程和子进程内返回。返回值有三种情况：
    (1) 返回值小于0，表示复制子进程失败
    (2) 返回值为0，表示处在子进程中
    (3) 返回值大于0，表示处在父进程中，返回值就是子进程的id
    在Windows操作系统上无法调用函数fork()，因为函数fork()不是跨平台的。而模块multiprocessing
    是跨平台的。
"""

import os

try:
    pid = os.fork()
except OSError:
    print('你的操作系统不支持调用函数fork()')
    exit()

if pid < 0:
    print('复制子进程失败')
elif pid == 0:
    print('我是子进程%d, 我的父进程是%d' % (os.getpid(), os.getppid()))
else:
    print('我是父进程%d，我的子进程是%d' % (os.getpid(), pid))


"""二、自动创建与启动的父线程"""

"""
    任何进程都会自动创建并启动一个线程，该线程被称为父(主)线程。
    父(主)线程的默认名称是MainThread。
"""

import time, threading

# 方法current_thread()用于获得当前线程实例对象(自动创建与启动的父线程)
print('自动创建并启动了父(主)线程：%s' % threading.current_thread().getName())

time.sleep(20)