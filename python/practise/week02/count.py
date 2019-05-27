#!/usr/bin/env python
# coding: utf8

chars = ['a', 'b', 'c', 'c', 'e', 'd', 'b', 'z', 'u', 'w',123, 1, 2]
char = raw_input("please input a char:")
count = 0

for c in chars:
    if c == char:
        count += 1

print "%s:%d" % (char, count)
