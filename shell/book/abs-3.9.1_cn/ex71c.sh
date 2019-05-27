#!/bin/bash
#  一个使用'cat'的here document, 但是禁用了参数替换. 

NAME="John Doe"
RESPONDENT="the author of this fine script"  

cat &lt;&lt;'Endofmessage'

Hello, there, $NAME.
Greetings to you, $NAME, from $RESPONDENT.

Endofmessage

#  如果"limit string"被引用或转义的话, 那么就禁用了参数替换. 
#  下边的两种方式具有相同的效果. 
#  cat &lt;&lt;"Endofmessage"
#  cat &lt;&lt;\Endofmessage

exit 0
