#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    process(thread)_global_variable.py
 @Function:    进程和线程中的全局变量
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/30
"""


"""一、全局变量在多个进程中不能共享"""

"""
    每个进程都有独立的内存空间，从而进程间是相互独立的。因此，全局变量在多个进程中不能共享。
"""

from multiprocessing import Process

num = 18

def do_sth():
    global num
    num += 1

if __name__ == '__main__':

    p = Process(target=do_sth)
    p.start()
    p.join()

    # 在子进程中修改全局变量，对父进程中的全局变量没有影响
    # 因为，子进程对父进程中的全局变量做了一份拷贝，子进程与父进程中的num是完全不同的两个变量
    print(num)  # 18


"""二、全局变量在进程的所有线程中可以共享"""

"""
    进程内的所有线程共享内存空间，所以，全局变量在进程的所有线程中可以共享
"""

from threading import Thread

num = 18

def do_sth2():
    global num
    num += 1

if __name__ == '__main__':

    p = Thread(target=do_sth2)
    p.start()
    p.join()

    print(num)  # 19