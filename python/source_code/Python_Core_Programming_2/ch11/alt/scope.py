#!/usr/bin/env python
# $Id$
#
# scope.py -- variable scope example
#

"""This script highlights some elements of variable scope
and how it relates to Python programming.  Global and local
variables and the changing of their values are used to
illustrate which variables are active in various execution
scopes.

main() contains global variables and calls proc1() and proc2().
"""

j, k = 1, 2                # global


def proc1():               # proc1()
    "proc1() includes local variables"

    j, k = 3, 4            # local
    
    print "j == %d and k == %d" % (j, k)

    k = 5


def proc2():               # proc2()
    'proc2() includes a local variable and calls proc1()'

    #global j              # use global not local 'j'
    j = 6                  # local

    proc1()

    print "j == %d and k == %d" % (j, k)


k = 7

proc1()

print "j == %d and k == %d" % (j, k)

j = 8

proc2()

print "j == %d and k == %d" % (j, k)
