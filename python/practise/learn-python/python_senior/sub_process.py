#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    sub_process.py
 @Function:    子进程的创建与启动之直接实例化和继承Process
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/24
"""


"""一、子进程的创建与启动之直接实例化Process"""

"""
    标准库模块multiprocessing中提供了一个类对象Process，用于表示进程。
    
    使用类对象Process创建并启动子进程的第1种方式为：
    (1) 根据类对象Process创建进程实例对象
    (2) 调用进程实例对象的方法start()启动进程
        调用方法start()后，会自动调用方法run(),方法run()会自动调用参数target指定的函数
        
    Process的特殊方法__init__()的定义如下：
    __init__(self, group=None, target=None, name=None, args=(), kwargs={})
    调用特殊方法__init__()必须指定关键字实参，其中，
    (1) 参数group用于指定进程实例对象所属的进程组，默认不属于任何进程组
    (2) 参数target用于指定被方法run()调用的函数，默认没有函数被调用
    (3) 参数name用于指定创建的进程实例对象的名称，第n个子进程的默认名称为'Process-n'
    (4) 参数args用于指定target接收的位置参数，用元组表示，默认不接收位置参数
    (5) 参数kwargs用于指定target接收的关键字参数，用字典表示，默认不接收关键字参数
"""

from multiprocessing import Process, current_process
import time

def do_sth(arg1, arg2):
    print('子进程启动(%d--%s)' % (current_process().pid, current_process().name))
    print('arg1 = %d, arg2 = %d' % (arg1, arg2))
    print('子进程结束(%d--%s)' % (current_process().pid, current_process().name))

if __name__ == '__main__':
    print('父进程启动(%d--%s)' % (current_process().pid, current_process().name))

    process = Process(target=do_sth, args=(5, 8), name='myprocess')
    process.start()

    time.sleep(2)

    print('父进程结束(%d--%s)' % (current_process().pid, current_process().name))


"""二、子进程的创建与启动之继承Process"""

"""
    使用类对象Process创建并启动子进程的第2种方式为：
    (1) 自定义继承自Process的类对象，重写特殊方法__init__()和方法run()
    (2) 根据自定义的类对象创建进程实例对象
    (3) 调用进程实例对象的方法start()启动进程
        调用方法start后，会自动调用重写后的方法run()
    
    与第1种方式相比，相当于把参数target指定的函数体转移到了方法run()中。因此，在创建
    进程实例对象时无需再指定参数target
    第1种方式创建进程实例对象时指定的其它参数，在第2种方式中可以传递给重写后的特殊方法__init__()
"""

print('-'*20)

class MyProcess(Process):
    def __init__(self, name, args):
        super().__init__(name = name)
        self.args = args

    def run(self):
        print('子进程启动(%d--%s)' % (current_process().pid, current_process().name))
        print('arg1 = %d, arg2 = %d' % self.args)
        print('子进程结束(%d--%s)' % (current_process().pid, current_process().name))

if __name__ == '__main__':
    print('父进程启动(%d--%s)' % (current_process().pid, current_process().name))

    mp = MyProcess(name = 'myprocess1', args= (5, 8))
    mp.start()

    time.sleep(2)

    print('父进程结束(%d--%s)' % (current_process().pid, current_process().name))
