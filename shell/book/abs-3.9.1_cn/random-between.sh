#!/bin/bash
# random-between.sh
# 产生两个指定值之间的随机数.
# 由Bill Gradwohl编写, 本书作者做了一些修改.
# 脚本作者允许在这里使用.


randomBetween() {
   #  在$min和$max之间,
   #+ 产生一个正的或负的随机数.
   #+ 并且可以被$divisibleBy所整除.
   #  给出一个合理的随机分配的返回值.
   #
   #  Bill Gradwohl - Oct 1, 2003

   syntax() {
   # 在函数中内嵌函数
      echo
      echo    "Syntax: randomBetween [min] [max] [multiple]"
      echo
      echo    "Expects up to 3 passed parameters, but all are completely optional."
      echo    "min is the minimum value"
      echo    "max is the maximum value"
      echo    "multiple specifies that the answer must be a multiple of this value."
      echo    "    i.e. answer must be evenly divisible by this number."
      echo    
      echo    "If any value is missing, defaults area supplied as: 0 32767 1"
      echo    "Successful completion returns 0, unsuccessful completion returns"
      echo    "function syntax and 1."
      echo    "The answer is returned in the global variable randomBetweenAnswer"
      echo    "Negative values for any passed parameter are handled correctly."
   }

   local min=${1:-0}
   local max=${2:-32767}
   local divisibleBy=${3:-1}
   # 默认值分配, 用来处理没有参数传递进来的情况.

   local x
   local spread

   # 确认divisibleBy是正值.
   [ ${divisibleBy} -lt 0 ] && divisibleBy=$((0-divisibleBy))

   # 完整性检查.
   if [ $# -gt 3 -o ${divisibleBy} -eq 0 -o  ${min} -eq ${max} ]; then 
      syntax
      return 1
   fi

   # 查看min和max是否颠倒了.
   if [ ${min} -gt ${max} ]; then
      # 交换它们.
      x=${min}
      min=${max}
      max=${x}
   fi

   #  如果min自己并不能够被$divisibleBy所整除,
   #+ 那么就调整max的值, 使其能够被$divisibleBy所整除, 前提是不能放大范围.
   if [ $((min/divisibleBy*divisibleBy)) -ne ${min} ]; then 
      if [ ${min} -lt 0 ]; then
         min=$((min/divisibleBy*divisibleBy))
      else
         min=$((((min/divisibleBy)+1)*divisibleBy))
      fi
   fi

   #  如果min自己并不能够被$divisibleBy所整除,
   #+ 那么就调整max的值, 使其能够被$divisibleBy所整除, 前提是不能放大范围.
   if [ $((max/divisibleBy*divisibleBy)) -ne ${max} ]; then 
      if [ ${max} -lt 0 ]; then
         max=$((((max/divisibleBy)-1)*divisibleBy))
      else
         max=$((max/divisibleBy*divisibleBy))
      fi
   fi

   #  ---------------------------------------------------------------------
   #  现在, 来做点真正的工作.

   #  注意, 为了得到对于端点来说合适的分配,
   #+ 随机值的范围不得不落在
   #+ 0 和 abs(max-min)+divisibleBy 之间, 而不是 abs(max-min)+1.

   #  对于端点来说,
   #+ 这个少量的增加将会产生合适的分配.

   #  如果修改这个公式, 使用 abs(max-min)+1 来代替 abs(max-min)+divisibleBy的话, 
   #+ 也能够得到正确的答案, 但是在这种情况下所生成的随机值对于正好为端点倍数
   #+ 的这种情况来说将是不完美的, 因为正好为端点倍数情况下的随机率比较低,
   #+ 因为你才加1而已, 这比正常的公式下所产生的几率要小的多(正常为加divisibleBy).
   #  ---------------------------------------------------------------------

   spread=$((max-min))
   [ ${spread} -lt 0 ] && spread=$((0-spread))
   let spread+=divisibleBy
   randomBetweenAnswer=$(((RANDOM%spread)/divisibleBy*divisibleBy+min))   

   return 0

   #  然而, Paulo Marcel Coelho Aragao 指出
   #+ 当 $max 和 $min 不能够被$divisibleBy所整除时,
   #+ 这个公式将会失败.
   #
   #  他建议使用如下公式:
   #    rnumber = $(((RANDOM%(max-min+1)+min)/divisibleBy*divisibleBy))

}

# 让我们测试一下这个函数.
min=-14
max=20
divisibleBy=3


#  产生一个所期望的数组answers, 数组下标用来表示在范围内可能出现的值,
#+ 而元素内容记录的是这个值所出现的次数, 如果我们循环足够多次, 那么我们一定会得到至少一次出现机会.

declare -a answer
minimum=${min}
maximum=${max}
   if [ $((minimum/divisibleBy*divisibleBy)) -ne ${minimum} ]; then 
      if [ ${minimum} -lt 0 ]; then
         minimum=$((minimum/divisibleBy*divisibleBy))
      else
         minimum=$((((minimum/divisibleBy)+1)*divisibleBy))
      fi
   fi


132    #  如果max本身并不能够被$divisibleBy整除,
133    #+ 那么就调整max的值, 使其能够被$divisibleBy整除, 前提是不能放大范围.

   if [ $((maximum/divisibleBy*divisibleBy)) -ne ${maximum} ]; then 
      if [ ${maximum} -lt 0 ]; then
         maximum=$((((maximum/divisibleBy)-1)*divisibleBy))
      else
         maximum=$((maximum/divisibleBy*divisibleBy))
      fi
   fi


#  我们需要产生一个下标全部为正的数组.
#+ 所以我们需要一个displacement, 
#+ 这样就可以保证结果都为正. 

displacement=$((0-minimum))
for ((i=${minimum}; i<=${maximum}; i+=divisibleBy)); do
   answer[i+displacement]=0
done


# 现在, 让我们循环足够多的次数, 来得到我们想要的答案.
loopIt=1000   #  脚本作者建议循环 100000 次,
              #+ 但是这需要的时间太长了.

for ((i=0; i<${loopIt}; ++i)); do

   #  注意, 我们在这里调用randomBetweenAnswer函数时, 估计将min和max颠倒顺序.
   #+ 这是为了测试在这种情况下, 此函数是否还能正确的运行.

   randomBetween ${max} ${min} ${divisibleBy}

   # 如果答案不是我们所期望的, 就报错.
   [ ${randomBetweenAnswer} -lt ${min} -o ${randomBetweenAnswer} -gt ${max} ] && echo MIN or MAX error - ${randomBetweenAnswer}!
   [ $((randomBetweenAnswer%${divisibleBy})) -ne 0 ] && echo DIVISIBLE BY error - ${randomBetweenAnswer}!

   # 将统计值保存到answer中.
   answer[randomBetweenAnswer+displacement]=$((answer[randomBetweenAnswer+displacement]+1))
done



# 让我们来察看一下结果.

for ((i=${minimum}; i<=${maximum}; i+=divisibleBy)); do
   [ ${answer[i+displacement]} -eq 0 ] && echo "We never got an answer of $i." || echo "${i} occurred ${answer[i+displacement]} times."
done


exit 0
