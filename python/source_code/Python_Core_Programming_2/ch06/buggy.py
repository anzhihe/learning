#!/usr/bin/env python

#
import string

#
while 1:

    #
    num_str = raw_input('Enter a number: ')

    #
    try:
        #
        num_num = string.atoi(num_str)

        #
        break

    #
    except ValueError:
        print "invalid input... try again"

#
fac_list = range(1, num_num+1)
print "BEFORE:", `fac_list`

#
i = 0

#
while i < len(fac_list):

    #
    if num_num % fac_list[i] == 0:
        del fac_list[i]

    #
    i = i+1

#
print "AFTER:", `fac_list`
