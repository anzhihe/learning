#!/bin/bash

while true
do
  echo; echo "Hit a key, then hit return."
  read Keypress

  case "$Keypress" in
    "X"         ) exit;;
    [[:lower:]] ) echo "Lowercase letter";;
    [[:upper:]] ) echo "Uppercase letter";;
    [0-9]       ) echo "Digit";;
    *           ) echo "Punctuation, whitespace, or other";;
  esac
done
exit 0
