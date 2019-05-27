#!/usr/bin/env python
# $Id: capOpen.py,v 1.1 2000/07/01 23:10:01 wesc Exp $
#
# capOpen.py -- short delegation example with files
#
# created on 00/06/01 by wesc
#

from string import upper	# import string.upper()

class capOpen:

    # constructor
    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    # str() calls this
    def __str__(self):
        return str(self.file)

    # repr() and `` call this
    def __repr__(self):
        return `self.file`

    # implement/override write() (which calls the real write())
    def write(self, line):
        self.file.write(upper(line))

    # delegation happens here, i.e., delegate all other methods
    def __getattr__(self, attr):
        return getattr(self.file, attr)
