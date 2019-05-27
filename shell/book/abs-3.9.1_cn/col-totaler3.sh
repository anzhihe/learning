#!/bin/bash

#  这是"求列的和"脚本的另外一个版本(col-totaler.sh)
#+ 那个脚本可以把目标文件中的指定的列上的所有数字全部累加起来,求和.
#  这个版本将把一个变量通过export的形式传递到'awk'中 . . .
#+ 并且把awk脚本放到一个变量中.


ARGS=2
E_WRONGARGS=65

if [ $# -ne "$ARGS" ] # 检查命令行参数的个数.
then
   echo "Usage: `basename $0` filename column-number"
   exit $E_WRONGARGS
fi

filename=$1
column_number=$2

#===== 上边的这部分,与原始脚本完全一样 =====#

export column_number
# 将列号export出来, 这样后边的进程就可用了.


# -----------------------------------------------
awkscript='{ total += $ENVIRON["column_number"] }
END { print total }'
# 是的, 变量可以保存awk脚本.
# -----------------------------------------------

# 现在, 运行这个awk脚本.
awk "$awkscript" "$filename"

# 感谢, Stephane Chazelas.

exit 0
