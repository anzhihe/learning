#!/bin/bash
# horserace.sh: 一个非常简单的模拟赛马的游戏. 
# 作者: Stefano Palmeri
# 经过授权可以在本书中使用. 

################################################################
#  脚本目的: 
#  使用转义序列和终端颜色进行游戏. 
#
#  练习: 
#  编辑脚本, 使它运行起来更具随机性, 
#+ 建立一个假的赌场 . . .     
#  嗯 . . . 嗯 . . . 这种开场让我联想起一部电影 . . .
#
#  脚本将会给每匹马分配一个随机障碍. 
#  按照马的障碍来计算几率, 
#+ 并且使用一种欧洲(?)的风格表达出来. 
#  比如: 几率(odds)=3.75的话, 那就意味着如果你押$1,
#+ 你就会赢得$3.75.
# 
#  此脚本已经在GNU/Linux操作系统上测试过, 
#+ 测试终端有xterm, rxvt, 和konsole. 
#  测试机器上安装的是AMD 900 MHz处理器, 
#+ 平均比赛时间为75秒.    
#  如果使用更快的机器, 那么比赛用时会更少. 
#  所以, 如果你想增加比赛的悬念, 可以重置变量USLEEP_ARG. 
#
#  本脚本由Stefano Palmeri编写. 
################################################################

E_RUNERR=65

# 检查一下md5sum和bc是否已经被安装. 
if ! which bc &> /dev/null; then
   echo bc is not installed.  
   echo "Can\'t run . . . "
   exit $E_RUNERR
fi
if ! which md5sum &> /dev/null; then
   echo md5sum is not installed.  
   echo "Can\'t run . . . "
   exit $E_RUNERR
fi

#  设置下面的变量将会降低脚本的运行速度. 
#  它会作为参数, 传递给usleep命令(man usleep),   
#+ 并且单位是微秒(500000微秒 = 半秒).
USLEEP_ARG=0  

#  如果脚本被Ctl-C中断, 那就清除临时目录, 
#+ 恢复终端光标和终端颜色. 
trap 'echo -en "\E[?25h"; echo -en "\E[0m"; stty echo;\
tput cup 20 0; rm -fr  $HORSE_RACE_TMP_DIR'  TERM EXIT
#  请参考与调试相关的章节, 可以获得'trap'命令的详细用法. 

# 为脚本设置一个唯一的(实际上不是绝对唯一)临时目录名. 
HORSE_RACE_TMP_DIR=$HOME/.horserace-`date +%s`-`head -c10 /dev/urandom | md5sum | head -c30`

# 创建临时目录, 并移动到该目录下. 
mkdir $HORSE_RACE_TMP_DIR
cd $HORSE_RACE_TMP_DIR


#  这个函数将会把光标移动到行为$1, 列为$2的位置上, 然后打印$3. 
#  例如: "move_and_echo 5 10 linux"等价与"tput cup 4 9; echo linux", 
#+ 但是使用一个命令代替了两个命令. 
#  注意: "tput cup"定义0 0位置, 为终端左上角, 
#+ 而echo定义1 1位置, 为终端左上角. 
move_and_echo() {
          echo -ne "\E[${1};${2}H""$3" 
}

# 此函数用来产生1-9之间的伪随机数. 
random_1_9 () {
                head -c10 /dev/urandom | md5sum | tr -d [a-z] | tr -d 0 | cut -c1 
}

#  在画马的时候, 这两个函数用来模拟"移动". 
draw_horse_one() {
               echo -n " "//$MOVE_HORSE//
}
draw_horse_two(){
              echo -n " "\\\\$MOVE_HORSE\\\\ 
}   


# 定义当前终端尺寸. 
N_COLS=`tput cols`
N_LINES=`tput lines`

# 至少需要一个20(行) X 80(列)的终端. 检查一下. 
if [ $N_COLS -lt 80 ] || [ $N_LINES -lt 20 ]; then
   echo "`basename $0` needs a 80-cols X 20-lines terminal."
   echo "Your terminal is ${N_COLS}-cols X ${N_LINES}-lines."
   exit $E_RUNERR
fi


# 开始画赛场. 

# 需要一个80字符的字符串. 见下面. 
BLANK80=`seq -s "" 100 | head -c80`

clear

# 将前景色与背景色设为白. 
echo -ne '\E[37;47m'

# 将光标移动到终端的左上角. 
tput cup 0 0 

# 画6条白线. 
for n in `seq 5`; do
      echo $BLANK80        # 用这个80字符的字符串将终端变为彩色的. 
done

# 将前景色设为黑色. 
echo -ne '\E[30m'

