#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
'''

for i in range(1, 5):
    for j in range(1, 5):
        if (j==i) :
            continue;
        for k in range(1, 5):
            if (k==i or k==j):
                continue;
            print(i,j,k);

'''
list_num = [1,2,3,4]
list_add = [ i*100 + j*10 + k for i in list_num for j in list_num for k in list_num if (i != j and i != k and j != k)]
print len(list_add)
print list_add

'''


'''
from itertools import permutations

for i in permutations([1,2,3,4], 3):
    print(i)
'''

