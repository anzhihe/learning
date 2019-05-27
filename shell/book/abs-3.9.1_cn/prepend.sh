#!/bin/bash
# prepend.sh: 在文件的开头添加文本. 
#
#  Kenny Stauffer所捐助的脚本例子, 
#+ 本文作者对这个脚本进行了少量修改. 


E_NOSUCHFILE=65

read -p "File: " file   #  'read'命令的-p参数用来显示提示符. 
if [ ! -e "$file" ]
then   # 如果这个文件不存在, 那就进来. 
  echo "File $file not found."
  exit $E_NOSUCHFILE
fi

read -p "Title: " title
cat - $file &lt;&lt;&lt;$title &gt; $file.new

echo "Modified file is $file.new"

exit 0

# 下边是'man bash'中的一段: 
# Here String
# 	here document的一种变形，形式如下: 
# 
# 		&lt;&lt;&lt;word
# 
# 	word被扩展并且被提供到command的标准输入中. 
