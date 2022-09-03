#!/bin/bash

exec echo "Exiting \"$0\"."	# 脚本在此处就退出了

# 永远不会执行下面的代码

echo "This echo will never echo."
exit 99
