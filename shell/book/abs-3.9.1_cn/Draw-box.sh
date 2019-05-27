#!/bin/bash
# Draw-box.sh: 使用ASCII字符画一个盒子. 

# 由Stefano Palmeri编写, 本书作者做了少量修改. 
# 经过授权, 可以在本书中使用. 


######################################################################
###  draw_box函数注释  ###

#  "draw_box"函数可以让用户
#+ 在终端上画一个盒子. 
#
#  用法: draw_box ROW COLUMN HEIGHT WIDTH [COLOR] 
#  ROW和COLUMN用来定位你想要
#+ 画的盒子的左上角. 
#  ROW和COLUMN必须大于0, 
#+ 并且要小于当前终端的尺寸. 
#  HEIGHT是盒子的行数, 并且必须 >0 . 
#  HEIGHT + ROW 必须 <= 终端的高度. 
#  WIDTH是盒子的列数, 必须 >0 .
#  WIDTH + COLUMN 必须 <= 终端的宽度. 
#
# 例如: 如果你的终端尺寸为20x80, 
#  draw_box 2 3 10 45 是合法的
#  draw_box 2 3 19 45 的HEIGHT是错的 (19+2 > 20)
#  draw_box 2 3 18 78 的WIDTH是错的 (78+3 > 80)
#
#  COLOR是盒子边框的颜色. 
#  这是第5个参数, 并且是可选的. 
#  0=黑 1=红 2=绿 3=棕褐 4=蓝 5=紫 6=青 7=白.
#  如果你传递给函数的参数错误, 
#+ 它将会退出, 并返回65, 
#+ 不会有消息打印到stderr上. 
#
#  开始画盒子之前, 会清屏. 
#  函数内不包含清屏命令. 
#  这样就允许用户画多个盒子, 甚至可以叠加多个盒子. 

###  draw_box函数注释结束  ### 
######################################################################

draw_box(){

#=============#
HORZ="-"
VERT="|"
CORNER_CHAR="+"

MINARGS=4
E_BADARGS=65
#=============#


if [ $# -lt "$MINARGS" ]; then                 # 如果参数小于4, 退出. 
    exit $E_BADARGS
fi

# 找出参数中非数字的字符. 
# 还有其他更好的方法么(留给读者作为练习?). 
if echo $@ | tr -d [:blank:] | tr -d [:digit:] | grep . &> /dev/null; then
   exit $E_BADARGS
fi

BOX_HEIGHT=`expr $3 - 1`   #  必须-1, 因为边角的"+"是
BOX_WIDTH=`expr $4 - 1`    #+ 高和宽共有的部分. 
T_ROWS=`tput lines`        #  定义当前终端的
T_COLS=`tput cols`         #+ 长和宽的尺寸. 
         
if [ $1 -lt 1 ] || [ $1 -gt $T_ROWS ]; then    #  开始检查参数
   exit $E_BADARGS                             #+ 是否正确. 
fi
if [ $2 -lt 1 ] || [ $2 -gt $T_COLS ]; then
   exit $E_BADARGS
fi
if [ `expr $1 + $BOX_HEIGHT + 1` -gt $T_ROWS ]; then
   exit $E_BADARGS
fi
if [ `expr $2 + $BOX_WIDTH + 1` -gt $T_COLS ]; then
   exit $E_BADARGS
fi
if [ $3 -lt 1 ] || [ $4 -lt 1 ]; then
   exit $E_BADARGS
fi                                 # 参数检查结束. 

plot_char(){                       # 函数内的函数. 
   echo -e "\E[${1};${2}H"$3
}

echo -ne "\E[3${5}m"               # 如果定义了, 就设置盒子边框的颜色. 

# 开始画盒子

count=1                                         #  使用plot_char函数
for (( r=$1; count<=$BOX_HEIGHT; r++)); do      #+ 画垂直线. 
  plot_char $r $2 $VERT
  let count=count+1
done 

count=1
c=`expr $2 + $BOX_WIDTH`
for (( r=$1; count<=$BOX_HEIGHT; r++)); do
  plot_char $r $c $VERT
  let count=count+1
done 

count=1                                        #  使用plot_char函数
for (( c=$2; count<=$BOX_WIDTH; c++)); do      #+ 画水平线. 
  plot_char $1 $c $HORZ
  let count=count+1
done 

count=1
r=`expr $1 + $BOX_HEIGHT`
for (( c=$2; count<=$BOX_WIDTH; c++)); do
  plot_char $r $c $HORZ
  let count=count+1
done 

plot_char $1 $2 $CORNER_CHAR                   # 画盒子的角. 
plot_char $1 `expr $2 + $BOX_WIDTH` +
plot_char `expr $1 + $BOX_HEIGHT` $2 +
plot_char `expr $1 + $BOX_HEIGHT` `expr $2 + $BOX_WIDTH` +

echo -ne "\E[0m"             #  恢复原来的颜色. 

P_ROWS=`expr $T_ROWS - 1`    #  在终端的底部打印提示符. 

echo -e "\E[${P_ROWS};1H"
}      


# 现在, 让我们开始画盒子吧. 
clear                       # 清屏. 
R=2      # 行
C=3      # 列
H=10     # 高
W=45     # 宽
col=1    # 颜色(红)
draw_box $R $C $H $W $col   # 画盒子. 

exit 0

# 练习:
# -----
# 添加一个选项, 用来支持可以在所画的盒子中打印文本. 
