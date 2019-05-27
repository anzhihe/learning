#!/usr/bin/env python

from random import randrange as rr

def randGen(aList):
    while aList:
	yield aList.pop(rr(len(aList)))

if __name__ == '__main__':
    for item in randGen(['rock', 'paper', 'scissors']):
	print item
