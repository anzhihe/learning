#!/bin/bash
# assert.sh

assert ()                 #  如果条件为false, 
{                         #+ 那么就打印错误信息并退出脚本. 
  E_PARAM_ERR=98
  E_ASSERT_FAILED=99


  if [ -z "$2" ]          # 传递进来的参数个数不够. 
  then
    return $E_PARAM_ERR   # 什么都不做就return. 
  fi

  lineno=$2

  if [ ! $1 ] 
  then
    echo "Assertion failed:  \"$1\""
    echo "File \"$0\", line $lineno"
    exit $E_ASSERT_FAILED
  # else
  #   返回
  #   然后继续执行脚本余下的代码. 
  fi  
}    


a=5
b=4
condition="$a -lt $b"     # 产生错误信息并退出脚本. 
                          #  尝试把这个"条件"放到其他的地方, 
                          #+ 然后看看发生了什么. 

assert "$condition" $LINENO
# 只有在"assert"成功时, 脚本余下的代码才会继续执行. 


# 这里放置的是其他的一些命令. 
# ...
echo "This statement echoes only if the \"assert\" does not fail."
# ...
# 这里也放置其他一些命令. 

exit 0
