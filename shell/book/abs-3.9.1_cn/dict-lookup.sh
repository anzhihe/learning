#!/bin/bash
# dict-lookup.sh

#  这个脚本在1913年的韦氏词典中查找定义.
#  这本公共词典可以通过不同的
#+ 站点来下载,包括
#+ Project Gutenberg (http://www.gutenberg.org/etext/247).
#                                                                  
#  在使用本脚本之前,
#+ 先要将这本字典由DOS格式转换为UNIX格式(只以LF作为行结束符).
#  将这个文件存储为纯文本形式, 并且保证是未压缩的ASCII格式.
#  将DEFAULT_DICTFILE变量以path/filename形式设置好.


E_BADARGS=65
MAXCONTEXTLINES=50                        # 显示的最大行数. 
DEFAULT_DICTFILE="/usr/share/dict/webster1913-dict.txt"
                                          # 默认的路径和文件名.
                                          # 在必要的时候可以进行修改.
#  注意:
#  -----
#  这个特定的1913年版的韦氏词典
#+ 在每个入口都是以大写字母开头的
#+ (剩余的字符都是小写).
#  只有每部分的第一行是以这种形式开始的,
#+ 这也就是为什么搜索算法是下边的这个样子.



if [[ -z $(echo "$1" | sed -n '/^[A-Z]/p') ]]
#  必须指定一个要查找的单词,
#+ 并且这个单词必须以大写字母开头.
then
  echo "Usage: `basename $0` Word-to-define [dictionary-file]"
  echo
  echo "Note: Word to look up must start with capital letter,"
  echo "with the rest of the word in lowercase."
  echo "--------------------------------------------"
  echo "Examples: Abandon, Dictionary, Marking, etc."
  exit $E_BADARGS
fi


if [ -z "$2" ]                            #  也可以指定不同的词典
                                          #+ 作为这个脚本的第2个参数传递进来.
then
  dictfile=$DEFAULT_DICTFILE
else
  dictfile="$2"
fi

# ---------------------------------------------------------
Definition=$(fgrep -A $MAXCONTEXTLINES "$1 \\" "$dictfile")
#                                   以 "Word \..." 这种形式定义
#                                                               
#  当然, 即使搜索一个特别大的文本文件的时候
#+ "fgrep"也是足够快的.


# 现在, 剪掉定义块.

echo "$Definition" |
sed -n '1,/^[A-Z]/p' |
#  从输出的第一行
#+ 打印到下一部分的第一行.
sed '$d' | sed '$d'
#  删除输出的最后两行
#+ (空行和下一部分的第一行).
# ---------------------------------------------------------

exit 0

# 练习:
# -----
# 1)  修改这个脚本, 让它具备能够处理任何字符形式的输入
#   + (大写, 小写, 或大小写混合), 然后将其转换为
#   + 能够处理的统一形式.
#                                                       
# 2)  将这个脚本转化为一个GUI应用,
#   + 使用一些比如像"gdialog"的东西 .  .  .
#     这样的话, 脚本将不再从命令行中
#   + 取得这些参数.
#                                                       
# 3)  修改这个脚本让它具备能够分析另外一个
#   + 公共词典的能力, 比如 U.S. Census Bureau Gazetteer.
