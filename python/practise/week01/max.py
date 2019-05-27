#!/usr/bin/env python
# coding: utf8

num_list = [-10, -2, -1, 0, 2, 11, 32, 148, 1, 20]
num_max = None
for num in num_list:
    if num_max is None:
        num_max = num
    elif num_max < num:
        num_max = num

print 'num_max in num_list is :%s' % num_max
