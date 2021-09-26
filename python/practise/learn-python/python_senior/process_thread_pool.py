#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    process_thread_pool.py
 @Function:    进程池Pool和线程池ThreadPool
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/27
"""


"""一、进程池Pool"""

"""
    如果并发的任务数过多，一次性创建并启动大量的进程会给计算机带来很大的压力，那么就可以使用进程池
对创建与启动的进程进行限制和管理。
    进程池中所能容纳的进程数目是固定的。
    标准库模块multiprocessing中提供了一个类对象Pool，用于表示进程池。进程池中所能容纳的进程数目
可以在创建Pool实例对象时进行指定；如果不指定，默认大小是CPU的核数
"""

from multiprocessing import Pool
import time, random


def do_sth(i):
    print('子进程%d启动' % i)

    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()

    print('子进程%d结束，耗时%.2f秒' % (i, end - start))


if __name__ == '__main__':

    print('父进程启动')

    # 将进程池所能容纳的最大进程数指定为3
    pp = Pool(3)

    for i in range(1, 11):
        # 与方法start()类似，不同的是，创建并启动由进程池管理的子进程
        pp.apply_async(do_sth, args=(i,))

    # 调用方法join()之前必须先调用方法close()
    # 调用方法close()之后就不能让进程池再管理新的进程了
    pp.close()

    # 父进程被阻塞
    # 进程池管理的所有子进程执行完之后，父进程再从被阻塞的地方继续执行
    pp.join()

    print('父进程结束')

    # 程序运行后会同时创建3个子进程，第4个子进程要等前面3个中的某一个执行结束后才会创建并启动


"""二、线程池ThreadPool"""

"""
    如果并发的任务数过多，一次性创建并启动大量的线程会给计算机带来很大的压力，那么就可以使用线程池
对创建与启动的线程进行限制和管理。
    线程池所能容纳的线程数目是固定的。
    第三方库threadpool中提供了一个类对象ThreadPool，用于表示线程池。线程池中所能容纳的线程数目
可以在创建ThreadPool实例对象时进行指定；如果不指定，默认大小是CPU的核数。
"""

from threadpool import ThreadPool, makeRequests
import time, random

def do_sth(i):
    print('子线程%d启动' % i)

    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()

    print('子进程%d结束，耗时%.2f秒' % (i, end - start))


if __name__ == '__main__':

    print('父线程启动')

    args_list = []
    for i in range(1, 11):
        args_list.append(i)

    # 将线程池所能容纳的最大线程数指定为3
    tp = ThreadPool(3)

    # 创建需要线程池处理的任务
    requests = makeRequests(do_sth, args_list)

    # 将需要线程池处理的任务全部交给线程池，此后会创建并启动由线程池管理的子线程
    for req in requests:
        tp.putRequest(req)

    # 父线程被阻塞
    # 线程池管理的所有子线程执行完之后，父线程再从被阻塞的地方继续执行
    tp.wait()

    print('父线程结束')

    # 程序运行后会同时创建3个子进程，第4个子进程要等前面3个中的某一个执行结束后才会创建并启动
