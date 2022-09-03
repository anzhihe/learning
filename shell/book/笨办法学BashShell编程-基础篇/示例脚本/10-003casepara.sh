#!/bin/bash
E_PARM=65

case "$1" in
  "" ) 
    echo "Usage: ${0##*/} <filename>"
    exit $E_PARM 
    ;;
  -* ) 
    FILENAME=./$1 
    ;;
  *  ) 
    FILENAME=$1 
    ;;
esac

echo "File Name: $FILENAME"
exit 0
