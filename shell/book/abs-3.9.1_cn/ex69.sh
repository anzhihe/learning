#!/bin/bash

# 用非交互的方式来使用'vi'编辑一个文件. 
# 模仿'sed'.

E_BADARGS=65

if [ -z "$1" ]
then
  echo "Usage: `basename $0` filename"
  exit $E_BADARGS
fi

TARGETFILE=$1

# 在文件中插入两行, 然后保存. 
#--------Begin here document-----------#
vi $TARGETFILE &lt;&lt;x23LimitStringx23
i
This is line 1 of the example file.
This is line 2 of the example file.
^[
ZZ
x23LimitStringx23
#----------End here document-----------#

#  注意上边^[是一个转义符, 键入Ctrl+v &lt;Esc&gt;就行,
#+ 事实上它是&lt;Esc&gt键;. 

#  Bram Moolenaar指出这种方法不能使用在'vim'上, (译者注: Bram Moolenaar是vim作者)
#+ 因为可能会存在终端相互影响的问题. 

exit 0
