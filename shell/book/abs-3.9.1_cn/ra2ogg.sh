#!/bin/bash
# ra2ogg.sh: 将音频流文件(*.ra)转换为ogg格式的文件.

# 使用"mplayer"媒体播放器程序:
#      http://www.mplayerhq.hu/homepage
#      可能需要安装合适的编解码程序(codec)才能够正常的运行这个脚本. 
# 需要使用"ogg"库和"oggenc":
#      http://www.xiph.org/


OFILEPREF=${1%%ra}      # 去掉"ra"后缀.
OFILESUFF=wav           # wav文件的后缀.
OUTFILE="$OFILEPREF""$OFILESUFF"
E_NOARGS=65

if [ -z "$1" ]          # 必须要指定一个需要转换的文件名.
then
  echo "Usage: `basename $0` [filename]"
  exit $E_NOARGS
fi


##########################################################################
mplayer "$1" -ao pcm:file=$OUTFILE
oggenc "$OUTFILE"  # oggenc编码后会自动加上正确的文件扩展名.
##########################################################################

rm "$OUTFILE"      # 删除中介的*.wav文件. 
                   # 如果你想保留这个文件的话, 可以把上边这行注释掉.

exit $?

#  注意:
#  ----
#  在网站上, 简单的在*.ram流音频文件上单击的话, 
#+ 一般都只会下载真正音频流文件(就是*.ra文件)的URL.
#  你可以使用"wget"或者一些类似的工具
#+ 来下载*.ra文件本身.


#  练习:
#  -----
#  像上面所看到的, 这个脚本只能够转换*.ra文件.
#  给这个脚本添加一些灵活性, 让它能够转换*.ram and other filenames.
#
#  如果你觉得这还不过瘾, 那么你可以扩展这个脚本, 
#+ 让它自动下载并转换音频流文件.
#  给出一个URL, (使用"wget")批处理下载音频流文件,
#+ 然后转换它们.
