#!/usr/bin/env python

'readTextFile.py -- read and display text file'

# get filename
fname = raw_input('Enter file name: ')
print

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except IOError, e:
    print"*** file open error:", e
else:
    # display contents to the screen
    for eachLine in fobj:
        print eachLine,
    fobj.close()
