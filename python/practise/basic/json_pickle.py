#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#Json: dumps、dump、loads、load
#pickle: dumps、dump、loads、load

#import pickle

data = {'k1':123,'k2':'hello'}

# p_str = pickle.dumps(data)
# print(p_str)


# with open('/tmp/test','wb') as fp:
#     pickle.dump(data,fp)

import json
j_str = json.dumps(data)
print(j_str)

with open('/tmp/test','w') as fp:
    json.dump(data,fp)
