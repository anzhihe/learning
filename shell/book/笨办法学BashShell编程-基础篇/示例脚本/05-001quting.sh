variable1="a variable containing five words"
COMMAND This is $variable1
# 这相当于传递给COMMND 7个参数
# "This" "is" "a" "variable" "containing" "five" "words"


COMMAND "This is $variable1"
# 这相当于传递给COMMND 1个参数
# "This is a variable containing five words"

variable2=""  # 空白
COMMNAD $varible2 $variable2 $variable2  	# 不带参数执行
COMMNAD "$varible2" "$variable2" "$variable2"  	# 带3个空参数执行
COMMNAD "$varible2 $variable2 $variable2"  	# 带1个空参数执行


