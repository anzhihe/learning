#!/bin/bash
# reassign-stdout.sh

LOGFILE=logfile.txt

exec 6>&1           # 将fd #6与stdout链接起来. 
                    # 保存stdout. 

exec > $LOGFILE     # stdout就被文件"logfile.txt"所代替了. 

# ----------------------------------------------------------- #
# 在这块中所有命令的输出都会发送到文件$LOGFILE中. 

echo -n "Logfile: "
date
echo "-------------------------------------"
echo

echo "Output of \"ls -al\" command"
echo
ls -al
echo; echo
echo "Output of \"df\" command"
echo
df

# ----------------------------------------------------------- #

exec 1>&6 6>&-      # 恢复stdout, 然后关闭文件描述符#6. 

echo
echo "== stdout now restored to default == "
echo
ls -al
echo

exit 0
