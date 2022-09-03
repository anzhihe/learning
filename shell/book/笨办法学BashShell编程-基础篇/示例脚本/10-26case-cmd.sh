#!/bin/bash
# 使用命令替换来生成case变量

case $( arch ) in
  i386  ) echo "80386-base machine." ;;
  i486  ) echo "80486-base machine." ;;
  i586  ) echo "Pentium-base machine." ;;
  i686  ) echo "Pentium2+-base machine." ;;
  x86_64) echo "64-bit version x86 machine." ;;
  *     ) echo "Other type of machine." ;;
esac

exit 0 
