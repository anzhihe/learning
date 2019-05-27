#!/bin/bash
# hexconvert.sh: 将10进制数字转换为16进制数字.

E_NOARGS=65 # 缺少命令行参数错误.
BASE=16     # 16进制.

if [ -z "$1" ]
then
  echo "Usage: $0 number"
  exit $E_NOARGS
  # 需要一个命令行参数. 
fi
# 练习: 添加命令行参数检查. 


hexcvt ()
{
if [ -z "$1" ]
then
  echo 0
  return    # 如果没有参数传递到这个函数中的话就"return" 0.
fi

echo ""$1" "$BASE" o p" | dc
#                 "o" 设置输出的基数(数制).
#                   "p" 打印栈顶.
# 参考dc的man页来了解其他的选项. 
return
}

hexcvt "$1"

exit 0
