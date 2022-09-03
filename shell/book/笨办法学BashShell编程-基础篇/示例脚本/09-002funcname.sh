#!/bin/bash
# 函数的名称 

xyz23 ()
{
  echo "$FUNCNAME now executing."
}

xyz23

echo "FUNCNAME = $FUNCNAME"
exit 0
