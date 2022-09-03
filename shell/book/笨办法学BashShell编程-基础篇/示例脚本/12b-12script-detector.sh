#!/bin/bash

TestChars=2
SHABANG='#!'

for file in *
do
  if [[ `head -c$TestChars "$file"` = "$SHABANG" ]]; then
    echo "File \"$file\" is a script."
  else
    echo "File \"$file\" is *not* a script."
  fi
done

exit 0 
