#!/bin/bash

if [ $# -eq 0 ]; then
  echo "Try harder"
  exit 1
fi

pushd $1
ls
popd

exit 0
