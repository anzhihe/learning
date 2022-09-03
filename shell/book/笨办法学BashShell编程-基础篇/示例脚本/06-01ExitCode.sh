#!/bin/bash 
# 退出状态码

echo hello				
echo $?					# 0

badcmd
echo $?					# 非零的值，比如：127

echo 

true # true是Bash的一个内置命令
echo "exit status of \"true\" = $?"	# 0

! true
echo "exit status of \"true\" = $?"	# 1

exit 113				# 非零退出码，通常表示错误
