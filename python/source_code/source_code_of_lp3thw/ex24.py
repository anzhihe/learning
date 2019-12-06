print("Let's practice everything.")
print('You\'d need to know \'bout escape with \\ that do:') #反斜杠是用来转换意义的\'是把单引号的公式功能注释掉，只保留纯意义上的字符，免得造成引用混乱。
print("You'd need to know about escape with \\ that do:")
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""
# 上面可以看到\t这个转意字符的作用是在一段文字前面加一个tab
print("-------------")
print(poem)
print("-------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):#这里started算是函数的一个种子。
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars /100
    return jelly_beans, jars, crates #一个函数返回多个变量。


start_point = 10000 #设置好种子的数值；注意这里将started这个参数替换为了start_point，具体叫啥名字都行.
beans, jars, crates = secret_formula(start_point) #将种子通过函数计算的结果分别赋予了3个变量，只不过这里新起了个变量名beans就是函数里的jelly_beans。

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))#在字符串中引用变量的方法2.
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print ("We'd have {} beans, {} jars, and {} crates.".format(*formula))#在字符串中可以这样引用一组格式的变量。变量数要相等？
print ("We'd have {} beans, {} jars, and 23 crates.".format(*formula))#减少变量测试,结果是前两个{}可以有效承接变量。
# print ("We'd have {} beans, {} jars, and {} crates，and {} crazy.".format(*formula))#增加变量测试。结果是增加的{}无法有效承接变量。
