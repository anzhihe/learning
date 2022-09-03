#!/bin/bash
# 设置read的超时时间

TMOUT=3 #设置Bash内置变量$TMOUT

echo "What is your favorite song?"
echo "Quickly now, you only hav $TMOUT seconds to answer!"
read song

if [ -z "$song" ]; then
  song="(no answer)"
fi

echo "Your favorite song is $song."
exit 0
