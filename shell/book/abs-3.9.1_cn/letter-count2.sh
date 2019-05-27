#! /bin/sh
# letter-count2.sh: 在文本文件中计算字符的出现次数. 
#
# 由nyal [nyal@voila.fr]编写.
# 授权使用. 
# 本文作者重新注释. 
# 版本 1.1: 经过修改可用于gawk 3.1.3.
#              (也可用于awk的早期版本.)


INIT_TAB_AWK=""
# 初始化awk脚本的参数. 
count_case=0
FILE_PARSE=$1

E_PARAMERR=65

usage()
{
    echo "Usage: letter-count.sh file letters" 2>&1
    # 比如:   ./letter-count2.sh filename.txt a b c
    exit $E_PARAMERR  # 传递到脚本的参数个数不够. 
}

if [ ! -f "$1" ] ; then
    echo "$1: No such file." 2>&1
    usage                 # 打印使用信息并退出. 
fi 

if [ -z "$2" ] ; then
    echo "$2: No letters specified." 2>&1
    usage
fi 

shift                      # 指定的字符. 
for letter in `echo $@`    # for循环遍历 . . .
  do
  INIT_TAB_AWK="$INIT_TAB_AWK tab_search[${count_case}] = \"$letter\"; final_tab[${count_case}] = 0; " 
  # 作为参数传递到下边的awk脚本中. 
  count_case=`expr $count_case + 1`
done

# 调试:
# echo $INIT_TAB_AWK;

cat $FILE_PARSE |
# 将目标文件通过管道传递下边的awk脚本中. 

# ----------------------------------------------------------------------------------
# 下边是本脚本的早期版本使用的方法: 
# awk -v tab_search=0 -v final_tab=0 -v tab=0 -v nb_letter=0 -v chara=0 -v chara2=0 \

awk \
"BEGIN { $INIT_TAB_AWK } \
{ split(\$0, tab, \"\"); \
for (chara in tab) \
{ for (chara2 in tab_search) \
{ if (tab_search[chara2] == tab[chara]) { final_tab[chara2]++ } } } } \
END { for (chara in final_tab) \
{ print tab_search[chara] \" => \" final_tab[chara] } }"
# ----------------------------------------------------------------------------------
#  不是所有的都那么复杂, 只是 . . . 
#+ for循环, if条件判断, 和几个指定函数而已. 

exit $?

# 与脚本letter-count.sh相比较.
