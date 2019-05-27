#!/bin/bash
# alias.sh

shopt -s expand_aliases
# 必须设置这个选项, 否则脚本不会打开别名功能. 


# 首先, 来点有趣的. 
alias Jesse_James='echo "\"Alias Jesse James\" was a 1959 comedy starring Bob Hope."'
Jesse_James

echo; echo; echo;

alias ll="ls -l"
# 可以使用单引号(')或双引号(")来定义一个别名. 

echo "Trying aliased \"ll\":"
ll /usr/X11R6/bin/mk*   #* 别名工作了. 

echo

directory=/usr/X11R6/bin/
prefix=mk*  # 看一下通配符会不会引起麻烦. 
echo "Variables \"directory\" + \"prefix\" = $directory$prefix"
echo

alias lll="ls -l $directory$prefix"

echo "Trying aliased \"lll\":"
lll         # 详细列出/usr/X11R6/bin目录下所有以mk开头的文件. 
# 别名能处理连接变量 -- 包括通配符 -- o.k. 




TRUE=1

echo

if [ TRUE ]
then
  alias rr="ls -l"
  echo "Trying aliased \"rr\" within if/then statement:"
  rr /usr/X11R6/bin/mk*   #* 产生错误信息! 
  # 别名不能在混合结构中使用. 
  echo "However, previously expanded alias still recognized:"
  ll /usr/X11R6/bin/mk*
fi  

echo

count=0
while [ $count -lt 3 ]
do
  alias rrr="ls -l"
  echo "Trying aliased \"rrr\" within \"while\" loop:"
  rrr /usr/X11R6/bin/mk*   #* 这里, 别名也不会扩展. 
                           #  alias.sh: line 57: rrr: command not found
  let count+=1
done 

echo; echo

alias xyz='cat $0'   # 脚本打印自身内容. 
                     # 注意是单引号(强引用). 
xyz
#  虽然Bash文档建议, 它不能正常运行, 
#+ 不过它看起来是可以运行的. 
#
#  然而, 就像Steve Jacobson所指出的那样, 
#+ 参数"$0"立即扩展成了这个别名的声明. 

exit 0
