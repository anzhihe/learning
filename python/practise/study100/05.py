#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''

# l = []
# for i in range(3):
#     x = int(raw_input('integer:\n'))
#     l.append(x)
# l.sort()
# print l


print(sorted([int(input("enter a integer: ")) for x in range(3)]))