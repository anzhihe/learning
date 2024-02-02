sorted_list = sorted([30, 50, 20, 10, 40])
print(sorted_list)
# [10, 20, 30, 40, 50]


sorted_list2 = sorted(["a", str(1), "bb"])
print(sorted_list2)

list3 = ["a", "c", "bb"]
no_value = list3.sort()
print(list3)
print(no_value)

sorted_list4 = sorted([30, 50, 20, 10, 40], reverse=True)
print(sorted_list4[:3])
# [50, 40, 30, 20, 10]

students = [('Tom', 'M', '1005'), 
            ('Jerry', 'M', '1003'),
            ('shuke', 'M', '2003'), 
            ('Beta', 'M', '2001')]

print(sorted(students))
# 排序结果
# [('Beta', 'M', '2001'), 
# ('Jerry', 'M', '1003'), 
# ('Tom', 'M', '1005'), 
# ('shuke', 'M', '2003')]

print(sorted(students, key=lambda s: s[2]))
#  排序结果
# [('Jerry', 'M', '1003'), 
# ('Tom', 'M', '1005'), 
# ('Beta', 'M', '2001'), 
# ('shuke', 'M', '2003')]

def get_tuple_pos3(my_tuple):
    return my_tuple[2]

print(get_tuple_pos3(('Jerry', 'M', '1003')))

print(sorted(students, key=get_tuple_pos3))


student_dict1 = {'Jerry':'1003', 
                 'Tom':'1005', 
                 'Beta':'2001', 
                 'Shuke':'2003'
}
print(student_dict1.items())
# dict_items([('Jerry', '1003'), ('Tom', '1005'), ('Beta', '2001'), ('Shuke', '2003')])
print(sorted(student_dict1.items(), key=lambda d: d[0]))
# [('Beta', '2001'), ('Jerry', '1003'), ('Shuke', '2003'), ('Tom', '1005')]

result = sorted(student_dict1.items(), key=lambda d: d[1])
print(result)
[('Jerry', '1003'), ('Tom', '1005'), ('Beta', '2001'), ('Shuke', '2003')]
print(dict(result))
# {'Jerry': '1003', 'Tom': '1005', 'Beta': '2001', 'Shuke': '2003'}