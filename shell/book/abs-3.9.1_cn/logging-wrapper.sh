#!/bin/bash
#  通用的shell包装, 
#+ 执行一个操作, 然后把所作的操作写入到日志文件中. 

# 需要设置如下两个变量. 
OPERATION=
#         可以是一个复杂的命令链, 
#+        比如awk脚本或者一个管道 . . .
LOGFILE=
#         命令行参数, 不管怎么样, 操作一般都需要参数. (译者注: 这行解释的是下面的OPTIONS变量, 不是LOGFILE.)


OPTIONS="$@"


# 记录下来. 
echo "`date` + `whoami` + $OPERATION "$@"" >> $LOGFILE
# 现在, 执行操作. 
exec $OPERATION "$@"

# 必须在操作执行之前, 记录到日志文件中. 
# 为什么? 
