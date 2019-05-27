#!/bin/bash

# 给目标文件添加(由数字组成的)指定的一列. 

ARGS=2
E_WRONGARGS=65

if [ $# -ne "$ARGS" ] # 检查命令行参数个数是否正确. 
then
   echo "Usage: `basename $0` filename column-number"
   exit $E_WRONGARGS
fi

filename=$1
column_number=$2

#  将shell变量传递给脚本的awk部分, 需要一点小技巧. 
#  一种办法是, 将awk脚本中的Bash脚本变量, 
#+ 强引用起来. 
#     $'$BASH_SCRIPT_VAR'
#      ^                ^
#  在下面的内嵌awd脚本中, 就会这么做. 
#  请参考awk的相关文档来了解更多的细节. 

# 多行awk脚本的调用格式为:  awk ' ..... '


# 开始awk脚本. 
# -----------------------------
awk '

{ total += $'"${column_number}"'
}
END {
     print total
}     

' "$filename"
# -----------------------------
# 结束awk脚本. 


#   将shell变量传递给内嵌awk脚本可能是不安全的, 
#+  所以Stephane Chazelas提出了下边这种替代方法: 
#   ---------------------------------------
#   awk -v column_number="$column_number" '
#   { total += $column_number
#   }
#   END {
#       print total
#   }' "$filename"
#   ---------------------------------------


exit 0
