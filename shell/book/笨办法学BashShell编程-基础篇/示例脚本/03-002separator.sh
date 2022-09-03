#!/bin/bash

# 分号(separator [semicolon])测试
echo hello; echo there

filename='mytestfile.txt'

if [ -e "$filename" ]; then # 注意：if 和 then需要分隔
  echo "File $filename exists." ; cp $filename $filename.bak
else
  echo "File $filename not found." ; touch $filename
fi; echo "File test complete."
