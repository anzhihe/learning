#coding:utf-8
'''
服务进程(taskManager.py)(linux版)

import random,time,Queue
from multiprocessing.managers import BaseManager
#实现第一步：建立task_queue和result_queue，用来存放任务和结果
task_queue=Queue.Queue()
result_queue=Queue.Queue()

class Queuemanager(BaseManager):
    pass
#实现第二步：把创建的两个队列注册在网络上，利用register方法，callable参数关联了Queue对象，
# 将Queue对象在网络中暴露
Queuemanager.register('get_task_queue',callable=lambda:task_queue)
Queuemanager.register('get_result_queue',callable=lambda:result_queue)

#实现第三步：绑定端口8001，设置验证口令‘qiye’。这个相当于对象的初始化
manager=Queuemanager(address=('',8001),authkey='qiye')

#实现第四步：启动管理，监听信息通道
manager.start()

#实现第五步：通过管理实例的方法获得通过网络访问的Queue对象
task=manager.get_task_queue()
result=manager.get_result_queue()

#实现第六步：添加任务
for url in ["ImageUrl_"+str(i) for i in range(10)]:
    print 'put task %s ...' %url
    task.put(url) 
#获取返回结果
print 'try get result...'
for i in range(10):
    print 'result is %s' %result.get(timeout=10)
#关闭管理
manager.shutdown()

'''

'''
程序taskWorker.py代码(win/linux版)

#coding:utf-8
import time
from multiprocessing.managers import BaseManager
# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass
# 实现第一步：使用QueueManager注册获取Queue的方法名称
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
# 实现第二步：连接到服务器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证口令注意保持与服务进程设置的完全一致:
m = QueueManager(address=(server_addr, 8001), authkey='qiye')
# 从网络连接:
m.connect()
# 实现第三步：获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 实现第四步：从task队列取任务,并把结果写入result队列:
while(not task.empty()):
        image_url = task.get(True,timeout=5)
        print('run task download %s...' % image_url)
        time.sleep(1)
        result.put('%s--->success'%image_url)

# 处理结束:
print('worker exit.')

'''

'''
taskManager.py程序(Windows版)
'''

# taskManager.py for windows
import Queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
#任务个数
task_number = 10
#定义收发队列
task_queue = Queue.Queue(task_number)
result_queue = Queue.Queue(task_number)
def get_task():
    return task_queue
def get_result():
     return result_queue
# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass
def win_run():
    #windows下绑定调用接口不能使用lambda，所以只能先定义函数再绑定
    QueueManager.register('get_task_queue',callable = get_task)
    QueueManager.register('get_result_queue',callable = get_result)
    #绑定端口并设置验证口令，windows下需要填写ip地址，linux下不填默认为本地
    manager = QueueManager(address = ('127.0.0.1',8001),authkey = b'qiye')
    #启动
    manager.start()
    try:
        #通过网络获取任务队列和结果队列
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        #添加任务
        for url in ["ImageUrl_"+str(i) for i in range(10)]:
            print 'put task %s ...' %url
            task.put(url)
        print 'try get result...'
        for i in range(10):
            print 'result is %s' %result.get(timeout=10)
    except:
        print('Manager error')
    finally:
        #一定要关闭，否则会爆管道未关闭的错误
        manager.shutdown()

if __name__ == '__main__':
    #windows下多进程可能会有问题，添加这句可以缓解
    freeze_support()
    win_run()

