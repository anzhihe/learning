#!/usr/bin/env python

def simpleGen():
    yield 1
    yield '2 --> punch!'

if __name__ == '__main__':
    for item in simpleGen():
	print item
