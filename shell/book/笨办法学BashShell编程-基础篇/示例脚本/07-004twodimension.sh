#!/bin/bash
arr1=(a b c)
arr2=(d e f)
arr3=(g h i)

for ((i=1; i<=3; i++))
do
  eval "tmp=\${arr${i}[@]}"
  for var in ${tmp}
  do
    echo -e "${var} \c"
  done
  echo
done
exit 0
