#!/bin/bash

# Shell命令可以放到Perl脚本的前面. 
echo "This precedes the embedded Perl script within \"$0\"."
echo "==============================================================="

perl -e 'print "This is an embedded Perl script.\n";'
# 类似于sed, Perl也可以使用"-e"选项. 

echo "==============================================================="
echo "However, the script may also contain shell and system commands."

exit 0
