#!/bin/bash

variable1=`for i in 1 2 3 4 5
do
  echo -n "$i"
done`

echo "variable1 = $variable1"
exit 0
