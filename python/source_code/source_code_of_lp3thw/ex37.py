
print(
"""
现在该复习你学过的符号和 python 关键字了，而且你在本节还会学到一些新的 东西。我在这里所作的是将所有的 Python 符号和关键字列出来，这些都是值 得掌握的重点。
在这节课中，你需要复习每一个关键字，从记忆中想起它的作用并且写下来，接 着上网搜索它真正的功能。有些内容可能是无法搜索的，所以这对你可能有些难
度，不过你还是需要坚持尝试。

如果你发现记忆中的内容有误，就在索引卡片上写下正确的定义，试着将自己的 记忆纠正过来。如果你就是不知道它的定义，就把它也直接写下来，以后再做研究。
最后，将每一种符号和关键字用在程序里，你可以用一个小程序来做，也可以尽量多写一些程序来巩固记忆。这里的关键点是明白各个符号的作用，确认自己没搞错，如果搞错了就纠正过来，然后将其用在程序里，并且通过这样的方式巩固自己的记忆。

查看方法：

import keyword

keyword.kwlist

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def',
 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
)

print(
'''
# 关键词练习：
and ----------
as
assert
break
class
continue
def-----------
del
elif----------
else----------
except
exec
finally
for-----------
from-----------
global
if-------------
import---------
in
is
lambda
not------------
or-------------
pass
print----------
raise
return---------
try
while-----------
with
yield
------------------
新关键词学习：


assert: 断言

break：break是跳出整个循环，continue是跳出当前循环

class

continue：break是跳出整个循环，continue是跳出当前循环

del：删除



exec–eval–execfile ：exec是一条语句将字符串str当成有效的python代码来执行 ，eval与execfile是pytho内置函数 ，eval(str[globals[locals]])函数将字符串str当成有效的python表达式来求值，并提供返回计算值。execfile(filename)函数可以用来执行文件



global：声明全局变量

in

is

lambda—filter—map—reduce— lambda 只是一个表达式，定义了一个匿名函数，起到函数速写的作用。

pass——pass不做任何事情，一般用作占位语句，当你编写程序部分内容还没想好，可用pass语句占位

raise-if-not  ——raise 触发异常。

try-except-else-finally——如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。

with-as:


yield——yield的意思是生产，返回了一个生成器对象，每个生成器只能使用一次

die：py3里还有吗？


#学习地址
# http://blog.csdn.net/s1h2e3n4g5/article/details/76416257
'''
)

print(
"""
## 字符串转义序列（Escape Sequences）

- \\ 反斜杠
- \' 单引号
-\" 双引号
-\a 响铃符号？
-\b 退格符？
-\f 进纸符？
-\n 新起一行
-\r 回车符号。Carriage啥意思
-\t 水平制表符
-\v 垂直制表符
参见：http://blog.sina.com.cn/s/blog_5ffc44ab0102ux1h.html
##字符格式化（String Formats）
- %d
- %i
- %o
- %u
- %x
- %X
- %e
- %E
- %f
- %g
- %G
- %c
- %r
- %s
- %%
# 参见：http://blog.sina.com.cn/s/blog_5ffc44ab0102ux1i.html

# 操作符号
优秀符号你可能还不熟悉，不过还是意义看过去，研究一下她们的功能，记录下来日后解决。

+
-
*
**
/  除以
// Floor division ?
%  string interpolate or modulus?
<
>
<=
>=
== 等于
!= 不等于
< ># 现在不用了，就是不等于的意思。
( )
[ ] 列表
{ } 字典
@ decorators?
,
:
.
=
;
+=  加上然后等于
-= 减去然后等于
*= 乘以然后等于
/= 除以然后等于
//= floor除以然后等于
%= 模除然后等于
**= 乘方然后等于



"""
)
