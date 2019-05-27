#!/bin/bash
# Du.sh: DOS到UNIX文本文件的转换.

E_WRONGARGS=65

if [ -z "$1" ]
then
  echo "Usage: `basename $0` filename-to-convert"
  exit $E_WRONGARGS
fi

NEWFILENAME=$1.unx

CR='\015'  # 回车.
           # 015是8进制的ASCII码的回车.
           # DOS中文本文件的行结束符是CR-LF.
           # UNIX中文本文件的行结束符只是LF.

tr -d $CR &lt; $1 &gt; $NEWFILENAME
# 删除回车并且写到新文件中. 

echo "Original DOS text file is \"$1\"."
echo "Converted UNIX text file is \"$NEWFILENAME\"."

exit 0

# 练习:
# -----
# 修改上边的脚本完成从UNIX到DOS的转换. 
