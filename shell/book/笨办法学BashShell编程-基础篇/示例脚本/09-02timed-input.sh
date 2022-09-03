#!/bin/bash
# 采用trap来实现定时输入

TIMELIMIT=3

PrintAnswer()
{
  if [ "$answer" = "TIMEOUT" ]; then
    echo $answer
  else
    echo "Your favorite veggie is $answer."
    kill $!
  fi
}

TimerOn()
{
  sleep $TIMELIMIT && kill -s 14 $$ &
}

Int14Vector()
{
  answer="TIMEOUT"
  PrintAnswer
  exit 14
}

trap Int14Vector 14  # 定时中断14，会暗中给定时间限制

echo "What is your favorite vegetable? "
TimerOn

read answer
PrintAnswer

exit 0 
