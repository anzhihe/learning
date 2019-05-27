#!/usr/bin/env python
# coding: utf8

total = 0
value = 0
cnt = 0
while value != 'pc':
    total += int(value)
    cnt += 1
    value = raw_input("Please input your number:")

if cnt == 0:
    print 'total: %s, avg:0' % total
else:
    print 'total: %s, avg: %s' % (total, total * 1.0 / cnt)
