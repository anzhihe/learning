#!/bin/bash

directory=${1-`pwd`}

echo "Symbolic links in directory \"$directory\""

for strFile in "$( find $directory -type l)"
do
  echo "$strFile"
done | sort 

exit 0
