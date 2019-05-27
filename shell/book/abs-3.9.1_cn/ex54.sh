#!/bin/bash

exec echo "Exiting \"$0\"."   # 脚本应该在这里退出.

# ----------------------------------
# The following lines never execute.

echo "This echo will never echo."

exit 99                       #  脚本是不会在这里退出的.
                              #  脚本退出后会使用'echo $?'
                              #+ 来检查一下退出码.
                              #  一定 *不是* 99.
