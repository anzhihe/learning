#!/usr/bin/env python

from random import randint, choice
from string import lowercase        
from sys import maxint
from time import ctime

doms = ( 'com', 'edu', 'net', 'org', 'gov' )
    
for i in range(randint(5, 10)):
    dtint = randint(0, maxint-1) # pick date
    dtstr = ctime(dtint)        # date string

    shorter = randint(4, 7)        # login shorter
    em = ''
    for j in range(shorter):        # generate login
        em += choice(lowercase)

    longer = randint(shorter, 12) # domain longer
    dn = ''
    for j in range(longer):         # create domain
        dn += choice(lowercase)

    print '%s::%s@%s.%s::%d-%d-%d' % (dtstr, em,
        dn, choice(doms), dtint, shorter, longer)
