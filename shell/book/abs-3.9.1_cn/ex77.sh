#!/bin/bash

# 字符串扩展. 
# Bash版本2中引入的特性. 

#  $'xxx'格式的字符串
#+ 具备解释里面标准转义字符的能力. 

echo $'Ringing bell 3 times \a \a \a'
     # 可能在某些终端中, 只会响一次铃. 
echo $'Three form feeds \f \f \f'
echo $'10 newlines \n\n\n\n\n\n\n\n\n\n'
echo $'\102\141\163\150'   # Bash
                           # 8进制的等价字符. 

exit 0
