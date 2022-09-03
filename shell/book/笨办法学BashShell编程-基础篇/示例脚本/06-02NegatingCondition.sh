#!/bin/bash
# 叹号！取反操作符 与 退出状态码 的练习

# ture 与 冒号都是什么都不做的命令
true
echo "Exit status of \"true\" = $?" 

! true   # 注意 感叹号! 与 命令之间空格 
echo "Exit status of \"! true\" = $?" 


# 退出状态码必须是十进制数, 范围是0 - 255
exit 286
