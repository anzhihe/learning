#!/usr/bin/env python
# coding: utf8


src = 'anzhihe:18,chegva:2,hehe:3,haha:4'

rt_list = []

for user in src.split(','):
    name,age = user.split(':')
    rt_list.append((name,int(age)))

print rt_list
