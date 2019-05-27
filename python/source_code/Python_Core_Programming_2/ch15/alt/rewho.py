#!/usr/bin/env python

from os import popen                # import os.popen()
from re import split                # import re.split() [not string.split()]
from string import strip        # import string.strip()

f = popen('who', 'r')                # call the 'who' cmd and read from it

# read all output from 'who' and strip the leading & trailing whitespaces
for eachLine in map(strip, f.readlines()):
    print split('\s\s+|\t', eachLine)        # split on TAB or multiple SPACEs
f.close()                        # close input channel
