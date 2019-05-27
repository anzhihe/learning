#!/bin/bash
# allprofs.sh: 打印所有用户的配置文件

# 由Heiner Steven编写, 并由本书作者进行了修改. 

FILE=.bashrc  #  在原始脚本中, File containing user profile,
              #+ 包含用户profile的是文件".profile". 

for home in `awk -F: '{print $6}' /etc/passwd`
do
  [ -d "$home" ] || continue    # 如果没有home目录, 跳出本次循环. 
  [ -r "$home" ] || continue    # 如果home目录没有读权限, 跳出本次循环. 
  (cd $home; [ -e $FILE ] && less $FILE)
done

#  当脚本结束时，不必使用'cd'命令返回原来的目录. 
#+ 因为'cd $home'是在子shell中发生的, 不影响父shell. 

exit 0
