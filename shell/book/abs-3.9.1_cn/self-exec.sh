#!/bin/bash
# self-exec.sh

echo

echo "This line appears ONCE in the script, yet it keeps echoing."
echo "The PID of this instance of the script is still $$."
#     上边这行展示了并没有fork出子shell.

echo "==================== Hit Ctl-C to exit ===================="

sleep 1

exec $0   #  产生了本脚本的另一个实例,
          #+ 但是这个新产生的实例却代替了原来的实例.

echo "This line will never echo!"  # 为什么不是这样?

exit 0
