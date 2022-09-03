#!/bin/bash
# look命令默认字典文件是：/usr/share/dict/words

DocFile=doc1.txt

while [ "$word" != end ]
do
  read word
  look $word > /dev/null
  lookup=$?
  
  if [ "$lookup" -eq 0 ]; then
    echo "\"$word\" is a valid."
  else
    echo "\"$word\" is a invalid."
  fi
done <"$DocFile"

echo
exit 0 
