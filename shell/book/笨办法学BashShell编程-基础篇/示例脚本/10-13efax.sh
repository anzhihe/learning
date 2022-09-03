#!/bin/bash
# Faxing, 要求系统有efax软件

EXPECT_ARGS=2
E_BADARGS=65

if [ $# -ne $EXPECT_ARGS ]; then
  echo "Usage: `basename $0` phone# text-file"
  exit $E_BADARGS
fi

if [ ! -f "$2" ]; then
  echo "File $2 is not a text file"
  exit $E_BADARGS
fi

fax make $2

for strFile in $(ls $2.0*)
do
  fil="$fil $strFile"
done

efax -d /dev/ttyS3 -o1 -t "T$1" $fil

exit 0

