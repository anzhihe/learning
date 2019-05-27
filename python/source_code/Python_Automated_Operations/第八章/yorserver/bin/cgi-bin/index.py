#!/usr/bin/env python
#coding=utf-8
print "Content-type: text/html\n\n";
print "<html><head><title>Python冒泡排序测试</title></head><body>"
my_list = [23,45,67,3,56,82,24,23,5,77,19,33,51,99]

def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i+1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]

bubble(my_list)
print my_list
print "</body></html>"
