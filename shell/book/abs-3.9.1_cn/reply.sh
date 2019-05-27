#!/bin/bash
# reply.sh

# REPLY是提供给'read'命令的默认变量.

echo
echo -n "What is your favorite vegetable? "
read

echo "Your favorite vegetable is $REPLY."
#  当且仅当没有变量提供给"read"命令时, 
#+ REPLY才保存最后一个"read"命令读入的值.

echo
echo -n "What is your favorite fruit? "
read fruit
echo "Your favorite fruit is $fruit."
echo "but..."
echo "Value of \$REPLY is still $REPLY."
#  $REPLY还是保存着上一个read命令的值,
#+ 因为变量$fruit被传入到了这个新的"read"命令中.

echo

exit 0
