#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    exception_def.py
 @Function:    python异常的概述
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/19
"""


"""异常的概述"""

"""
1、什么是异常？
    异常指的是程序在没有语法错误的前提下，在运行期间产生的特定错误。
    每个特定错误都对应一个异常类对象。当产生某个特定错误时，其对应的异常类对象的实例对象就会被抛出。
    如果在程序中抛出的异常实例对象不进行捕获和处理，程序就会停止运行，并且打印错误的详细信息，包括：
    (1) Traceback，它指的是异常调用堆栈的跟踪信息，其中列出了程序中的相关行数
    (2) 对应的异常类对象的名称，以及异常的错误信息
        如果在程序中对抛出的异常实例对象进行捕获和处理，程序就会继续运行
        
    哪些特定错误会被看作异常呢？
    首先，python内置了很多异常类对象，其次，可以自定义异常类对象，
    所以，内置的异常类对象和自定义的异常类对象对应的错误会被看作异常。
"""

print(1 / 0)    # ZeroDivisionError: division by zero

# print('123' + 456)  # TypeError: can only concatenate str (not "int") to str

# print(int('abc'))   # ValueError: invalid literal for int() with base 10: 'abc'

"""
2、内置的异常类对象
    python内置的异常类对象及其继承关系如下所示：
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
           
    对于每个异常类对象所表示的特定错误，可以参考官方文档：
    https://docs.python.org/3/library/exceptions.html
    
    所有内置异常类对象的基类是Exception
"""