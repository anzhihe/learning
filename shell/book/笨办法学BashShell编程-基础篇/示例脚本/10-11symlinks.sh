#!/bin/bash
# 列出目录中所有的符号文件，并保存到一个文件中

OUTFILE=symlinks.list.txt
directory=${1-`pwd`}

echo "Symbolic links in directory \"$directory\"" > "$OUTFILE"
echo "------------------------------------------" >> "$OUTFILE"

for strFile in "$( find $directory -type l)"
do
  echo "$strFile"
done | sort >> "$OUTFILE"

exit 0
