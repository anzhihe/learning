#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    try_except_else_finally.py
 @Function:    try-except语句添加else和finally从句，
               使用raise语句手动抛出异常
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/19
"""


"""一、在try-except语句的后面添加else从句"""

"""
    可以在while语句或for-in语句的后面添加else从句，这样，如果没有执行循环体中的break语句
从而提前退出循环，就会执行else从句。

    类似地，可以在try-except语句的后面添加else从句，其语法格式为：
    try:
        可能会产生异常的代码
    except 异常类对象1:
        当前except子句处理异常的代码
    except 异常类对象2:
        当前except子句处理异常的代码
    ...
    except 异常类对象n:
        当前except子句处理异常的代码
    else：
        try语句块中没有产生异常时执行的代码
"""

try:
    # result = 1 / 0
    result = 1 / 2
    # result = int('abc')
except ImportError:
    print("导入错误")
except ZeroDivisionError:
    print("0不能作为除数")
except TypeError:
    print("类型错误")
else:
    print(result)
print("结束")

"""
while True:
    try:
        x = int(input("请输入一个整数："))
    except ValueError:
        print("无效的输入，请再次输入")
    else:
        print("输入的整数为：", x)
        break
"""


"""二、在try-except语句的后面添加finally从句"""

"""
    可以在try-except语句的后面添加finally从句，其语法格式为：
    try:
        可能会产生异常的代码
    except 异常类对象1:
        当前except子句处理异常的代码
    except 异常类对象2:
        当前except子句处理异常的代码
    ...
    except 异常类对象n:
        当前except子句处理异常的代码
    finally：
        总会被执行的代码
        
        因为finally从句总会被执行，所以通常在finally从句中释放资源，例如：关闭文件、关闭网络连接等
"""

try:
    result = 1 / 0
    # result = 1 / 2
    # result = int('abc')
except ImportError:
    print("导入错误")
except ZeroDivisionError:
    print("0不能作为除数")
except TypeError:
    print("类型错误")
finally:
    print("释放资源")
print("结束")

"""
    可以在try-except语句的后面添加else从句和finally从句，其语法格式为：
    try:
        可能会产生异常的代码
    except 异常类对象1:
        当前except子句处理异常的代码
    except 异常类对象2:
        当前except子句处理异常的代码
    ...
    except 异常类对象n:
        当前except子句处理异常的代码
    else：
        try语句块中没有产生异常时执行的代码
    finally：
        总会被执行的代码
"""

try:
    # result = 1 / 0
    result = 1 / 2
    # result = int('abc')
except ImportError:
    print("导入错误")
except ZeroDivisionError:
    print("0不能作为除数")
except TypeError:
    print("类型错误")
else:
    print(result)
finally:
    print("释放资源")
print("结束")


"""三、使用raise语句手动抛出异常"""

"""
    对于前面课程中的示例，在发生异常时的异常实例都是被自动抛出的。
    我们可以使用raise语句手动抛出异常实例对象，其语法格式为：
    raise 异常类对象[([参数])]
    如果没有传入参数，可以省略掉小括号
"""

# raise ZeroDivisionError("0不能作为除数")

# raise ZeroDivisionError()
# raise ZeroDivisionError

try:
    raise ZeroDivisionError("0不能作为除数")
except ZeroDivisionError as err:
    print(err)

"""
    如果在except语句块中不想对异常实例对象进行处理，可以使用关键字raise将其原样抛出
"""

""" 
try:
    raise ZeroDivisionError("0不能作为除数")
except ZeroDivisionError:
    raise
"""

"""
    如果在except语句块中不想对异常实例对象进行处理，还可以使用raise语句手动抛出另外一个
异常类对象的实例对象
"""

try:
    raise ZeroDivisionError("0不能作为除数")
except ZeroDivisionError:
    raise ValueError("输入错误")