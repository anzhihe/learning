#!/bin/bash
# pb.sh: 电话本

# 由Rick Boivie编写, 已经得到作者授权, 可以在本书中使用. 
# 本书作者做了一些修改. 

MINARGS=1     #  脚本至少需要一个参数. 
DATAFILE=./phonebook
              #  当前目录下, 
              #+ 必须有一个名字为"phonebook"的数据文件. 
PROGNAME=$0
E_NOARGS=70   #  未传递参数错误. 

if [ $# -lt $MINARGS ]; then
      echo "Usage: "$PROGNAME" data"
      exit $E_NOARGS
fi      


if [ $# -eq $MINARGS ]; then
      grep $1 "$DATAFILE"
      # 如果文件$DATAFILE不存在, 'grep'就会打印一个错误信息. 
else
      ( shift; "$PROGNAME" $* ) | grep $1
      # 脚本递归调用自身. 
fi

exit 0        #  脚本在此退出. 
              #  因此, 在这句之后, 
			  #+ 即使不加"#"号, 也可以添加注释和数据. 

# ------------------------------------------------------------------------
"phonebook"数据文件的例子: 

John Doe        1555 Main St., Baltimore, MD 21228          (410) 222-3333
Mary Moe        9899 Jones Blvd., Warren, NH 03787          (603) 898-3232
Richard Roe     856 E. 7th St., New York, NY 10009          (212) 333-4567
Sam Roe         956 E. 8th St., New York, NY 10009          (212) 444-5678
Zoe Zenobia     4481 N. Baker St., San Francisco, SF 94338  (415) 501-1631
# ------------------------------------------------------------------------

$bash pb.sh Roe
Richard Roe     856 E. 7th St., New York, NY 10009          (212) 333-4567
Sam Roe         956 E. 8th St., New York, NY 10009          (212) 444-5678

$bash pb.sh Roe Sam
Sam Roe         956 E. 8th St., New York, NY 10009          (212) 444-5678

#  如果给脚本传递的参数超过了一个, 
#+ 那这个脚本就*只*会打印包含所有参数的行. 
