#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    Process(Thread)PoolExecutor.py
 @Function:    进程池ProcessPoolExecutor、线程池ThreadPoolExecutor
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/28
"""


"""一、进程池ProcessPoolExecutor"""

"""
    标准库模块concurrent.futures中提供了一个类对象ProcessPoolExecutor，也用于表示进程池。
与Pool相比，ProcessPoolExecutor的功能和性能更加强大。
    类对象ProcessPoolExecutor遵守了上下文管理协议，所以可以使用with语句，这样，在离开运行时
上下文会自动调用方法shutdown(wait=True)
"""
'''
from concurrent.futures import ProcessPoolExecutor
import time, random


def do_sth(i):
    print('子进程%d启动' % i)

    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()

    print('子进程%d结束，耗时%.2f秒' % (i, end - start))

if __name__ == '__main__':
    print('父进程启动')

    """
    # 将进程池所能容纳的最大进程数指定为3
    ppe = ProcessPoolExecutor(max_workers=3)

    # 将需要进程池处理的任务全部交给进程池，此后会创建并启动由进程池管理的子进程
    for i in range(1, 11):
        ppe.submit(do_sth, i)

    # 父进程被阻塞，进程池管理的所有子进程执行完之后，父进程再从被阻塞的地方继续执行
    ppe.shutdown(wait=True)
    """

    with ProcessPoolExecutor(max_workers=3) as ppe:
        """
        for i in range(1, 11):
            ppe.submit(do_sth, i)
        """
        ppe.map(do_sth, range(1, 11))

    print('父进程结束')

    # 程序运行后会同时创建并启动3个子进程，第4个子进程要等前面3个中的某一个执行结束后才会创建并启动
'''

"""
    方法submit()的返回值是一个Future实例对象，表示子进程所调用的那个函数的执行(比如：do_sth())。
可以调用Future的方法result()得到这个函数的返回值。
"""

'''
from concurrent.futures import ProcessPoolExecutor
import time

def do_sth(i):
    time.sleep(2)
    return i * i

if __name__ == '__main__':

    """
    with ProcessPoolExecutor(max_workers=3) as ppe:
        for i in range(1, 5):
            future = ppe.submit(do_sth, i)
            # 同步，需要等待do_sth执行完毕
            print(future.result())
    """

    with ProcessPoolExecutor(max_workers=3) as ppe:
        objs = []
        for i in range(1, 5):
            future = ppe.submit(do_sth, i)
            # 异步，无需等待do_sth执行完毕
            print(future)
            objs.append(future)

    for obj in objs:
        print(obj.result())
'''

"""
    标准库模块concurrent.futures中还提供了两个函数：
    (1) wait(fs, timeout=None, return_when=ALL_COMPLETED)
        该函数用于阻塞父进程，以等待指定的Future实例对象序列，直到满足指定的条件。
        参数fs用于指定要等待的Future实例对象序列。
        参数timeout用于指定等待的最长时间。如果指定为None或不指定，则一直等待。
        参数return_when用于指定该函数何时返回，有三种取值：FIRST_COMPLETED、FIRST_EXCEPTION
    和ALL_COMPLETED，分别表示：当第一个Future实例对象已经完成或已被取消时、当第一个Future实例对象
    抛出异常时、当所有Future实例对象已经完成或已被取消时。
        该函数的返回值是由两个集合组成的元组，第一个集合包含了已经完成或已被取消的所有Future实例对象，
    第二个集合包含了没有完成并且没有被取消的Future实例对象。
    (2) as_completed(fs, timeout=None)
        该函数用于将指定的Future实例对象序列转换为一个迭代器，当序列中的任意一个Future实例对象
    已经完成或已被取消时都会被yield。这样，通过遍历得到的迭代器，就可以在任意一个Future实例对象
    已经完成或已被取消时立即做一些处理，比如调用方法result()得到执行结果。
        参数fs用于指定Future实例对象序列。
        参数timeout用于指定超时时间。如果指定为None或不指定，则不会超时。
        该函数的返回值是Future实例对象的迭代器。
"""

from concurrent.futures import ProcessPoolExecutor, wait, as_completed, \
    ALL_COMPLETED, FIRST_COMPLETED
import time, random

def do_sth(i):
    time.sleep(random.random() * 10)
    return i * i

if __name__ == '__main__':

    ppe = ProcessPoolExecutor(max_workers=3)

    """
    objs = []
    for i in range(1, 5):
        future = ppe.submit(do_sth, i)
        objs.append(future)

    # (done, not_done) = wait(objs, return_when=ALL_COMPLETED)
    (done, not_done) = wait(objs, return_when=FIRST_COMPLETED)

    print(done)
    print(not_done)
    """

    objs = []
    for i in range(1, 5):
        future = ppe.submit(do_sth, i)
        objs.append(future)

    future_iterator = as_completed(objs)
    for future in future_iterator:
        print(future.result())


"""二、线程池ThreadPoolExecutor"""

"""
    标准库模块concurrent.futures中提供了一个类对象ThreadPoolExecutor，也用于表示线程池。
与ThreadPool相比，ThreadPoolExecutor的功能和性能更加强大。
    类对象ThreadPoolExecutor遵守了上下文管理协议，所以可以使用with语句，这样，在离开运行时
上下文会自动调用方法shutdown(wait=True)
"""

from concurrent.futures import ThreadPoolExecutor
import time, random

def do_sth2(i):
    print('子线程%d启动' % i)

    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()

    print('子线程%d结束，耗时%.2f秒' % (i, end - start))

if __name__ == '__main__':

    print('父线程启动')

    """
    # 将线程池所能容纳的最大线程数指定为3
    tpe = ThreadPoolExecutor(max_workers=3)

    # 将需要线程池处理的任务全部交给线程池，此后会创建并启动由线程池管理的子线程
    for i in range(1, 11):
        tpe.submit(do_sth, i)

    # 父线程被阻塞，线程池管理的所有子线程执行完之后，父线程再从被阻塞的地方继续执行
    tpe.shutdown(wait=True)
    """

    with ThreadPoolExecutor(max_workers=3) as tpe:
        """
        for i in range(1, 11):
            tpe.submit(do_sth2, i)
        """
        tpe.map(do_sth2, range(1, 11))

    print('父线程结束')

    # 程序运行后会同时创建并启动3个子线程，第4个子线程要等前面3个中的某一个执行结束后才会创建并启动