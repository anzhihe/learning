#!/usr/bin/env python

def foo():
    return True

def bar():
    'bar() does not do much'
    return True

foo.__doc__ = 'foo() does not do much'
foo.tester = '''
if foo():
    print 'PASSED'
else:
    print 'FAILED'
'''

for eachAttr in dir():
    obj = eval(eachAttr)
    if isinstance(obj, type(foo)):
	if hasattr(obj, '__doc__'):
	    print '\nFunction "%s" has a doc string:\n\t%s' % (eachAttr, obj.__doc__)
	if hasattr(obj, 'tester'):
	    print 'Function "%s" has a tester... executing' % eachAttr
	    exec obj.tester 
	else:
	    print 'Function "%s" has no tester... skipping' % eachAttr
    else:
	print '"%s" is not a function' % eachAttr
