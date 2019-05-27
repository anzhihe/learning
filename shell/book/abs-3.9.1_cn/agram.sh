#!/bin/bash
# agram.sh: 使用anagram来玩游戏. 

# 寻找anagram...
LETTERSET=etaoinshrdlu
FILTER='.......'       # 最少有多少个字母? 
#       1234567

anagram "$LETTERSET" | # 找出这个字符串中所有的anagram...
grep "$FILTER" |       # 至少需要7个字符, 
grep '^is' |           # 以'is'开头
grep -v 's$' |         # 不是复数(指英文单词的复数)
grep -v 'ed$'          # 不是过去时(也指英文单词)
# 可以添加许多种组合条件和过滤器. 

#  使用"anagram"工具, 
#+ 这是作者的"yawl"文字表软件包中的一部分. 
#  http://ibiblio.org/pub/Linux/libs/yawl-0.3.2.tar.gz
#  http://personal.riverusers.com/~thegrendel/yawl-0.3.2.tar.gz

exit 0                 # 代码结束. 


bash$ sh agram.sh
islander
isolate
isolead
isotheral



#  练习:
#  -----
#  修改这个脚本, 使其能够让LETTERSET作为命令行参数. 
#  将第11 - 13行的过滤器参数化(比如, 可以使用变量$FILTER), 
#+ 这样我们就可以根据传递的参数来指定功能. 

#  可以参考脚本agram2.sh, 
#+ 与这个例子稍微有些不同. 
