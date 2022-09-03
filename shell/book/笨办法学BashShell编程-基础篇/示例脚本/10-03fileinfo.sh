#!/bin/bash

FILES="/etc/fstab
/usr/bin/gawk
/usr/bin/fakefile"

for strFile in $FILES
do
  if [ ! -e "$strFile" ]; then
    echo "$strFile does not exits."; echo
    continue
  fi

  ls -l $strFile | awk '{print $9 " size: " $5}'
  echo
done
exit 0

