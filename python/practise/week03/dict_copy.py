#!/usr/bin/env python
# coding: utf8

src_dict = {
    'a' : 1,
    'b' : 2,
    'c' : range(0, 10),
    'd' : {
        'name' : 'anzhihe',
        'age' : 18,
        'score' : 100
    }
}

dest_dict = {}

for key in src_dict:
    #key, src_dict[key]
    dest_dict[key] = src_dict[key]

print 'dest_dict: %s' % (dest_dict)

dest_dict2 = {}

for key,value in src_dict.items():
    dest_dict2[key] = value

print 'dest_dict2: %s' %(dest_dict2)


dest_dict3 = {}

dest_dict3 = dict(zip(src_dict.keys(), src_dict.values()))

print 'dest_dict3: %s' %(dict(zip(src_dict.keys(), src_dict.values())))


