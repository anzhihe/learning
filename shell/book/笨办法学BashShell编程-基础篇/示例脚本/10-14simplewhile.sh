#!/bin/bash
n=0
var=1
LIMIT=100

while [ "$var" -le "$LIMIT" ]
do
  if [ "$var" -eq "1" ]; then
    echo -n "$var"
  else
    echo -n "+$var"
  fi
  let "n=$n+$var"
  let "var += 1"     # var=`expr $var + 1` 或  var=$((var+1))
done

echo -n "=$n"
echo;echo;
exit 0 
