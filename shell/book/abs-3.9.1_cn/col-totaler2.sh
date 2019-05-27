#!/bin/bash

#  这是"求文件中指定列的总和"脚本的另一个版本,
#+ 这个脚本可以计算目标文件中指定列(此列的内容必须都是数字)的所有数字的和.
#  这个脚本使用了间接引用.

ARGS=2
E_WRONGARGS=65

if [ $# -ne "$ARGS" ] # 检查命令行参数的个数是否合适.
then
   echo "Usage: `basename $0` filename column-number"
   exit $E_WRONGARGS
fi

filename=$1
column_number=$2

#===== 在这一行上边的部分, 与原始脚本是相同的 =====#


# 多行的awk脚本的调用方法为: awk ' ..... '


# awk脚本开始.
# ------------------------------------------------
awk "

{ total += \$${column_number} # 间接引用
}
END {
     print total
     }

     " "$filename"
# ------------------------------------------------
# awk脚本结束.

#  间接变量引用避免了在一个内嵌awk脚本中引用shell变量的混乱行为.
#  感谢, Stephane Chazelas.


exit 0
