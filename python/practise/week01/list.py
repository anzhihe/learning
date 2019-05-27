#!/usr/bin/env python
# coding: utf8

languages = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']
cnt = 0
for l in languages:
    if l == 'js':
        cnt += 1

print 'js的次数：%s' % cnt
