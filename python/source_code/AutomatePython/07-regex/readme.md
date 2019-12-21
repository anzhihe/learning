虽然在 Python 中使用正则表达式有几个步骤，但每一步都相当简单。
1． 用 import re 导入正则表达式模块。
import re
2．用 re.compile()函数创建一个 Regex 对象（记得使用原始字符串）。
regexObj = re.compile(r'\d{3}-\d{3}-\d{4}')
3．向 Regex 对象的 search()方法传入想查找的字符串。它返回一个 Match 对象。
mo = regexObj.search(strObj)
4．调用 Match 对象的 group()方法，返回实际匹配文本的字符串。
mo.group()

regex test site:
http://www.regexpal.com/

花括号的“非贪心” 版本匹配尽可能最短的字符串，即在结束的花括号后跟着一个问号。

\d 0 到 9 的任何数字
\D 除 0 到 9 的数字以外的任何字符
\w 任何字母、数字或下划线字符（可以认为是匹配“单词”字符）
\W 除字母、数字和下划线以外的任何字符
\s 空格、制表符或换行符（可以认为是匹配“空白”字符）
\S 除空格、制表符和换行符以外的任何字符


通过传入 re.DOTALL 作为 re.compile()的第二个参数， 可以让句点字符匹配所有字符， 包括换行字符。