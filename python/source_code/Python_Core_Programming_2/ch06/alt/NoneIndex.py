#!/usr/bin/python

s = 'abcde'

#for x,y in enumerate(s):
#    print s[x:], s[:x]
#for i in range(len(s), -1, -1):
    #print s[i:], s[:i], s[i::-1], s[:i:-1]

s = 'abcde'
for i in [None] + range(-1, -len(s), -1):
    print s[:i]

raw_input()
