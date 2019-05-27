#!/bin/bash
# usage-message.sh

: ${1?"Usage: $0 ARGUMENT"}
#  如果没有提供命令行参数的话, 那么脚本就在这里退出了, 
#+ 并且打印如下错误消息.
#    usage-message.sh: 1: Usage: usage-message.sh ARGUMENT

echo "These two lines echo only if command-line parameter given."
echo "command line parameter = \"$1\""

exit 0  # 如果提供了命令行参数, 那么脚本就会在这里退出.

# 分别检查有命令行参数时和没有命令行参数时, 脚本的退出状态.
# 如果有命令行参数, 那么"$?"就是0.
# 如果没有的话, 那么"$?"就是1.
