#!/usr/bin/env python

from time import ctime, sleep

'''
def counter(func):
    if not hasattr(func, 'ncalls'):
        print '*** initializing ctr'
        func.ncalls = [0]
    def wrappedFunc():
        func.ncalls[0] += 1
        print '*** incrementing ctr to', func.ncalls
        print 'INSIDE: id(func) =', id(func)
        return func()
    print 'id(func) =', id(func)
    print 'id(wrappedfunc) =', id(wrappedFunc)
    wrappedFunc.ncalls = func.ncalls
    return wrappedFunc
'''

def tsfunc(func):
    def wrappedFunc():
        print '[%s] %s() called' % (
            ctime(), func.__name__)
        return func()
    return wrappedFunc

@tsfunc
def foo():
    pass

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()

'''
#exer
update example XXX to:
- write the timestamp to a logfile instead of screen output
- time how long it takes to exec the given function, i.e., see the timeit() exercise above
- create a function registry:
    track the number of functions which have registered with your system,
    how many times those functions have been called,
    and what are the avg time of each execution and total time of execution

- write a memoizer... for small recursive functions or just for simple functions that are called a lot, cache the results given a set of arguments (must be hashable, i.e, immutable objects), so that if the same function is called again with the same args, then just return the previously saved value instead of (re)running the function from scratch.  There are many examples online (use a search engine), so that even if you are inspired by an existing piece of code, customize that code by making an improvement that is truly your own.

'''
