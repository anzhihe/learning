#!/bin/bash

function1 ()
{
  echo "Without expr: "
  caller

  echo ; echo "Non-negative integer: "
  caller 0
}

function1

echo; echo "Main script: "
caller 0
exit 0
