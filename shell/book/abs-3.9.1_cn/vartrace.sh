#!/bin/bash

trap 'echo "VARIABLE-TRACE> \$variable = \"$variable\""' DEBUG
# 当每个命令执行之后, 就会打印出$variable的值. 

variable=29

echo "Just initialized \"\$variable\" to $variable."

let "variable *= 3"
echo "Just multiplied \"\$variable\" by 3."

exit $?

#  "trap 'command1 . . . command2 . . .' DEBUG"结构更适合于
#+ 使用在复杂脚本的上下文中, 
#+ 如果在这种情况下大量使用"echo $variable"语句的话, 
#+ 将会非常笨拙, 而且很耗时. 

# 感谢, Stephane Chazelas指出这点. 


脚本的输出: 

VARIABLE-TRACE> $variable = ""
VARIABLE-TRACE> $variable = "29"
Just initialized "$variable" to 29.
VARIABLE-TRACE> $variable = "29"
VARIABLE-TRACE> $variable = "87"
Just multiplied "$variable" by 3.
VARIABLE-TRACE> $variable = "87"
