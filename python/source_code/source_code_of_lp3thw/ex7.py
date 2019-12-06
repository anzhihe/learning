print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))#一个字符串中用{}作为占位符，这个占位符的格式是.format()来表示的。
print("And everywhere that Mary went.")
print("." * 10) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.try removing it to see what h
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)# 为什么打印出来的不是另外起一行。

'''
itifadeMacBook-Pro:LP3THW yyy$ python ex7.py
Mary had a little lamb.
Its fleece was white as snow.
And everywhere that Mary went.
..........
Cheese Burger

'''
