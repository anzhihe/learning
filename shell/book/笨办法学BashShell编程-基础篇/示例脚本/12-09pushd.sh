#!/bin/bash

dir1=/usr/local
dir2=/var/spool

pushd $dir1
echo "Now in directory `pwd`."; echo 

pushd $dir2
echo "Now in directory `pwd`."; echo 

echo "The top entry in the DIRSTACK array in $DIRSTACK." ; echo

dirs -v ; echo

popd
echo "Now back in directory `pwd`."; echo

popd
echo "Now back in original working directory `pwd`."; echo

exit 0
