#!/bin/bash

TIME_LIMIT=10
INTERVAL=1

echo
echo "Hit Control-C to exit before $TIME_LIMIT seconds."
echo

while [ "$SECONDS" -le "$TIME_LIMIT" ]
do
  if [ "$SECONDS" -eq 1 ]
  then
    units=second
  else  
    units=seconds
  fi

  echo "This script has been running $SECONDS $units."
  #  在一台比较慢或者是附载过大的机器上, 
  #+ 在单次循环中, 脚本可能会忽略计数. 
  sleep $INTERVAL
done

echo -e "\a"  # Beep!(哔哔声!)

exit 0
