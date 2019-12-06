formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format("Try your","Own text here","Maybe a poem","Or a song about fear"
))

'''
运行后显示
itifadeMacBook-Pro:LP3THW yyy$ python ex8.py
1 2 3 4
one two three four
True False False True
{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}
Try your Own text here Maybe a poem Or a song about fear
# 关于formatter = "{} {} {} {}" 这个格式的理解还不是很好。
'''
