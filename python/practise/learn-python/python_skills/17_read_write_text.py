#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    17_read_write_text.py
 @Function:    读写文本文件与处理二进制文件
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/9/5
"""

"""一、如何读写文本文件？"""

"""
实际案例：
    某文本文件编码格式已知(如UTF-8, GBK, BIG5),
    在python 2.x和python 3.x中分别如何读取该文件?
"""

"""
解决方案：
    字符串的语言发生变化：
    python2     python3
    -------------------
    str     →   bytes
    unicode →   str
    
    python 2.x：写入文件前对unicode编码，读入文件后对二进制字符串解码
    python 3.x：open函数指定't'的文本模式，encoding指定编码格式
"""

"""
    python 2.x 读写文件
"""

"""
f = open('py2.txt', 'w')
s = u'你好'
f.write(s.encode('gbk'))
f.close()

f = open('py2.txt', 'r')
t = f.read()
print t
print t.decode('gbk')
"""

"""
    python 3.x 读写文件
"""

# 默认't'模式，可以不写
with open('py3.txt', 'wt', encoding='utf8') as f:
    f.write('你好，世界')

with open('py3.txt', 'rt', encoding='utf8') as f:
    s = f.read()
    print(s)


"""二、如何处理二进制文件？"""

"""
实际案例：
    wav是一种音频文件的格式，音频文件为二进制文件.
    wav文件由头部信息和音频采样数据构成.前44个字节
    为头部信息,包括声道数，采样频率, PCM位宽等等,后面
    是音频采样数据. 
    
    使用python,分析一个wav文件头部信息，处理音频数据.
"""

"""
解决方案：
    1、open函数想以二进制模式打开文件，指定mode参数为'b'
    2、二进制数据可以用readinfo，读入到提前分配好的buffer中，便于数据处理
    3、解析二进制数据可以使用标准库中的struct模块的unpack方法
"""
import struct
import array

with open('boom.wav', 'rb') as f:
    info = f.read(44)
    print(info)

    # 音频文件声道数
    print(struct.unpack('h', info[22:24]))  # (1,)

    # 采样频率(int)
    print(struct.unpack('i', info[24:28]))  # (11025,)

    # 编码宽度
    print(struct.unpack('h', info[34:36]))  # (8,)

    # 读取数据部分
    # 修改文件指针，挪到末尾，得到文件大小
    f.seek(0, 2)
    print(f.tell())
    n = (f.tell() - 44) / 2
    buf = array.array('h', (0 for _ in range(n)))
    # 文件指针指向数据，把数据读入到到buffer中
    f.seek(44)
    f.readinto(buf)

    # 缩小采样，使声音变小
    for i in range(n):
        buf[i] / 8

    # 将数据写入到新声音文件中
    with open('demo.wav', 'wb') as f2:
        f2.write(info)
        # 将buffer中数据写入到文件中
        buf.tofile(f2)



