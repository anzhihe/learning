#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    07_history_record.py
 @Function:    实现历史记录功能
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/8/26
"""


"""如何实现用户的历史记录功能(最多n条)"""

"""
实际案例：
    很多应用程序都有浏览用户的历史记录的功能，
    例如:
    浏览器可以查看最近访问过的网页.
    视频播放器可以查看最近播放过视频文件.
    Shell可以查看用户输入过的命令.
    ......
    制作了一个简单的猜数字的小游戏，
    添加历史记录功能，显示用户最近猜过的数字，
    如何实现?
"""

"""
解决方案：
    使用容量为n的队列存储历史记录
    1.使用标准库collections中的deque，它是一个双端循环队列
    2.程序退出前，可以使用pickle将队列对象存入文件，再次运行程序时将其导入
"""

from random import randint
from collections import deque
import pickle

N = randint(0, 100)

# 最多记录最近5次输入
history = deque([], 5)

def guess(k):
    if k == N:
        print('right')
        return True
    if k < N:
        print('%s is less-than N' % k)
    else:
        print('%s is greater-than N' % k)

    return False

while True:
    line = input("please input a number: ")
    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print(list(history))
    elif line == 'dump':
        pickle.dump(history, open('history.txt', 'wb'))
    elif line == 'load':
        print(pickle.load(open('history.txt', 'rb')))