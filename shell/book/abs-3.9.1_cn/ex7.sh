#!/bin/bash

var1=abcd-1234-defg
echo "var1 = $var1"

t=${var1#*-*}
echo "var1 (with everything, up to and including first - stripped out) = $t"
#  t=${var1#*-}  也一样,
#+ 因为#匹配最短的字符串,
#+ 同时*匹配任意前缀, 包括空字符串. 
# (感谢, Stephane Chazelas, 指出这点.)

t=${var1##*-*}
echo "If var1 contains a \"-\", returns empty string...   var1 = $t"


t=${var1%*-*}
echo "var1 (with everything from the last - on stripped out) = $t"

echo

# -------------------------------------------
path_name=/home/bozo/ideas/thoughts.for.today
# -------------------------------------------
echo "path_name = $path_name"
t=${path_name##/*/}
echo "path_name, stripped of prefixes = $t"
# 在这个特例中, 与	t=`basename $path_name`		效果相同. 
#  t=${path_name%/}; t=${t##*/}   是更一般的解决方法.
#+ 但有时还是会失败.
#  如果$path_name以一个换行符结尾的话, 那么	`basename $path_name` 就不能正常工作了,
#+ 但是上边的表达式可以.
# (感谢, S.C.)

t=${path_name%/*.*}
# 与	t=`dirname $path_name`	效果相同.
echo "path_name, stripped of suffixes = $t"
# 在某些情况下将失效, 比如 "../", "/foo////", # "foo/", "/".
#  删除后缀, 尤其是在basename没有后缀的情况下,
#+ 但是dirname可以, 不过这同时也使问题复杂化了.
# (感谢, S.C.)

echo

t=${path_name:11}
echo "$path_name, with first 11 chars stripped off = $t"
t=${path_name:11:5}
echo "$path_name, with first 11 chars stripped off, length 5 = $t"

echo

t=${path_name/bozo/clown}
echo "$path_name with \"bozo\" replaced  by \"clown\" = $t"
t=${path_name/today/}
echo "$path_name with \"today\" deleted = $t"
t=${path_name//o/O}
echo "$path_name with all o's capitalized = $t"
t=${path_name//o/}
echo "$path_name with all o's deleted = $t"

exit 0
