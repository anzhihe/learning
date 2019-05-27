#!/usr/bin/env python
# coding: utf8

year = 0
rate = 0.033
money = 10000
while money <= 20000:
    money = money * (1 + rate)
    year += 1
print year
