#!/bin/bash
# pr-ascii.sh: 打印ASCII码的字符表. 

START=33   # 可打印的ASCII字符的范围(十进制). 
END=125

echo " Decimal   Hex     Character"   # 表头. 
echo " -------   ---     ---------"

for ((i=START; i<=END; i++))
do
  echo $i | awk '{printf("  %3d       %2x         %c\n", $1, $1, $1)}'
# 在这种上下文中, 不会运行Bash内建的printf命令: 
#     printf "%c" "$i"
done

exit 0


#  十进制   16进制     字符
#  -------  ------   ---------
#    33       21         !
#    34       22         "
#    35       23         #
#    36       24         $
#
#    . . .
#
#   122       7a         z
#   123       7b         {
#   124       7c         |
#   125       7d         }


#  将脚本的输出重定向到一个文件中, 
#+ 或者通过管道传递给"more":  sh pr-asc.sh | more
