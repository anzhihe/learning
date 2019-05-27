#!/bin/bash

# 未经处理的地址资料

clear # 清屏.

echo "          Contact List"
echo "          ------- ----"
echo "Choose one of the following persons:" 
echo
echo "[E]vans, Roland"
echo "[J]ones, Mildred"
echo "[S]mith, Julie"
echo "[Z]ane, Morris"
echo

read person

case "$person" in
# 注意, 变量是被""引用的.

  "E" | "e" )
  # 接受大写或者小写输入.
  echo
  echo "Roland Evans"
  echo "4321 Floppy Dr."
  echo "Hardscrabble, CO 80753"
  echo "(303) 734-9874"
  echo "(303) 734-9892 fax"
  echo "revans@zzy.net"
  echo "Business partner & old friend"
  ;;
# 注意, 每个选项后边都要以双分号;;结尾.

  "J" | "j" )
  echo
  echo "Mildred Jones"
  echo "249 E. 7th St., Apt. 19"
  echo "New York, NY 10009"
  echo "(212) 533-2814"
  echo "(212) 533-9972 fax"
  echo "milliej@loisaida.com"
  echo "Ex-girlfriend"
  echo "Birthday: Feb. 11"
  ;;

# 后边的 Smith 和 Zane 的信息在这里就省略了.

          * )
   # 默认选项.
   # 空输入(敲回车RETURN), 也适用于这里. 
   echo
   echo "Not yet in database."
  ;;

esac

echo

#  练习:
#  -----
#  修改这个脚本, 让它能够接受多个输入,
#+ 并且能够显示多个地址.

exit 0
