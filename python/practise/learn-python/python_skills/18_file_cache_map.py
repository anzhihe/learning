#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    18_file_cache_map.py
 @Function:    设置文件缓冲、将文件映射到内存中
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/9/5
"""

"""一、如何设置文件的缓冲？"""

"""
实际案例：
    将文件内容写入到硬件设备时，使用系统调用,这类
    I/O操作的时间很长，为了减少I/O操作的次数,文件
    通常使用缓冲区.(有足够多的数据才进行系统调用)
    文件的缓冲行为，分为全缓冲，行缓冲，无缓冲.
    
    如何设置python中文件对象的缓冲行为?
"""

"""
解决方案：
    全缓冲：open函数的buffering设置为大于1的整数n，n为缓冲区大小
    行缓冲：open函数的buffering设置为1
    无缓冲：open函数的buffering设置为0
"""


# 全缓冲
f = open('demo1.txt', 'w', buffering=2048)
# tail -f demo1.txt观察
f.write('+' * 1024)
f.write('+' * 1023)
# 大于缓冲区大小，能看到demo1.txt文件被写入
f.write('-' * 2)

# 行缓冲
f = open('demo2.txt', 'w', buffering=1)
# tail -f demo2.txt观察
f.write('abc')
f.write('123')
# 写入\n后，可以看到文件输出
f.write('\n')
f.write('xyz\n')

# 无缓冲，python3中文本I/O无缓冲被禁用，使用二进制格式
f = open('demo3.txt', 'wb', buffering=0)
# 写入立即会显示
f.write(b'a')
f.write(b'1')


"""二、如何将文件映射到内存？"""

"""
实际案例：
    1.在访问某些二进制文件时，希望能把文件映射到内存中，可以
    实现随机访问.(framebuffer设备文件)
    
    2.某些嵌入式设备,寄存器被编址到内存地址空间，我们可以映
    射/dev/mem某范围，去访问这些寄存器.
    
    3.如果多个进程映射同一个文件,还能实现进程通信的目的.
"""

"""
解决方案：
    使用标准库中mmap模块的mmap()函数，它需要一个打开文件描述符作为参数
"""

import mmap

# dd if=/dev/zero of=demo.bin bs=1024 count=1024

f = open('demo.bin', 'r+b')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

print(m[0])         # 0
print(m[10:20])     # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

m[0] = 88

"""
od -x demo.bin                                                        
0000000      0058    0000    0000    0000    0000    0000    0000    0000
0000020      0000    0000    0000    0000    0000    0000    0000    0000
*
4000000
"""
