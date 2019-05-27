#!/usr/bin/env python
# coding: utf8


temp_dict = {'teach':'pc','waihao':'pc','name':'pc','age':12,'job':'IT'}

rt_dict = {}
#{a : 1, b : 1, c :1}


for key, value in temp_dict.items():
    _rvalue = rt_dict.get(value)
    if _rvalue is None:
        rt_dict[value] = key
    elif isinstance(_rvalue, list):
        _rvalue.append(key)
    else:
        rt_dict[value] = [_rvalue, key]

print rt_dict