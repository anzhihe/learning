#!/usr/bin/env python
# $Id: twrapme.py,v 1.1 2000/06/02 08:14:55 wesc Exp $
#
# twrapme.py -- another simple wrapping example
#
# created on 00/04/26 by wesc
#

from time import time, ctime	# import time.time(), time.ctime()

class TimedWrapMe:

    # constructor, sets data item to wrap and
    # updates create, modify, and access times
    def __init__(self, obj):
        self.__data = obj
        self.__ctime = self.__mtime = self.__atime = time()

    # sets new data value, updates modify and access times
    def set(self, obj):
        self.__data = obj
        self.__mtime = self.__atime = time()

    # gets current data value, updates access time
    def get(self):
        self.__atime = time()
        return self.__data

    # get request time value
    def gettimeval(self, t_type):
        if type(t_type) != type('') or t_type[0] not in 'cma':
            raise TypeError, "gettime() requires argument of 'c', 'm', or 'a'"
        return eval('self._%s__%stime' % (self.__class__.__name__, t_type[0]))

    # get request time string
    def gettimestr(self, t_type):
        return ctime(self.gettimeval(t_type))

    # repr() and `` call this
    def __repr__(self):
        self.__atime = time()
        return `self.__data`

    # str() calls this
    def __str__(self):
        self.__atime = time()
        return str(self.__data)

    # delegate all other functionality to object's native methods
    def __getattr__(self, attr):
        self.__atime = time()
        return getattr(self.__data, attr)
