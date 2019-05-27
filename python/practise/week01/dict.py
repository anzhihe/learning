#!/usr/bin/env python
# coding: utf8

langs = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']

langs_dict = {}
for lang in langs:
    if lang not in langs_dict:
        langs_dict[lang] = 1
    else:
        langs_dict[lang] += 1

print langs_dict