#!/bin/bash
# 通过命令替换将文件的内容赋值给数组
script_contents=( $(cat "$0") )
#script_contents=(`cat "$0"`)

for index in $(seq 0 $((${#script_contents[@]}-1)))
do
  echo -n "${script_contents[$index]}"
  echo -n "-"
done

echo
exit 0
