#!/bin/bash
# pid-identifier.sh: 给出与指定pid相关联进程的完整路径名. 

ARGNO=1  # 期望的参数个数. 
E_WRONGARGS=65
E_BADPID=66
E_NOSUCHPROCESS=67
E_NOPERMISSION=68
PROCFILE=exe

if [ $# -ne $ARGNO ]
then
  echo "Usage: `basename $0` PID-number" >&2  # Error message >stderr(错误信息重定向到标准错误). 
  exit $E_WRONGARGS
fi  

pidno=$( ps ax | grep $1 | awk '{ print $1 }' | grep $1 )
# 从"ps"命令的输出中搜索带有pid的行, pid位置在第一列#1, 由awk过滤出来. 
# 然后再次确认这就是我们所要找的进程, 而不是由这个脚本调用所产生的进程. 
# 最后的"grep $1"就是用来过滤掉这种可能性. 
#
#    pidno=$( ps ax | awk '{ print $1 }' | grep $1 )
#    这么写就可以了, 这一点由Teemu Huovila指出. 

if [ -z "$pidno" ]  # 如果经过所有的过滤之后, 得到的结果是一个长度为0的字符串, 
then                # 那就说明这个pid没有相应的进程在运行. 
  echo "No such process running."
  exit $E_NOSUCHPROCESS
fi  

# 也可以这么写: 
#   if ! ps $1 > /dev/null 2>&1
#   then                # 没有与给定pid相匹配的进程在运行. 
#     echo "No such process running."
#     exit $E_NOSUCHPROCESS
#    fi

# 为了简化整个过程, 可以使用"pidof". 


if [ ! -r "/proc/$1/$PROCFILE" ]  # 检查读权限. 
then
  echo "Process $1 running, but..."
  echo "Can't get read permission on /proc/$1/$PROCFILE."
  exit $E_NOPERMISSION  # 一般用户不能访问/proc目录下的某些文件. 
fi  

# 最后两个测试可以使用下面的语句来代替: 
#    if ! kill -0 $1 > /dev/null 2>&1 # '0'不是一个信号, but
                                      # 但是这么做, 可以测试一下是否
                                      # 可以向该进程发送信号. 
#    then echo "PID doesn't exist or you're not its owner" >&2
#    exit $E_BADPID
#    fi



exe_file=$( ls -l /proc/$1 | grep "exe" | awk '{ print $11 }' )
# 或       exe_file=$( ls -l /proc/$1/exe | awk '{print $11}' )
#
# /proc/pid-number/exe是一个符号链接, 
# 指向这个调用进程的完整路径名. 

if [ -e "$exe_file" ]  # 如果/proc/pid-number/exe存在...
then                 # 那么相应的进程就存在. 
  echo "Process #$1 invoked by $exe_file."
else
  echo "No such process running."
fi  


# 这个精心制作的脚本, *几乎*能够被下边这一行所替代: 
# ps ax | grep $1 | awk '{ print $5 }'
# 但是, 这样并不会工作...
# 因为'ps'输出的第5列是进程的argv[0](译者注: 这是命令行第一个参数, 即调用时程序用的程序路径本身.)
# 而不是可执行文件的路径. 
#
# 然而, 下边这两种方法都能正确地完成这个任务. 
#       find /proc/$1/exe -printf '%l\n'
#       lsof -aFn -p $1 -d txt | sed -ne 's/^n//p'

# 附加注释, 是Stephane Chazelas添加的. 

exit 0
