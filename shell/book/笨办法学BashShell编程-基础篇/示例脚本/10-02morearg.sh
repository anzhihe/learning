#!/bin/bash

for fruit in "Apple 1" "Banana 2"  "Pear 3"  "Peach 4"
do 
  echo $fruit
  set - $fruit
  echo "$1 : $2 kg"
done 

exit 0
