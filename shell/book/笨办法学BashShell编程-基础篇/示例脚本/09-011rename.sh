#!/bin/bash
# 批量修改文件名，保留"扩展名"

num=1

for OldFilename in *.tar *.tar.gz
do
  NewFilename=new_${num}.${OldFilename#*.}
  mv $OldFilename $NewFilename 2>/dev/null

  if [ $? -eq 0 ] ; then
    echo "rename $OldFilename to $NewFilename"
    let num++
  fi
done

exit 0 
