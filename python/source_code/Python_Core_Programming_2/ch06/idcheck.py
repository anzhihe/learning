#!/usr/bin/env python

import string

alphas = string.letters + '_'
nums = string.digits

print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
inp = raw_input('Identifier to test? ')

if len(inp) > 1:

    if inp[0] not in alphas:
        print '''invalid: first symbol must be
	  alphabetic'''
    else:
        for otherChar in inp[1:]:

            if otherChar not in alphas + nums:
                print '''invalid: remaining
		  symbols must be alphanumeric'''
                break
        else:
            print "okay as an identifier"
