#!/usr/bin/env python

import threading
from time import sleep, ctime

loops = [ 4, 2 ]

class ThreadFunc(object):

    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func, self.args)

def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()

def main():
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:	# create all threads
        t = threading.Thread(
	    target=ThreadFunc(loop, (i, loops[i]),
	    loop.__name__))
        threads.append(t)

    for i in nloops:	# start all threads
        threads[i].start()

    for i in nloops:	# wait for completion
        threads[i].join()

    print 'all DONE at:', ctime()

if __name__ == '__main__':
    main()
