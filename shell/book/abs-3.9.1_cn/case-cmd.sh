#!/bin/bash
# case-cmd.sh: 使用命令替换来产生"case"变量.

case $( arch ) in   # "arch" 返回机器体系的类型.
                    # 等价于 'uname -m' ...
i386 ) echo "80386-based machine";;
i486 ) echo "80486-based machine";;
i586 ) echo "Pentium-based machine";;
i686 ) echo "Pentium2+-based machine";;
*    ) echo "Other type of machine";;
esac

exit 0
