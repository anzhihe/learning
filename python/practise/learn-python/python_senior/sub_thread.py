#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    sub_thread.py
 @Function:    子线程的创建与启动之直接实例化Thread和继承Thread
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/25
"""


"""一、子线程的创建之启动之直接实例化Thread"""

"""
    标准库模块threading中提供了一个类对象Thread，用于表示线程。
    
    使用类对象Thread创建并启动子线程的第1种方式为：
    (1) 根据类对象Thread创建线程实例对象
    (2) 调用线程实例对象的方法start()启动线程
        调用方法start()后，会自动调用方法run()，方法run()会自动调用参数target指定的函数。
        
    Thread的特殊方法__init__()的定义如下：
    __init__(self, group=None, target=None, name=None,
                    args=(), kwargs=None, *, daemon=None)
    调用特殊方法__init__()时必须指定关键字实参，其中：
    (1) 参数group用于指定线程实例对象所属的线程组，默认不属于任何线程组
    (2) 参数target用于指定被方法run()调用的函数，默认没有函数被调用
    (3) 参数name用于指定创建的线程实例对象的名称，第n个子进程的默认名称为'Thread-n'
    (4) 参数args用于指定target接收的位置参数，用元组表示，默认不接收位置参数
    (5) 参数kwargs用于指定target接收的关键字参数，用字典表示，默认不接收关键字参数
    (6) 参数daemon用于指定线程实例对象是否是守护线程，默认不是守护线程
"""

from threading import Thread, current_thread
import time

def do_sth(arg1, arg2):
    print('子线程%s启动' % current_thread().getName())
    time.sleep(20)
    print('arg1 = %d，arg2 = %d' % (arg1, arg2))
    print('子线程%s结束' % current_thread().getName())

if __name__ == '__main__':
    print('父线程%s启动' % current_thread().getName())

    # process = Thread(target=do_sth, args = (5, 8), name = 'mythread')
    process = Thread(target=do_sth, args = (5, 8))
    process.start()

    time.sleep(25)

    print('父线程%s结束' % current_thread().getName())


"""二、子线程的创建与启动之继承Thread"""

"""
    使用类对象Thread创建并启动子线程的第2种方式为：
    (1) 自定义继承自Thread的类对象，重写特殊方法__init__()和方法run()
    (2) 根据自定义的类对象创建线程实例对象
    (3) 调用线程实例对象的方法start()启动线程
        调用方法start()后，会自动调用重写后的方法run()。
        
    与第1种方式相比，相当于把参数target指定的函数体转移到了方法run()中。因此，在创建
线程实例对象时无需再指定参数target。
    第1种方式创建线程实例对象时指定的其它参数，在第2种方式中可以传递给重写后的特殊方法__init__()。
"""

from threading import Thread, current_thread
import time

print('父线程%s启动' % current_thread().getName())

class MyThread(Thread):
    def __init__(self, name, args):
        super().__init__(name = name)
        self.args = args

    def run(self):
        print('子线程%s启动' % current_thread().getName())
        time.sleep(20)
        print('arg1 = %d, arg2 = %d' % self.args)
        print('子线程%s结束' % current_thread().getName())

mt = MyThread(name = 'mythread', args = (5, 8))
mt.start()

time.sleep(25)

print('父线程%s结束' % current_thread().getName())
