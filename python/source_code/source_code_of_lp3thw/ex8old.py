formatter ="%r %r %r %r"
# 下面这个是4个数字按照上面这个样子的格式打出来。
print (formatter % (1,2,3,4)) # 经过py3改造的代码，原来是{print formatter % (1, 2, 3, 4)}这明显是不行的。
# 下面这四个英文单词是按照上面的既定格式打出来的。
print (formatter % ('one',"two","three","four"))#字符串里可以用单引号或者双引号，都是可以的。但是为什么打印出来的one two等是带单引号的呢？
print (formatter %(True,False,False,True))

print (formatter% (formatter,formatter,formatter,formatter))
# 注意：%号后看是给某个格式，提供素材的，
print (formatter %("I had this thing.","That you could type up right.","But it didn't sing.","So I said goodnight."))# 为什么倒数第二个是双引号？其他都是单引号？-作者提出了这个问题，当然我也发现了，但是经过观察和思考，我依然没有答案。



# LOG 20170929 测试通过。