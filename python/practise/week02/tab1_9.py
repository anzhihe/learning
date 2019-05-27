#!/usr/bin/env python
# coding: utf8

for i in range(1, 10):
    for j in range(1, i + 1):
        print '%s * %s = %s' % (i, j, i * j),
    print ''