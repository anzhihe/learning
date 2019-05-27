#!/bin/sh
# readpipe.sh
# 这个例子是由Bjon Eriksson所编写的.

last="(null)"
cat $0 |
while read line
do
    echo "{$line}"
    last=$line
done
printf "\nAll done, last:$last\n"

exit 0  # 代码结束.
        # 下边是脚本的(部分)输出.
        # 'echo'出了多余的大括号.

#############################################

./readpipe.sh 

{#!/bin/sh}
{last="(null)"}
{cat $0 |}
{while read line}
{do}
{echo "{$line}"}
{last=$line}
{done}
{printf "nAll done, last:$lastn"}


All done, last:(null)

变量(last)被设置在子shell中, 并没有被设置在外边. 
