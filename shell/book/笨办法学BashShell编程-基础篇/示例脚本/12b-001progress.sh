#!/bin/bash
b=''
for (( i=0; $i<100;i++ ))
do
  printf "Progress: [%-100s]%d%%\r" $b $i
  sleep 0.1
  b=#$b
done

echo
exit 0
