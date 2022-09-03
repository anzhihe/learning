#!/bin/bash

PS3='Choose your favorite vegetable: '
echo

choice_of ()
{
  select vegetable
  do
    echo
    echo "Your favorite veggie is $vegetable."
    echo
    break
  done
}

choice_of "beans" "carrots" "potatoes"

exit 0
