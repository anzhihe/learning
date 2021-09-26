#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    file_operations2.py
 @Function:    python文件操作之写文件、关闭文件，文件指针
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/20
"""


"""一、写文件"""

"""
    写文件之前，必须先打开文件。
    可以调用内置函数open()并以只写方式、追加方式或读写方式打开文件。这样，返回的文件对象有两个
用于写文件的方法:
1. write(text)
    用于将指定的字符串写入到文件中。调用后，会先将指定的字符串写入到缓存中，手动调用方法flush()
或close()之后，或者当写入的数据量大于等于缓存的容量时，缓存中的字符串才会被写入到文件中。

    方法的返回值为写入的字符数，即指定的字符串的长度。
"""

"""
>>> file = open('myfile.txt', 'w')
>>> file.write('hello')
5
>>> file.write('python')
6
>>> file.flush()
>>> file.close() 
>>> file = open('myfile.txt', 'a')
>>> file.write('hello')
5
>>> file.write('python')
6
>>> file.close()
"""

"""
2. writelines(seq)
    用于将指定的字符串序列依次写入到文件中。调用后，会先将指定的字符串序列写入到缓存中，手动调用
方法flush()或close()之后，或者当写入的数据量大于等于缓存的容量时，缓存中的字符串序列才会被
写入到文件中。
"""

"""
>>> file = open('myfile.txt', 'w')
>>> file.writelines(['123\n', '456\n', '789'])
>>> file.close()
"""


"""二、关闭文件"""

"""
    文件在使用完毕后必须要关闭，这是因为文件对象会占用操作系统的资源，并且操作系统在某一时刻
所能打开的文件数量也是有限的。
    读文件或写文件时都有可能发生异常，从而导致方法close()不会被调用。为了保证方法close()总能
被调用，可以把读文件或写文件的操作放在try语句块中，把方法close()的调用放在finally从句中，
    伪代码如下:
    打开文件
    try:
        读文件或写文件
    finally:
        调用方法close()关闭文件
        
    由于文件对象实现了特殊方法__enter__()和__exit__()， 所以文件对象可以作为上下文管理器。
其中，特殊方法__enter__()返回打开的文件对象，特殊方法__exit__()中关闭打开的文件，因此,
上面的伪代码可以使用with语句来实现:
    with 打开文件 as file:
        读文件或写文件
"""

file = open('myfile.txt', 'w')
try:
    file.write('hello')
finally:
    file.close()

with open('myfile.txt', 'a') as file:
    file.write('python')


"""三、文件指针"""

"""
1、什么是文件指针？
    任何文件对象都有一个文件指针，指向文件中的某个位置
    读写文件时，是从文件指针的当前位置开始读写的，在读写的过程中，文件指针会随之往后移动
    
2、打开文件后文件指针的位置
    以追加方式打开文件后，文件指针指向文件的结尾位置；以其它方式打开文件后，文件指针指向文件的
起始位置。
    可以调用文件对象的方法tell()，返回文件指针的当前位置。
"""

with open('myfile.txt', 'r') as file:
    print(file.tell())  # 0

with open('myfile.txt', 'r') as file:
    print(file.tell())  # 10

"""
3、读写文件时文件指针的移动过程
"""

with open('myfile.txt', 'r') as file:
    print(file.tell())  # 0

    file.read(3)
    print(file.tell())  # 3

    file.read(4)
    print(file.tell())  # 7

    file.read()
    print(file.tell())  # 10

with open('myfile.txt', 'a') as file:
    print(file.tell())  # 10

    file.write('hello')
    print(file.tell())  # 15

with open('myfile.txt', 'w') as file:
    print(file.tell())  # 0

    file.write('hello')
    print(file.tell())  # 5

"""
4、自由移动文件指针
    可以调用文件对象的方法seek(offset[, whence])，将文件指针自由移动到参数指定的位置，其中:
参数offset表示偏移量，可以为负数;参数whence是可选的，表示相对偏移位置，有三种取值:
    (1) os.SEEK_SET: 相对文件的起始位置，值为0，默认值
    (2) os.SEEK_CUR: 相对文件的当前位置，值为1
    (3) os.SEEK_END: 相对文件的结尾位置，值为2
    
    以文本方式打开的文件，只支持相对文件的起始位置。
"""

import os

with open('myfile2.txt', 'rb') as file:
    print(file.tell())  # 0

    # file.seek(3, os.SEEK_SET)
    # file.seek(3, 0)
    file.seek(3)
    print(file.tell())  # 3

    file.seek(4, os.SEEK_CUR)
    print(file.tell())  # 7

    file.seek(-2, os.SEEK_END)
    print(file.tell())  # 8

with open('myfile2.txt', 'r+') as file:
    print(file.tell())  # 0

    file.seek(3)
    print(file.tell())  # 3

    file.write('python')
    print(file.tell())  # 9
