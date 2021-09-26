#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    with.py
 @Function:    python with语句
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/20
"""


"""with语句"""

"""
    如果一个类对象实现了特殊方法__enter__()和__exit__()，那么就称这个类对象遵守了上下文管理协议，
同时，这个类对象的实例对象被称为上下文管理器。
    with语句会让上下文管理器创建一个运行时上下文，当进入运行时上下文时自动调用特殊方法__enter__(),
当离开运行上下文时自动调用特殊方法__exit__()。
    with语句的语法格式：
    with 上下文表达式 [as 变量]:
        with语句体
        
    如果with语句体中产生了异常，那么sys.exc_info()的返回值中的三个元素会被自动传递给特殊方法
__exit__()的形参exc_type, exc_val, exc_tb, 这三个形参分别表示异常的类型、异常的错误信息和
异常调用堆栈的跟踪信息

    与finally从句类似，特殊方法__exit__()总会被调用，通常在特殊方法__exit__()中释放资源，
例如：关闭文件、关闭网络连接等
"""

class MyContextManager(object):
    def __enter__(self):
        print("特殊方法__enter__()被调用")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("特殊方法__exit__()被调用")

        print("异常的类型：%s" % exc_type)
        print("异常的错误信息：%s" % exc_val)
        print("异常调用堆栈的跟踪信息：%s" % exc_tb)

        # return True

    def do_sth(self):
        print("方法do_sth()被调用")
        print(1 / 0)

"""
with MyContextManager() as mcm:
    mcm.do_sth()
"""

"""
    当with语句体中产生异常，并且特殊方法__exit__()没有返回True时，为了让程序能够继续执行，
可以使用try-except语句对抛出的异常实例对象进行捕获和处理。
"""

try:
    with MyContextManager() as mcm:
        mcm.do_sth()
except ZeroDivisionError as err:
    print(err)