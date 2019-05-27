#!/bin/bash
# generate-script.sh
# 这个脚本的诞生基于Albert Reiner的一个主意. 

OUTFILE=generated.sh         # 所产生文件的名字. 


# -----------------------------------------------------------
# 'Here document包含了需要产生的脚本的代码. 
(
cat <<'EOF'
#!/bin/bash

echo "This is a generated shell script."
#  Note that since we are inside a subshell,
#+ we can't access variables in the "outside" script.

echo "Generated file will be named: $OUTFILE"
#  Above line will not work as normally expected
#+ because parameter expansion has been disabled.
#  Instead, the result is literal output.

a=7
b=3

let "c = $a * $b"
echo "c = $c"

exit 0
EOF
) > $OUTFILE
# -----------------------------------------------------------

#  将'limit string'引用起来将会阻止上边
#+ here document消息体中的变量扩展. 
#  这会使得输出文件中的内容保持here document消息体中的原文. 

if [ -f "$OUTFILE" ]
then
  chmod 755 $OUTFILE
  # 让所产生的文件具有可执行权限. 
else
  echo "Problem in creating file: \"$OUTFILE\""
fi

#  这个方法也可以用来产生
#+ C程序代码, Perl程序代码, Python程序代码, makefile, 
#+ 和其他的一些类似的代码. 
#  (译者注: 中间一段没译的注释将会被here document打印出来)
exit 0
