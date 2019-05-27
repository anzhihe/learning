#!/bin/bash

ARGS=1        # 期望的参数个数. 
E_BADARGS=65  # 如果传递的参数个数不正确, 那么给出这个退出码. 

test $# -ne $ARGS && echo "Usage: `basename $0` $ARGS argument(s)" && exit $E_BADARGS
#  如果"条件1"测试为true (表示传递给脚本的参数个数不对), 
#+ 则余下的命令会被执行, 并且脚本将结束运行. 

# 只有当上面的测试条件为false的时候, 这行代码才会被执行. 
echo "Correct number of arguments passed to this script."

exit 0

# 为了检查退出码, 在脚本结束的时候可以使用"echo $?"来查看退出码. 
