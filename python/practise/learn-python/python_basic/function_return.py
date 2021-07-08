#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @FileName:    function_return.py
 @Function:    python function return
 @Author:      Zhihe An
 @Site:        https://chegva.com
 @Time:        2021/7/4
"""

"""一、函数的定义之多个返回值"""

"""
    如果需要在调用函数后有多个返回值，可以在定义函数时在函数体内使用return语句返回由多个返回值组成的元组
"""

# 把列表中的所有数分成奇数和偶数两类
def classify_numbers(numbers):
    odds = []
    evens = []

    # 使用列表生成式之if-else
    # [odds.append(number) if number % 2 else evens.append(number) for number in numbers]

    for number in numbers:
        if number % 2:
            odds.append(number)
        else:
            evens.append(number)

    return odds, evens

print(classify_numbers([15, 86, 39, 26, 53, 68]))   # ([15, 39, 53], [86, 26, 68])

# 查找列表中的最小值和最大值
def lookup_min_max(numbers):
    if len(numbers) == 0:
        return

    min_num = max_num = numbers[0]

    for number in numbers[1:len(numbers)]:
        if number < min_num:
            min_num = number
        elif number > max_num:
            max_num = number

    return min_num, max_num

print(lookup_min_max([35, 26, 19, 86, 93, 68])) # (19, 93)