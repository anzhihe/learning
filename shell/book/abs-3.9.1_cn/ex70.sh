#!/bin/bash

wall &lt;&lt;zzz23EndOfMessagezzz23
E-mail your noontime orders for pizza to the system administrator.
    (Add an extra dollar for anchovy or mushroom topping.)
# 附加的消息文本放在这里. 
# 注意: 'wall'命令会把注释行也打印出来. 
zzz23EndOfMessagezzz23

# 当然, 更有效率的做法是: 
#         wall &lt;message-file
#  然而, 将消息模版嵌入到脚本中
#+ 只是一种"小吃店"(译者注: 方便但是不卫生)的做法, 而且这种做法是一次性的. 

exit 0
