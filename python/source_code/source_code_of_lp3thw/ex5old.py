# -- coding: utf-8 --
## 以下代码在py3下调试通过
my_name = "Zed A.Shaw"

my_age = 35 # not a lie

my_height = 74 #inches

my_weight = 180 #lbs

my_eyes = 'Blue' #注意：字符串内容可以选择单引号或者双引号。放在print函数后面加上括号就可以被打印出来。


my_teeth = 'White'

my_hair = 'Brown'


print ("Let's talk about %s ." % my_name) 

#格式化字符%s、%d。
# 只要将格式化的变量放到字符串中，再紧跟着一个百分号%，再紧跟着变量名即可。唯一要注意的地方，是如果你想要在字符串中通过格式化字符放入多个变量的时候，你需要将变量放到（）圆括号里，变量之间采用逗号，隔开。

print ("He's %d inches tall." % my_height) 

print ("He's %d pounds heavy." % my_weight) 

print ("Actually that's not too heavy.")

print ("He's got %s eyes and %s hair."  %(my_eyes,my_hair))#在pyhon3中将%号转移到括号之外，最左端，而且左右参数可以塞到一个括号里，右侧可以有两个括号。

print ("His teeth are usually %s depending on the coffee."  % my_teeth)

# this line is tricky,try to get it exactly right

print ("If I add %d,%d,and %d I get %d." %(my_age,my_height,my_weight,my_age+my_height + my_weight))
# 在26行受到32行的启发，知道了Py3下如何表示。
# 程序员喜欢用恼人的难度大简写来节约打字事件，我们尽早学会就可以读懂这些东西。


#Log
#本文件于20170928建立。
