#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    threadlocal.py
 @Function:    线程之ThreadLocal
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/1
"""


"""一、为什么需要ThreadLocal"""

"""
    多线程操作共享的全局变量是不安全的。那局部变量呢？
    局部变量只归某个线程私有，其它线程是无法访问的。但是，在线程内操作局部变量也存在问题：
    如果线程内有多个函数都需要访问多个局部变量，则需要将这些局部都作为实参分别传递给这些函数。
这样，传递参数就会很麻烦。
"""

"""
import threading

def do_sth(arg1, arg2, arg3):
    local_var1 = arg1
    local_var2 = arg2
    local_var3 = arg3

    fun1(local_var1, local_var2, local_var3)
    fun2(local_var1, local_var2, local_var3)
    fun3(local_var1, local_var2, local_var3)

def fun1(local_var1, local_var2, local_var3):
    print('%s: %s -- %s -- %s' % (threading.current_thread().name, local_var1,
                        local_var2, local_var3))

def fun2(local_var1, local_var2, local_var3):
    print('%s: %s -- %s -- %s' % (threading.current_thread().name, local_var1,
                                  local_var2, local_var3))

def fun3(local_var1, local_var2, local_var3):
    print('%s: %s -- %s -- %s' % (threading.current_thread().name, local_var1,
                                  local_var2, local_var3))

t1 = threading.Thread(target=do_sth, args=('a', 'b', 'c'))
t2 = threading.Thread(target=do_sth, args=('d', 'e', 'f'))

t1.start()
t2.start()
"""


"""二、什么是ThreadLocal"""

"""
    ThreadLocal是一个全局变量，用来存放各个线程的局部变量。ThreadLocal中会维护
"某个线程 - 该线程内的某个局部变量名 - 该局部变量的值"的映射。
    在线程中将局部变量写入ThreadLocal的语法格式为: threadlocal.局部变量名 = 局部变量值;
在线程中从ThreadLocal中读取局部变量的语法格式为: threadlocal.局部变量名。
"""

from threading import Thread, local, current_thread

thread_local = local()

def do_sth(arg1, arg2, arg3):
    thread_local.local_var1 = arg1
    thread_local.local_var2 = arg2
    thread_local.local_var3 = arg3

    fun1()
    fun2()
    fun3()

def fun1():
    print('%s: %s -- %s -- %s' % (current_thread().name, thread_local.local_var1,
                                  thread_local.local_var2,
                                  thread_local.local_var3))

def fun2():
    print('%s: %s -- %s -- %s' % (current_thread().name, thread_local.local_var1,
                                  thread_local.local_var2,
                                  thread_local.local_var3))

def fun3():
    print('%s: %s -- %s -- %s' % (current_thread().name, thread_local.local_var1,
                                  thread_local.local_var2,
                                  thread_local.local_var3))

t1 = Thread(target=do_sth, args=('a', 'b', 'c'))
t2 = Thread(target=do_sth, args=('d', 'e', 'f'))

t1.start()
t2.start()