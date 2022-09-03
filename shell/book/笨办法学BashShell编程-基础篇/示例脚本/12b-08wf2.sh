#!/bin/bash
# 分析一个文件文件中单词出现的频率

ARGS=1
E_BADARGS=65
E_NOFILE=66

if [ $# -ne "$ARGS" ] ; then
  echo "Usage `basename $0` filename"
  exit $E_BADARGS
fi

if [ ! -f "$1" ]; then
  echo "File \"$1\" does net exist."
  exit $E_NOFILE
fi

cat "$1" | xargs -n1 | \
tr A-Z a-z | \
sed -e 's/\.//g' -e 's/\,//g' -e 's/ //g'| \
sort | uniq -c | sort -nr

exit 0  
