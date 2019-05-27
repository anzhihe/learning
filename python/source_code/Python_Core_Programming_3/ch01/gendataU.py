#!/usr/bin/env python

from distutils.log import warn as printf
from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime

tlds = ( 'com', 'edu', 'net', 'org', 'gov' )

if hasattr(__builtins__, 'xrange'):
    myrng = xrange
else:
    myrng = range

for i in myrng(randrange(5, 11)):
    dtint = randrange(2**32)    # pick date
    dtstr = ctime(dtint)        # date string
    llen = randrange(4, 7)      # login is shorter
    login = ''.join(choice(lc) for j in myrng(llen))
    dlen = randrange(llen, 13)  # domain is longer
    dom = ''.join(choice(lc) for j in myrng(dlen))
    printf('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,
        dom, choice(tlds), dtint, llen, dlen))
