print ( "Mary had a little lamb.")
print ("Its fleece was white as %s."%'snow')
print ("And everywhere that Mary went.")
print ("."*10)#what'd that do?

end1="C"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"
end7="B"
end8="u"
end9="r"
end10="g"
end11="e"
end12="r"
end0= " "# 我新加的一个字符串---“空格”

#watch that comma at the end. try removing it to see what happens.在Py3里，更改了逗号的位置（无论是括号内外都没有什么影响，都不能使得 英文的姓名 之间出现 空格）；但是
print (end1 + end2 + end3 + end4 + end5 + end6,) ,print (end7 + end8 + end9 + end10 + end11 +end12)

print ("------我们是有底线的------")
# 运行结果证明，我在两段文字之间加上空格字符串的方法是可以实现 原文py中的案例的。
print (end1 + end2 + end3 + end4 + end5 + end6+end0+end7 + end8 + end9 + end10 + end11 +end12)