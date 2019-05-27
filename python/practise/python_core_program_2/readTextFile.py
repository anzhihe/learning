#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 'readTextFile.py -- read and display text file'

# get filename
fname = raw_input('Enter file name: ')
print

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError, e:
    print "*** file open error:", e
else:
   for eachLine in fobj:
       print eachLine,
   fobj.close()
