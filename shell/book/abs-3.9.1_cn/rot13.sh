#!/bin/bash
# rot13.sh: 典型的rot13算法, 
#           使用这种方法加密至少可以愚弄一下3岁小孩. 

# 用法: ./rot13.sh filename
# 或     ./rot13.sh &lt;filename
# 或     ./rot13.sh and supply keyboard input (stdin)

cat "$@" | tr 'a-zA-Z' 'n-za-mN-ZA-M'   # "a"变为"n", "b"变为"o", 等等. 
#  'cat "$@"'结构
#+ 允许从stdin或者从文件中获得输入. 

exit 0
