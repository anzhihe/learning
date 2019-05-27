#!/bin/bash
# 与之前的例子相同, 但是... 

#  - 选项对于here docutment来说, 
#+ <<-可以抑制文档体前边的tab, 
#+ 而*不*是空格. 

cat &lt;&lt;-ENDOFMESSAGE
	This is line 1 of the message.
	This is line 2 of the message.
	This is line 3 of the message.
	This is line 4 of the message.
	This is the last line of the message.
ENDOFMESSAGE
# 脚本在输出的时候左边将被刷掉. 
# 就是说每行前边的tab将不会显示. 

# 上边5行"消息"的前边都是tab, 而不是空格. 
# 空格是不受<<-影响的. 

# 注意, 这个选项对于*嵌在*中间的tab没作用. 

exit 0
