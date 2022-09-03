#!/bin/bash

E_BADARGS=65

if test -z "$1" ; then
  echo "Usage: `basename $0` Process(es)_to_kill"
  exit $E_BADARGS
fi

PROCESS_NAME="$1"
ps ax | grep "$PROCESS_NAME" | awk '{print $1}' | xargs -i kill -9 {} 2&> /dev/null
#                                                       ^^         ^^
#  -i 是"替换字符串"选项.
#  {} 是输出文本的替换点.
#  这与在"find"命令中使用{}的情况很相像.

exit $?
