#!/usr/bin/env python
# coding: utf8

while True:
    year = raw_input('Please input year:')
    if year == 'quit':
        break
    year = int(year)
    if year % 100 == 0 and year % 400 == 0:
        print '闰年'
    elif year % 100 != 0 and year % 4 == 0:
        print '闰年'
    else:
        print '非闰年'

