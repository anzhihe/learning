#!/bin/bash

PS3='Choose your favorite vegetable: '
echo

select vegetable in "beans" "carrots" "potatoes"
do
  echo
  echo "Your favorite veggie is $vegetable."
  echo
  break
done

exit 0
