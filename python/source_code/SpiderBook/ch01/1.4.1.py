#coding:utf-8
'''
第一种方式：使用os模块中的fork方式实现多进程

import os
if __name__ == '__main__':
    print 'current Process (%s) start ...'%(os.getpid())
    pid = os.fork()
    if pid < 0:
        print 'error in fork'
    elif pid == 0:
        print 'I am child process(%s) and my parent process is (%s)',(os.getpid(),os.getppid())
    else:
        print 'I(%s) created a chlid process (%s).',(os.getpid(),pid)
'''
'''
第二种方法：使用multiprocessing模块创建多进程
import os
from multiprocessing import Process
# 子进程要执行的代码
def run_proc(name):
    print 'Child process %s (%s) Running...' % (name, os.getpid())
if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p_list=[]
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        p_list.append(p)
        print 'Process will start.'
        p_list[i].start()
    for p in p_list:
        p.join()
    print 'Process end.'

'''
'''
multiprocessing模块提供了一个Pool类来代表进程池对象

from multiprocessing import Pool
import os, time, random

def run_task(name):
    print 'Task %s (pid = %s) is running...' % (name, os.getpid())
    time.sleep(random.random() * 3)
    print 'Task %s end.' % name

if __name__=='__main__':
    print 'Current process %s.' % os.getpid()
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'

'''
'''
Queue进程间通信

from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def proc_write(q,urls):
    print('Process(%s) is writing...' % os.getpid())
    for url in urls:
        q.put(url)
        print('Put %s to queue...' % url)
        time.sleep(random.random())

# 读数据进程执行的代码:
def proc_read(q):
    print('Process(%s) is reading...' % os.getpid())
    while True:

        url = q.get(True)
        print('Get %s from queue.' % url)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    proc_writer1 = Process(target=proc_write, args=(q,['url_1', 'url_2', 'url_3']))
    proc_writer2 = Process(target=proc_write, args=(q,['url_4','url_5','url_6']))
    proc_reader = Process(target=proc_read, args=(q,))
    # 启动子进程proc_writer，写入:
    proc_writer1.start()
    proc_writer2.start()
    # 启动子进程proc_reader，读取:
    proc_reader.start()
    # 等待proc_writer结束:
    proc_writer1.join()
    proc_writer2.join()
    # proc_reader进程里是死循环，无法等待其结束，只能强行终止:
    proc_reader.terminate()
'''
'''
pipe进程间通信

import multiprocessing
import random
import time,os

def proc_send(pipe,urls):
    for url in urls:
        print "Process(%s) send: %s" %(os.getpid(),url)
        pipe.send(url)
        time.sleep(random.random())

def proc_recv(pipe):
    while True:
        print "Process(%s) rev:%s" %(os.getpid(),pipe.recv())
        time.sleep(random.random())

'''


