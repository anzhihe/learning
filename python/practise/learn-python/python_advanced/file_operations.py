#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    file_operations.py
 @Function:    python文件操作之打开文件与读文件
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/20
"""

"""一、打开文件"""

"""
    把数据存储到文件中是数据存储的方式之一。
    如何将数据写入文件，并将写入到文件中的数据读取出来呢？

    读写文件之前，必须先打开文件。
    内置函数open()用于打开文件，
        第一个参数是文件的路径，必须要指定。既可以指定绝对路径，也可以指定相对路径。
        第二个参数是文件的打开方式，默认值是'r'，表示以只读方式打开。
        其它参数都是带默认值的，可参考官方文档。
        函数的返回值是一个文件对象，通过该对象就可以操作文件了，例如：读文件、写文件、关闭文件等。
"""
# file = open('myfile.txt')
# file = open('myfile.txt', 'r')
# file = open('myfile2.txt')

# file = open('myfile.txt', 'w')
# file = open('myfile2.txt', 'w')

# file = open('myfile.txt', 'a')
# file = open('myfile2.txt', 'a')

# file = open('myfile.txt', 'x')
# file = open('myfile2.txt', 'x')

# file = open('myfile.txt', 'r+')
# file = open('myfile2.txt', 'r+')


"""二、读文件"""

"""
    读文件之前，必须先打开文件。
    可以调用内置函数open()并以只读方式或读写方式打开文件。返回的文件对象有三个用于读文件的方法:
    
1. read([size])
    如果不传参数，读到文件尾。
    如果传入参数，size用于指定字节数,
        当指定的字节数小于读到文件尾的字节数时，读取指定的字节数;
        当指定的字节数大于读到文件尾的字节数时，或当指定的字节数小于0，读到文件尾。
    
    如果文件较大，调用read()一次性读取整个文件会导致内存占用较大，因此，最好多次调用read(size)。
    指定的size不要超过默认缓冲区的大小，否则，可能并不能读取到指定的字节数。通过标准库中模块io
的属性DEFAULT_ BUFFER_ SIZE可以查看默认缓冲区的大小。
"""

"""
>>> import io
>>> io.DEFAULT_BUFFER_SIZE
8192    

>>> file = open('myfile.txt')
>>> file.read()
'1234567890\nabcdefghijklmn\nopqrstuvwxyz'
>>> file.close()    # 文件在使用完毕后必须要关闭

>>> file = open('myfile.txt')
>>> file.read(12)
'1234567890\na'
>>> file.read(30)   # 因为没有关闭文件，所以继续读取
'bcdefghijklmn\nopqrstuvwxyz'
>>> file.close()

>>> file = open('myfile.txt')
>>> file.read(12)
'1234567890\na'
>>> file.read(-5)
'bcdefghijklmn\nopqrstuvwxyz'
>>> file.close()
"""

"""
2. readline([size])
    如果不传参数，读到行尾。
    如果传入参数，size用于指定字节数，
        当指定的字节数小于读到行尾的字节数时，读取指定的字节数;
        当指定的字节数大于读到行尾的字节数时，或当指定的字节数小于0，读到行尾。
    总之，最多读到行尾。
"""

"""
>>> file = open('myfile.txt')
>>> file.readline()
'1234567890\n'
>>> file.readline(7)
'abcdefg'
>>> file.readline(10)
'hijklmn\n'
>>> file.readline(3)
'opq'
>>> file.readline(-5)
'rstuvwxyz'
>>> file.close()
"""

"""
3. readlines([size])
    如果不传参数，读到文件尾，返回每一行组成的列表。
    如果传入参数，size用于指定字节数,
        当指定的字节数小于读到文件尾的字节数时，一直读取到最后一个字符所在行的行尾;
        当指定的字节数大于读到文件尾的字节数时，或当指定的字节数小于0，读到文件尾。

    如果文件较大，调用readlines()一次性读取整个文件会导致内存占用较大，因此，最好多次调用
readlines(size)。
    指定的size不要超过默认缓冲区的大小。
"""

"""  
>>> file = open('myfile.txt')
>>> file.readlines()
['1234567890\n', 'abcdefghijklmn\n', 'opqrstuvwxyz']
>>> file.close()

>>> file = open('myfile.txt')
>>> file.readlines(8)
['1234567890\n']
>>> file.readlines(50)
['abcdefghijklmn\n', 'opqrstuvwxyz']
>>> file.close()
>>> file = open('myfile.txt')
>>> file.readlines(8)
['1234567890\n']
>>> file.readlines(-5)
['abcdefghijklmn\n', 'opqrstuvwxyz']
>>> file.close()    
"""