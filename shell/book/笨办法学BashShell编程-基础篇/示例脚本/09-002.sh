#!/bin/bash
# 代码风格示例

fl=`ls -al $dirname`                 # 含义模糊. 
file_listing=`ls -al $dirname`       # 更好的名字. 

MAXVAL=10   # 使用变量来代替脚本常量, 并且在脚本中都是用这个变量. 
if [ "$index" -le "$MAXVAL" ]; then
  # ...
fi

E_NOTFOUND=75                        #  错误码使用大写, 用"E_"作为前缀
if [ ! -e "$filename" ]; then
  exit $E_NOTFOUND
fi  

MAIL_DIRECTORY=/var/spool/mail/bozo  # 环境变量名使用大写
export MAIL_DIRECTORY

GetAnswer ()                         # 函数名采用大小写混合的方式
{
  read answer
  return $answer
}  

_uservariable=23                     #  不推荐使用下划线开头的命令方法 


