#!/usr/bin/env python

def displayNumType(num):
    print num, 'is',
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all!!'

displayNumType(-69)
displayNumType(9999999999999999999999L)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xxx')