move_and_echo 3 1 "START  1"            
move_and_echo 3 75 FINISH
move_and_echo 1 5 "|"
move_and_echo 1 80 "|"
move_and_echo 2 5 "|"
move_and_echo 2 80 "|"
move_and_echo 4 5 "|  2"
move_and_echo 4 80 "|"
move_and_echo 5 5 "V  3"
move_and_echo 5 80 "V"

# 将前景色设置为红色. 
echo -ne '\E[31m'

# 一些ASCII的艺术效果. 
move_and_echo 1 8 "..@@@..@@@@@...@@@@@.@...@..@@@@..."
move_and_echo 2 8 ".@...@...@.......@...@...@.@......."
move_and_echo 3 8 ".@@@@@...@.......@...@@@@@.@@@@...."
move_and_echo 4 8 ".@...@...@.......@...@...@.@......."
move_and_echo 5 8 ".@...@...@.......@...@...@..@@@@..."
move_and_echo 1 43 "@@@@...@@@...@@@@..@@@@..@@@@."
move_and_echo 2 43 "@...@.@...@.@.....@.....@....."
move_and_echo 3 43 "@@@@..@@@@@.@.....@@@@...@@@.."
move_and_echo 4 43 "@..@..@...@.@.....@.........@."
move_and_echo 5 43 "@...@.@...@..@@@@..@@@@.@@@@.."


# 将前景色和背景色设为绿色. 
echo -ne '\E[32;42m'

# 画11行绿线. 
tput cup 5 0
for n in `seq 11`; do
      echo $BLANK80
done

# 将前景色设为黑色. 
echo -ne '\E[30m'
tput cup 5 0

# 画栅栏. 
echo "++++++++++++++++++++++++++++++++++++++\
++++++++++++++++++++++++++++++++++++++++++"

tput cup 15 0
echo "++++++++++++++++++++++++++++++++++++++\
++++++++++++++++++++++++++++++++++++++++++"

# 将前景色和背景色设回白色. 
echo -ne '\E[37;47m'

# 画3条白线. 
for n in `seq 3`; do
      echo $BLANK80
done

# 将前景色设为黑色. 
echo -ne '\E[30m'

# 创建9个文件, 用来保存障碍物. 
for n in `seq 10 7 68`; do
      touch $n
done  

# 将脚本所要画的"马"设置为第一种类型. 
HORSE_TYPE=2

#  为每匹"马"创建位置文件和几率文件. 
#+ 在这些文件中, 保存马的当前位置, 
#+ 类型和几率. 
for HN in `seq 9`; do
      touch horse_${HN}_position
      touch odds_${HN}
      echo \-1 > horse_${HN}_position
      echo $HORSE_TYPE >>  horse_${HN}_position
      # 给马定义随机障碍物. 
       HANDICAP=`random_1_9`
      # 检查函数random_1_9是否返回一个有效值. 
      while ! echo $HANDICAP | grep [1-9] &> /dev/null; do
                HANDICAP=`random_1_9`
      done
      # 给马定义最后一个障碍物的位置. 
      LHP=`expr $HANDICAP \* 7 + 3`
      for FILE in `seq 10 7 $LHP`; do
            echo $HN >> $FILE
      done   
     
      # 计算几率. 
      case $HANDICAP in 
              1) ODDS=`echo $HANDICAP \* 0.25 + 1.25 | bc`
                                 echo $ODDS > odds_${HN}
              ;;
              2 | 3) ODDS=`echo $HANDICAP \* 0.40 + 1.25 | bc`
                                       echo $ODDS > odds_${HN}
              ;;
              4 | 5 | 6) ODDS=`echo $HANDICAP \* 0.55 + 1.25 | bc`
                                             echo $ODDS > odds_${HN}
              ;; 
              7 | 8) ODDS=`echo $HANDICAP \* 0.75 + 1.25 | bc`
                                       echo $ODDS > odds_${HN}
              ;; 
              9) ODDS=`echo $HANDICAP \* 0.90 + 1.25 | bc`
                                  echo $ODDS > odds_${HN}
      esac


done


# 打印几率. 
print_odds() {
tput cup 6 0
echo -ne '\E[30;42m'
for HN in `seq 9`; do
      echo "#$HN odds->" `cat odds_${HN}`
done
}

# 在起跑线上把马画出来. 
draw_horses() {
tput cup 6 0
echo -ne '\E[30;42m'
for HN in `seq 9`; do
      echo /\\$HN/\\"                               "
done
}

print_odds

