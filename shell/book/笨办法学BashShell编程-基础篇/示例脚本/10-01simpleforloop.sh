#!/bin/bash

for fruit in Apple Banana Pear Peach
do 
  echo $fruit
done 

echo 

for fruit in "Apple Banana Pear Peach"
do 
  echo $fruit
done 

exit 0
