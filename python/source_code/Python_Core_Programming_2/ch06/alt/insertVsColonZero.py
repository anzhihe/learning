#!/usr/bin/python

from time import time
REPS = 17500

def insert():
    m = [None]
    i = 0
    now = time()
    while i < REPS:
	m.insert(0, i)
	i += 1
    print 'Elapsed (insert):', time() - now

def colonZero():
    m = [None]
    i = 0
    now = time()
    while i < REPS:
	m[:0] = [i]
	i += 1
    print 'Elapsed (colon-0):', time() - now

def main():
    insert()
    colonZero()

if __name__ == '__main__':
    main()
    raw_input()
