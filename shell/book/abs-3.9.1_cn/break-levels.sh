#!/bin/bash
# break-levels.sh: 退出循环.

# "break N" 退出N层循环.

for outerloop in 1 2 3 4 5
do
  echo -n "Group $outerloop:   "

  # --------------------------------------------------------
  for innerloop in 1 2 3 4 5
  do
    echo -n "$innerloop "

    if [ "$innerloop" -eq 3 ]
    then
      break  # 试试   break 2   来看看发生什么事.
             # (内部循环和外部循环都被"Break"了. )
    fi
  done
  # --------------------------------------------------------

  echo
done  

echo

exit 0
