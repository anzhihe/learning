#!/bin/bash

cd /root/test/
echo `pwd`
for filename in *
do 
  oldname=`basename $filename`
  newname=`echo $oldname | tr a-z A-Z`
  echo -n "$oldname :"
  if [ "$newname" != "$oldname" ] ; then
    echo -n "==>  $newname"
    mv $oldname $newname
  fi
  echo 
done

exit 0
