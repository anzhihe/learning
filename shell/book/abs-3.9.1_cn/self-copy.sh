#!/bin/bash
# self-copy.sh

# 这个脚本会拷贝自身. 

file_subscript=copy

dd if=$0 of=$0.$file_subscript 2>/dev/null
# 阻止dd产生的消息:            ^^^^^^^^^^^

exit $?
