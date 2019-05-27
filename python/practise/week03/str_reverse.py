#!/usr/bin/env python
# coding: utf8

s = 'anzhihe'
l_str = list(s)
l_str.reverse()
print l_str
print ''.join(l_str)

ss = ''
for c in s:
    ss = c + ss

print ss