echo -ne '\E[47m'
# 等待按下回车键, 按下之后就开始比赛. 
# 转义序列'\E[?25l'禁用光标. 
tput cup 17 0
echo -e '\E[?25l'Press [enter] key to start the race...
read -s

#  禁用了终端的常规echo功能. 
#  这么做用来避免在比赛中, 
#+ 按键所导致的"花"屏. 
stty -echo

# --------------------------------------------------------
# 开始比赛. 

draw_horses
echo -ne '\E[37;47m'
move_and_echo 18 1 $BLANK80
echo -ne '\E[30m'
move_and_echo 18 1 Starting...
sleep 1

# 设置终点线的列号. 
WINNING_POS=74

# 定义比赛开始的时间. 
START_TIME=`date +%s`

# 下面的"while"结构需要使用COL变量. 
COL=0    

while [ $COL -lt $WINNING_POS ]; do
                   
          MOVE_HORSE=0     
          
          # 检查random_1_9函数是否返回了有效值. 
          while ! echo $MOVE_HORSE | grep [1-9] &> /dev/null; do
                MOVE_HORSE=`random_1_9`
          done
          
          # 定义"随机抽取的马"的原来类型和位置. 
          HORSE_TYPE=`cat  horse_${MOVE_HORSE}_position | tail -1`
          COL=$(expr `cat  horse_${MOVE_HORSE}_position | head -1`) 
          
          ADD_POS=1
          # 判断当前位置是否存在障碍物. 
          if seq 10 7 68 | grep -w $COL &> /dev/null; then
                if grep -w $MOVE_HORSE $COL &> /dev/null; then
                      ADD_POS=0
                      grep -v -w  $MOVE_HORSE $COL > ${COL}_new
                      rm -f $COL
                      mv -f ${COL}_new $COL
                      else ADD_POS=1
                fi 
          else ADD_POS=1
          fi
          COL=`expr $COL + $ADD_POS`
          echo $COL >  horse_${MOVE_HORSE}_position  # 保存新位置. 
                            
         # 选择要画出来的马的类型. 
          case $HORSE_TYPE in 
                1) HORSE_TYPE=2; DRAW_HORSE=draw_horse_two
                ;;
                2) HORSE_TYPE=1; DRAW_HORSE=draw_horse_one 
          esac       
          echo $HORSE_TYPE >>  horse_${MOVE_HORSE}_position # 保存当前类型. 
         
          # 将前景色设为黑, 背景色设为绿. 
          echo -ne '\E[30;42m'
          
          # 将光标移动到马的新位置. 
          tput cup `expr $MOVE_HORSE + 5`  `cat  horse_${MOVE_HORSE}_position | head -1` 
          
          # 画马. 
          $DRAW_HORSE
           usleep $USLEEP_ARG
          
           # 当所有的马都越过第15行之后, 再次打印几率. 
           touch fieldline15
           if [ $COL = 15 ]; then
             echo $MOVE_HORSE >> fieldline15  
           fi
           if [ `wc -l fieldline15 | cut -f1 -d " "` = 9 ]; then
               print_odds
               : > fieldline15
           fi           
          
          # 取得领头的马. 
          HIGHEST_POS=`cat *position | sort -n | tail -1`          
          
          # 将背景色设为白. 
          echo -ne '\E[47m'
          tput cup 17 0
          echo -n Current leader: `grep -w $HIGHEST_POS *position | cut -c7`"                              "           

done  

# 定义比赛结束的时间. 
FINISH_TIME=`date +%s`

# 将背景色设置为绿色, 并且开启闪烁文本的功能. 
echo -ne '\E[30;42m'
echo -en '\E[5m'

# 让获胜的马闪烁. 
tput cup `expr $MOVE_HORSE + 5` `cat  horse_${MOVE_HORSE}_position | head -1`
$DRAW_HORSE

# 禁用闪烁文本. 
echo -en '\E[25m'

# 将前景色和背景色设置为白色. 
echo -ne '\E[37;47m'
move_and_echo 18 1 $BLANK80

# 将前景色设置为黑色. 
echo -ne '\E[30m'

# 让获胜的马闪烁. 
tput cup 17 0
echo -e "\E[5mWINNER: $MOVE_HORSE\E[25m""  Odds: `cat odds_${MOVE_HORSE}`"\
"  Race time: `expr $FINISH_TIME - $START_TIME` secs"

# 恢复光标, 恢复原来的颜色. 
echo -en "\E[?25h"
echo -en "\E[0m"

# 恢复打印功能. 
stty echo

# 删除掉和赛马有关的临时文件. 
rm -rf $HORSE_RACE_TMP_DIR

tput cup 19 0

exit 0
