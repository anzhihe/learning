#!/bin/bash
# ASCII 字符<>比较

veg1=carrots
veg2=tomatoes

if [[ "$veg1" < "$veg2" ]]
then
  echo "$veg1 < $veg2"
else
  echo "What kind of dictionary are you using, anywho?"
fi

exit 0 
