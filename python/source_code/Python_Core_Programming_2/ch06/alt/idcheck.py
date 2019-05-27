#!/usr/bin/env python
'''
$Id$

idcheck.py -- checks identifiers for validity

This application is limited in that it currently only supports
checking identifiers with length > 1 (does not process identifiers
of length greater than 1.  This application also does not recognize
do keywords.

Exercise:

    6-2) update this script to process identifiers of length 1
        as well as recognizing keywords as invalid identifiers
        (for use by the programmer; they are valid Python
        identifiers otherwise).
'''

import string        # string utility module

# create alphabet and number sets
alphas = string.letters + '_'
nums = string.digits

# salutation message and input prompt
print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
inp = raw_input('Identifier to test? ')

# only take action for identifiers with length > 1
if len(inp) > 1:

    # first character must be alphabetic
    if inp[0] not in alphas:
        print 'invalid: first symbol must be alphabetic'

    # remaning characters can be alphanumeric
    else:
        for otherChar in inp[1:]:
            if otherChar not in alphas + nums:
                print 'invalid: remaining symbols must be alphanumeric'
                break
        else:
            print "okay as an identifier"
else:
    print 'invalid: length must be > 1'
