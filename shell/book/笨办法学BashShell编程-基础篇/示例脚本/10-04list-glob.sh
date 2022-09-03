#!/bin/bash
for file in *
do 
  ls -l "$file"
done

echo;

for file in [ct]*
do 
  # rm -f $file
  echo "Remove file \"$file\"."
done
exit 0
