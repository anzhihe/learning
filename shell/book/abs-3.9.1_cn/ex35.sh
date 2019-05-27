#!/bin/bash

a=/home/bozo/daily-journal.txt

echo "Basename of /home/bozo/daily-journal.txt = `basename $a`"
echo "Dirname of /home/bozo/daily-journal.txt = `dirname $a`"
echo
echo "My own home is `basename ~/`."         # `basename ~` 也可以.
echo "The home of my home is `dirname ~/`."  # `dirname ~`  也可以.

exit 0
