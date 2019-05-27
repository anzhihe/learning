#!/usr/bin/env python

from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime

tlds = ( 'com', 'edu', 'net', 'org', 'gov' )

for i in range(randrange(5, 11)):
    dtint = randrange(2**32)	# random date
    dtstr = ctime(dtint)	# date string
    llen = randrange(4, 7)	# login llen
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)	# domain dlen
    dom = ''.join(choice(lc) for j in range(dlen))
    print '%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,
        dom, choice(tlds), dtint, llen, dlen)
