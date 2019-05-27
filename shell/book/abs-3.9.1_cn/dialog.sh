#!/bin/bash
# dialog.sh: 使用'gdialog'窗口部件. 
# 必须在你的系统上安装'gdialog'才能运行这个脚本. 
# 版本1.1 (04/05/05最后修正)

# 这个脚本的灵感来源于下面的文章. 
#     "Scripting for X Productivity," by Marco Fioretti,
#      LINUX JOURNAL, Issue 113, September 2003, pp. 86-9.
# 感谢你们, 所有的LINUX JOURNAL好人. 


# 在对话框窗口中的输入错误. 
E_INPUT=65
# 输入窗口的显示尺寸. 
HEIGHT=50
WIDTH=60

# 输出文件名(由脚本名构造). 
OUTFILE=$0.output

# 将脚本的内容显示到文本窗口中. 
gdialog --title "Displaying: $0" --textbox $0 $HEIGHT $WIDTH



# 现在, 我们将输入保存到文件中. 
echo -n "VARIABLE=" > $OUTFILE
gdialog --title "User Input" --inputbox "Enter variable, please:" \
$HEIGHT $WIDTH 2>> $OUTFILE


if [ "$?" -eq 0 ]
# 检查退出状态码, 是一个好习惯. 
then
  echo "Executed \"dialog box\" without errors."
else
  echo "Error(s) in \"dialog box\" execution."
        # 或者, 点"Cancel"按钮, 而不是"OK". 
  rm $OUTFILE
  exit $E_INPUT
fi



# 现在, 我们将重新获得并显示保存的变量. 
. $OUTFILE   # 'Source'(执行)保存的文件. 
echo "The variable input in the \"input box\" was: "$VARIABLE""


rm $OUTFILE  # 清除临时文件. 
             # 某些应用可能需要保留这个文件. 

exit $?
