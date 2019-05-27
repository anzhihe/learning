#!/usr/bin/env python
# $Id$
#
# gendata.py -- generates test data
#
# created on 00/05/19 by wesc
#

from random import randint, choice
from time import ctime
from sys import maxint                        # (value, not function)
from string import lowercase
from os.path import exists

doms = ( 'com', 'edu', 'net', 'org', 'gov' )

def main():

    # this long version saves output to files which
    # can be directly used with regular expressions
    # (it does not write the strings to the screen)

    # open new test file
    i = 0
    fn = '/tmp/data%d.txt' % i
    while exists(fn):
        i = i + 1
        fn = '/tmp/data%d.txt' % i
    f = open(fn, 'w')

    # write test data and close file
    for i in range(randint(5, 10)):

        # randomly choose a date integer and
        # calculate the corresponding date string
        dtint = randint(0, maxint-1)
        dtstr = ctime(dtint)

        # the login should be between 4 and 7 chars in length;
        # the domain should be 
        loginlen = randint(4, 7)
        login = ''
        for j in range(loginlen):
            login = login + choice(lowercase)

        domainlen = randint(loginlen, 12)
        dom = ''
        for j in range(domainlen):
            dom = dom + choice(lowercase)
        f.write('%s:%s@%s.%s:%d-%d-%d\n' % (dtstr, login,
            dom, choice(doms), dtint, loginlen, domainlen))

    # close test file
    f.close()

if __name__ == '__main__':
    main()
