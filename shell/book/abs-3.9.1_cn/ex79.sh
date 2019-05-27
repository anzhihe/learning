#!/bin/bash

# 纸牌: 
# 处理4人打牌. 

UNPICKED=0
PICKED=1

DUPE_CARD=99

LOWER_LIMIT=0
UPPER_LIMIT=51
CARDS_IN_SUIT=13
CARDS=52

declare -a Deck
declare -a Suits
declare -a Cards
#  使用一个3维数组来代替这3个一维数组来描述数据, 
#+ 可以更容易实现, 而且可以增加可读性. 
#  或许在Bash未来的版本上会支持多维数组. 


initialize_Deck ()
{
i=$LOWER_LIMIT
until [ "$i" -gt $UPPER_LIMIT ]
do
  Deck[i]=$UNPICKED   # 将整副"牌"的每一张都设置为无人持牌的状态. 
  let "i += 1"
done
echo
}

initialize_Suits ()
{
Suits[0]=C #梅花
Suits[1]=D #方块
Suits[2]=H #红心
Suits[3]=S #黑桃
}

initialize_Cards ()
{
Cards=(2 3 4 5 6 7 8 9 10 J Q K A)
# 另一种初始化数组的方法. 
}

pick_a_card ()
{
card_number=$RANDOM
let "card_number %= $CARDS"
if [ "${Deck[card_number]}" -eq $UNPICKED ]
then
  Deck[card_number]=$PICKED
  return $card_number
else  
  return $DUPE_CARD
fi
}

parse_card ()
{
number=$1
let "suit_number = number / CARDS_IN_SUIT"
suit=${Suits[suit_number]}
echo -n "$suit-"
let "card_no = number % CARDS_IN_SUIT"
Card=${Cards[card_no]}
printf %-4s $Card
# 使用整洁的列形式来打印每张牌. 
}

seed_random ()  # 种子随机数产生器. 
{               # 如果不这么做, 会发生什么? 
seed=`eval date +%s`
let "seed %= 32766"
RANDOM=$seed
#  还有其他的方法
#+ 能够产生种子随机数么? 
}

deal_cards ()
{
echo

cards_picked=0
while [ "$cards_picked" -le $UPPER_LIMIT ]
do
  pick_a_card
  t=$?

  if [ "$t" -ne $DUPE_CARD ]
  then
    parse_card $t

    u=$cards_picked+1
    # 将数组索引改为从1(译者注: 数组都是从0开始索引的)开始(临时的). 为什么? 
    let "u %= $CARDS_IN_SUIT"
    if [ "$u" -eq 0 ]   # 内嵌的if/then条件测试. 
    then
     echo
     echo
    fi
    # 分手. 

    let "cards_picked += 1"
  fi  
done  

echo

return 0
}


# 结构化编程: 
# 将函数中的整个程序逻辑模块化. 

#================
seed_random
initialize_Deck
initialize_Suits
initialize_Cards
deal_cards
#================

exit 0



# 练习1:
# 完整的注释这个脚本. 

# 练习2:
# 添加一个例程(函数)按照花色打印出每手牌. 
# 如果你喜欢, 可以添加任何你想要添加的代码. 

# 练习3:
# 简化并理顺脚本逻辑. 
