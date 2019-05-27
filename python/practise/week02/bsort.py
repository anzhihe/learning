#!/usr/bin/env python
# coding: utf8

num_list = [25, 12, 45, 56, 56, 56, 4, 69]

cnt = 0
for j in range(0, len(num_list) - 1):
    for i in range(0, len(num_list) - 1):
        cnt += 1
        if num_list[i] > num_list[i + 1]:
            num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
    #print '将第%s个人排序到最后的结果为:\n%s' % ((j + 1), num_list)
print '第一次'
print num_list
print '%s次' % cnt

cnt = 0
num_list = [25, 12, 45, 56, 56, 56, 4, 69]
for j in range(0, len(num_list) - 1):
    for i in range(0, len(num_list) - 1 - j):
        cnt += 1
        if num_list[i] > num_list[i + 1]:
            num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
    #print '将第%s个人排序到最后的结果为:\n%s' % ((j + 1), num_list)
print '第二次'
print num_list
print '%s次' % cnt