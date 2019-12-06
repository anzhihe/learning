# 让字符扩展到多行的方法一： 采用 \n 隔开，这是一个放入“新行”的作用。
# “转义序列(escape sequences)”-----\  and  \\ and ' ' and " "。
# 你需要告诉Python----- "I "understand" joe."   到底哪个是哪个的边界。——其实你是想让中间的“”也表达是 字符串，而不是真正的双引号。

# 方法1:" I am 6'2\" tall.' # 将 字符串中的“双引号”转意义了;'I am 6\'2" tall.'# 将 字符串中的单引号转意义了。

# 方法2: 使用三引号，在一组三引号"""之间放入任意多行文字。
tabby_cat ="\t I'm tabbed in."
persian_cat= "I'm split\non a line."#发现\n前面加空格对显示没有影响，但是右侧加空格确有很大影响  打印的时候怎个行都向右移动了。
backslash_cat = "I'm\\a\\cat."# 明明是打了双反斜杠，但是打印的时候就出现了一个反斜杠而已。

fat_cat="""

I'll do a list: # 这一行没有转义字符的时候就会靠最左侧。
\t* Cat food   # 发现了没有【\  t 】出来之后，其后面的字符都向中间对其。
\t* Fishies
\t* Catnip\n\t* Grass #Catnip和Grass本来是在一行的但是由于中间增加了一个转义字符【\  n】所以就另外起了一行文字。
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

# 转义序列和格式化字符串放到一起，可以创建一种更复杂的格式。

#%r 打印出来的是你写在脚本里的内容，而%s打印出来的是你应该看到的内容。
