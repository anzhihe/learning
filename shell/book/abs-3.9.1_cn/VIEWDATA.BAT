REM VIEWDATA

REM 灵感来自于例子"DOS POWERTOOLS"
REM                           PAUL SOMERSON编写


@ECHO OFF

IF !%1==! GOTO VIEWDATA
REM  如果没有命令行参数...
FIND "%1" C:\BOZO\BOOKLIST.TXT
GOTO EXIT0
REM  打印出字符串匹配的行, 然后退出. 

:VIEWDATA
TYPE C:\BOZO\BOOKLIST.TXT | MORE
REM  显示整个文件, 一次一页. 

:EXIT0
