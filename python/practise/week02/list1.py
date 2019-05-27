#!/usr/bin/env python
# coding: utf8

names = ['anzhihe', 'hehe', 'haha', 'nb']
name = raw_input('please input your name:')
exists = False
for _name in names:
    if _name == name:
        exists = True
        break

if exists:
    print "名字在列表里"
else:
    print "名字不在列表里"
