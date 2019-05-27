#!/usr/bin/env python
# coding: utf8

num_list = range(0,10)

'''
for i in range(0,len(num_list)/2):
    temp = num_list[i]
    num_list[i] = num_list[-1-i]
    num_list[-1-i] = temp
'''

for i in range(0,len(num_list)/2):
    num_list[i],num_list[-1-i] = num_list[-1-i],num_list[i]

print num_list