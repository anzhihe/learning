#!/bin/bash
# 一个使用'cat'命令的here document, 使用了参数替换. 

# 不传命令行参数给它,   ./scriptname
# 传一个命令行参数给它,   ./scriptname Mortimer
# 传一个包含2个单词(用引号括起来)的命令行参数给它, 
#                           ./scriptname "Mortimer Jones"

CMDLINEPARAM=1     #  所期望的最少的命令行参数个数. 

if [ $# -ge $CMDLINEPARAM ]
then
  NAME=$1          #  如果命令行参数超过1个, 
                   #+ 那么就只取第一个参数. 
else
  NAME="John Doe"  #  默认情况下, 如果没有命令行参数的话. 
fi  

RESPONDENT="the author of this fine script"  
  

cat &lt;&lt;Endofmessage

Hello, there, $NAME.
Greetings to you, $NAME, from $RESPONDENT.

# This comment shows up in the output (why?).

Endofmessage

# 注意上边的空行也打印输出, 
# 而上边那行"注释"当然也会打印到输出. 
# (译者注: 这就是为什么不翻译那行注释的原因, 尽量保持代码的原样)
exit 0
