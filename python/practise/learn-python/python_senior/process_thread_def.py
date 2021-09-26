#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    process_thread_def.py
 @Function:    进程和线程的概述及自动创建与启动的进程
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/24
"""

"""一、进程和线程的概述"""

"""
    进程就是运行中的应用程序。应用程序是静态的，进程是动态的。
    
    查看所有正在运行的进程，每个进程至少对应一个线程。每个进程都用来完成一件任务，每个线程用来
完成进程内的一件子任务。线程就是进程内部的一个执行单元。

    每个进程都有独立的内存空间，而进程内的所有线程共享内存空间。
"""

"""
    不管是单核CPU还是多核CPU，都支持多任务。
    
    多个任务交替执行的方式称为并发。
    多个任务同时执行的方式称为并行。
"""


"""二、自动创建与启动的进程"""

"""
    当在PyCharm中运行一个py文件时，PyCharm对应的进程会自动创建并启动一个新进程，其默认名称为Python。
当py文件执行结束时，自动创建并启动的新进程也随之结束。
    创建并启动子进程的进程被称为父进程。
"""

import time, os
import multiprocessing

# 方法current_process用于获得当前进程实例对象(自动创建并启动的进程)
print(multiprocessing.current_process().pid)

# getpid：get process id
print(os.getpid())  # 打印当前进程的id

# getppid：get parent process id
print(os.getppid()) # 打印当前进程的父进程的id

time.sleep(20)  # 让py文件运行至少20秒钟