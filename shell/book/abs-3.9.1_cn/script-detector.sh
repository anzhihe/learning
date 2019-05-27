#!/bin/bash
# script-detector.sh: 在一个目录中检查所有的脚本文件. 

TESTCHARS=2    # 测试前两个字符.
SHABANG='#!'   # 脚本都是以"#!"开头的. 

for file in *  # 遍历当前目录下的所有文件. 
do
  if [[ `head -c$TESTCHARS "$file"` = "$SHABANG" ]]
  #      head -c2                      #!
  #  '-c' 选项将从文件头输出指定个数的字符, 
  #+ 而不是默认的行数. 
  then
    echo "File \"$file\" is a script."
  else
    echo "File \"$file\" is *not* a script."
  fi
done
  
exit 0

#  练习:
#  -----
#  1) 修改这个脚本, 
#+    让它可以指定扫描的路径. 
#+    (而不是只搜索当前目录). 
#
#  2) 以这个脚本目前的状况, 它不能正确识别出
#+    Perl, awk, 和其他一些脚本语言的脚本文件.
#     修正这个问题.
