#!/usr/bin/env python

def counter(start_at=0):
    count = start_at
    while True:
	val = (yield count)
	if val is not None:
	    count = val
	else:
	    count += 1

if __name__ == '__main__':
    print 'initializing counter to start counting at 5'
    count = counter(5)
    print 'calling count.next():', count.next()
    print 'calling count.next():', count.next()
    print 'calling count.send(9):', count.send(9)
    print 'calling count.next():', count.next()
    print 'calling count.close():', count.close()
    print 'calling count.next():', count.next()
