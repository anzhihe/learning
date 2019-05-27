#!/bin/bash
# kill-process.sh

NOPROCESS=2

process=xxxyyyzzz  # 使用不存在的进程. 
# 只不过是为了演示...
# ... 并不想在这个脚本中杀掉任何真正的进程. 
#
# 举个例子, 如果你想使用这个脚本来断线Internet, 
#     process=pppd

t=`pidof $process`       # 取得$process的pid(进程id). 
# 'kill'只能使用pid(不能用程序名)作为参数. 

if [ -z "$t" ]           # 如果没这个进程, 'pidof' 返回空. 
then
  echo "Process $process was not running."
  echo "Nothing killed."
  exit $NOPROCESS
fi  

kill $t                  # 对于某些顽固的进程可能需要使用'kill -9'. 

# 这里需要做一个检查, 看看进程是否允许自身被kill. 
# 或许另一个 " t=`pidof $process` " 或许 ...


# 整个脚本都可以使用下边这句来替换: 
#        kill $(pidof -x process_name)
# 或者
#        killall process_name
# 但是这就没有教育意义了. 

exit 0
