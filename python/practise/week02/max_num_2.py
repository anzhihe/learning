#!/usr/bin/env python
# coding: utf8

num_list = [1, 2, 3, 2, 110, 9]
right = None
left = None
for num in num_list:
    if right is None:
        right = num
    elif right < num:
        left = right
        right = num
    elif left is None:
        left = num
    elif left < num:
        left = num

print right,left
