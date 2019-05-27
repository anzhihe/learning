#!/bin/bash
# poem.sh: 将本书作者非常喜欢的一首诗, 漂亮的打印出来. 

# 诗的行数(单节). 
Line[1]="I do not know which to prefer,"
Line[2]="The beauty of inflections"
Line[3]="Or the beauty of innuendoes,"
Line[4]="The blackbird whistling"
Line[5]="Or just after."

# 出处. 
Attrib[1]=" Wallace Stevens"
Attrib[2]="\"Thirteen Ways of Looking at a Blackbird\""
# 这首诗已经是公共版权了(版权已经过期了). 

echo

for index in 1 2 3 4 5    # 5行. 
do
  printf "     %s\n" "${Line[index]}"
done

for index in 1 2          # 出处为2行. 
do
  printf "          %s\n" "${Attrib[index]}"
done

echo

exit 0

# 练习:
# -----
# 修改这个脚本, 使其能够从一个文本数据文件中提取出一首诗的内容, 然后将其漂亮的打印出来. 
