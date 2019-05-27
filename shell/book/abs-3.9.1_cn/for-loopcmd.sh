#!/bin/bash
#  for-loopcmd.sh: 带[list]的for循环, 
#+ [list]是由命令替换所产生的.

NUMBERS="9 7 3 8 37.53"

for number in `echo $NUMBERS`  # for number in 9 7 3 8 37.53
do
  echo -n "$number "
done

echo 
exit 0
