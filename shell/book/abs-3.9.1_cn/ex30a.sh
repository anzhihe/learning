#!/bin/bash
# ex30a.sh: 脚本ex30.sh的"彩色"版本. 
#            没被加工处理过的地址数据库


clear                                   # 清屏. 

echo -n "          "
echo -e '\E[37;44m'"\033[1mContact List\033[0m"
                                        # 在蓝色背景下的白色. 
echo; echo
echo -e "\033[1mChoose one of the following persons:\033[0m"
                                        # 粗体
tput sgr0
echo "(Enter only the first letter of name.)"
echo
echo -en '\E[47;34m'"\033[1mE\033[0m"   # 蓝色
tput sgr0                               # 将颜色重置为"常规". 
echo "vans, Roland"                     # "[E]vans, Roland"
echo -en '\E[47;35m'"\033[1mJ\033[0m"   # 红紫色
tput sgr0
echo "ones, Mildred"
echo -en '\E[47;32m'"\033[1mS\033[0m"   # 绿色
tput sgr0
echo "mith, Julie"
echo -en '\E[47;31m'"\033[1mZ\033[0m"   # 红色
tput sgr0
echo "ane, Morris"
echo

read person

case "$person" in
# 注意, 变量被引用起来了. 

  "E" | "e" )
  # 大小写的输入都能接受. 
  echo
  echo "Roland Evans"
  echo "4321 Floppy Dr."
  echo "Hardscrabble, CO 80753"
  echo "(303) 734-9874"
  echo "(303) 734-9892 fax"
  echo "revans@zzy.net"
  echo "Business partner & old friend"
  ;;

  "J" | "j" )
  echo
  echo "Mildred Jones"
  echo "249 E. 7th St., Apt. 19"
  echo "New York, NY 10009"
  echo "(212) 533-2814"
  echo "(212) 533-9972 fax"
  echo "milliej@loisaida.com"
  echo "Girlfriend"
  echo "Birthday: Feb. 11"
  ;;

# 稍后为Smith & Zane添加信息. 

          * )
   # 默认选项. 	  
   # 空输入(直接按回车)也会在这被匹配. 
   echo
   echo "Not yet in database."
  ;;

esac

tput sgr0                               # 将颜色重置为"常规". 

echo

exit 0
