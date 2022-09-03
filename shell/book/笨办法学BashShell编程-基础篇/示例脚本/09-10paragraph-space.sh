#!/bin/bash
# 在一个单倍行距的文件中插入空行
# 用法：$0 <FileName

MINLEN=45

while read line
do 
  echo "$line"

  len=${#line}
  if [ "$len" -lt "$MINLEN" ] ; then
    echo 
  fi
done

exit 0
