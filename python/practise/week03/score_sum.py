#!/usr/bin/env python
# coding: utf8

users = [
    {'name' : 'kk', 'score' : [61, 72, 80]},
    {'name' : 'kk2', 'score' : [52, 62, 60]},
    {'name' : 'kk3', 'score' : [43, 81, 64]},
    {'name' : 'kk4', 'score' : [64, 75, 65]},
    {'name' : 'kk5', 'score' : [75, 95, 66]},
    {'name' : 'kk6', 'score' : [82, 80, 72]},
    {'name' : 'kk7', 'score' : [61, 72, 90]},
    {'name' : 'kk8', 'score' : [82, 52, 73]},
    {'name' : 'kk9', 'score' : [73, 71, 74]},
    {'name' : 'kk10', 'score' : [64, 95, 85]},
    {'name' : 'kk11', 'score' : [65, 85, 66]},
    {'name' : 'kk12', 'score' : [92, 70, 82]},
]

scores = {}
for user in users:
    for i in range(0, 3):
        key = (i, user['score'][i] / 10)
        scores[key] = scores.get(key, 0) + 1


rt_list = []
class_names = {0 : 'math', 1 : 'chinese', 2 : 'english'}
for key, value in scores.items():
    #key = (课程, 分数区间)
    #value = 次数
    rt_list.append((class_names[key[0]], '%s0-%s9' % (key[1], key[1]), value))

print rt_list
