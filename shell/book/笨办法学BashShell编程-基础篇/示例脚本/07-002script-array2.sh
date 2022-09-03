#!/bin/bash
# 通过命令替换将脚本的内容赋值给数组
# 在V1的基础上修改为原格式输出
script_content=( $(cat "$0") )
echo ${#script_content[@]}
#declare -a | grep script_content

for index in $(seq 0 $((${#script_content[@]}-1)))
do
  echo -n "${script_content[$index]}"
  echo -n "-"
  echo 
  #printf "${script_content[$index]}"
done

echo
exit 0
