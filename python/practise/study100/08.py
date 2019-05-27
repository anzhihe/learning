#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
【程序8】
题目：输出9*9口诀。
1.程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
'''
from __future__ import print_function

for i in range(1,10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j),end='')
    print()
