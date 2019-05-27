#!/bin/bash
# logon.sh: 一个检查你是否在线的脚本, 这个脚本实现的很简陋. 

umask 177  # 确保temp文件并不是所有用户都有权限访问. 


TRUE=1
LOGFILE=/var/log/messages
#  注意: $LOGFILE必须是可读的
#+ (使用root身份来执行, chmod 644 /var/log/messages).
TEMPFILE=temp.$$
#  使用脚本的进程ID, 来创建一个"唯一"的临时文件名. 
#     也可以使用'mktemp'. 
#     比如: 
#     TEMPFILE=`mktemp temp.XXXXXX`
KEYWORD=address
#  登陆时, 把"remote IP address xxx.xxx.xxx.xxx"
#                      添加到/var/log/messages中. 
ONLINE=22
USER_INTERRUPT=13
CHECK_LINES=100
#  日志文件有多少行需要检查. 

trap 'rm -f $TEMPFILE; exit $USER_INTERRUPT' TERM INT
#  如果脚本被control-c中途中断的话, 那么就清除掉临时文件. 

echo

while [ $TRUE ]  #死循环. 
do
  tail -$CHECK_LINES $LOGFILE> $TEMPFILE
  #  将系统日志文件的最后100行保存到临时文件中. 
  #  这么做很有必要, 因为新版本的内核在登陆的时候, 会产生许多登陆信息. 
  search=`grep $KEYWORD $TEMPFILE`
  #  检查是否存在"IP address"片断, 
  #+ 它用来提示, 这是一次成功的网络登陆. 

  if [ ! -z "$search" ] #  必须使用引号, 因为变量可能会包含一些空白符. 
  then
     echo "On-line"
     rm -f $TEMPFILE    #  清除临时文件. 
     exit $ONLINE
  else
     echo -n "."        #  echo的-n选项不会产生换行符. 
                        #+ 这样你就可以在一行上连续打印. 
  fi

  sleep 1  
done  


#  注意: 如果你将变量KEYWORD的值改为"Exit", 
#+ 当在线时, 这个脚本就可以被用来检查
#+ 意外的掉线情况. 

# 练习: 按照上面"注意"中所说的那样来修改这个脚本, 
#       让它表现的更好. 

exit 0


# Nick Drage建议使用另一种方法: 

while true
  do ifconfig ppp0 | grep UP 1> /dev/null && echo "connected" && exit 0
  echo -n "."   # 不停的打印(.....), 用来提示用户等待, 直到连接上位置. 
  sleep 2
done

# 问题: 使用Control-C来终止这个进程可能是不够的. 
#+         (可能还会继续打印"...")
# 练习: 修复这个问题. 



# Stephane Chazelas提出了另一种方法: 

CHECK_INTERVAL=1

while ! tail -1 "$LOGFILE" | grep -q "$KEYWORD"
do echo -n .
   sleep $CHECK_INTERVAL
done
echo "On-line"

# 练习: 讨论一下这几种不同方法
#       各自的优缺点. 
