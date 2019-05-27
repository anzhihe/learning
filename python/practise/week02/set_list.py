#!/usr/bin/env python
# coding: utf8

arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]

comms = []

for num in arr1:
    if num in arr2 and num not in comms:
        print '%s是arr1和arr2共有的元素' % num
        comms.append(num)
print(comms)