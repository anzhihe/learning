#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
【程序12】
题目：判断101-200之间有多少个素数，并输出所有素数。
1.程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，
　　　　　　则表明此数不是素数，反之是素数。
'''

from math import sqrt

h = 0
leap = 1
for i in range(101,201):
    j = int(sqrt(i+1))
    for k in range(2,j+1):
        if i % k == 0:
            leap = 0
            break
    if leap == 1:
        print '%-4d' % i,
        h += 1
        if h % 10 == 0:
            print ''
    leap = 1
print 'The total is %d' % h