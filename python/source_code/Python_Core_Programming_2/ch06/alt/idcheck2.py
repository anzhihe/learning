#!/usr/bin/env python

from keyword import kwlist
import string

ALPHAS = string.ascii_letters + '_'
NUMS = string.digits

def main():
    print 'Welcome to the Identifier Checker v2.0'
    myInput = raw_input('Identifier to test? ').strip()

    if len(myInput) == 0:
	print "ERROR: no identifier candidate entered"
	return

    if myInput in kwlist:
	print "ERROR: %r is a keyword" % myInput
	return

    alnums = ALPHAS + NUMS
    for i, c in enumerate(myInput):
	if i == 0 and c not in ALPHAS:
	    print 'ERROR: first symbol must be alphabetic'
	    break
	if c not in alnums:
	    print 'ERROR: remaining symbols must be alphanumeric'
	    break
    else:
	print "okay as an identifier"

if __name__ == '__main__':
    main()
