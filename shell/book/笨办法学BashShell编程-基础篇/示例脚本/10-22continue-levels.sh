#!/bin/bash

for outer in I II III IV V
do
  echo; echo -n "Group $outer: "

  for inner in 1 2 3 4 5 6 7 8 9 10
  do
    if [ "$inner" -eq 7 ]; then
      continue 2
    fi
    echo -n "$inner "
  done
done

echo; echo
exit 0
