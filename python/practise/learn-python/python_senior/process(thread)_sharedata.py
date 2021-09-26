#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    process(thread)_sharedata.py
 @Function:    进程间通信之共享内存，多进程、多线程操作共享数据的不安全性
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/30
"""


"""一、进程间通信之共享内存"""

"""
    如果想要实现进程之间的通信，共享内存是常见的实现方式之一。它允许多个进程直接访问同一块内存。
    
    共享内存中对象的类型必须是ctypes的。ctypes是与C语言兼容的数据类型。
    
    为了在共享内存中创建ctypes类型的对象，标准库模块multiprocessing提供了如下两个函数：
    (1) Value(typecode_or_type: Any, *args: Any, lock: bool = ...) -> sharedctypes._Value: ...
        返回值表示一个数值。
        参数typecode_or_type用于指定数值的类型码或ctypes类型。
    (2) def Array(typecode_or_type: Any, size_or_initializer: Union[int, Sequence[Any]], *, lock: bool = ...) 
        返回值表示一个数组。
        参数typecode_or_type用于指定数组中元素的类型码或ctypes类型。
        参数size_or_initializer用于指定数组的长度或python中的序列。
"""

from multiprocessing import Process, Value, Array
import ctypes

def do_sth0(number, array):
    number.value = 1.8
    for i in range(len(array)):
        array[i] = -array[i]

if __name__ == '__main__':

    # 在共享内存中创建一个表示数值的ctypes对象
    number = Value('d', 2.3)
    # <Synchronized wrapper for c_double(2.3)>

    array = Array('i', range(1, 5))
    # <SynchronizedArray wrapper for <multiprocessing.sharedctypes.c_int_Array_4 object at 0x10f43f3c0>>

    p = Process(target=do_sth0, args=(number, array))
    p.start()
    p.join()

    print(number.value) # 1.8
    print(array[:])     # [-1, -2, -3, -4]


"""二、多进程操作共享数据的不安全性"""

"""
    由于多进程的执行是不确定的，导致多进程操作共享数据的结果是不可预期的，常被称为不安全的。
"""

from multiprocessing import Process, Value, Array

def do_sth(num):
    for i in range(100):
        # 相当于：num.value = num.value + 1
        # 首先计算num.value + 1，存入临时变量中，然后将临时变量的值赋给num
        num.value += 1

def do_sth1(arr):
    for i in range(len(arr)):
        arr[i] = -arr[i]

if __name__ == '__main__':

    num = Value('i', 0)
    arr = Array('i', range(10))

    p1 = Process(target=do_sth, args=(num,))
    p2 = Process(target=do_sth, args=(num,))
    p3 = Process(target=do_sth1, args=(arr,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print(num.value)    # not sure
    print(arr[:])       # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]




"""三、多线程操作共享数据的不安全性"""

"""
    由于多线程的执行是不确定的，导致多线程操作共享数据的结果是不可预期的，常被称为不安全的。
"""

from threading import Thread

num2 = 0

def do_sth2():
    global num2
    for i in range(100000):
        num2 += 1

if __name__ == '__main__':

    t1 = Thread(target=do_sth2)
    t2 = Thread(target=do_sth2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(num2) # not sure