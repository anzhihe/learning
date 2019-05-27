#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
【程序10】
题目：打印楼梯，同时在楼梯上方打印两个笑脸。
1.程序分析：用i控制行，j来控制列，j根据i的变化来控制输出黑方格的个数。
'''


import sys
sys.stdout.write(chr(1))
sys.stdout.write(chr(1))
print ''

for i in range(1,11):
    for j in range(1,i):
        sys.stdout.write(chr(219))
        sys.stdout.write(chr(219))
    print ''