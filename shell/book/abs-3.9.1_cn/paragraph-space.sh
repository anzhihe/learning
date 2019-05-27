#!/bin/bash
# paragraph-space.sh

# 在一个单倍行距的文本文件中插入空行.
# Usage: $0 &lt;FILENAME

MINLEN=45        # 可能需要修改这个值.
#  假定行的长度小于$MINLEN所指定的长度的时候 
#+ 才认为此段结束.

while read line  # 提供和输入文件一样多的行...
do
  echo "$line"   # 输入所读入的行本身.

  len=${#line}
  if [ "$len" -lt "$MINLEN" ]
    then echo    # 在短行(译者注: 也就是小于$MINLEN个字符的行)后面添加一个空行.
  fi  
done

exit 0
