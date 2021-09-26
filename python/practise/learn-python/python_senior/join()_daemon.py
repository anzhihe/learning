#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    join()_daemon.py
 @Function:    方法join()使用及守护进程和线程
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/25
"""


"""一、多进程执行的不确定性"""

"""
    默认情况下，多个进程的执行顺序和时间都是不确定的，完全取决于操作系统的调度
"""

"""
from multiprocessing import Process, current_process
import time

def do_sth():
    for i in range(5):
        print('%s: %d' % (current_process().name, i))
        time.sleep(2)

if __name__ == '__main__':
    for i in range(3):
        Process(target=do_sth).start()

    do_sth()
"""


"""二、多线程执行的不确定性"""

"""
    默认情况下，多个线程的执行顺序和时间都是不确定的，完全取决于操作系统的调度。
"""

"""
from threading import Thread, current_thread
import time

def do_sth():
    for i in range(5):
        print('%s: %d' % (current_thread().name, i))
        time.sleep(2)

if __name__ == '__main__':
    for i in range(3):
        Thread(target=do_sth).start()

    do_sth()
"""

"""三、阻塞父进程的子进程之方法join()"""

"""
    在父进程中创建并启动子进程后，可以调用子进程的方法join()，这样，子进程会把父进程阻塞，
父进程会等子进程执行完之后再从被阻塞的地方继续执行。
    在调用方法join()时，可以指定参数timeout，从而指定子进程阻塞父进程的时间。
"""

"""
from multiprocessing import current_process, Process
import time

class MyProcess(Process):
    def run(self):
        print('子进程%d启动' % current_process().pid)
        time.sleep(2)
        print('子进程%d结束' % current_process().pid)

if __name__ == '__main__':
    print('父进程%d启动' % current_process().pid)

    mp = MyProcess()
    mp.start()

    # mp.join()
    mp.join(1)

    print('父进程%d结束' % current_process().pid)
"""

"""四、阻塞父线程的子线程之方法join()"""

"""
    在父线程中创建并启动子线程后，可以调用子线程的方法join()，这样，子线程会把父线程阻塞，
父线程会等子线程执行完之后再从被阻塞的地方继续执行。
    在调用方法join()时，可以指定参数timeout，从而指定子线程阻塞父线程的时间。
"""

"""
from threading import current_thread, Thread
import time

class MyThread(Thread):
    def run(self):
        print('子线程%s启动' % current_thread().getName())
        time.sleep(2)
        print('子线程%s结束' % current_thread().getName())

if __name__ == '__main__':
    print('父线程%s开始' % current_thread().getName())

    mt = MyThread()
    mt.start()

    # mt.join()
    mt.join(1)

    print('父线程%s结束' % current_thread().getName())
"""


"""五、守护父进程的子进程"""

"""
    可以在调用进程实例对象的方法start()之前将属性daemon的值设置为True，从而将进程设置为守护进程。
    守护进程是为了守护父进程而存在的子进程。当父进程结束时，守护进程就没有存在的意义了，因此，
守护进程会随着父进程的结束而立刻结束。
"""

"""
from multiprocessing import current_process, Process
import time

class MyProcess(Process):
    def run(self):
        print('子进程%d启动' % current_process().pid)
        time.sleep(2)
        print('子进程%d结束' % current_process().pid)

if __name__ == '__main__':
    print('父进程%d启动' % current_process().pid)

    mp = MyProcess()
    mp.daemon = True
    mp.start()

    time.sleep(1)

    print('父进程%d结束' % current_process().pid)
"""


"""六、守护父线程的子线程"""

"""
    在创建线程实例对象时，可以将参数daemon指定为True，从而将创建的线程设置为守护线程。此外，
也可以在调用线程实例对象的方法start()之前调用线程实例对象的方法setDaemon(True)或
将属性daemon的值设置为True，从而将线程设置为守护线程。
    守护线程是为了守护父线程而存在的子线程。当父线程结束时，守护线程就没有存在的意义了，因此，
守护组进程会随着父线程的结束而立刻结束。
"""

from threading import current_thread, Thread
import time

class MyThread(Thread):
    def run(self):
        print('子线程%s启动' % current_thread().getName())
        time.sleep(2)
        print('子线程%s结束' % current_thread().getName())

if __name__ == '__main__':
    print('父线程%s开始' % current_thread().getName())

    mt = MyThread()
    mt.setDaemon(True)
    # mt.daemon = True
    mt.start()

    time.sleep(1)

    print('父线程%s结束' % current_thread().getName())