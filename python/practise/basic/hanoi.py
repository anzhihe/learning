#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def move(n, a='A', b='B', c='C'):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        print('move', a, '-->', c)
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')
