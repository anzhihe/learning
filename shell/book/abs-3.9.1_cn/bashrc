#===============================================================
#
# 个人的$HOME/.bashrc文件, 基于bash-2.05a(或更高版本)
#
# 最后更新日期: 星期2 4月15 20:32:34 CEST 2003
#
# 这个文件(一般情况下)被只会被交互式shell读取. 
# 这里可以定义你的别名, 函数, 
# 和其他的一些交互式特征, 比如你的提示符. 
#
# 这个文件(开始时)是为Solaris设计的, 
# 但是基于Redhat的默认.bashrc文件
# --> 为Linux修改. 
# 你在这里看到的大部分代码都是从网上找来的
# (即internet). 
# 这个bashrc文件有点挤 - 
# 记住, 它仅仅是个例子而已. 按照你自己的需求进行裁减. 
#
#
#===============================================================

# --> 注释由HOWTO的作者添加. 
# --> 然后又被ER编辑了一下 :-)

#--------------------------------------
# 如果有源代码的全局定义, 请在此处定义.
#--------------------------------------

if [ -f /etc/bashrc ]; then
        . /etc/bashrc   # --> 读取/etc/bashrc, 如果存在的话. 
fi

#-------------------------------------------------------------
# $DISPLAY的自动设置 (如果还没设置的话)
# 这用于linux - 可能运行的结果不同.... 
# 问题是不同的终端种类对于'who am i'来说, 
# 将会给出不同的答案......
# 我还没发现一种'通用'方法
#-------------------------------------------------------------

function get_xserver ()
{
    case $TERM in
	xterm )
            XSERVER=$(who am i | awk '{print $NF}' | tr -d ')''(' ) 
            # Ane-Pieter Wieringa建议使用下面这种方式:
            # I_AM=$(who am i)
            # SERVER=${I_AM#*(}
            # SERVER=${SERVER%*)}

            XSERVER=${XSERVER%%:*}
	    ;;
	aterm | rxvt)
 	# 找出一些运行在这里的代码.....
	    ;;
    esac  
}

if [ -z ${DISPLAY:=""} ]; then
    get_xserver
    if [[ -z ${XSERVER}  || ${XSERVER} == $(hostname) || ${XSERVER} == "unix" ]]; then 
	DISPLAY=":0.0"		# 在本地主机上显示
    else		
	DISPLAY=${XSERVER}:0.0	# 在远端主机上显示
    fi
fi

export DISPLAY

#----------
# 一些设置
#----------

ulimit -S -c 0		# 不需要任何coredump
set -o notify
set -o noclobber
set -o ignoreeof
set -o nounset
#set -o xtrace          # 对于调试来说非常有用

# 使能选项:
shopt -s cdspell
shopt -s cdable_vars
shopt -s checkhash
shopt -s checkwinsize
shopt -s mailwarn
shopt -s sourcepath
shopt -s no_empty_cmd_completion  # 仅限于bash>=2.04
shopt -s cmdhist
shopt -s histappend histreedit histverify
shopt -s extglob	# 对于complete命令(按情况补全)来说是必要的

# 禁用选项:
shopt -u mailwarn
unset MAILCHECK		# 当有邮件到达时, 我不希望我的shell提示我


export TIMEFORMAT=$'\nreal %3R\tuser %3U\tsys %3S\tpcpu %P\n'
export HISTIGNORE="&:bg:fg:ll:h"
export HOSTFILE=$HOME/.hosts	# 将远端主机的列表放入~/.hosts



#-----------------------
# 问候, 问侯报文等等...
#-----------------------

# 先定义一些颜色:
red='\e[0;31m'
RED='\e[1;31m'
blue='\e[0;34m'
BLUE='\e[1;34m'
cyan='\e[0;36m'
CYAN='\e[1;36m'
NC='\e[0m'              # 没有颜色
# --> 很好. 与使用"ansi.sys"的DOS效果相同. 

# 在黑色背景下看起来非常好.....
echo -e "${CYAN}This is BASH ${RED}${BASH_VERSION%.*}${CYAN} - DISPLAY on ${RED}$DISPLAY${NC}\n"
date
if [ -x /usr/games/fortune ]; then
    /usr/games/fortune -s     # 让我们的每天充满乐趣.... :-)
fi

function _exit()	# 在退出shell时运行的函数
{
    echo -e "${RED}Hasta la vista, baby${NC}"
}
trap _exit EXIT

#---------------
# Shell提示符
#---------------

if [[ "${DISPLAY#$HOST}" != ":0.0" &&  "${DISPLAY}" != ":0" ]]; then  
    HILIT=${red}   # 远端主机: 提示符为红
else
    HILIT=${cyan}  # 本地主机: 提示符为青色
fi

#  --> 下面提示符函数中\W和\w的替换实例, 
#+ --> 用来获得完整路径名的显示. 

function fastprompt()
{
    unset PROMPT_COMMAND
    case $TERM in
        *term | rxvt )
            PS1="${HILIT}[\h]$NC \W > \[\033]0;\${TERM} [\u@\h] \w\007\]" ;;
	linux )
	    PS1="${HILIT}[\h]$NC \W > " ;;
        *)
            PS1="[\h] \W > " ;;
    esac
}

function powerprompt()
{
    _powerprompt()
    {
        LOAD=$(uptime|sed -e "s/.*: \([^,]*\).*/\1/" -e "s/ //g")
    }

    PROMPT_COMMAND=_powerprompt
    case $TERM in
        *term | rxvt  )
            PS1="${HILIT}[\A \$LOAD]$NC\n[\h \#] \W > \[\033]0;\${TERM} [\u@\h] \w\007\]" ;;
        linux )
            PS1="${HILIT}[\A - \$LOAD]$NC\n[\h \#] \w > " ;;
        * )
            PS1="[\A - \$LOAD]\n[\h \#] \w > " ;;
    esac
}

powerprompt     # 这是默认提示符 - 可能比较慢
                # 如果很慢的话, 可以使用fastprompt来代替....

#===============================================================
#
# 别名和函数
#
# 事实上, 这里定义的一些函数非常大
# (比如'lowercase'), 但是我的机器是512M内存, 所以 .....
# 如果你想让这个文件小一点, 
# 可以将这些函数放到脚本中. 
#
# 其中的许多函数来自于bash-2.04
# 中的例子. 
#
#===============================================================

#-------------------
# 个人的别名
#-------------------

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'
# -> 防止偶然的文件误操作. 
alias mkdir='mkdir -p'

alias h='history'
alias j='jobs -l'
alias r='rlogin'
alias which='type -all'
alias ..='cd ..'
alias path='echo -e ${PATH//:/\\n}'
alias print='/usr/bin/lp -o nobanner -d $LPDEST'   # 假设LPDEST被定义
alias pjet='enscript -h -G -fCourier9 -d $LPDEST'  # 使用enscript的漂亮的打印
alias background='xv -root -quit -max -rmode 5'    # 将一张图片作为背景
alias du='du -kh'
alias df='df -kTh'

# 'ls'家族 (假定使用GNU ls)
alias la='ls -Al'               # 显示隐藏文件
alias ls='ls -hF --color'	# 为识别的文件类型添加颜色
alias lx='ls -lXB'              # 按扩展名排序
alias lk='ls -lSr'              # 按尺寸排序
alias lc='ls -lcr'		# 按修改时间排序
alias lu='ls -lur'		# 按访问时间排序
alias lr='ls -lR'               # 递归ls
alias lt='ls -ltr'              # 按日期排序
alias lm='ls -al |more'         # 管道给'more'
alias tree='tree -Csu'		# 'ls'的另一种好方法

# 裁减'less'
alias more='less'
export PAGER=less
export LESSCHARSET='latin1'
export LESSOPEN='|/usr/bin/lesspipe.sh %s 2>&-' # 如果lesspipe.sh存在, 就用这个
export LESS='-i -N -w  -z-4 -g -e -M -X -F -R -P%t?f%f \
:stdin .?pb%pb\%:?lbLine %lb:?bbByte %bb:-...'

# 拼写错误 - 纯粹个人喜好 :-)
alias xs='cd'
alias vf='cd'
alias moer='more'
alias moew='more'
alias kk='ll'

#----------------
# 一些有趣东西
#----------------

function xtitle ()
{
    case "$TERM" in
        *term | rxvt)
            echo -n -e "\033]0;$*\007" ;;
        *)  
	    ;;
    esac
}

# 别名...
alias top='xtitle Processes on $HOST && top'
alias make='xtitle Making $(basename $PWD) ; make'
alias ncftp="xtitle ncFTP ; ncftp"

# .. 和函数
function man ()
{
    for i ; do
	xtitle The $(basename $1|tr -d .[:digit:]) manual
	command man -F -a "$i"
    done
}

function ll(){ ls -l "$@"| egrep "^d" ; ls -lXB "$@" 2>&-| egrep -v "^d|total "; }
function te()  # xemacs/gnuserv的包装器
{
    if [ "$(gnuclient -batch -eval t 2>&-)" == "t" ]; then
        gnuclient -q "$@";
    else
        ( xemacs "$@" &);
    fi
}

#---------------------------
# 与文件和字符串相关的函数:
#---------------------------

# 使用名字模式来查找文件:
function ff() { find . -type f -iname '*'$*'*' -ls ; }
# 使用pattern $1和Execute $2来查找文件: 
function fe() { find . -type f -iname '*'$1'*' -exec "${2:-file}" {} \;  ; }
# 在一系列文件中找到模式, 并高亮
function fstr()
{
    OPTIND=1
    local case=""
    local usage="fstr: find string in files.
Usage: fstr [-i] \"pattern\" [\"filename pattern\"] "
    while getopts :it opt
    do
        case "$opt" in
        i) case="-i " ;;
        *) echo "$usage"; return;;
        esac
    done
    shift $(( $OPTIND - 1 ))
    if [ "$#" -lt 1 ]; then
        echo "$usage"
        return;
    fi
    local SMSO=$(tput smso)
    local RMSO=$(tput rmso)
    find . -type f -name "${2:-*}" -print0 | xargs -0 grep -sn ${case} "$1" 2>&- | \
sed "s/$1/${SMSO}\0${RMSO}/gI" | more
}

function cuttail() # 在文件中切掉n行, 默认为10行
{
    nlines=${2:-10}
    sed -n -e :a -e "1,${nlines}!{P;N;D;};N;ba" $1
}

function lowercase()  # 将文件名转换为小写
{
    for file ; do
        filename=${file##*/}
        case "$filename" in
        */*) dirname==${file%/*} ;;
        *) dirname=.;;
        esac
        nf=$(echo $filename | tr A-Z a-z)
        newname="${dirname}/${nf}"
        if [ "$nf" != "$filename" ]; then
            mv "$file" "$newname"
            echo "lowercase: $file --> $newname"
        else
            echo "lowercase: $file not changed."
        fi
    done
}

function swap()         # 交换两个文件名
{
    local TMPFILE=tmp.$$
    mv "$1" $TMPFILE
    mv "$2" "$1"
    mv $TMPFILE "$2"
}


#----------------------
# 进程/系统相关的函数:
#----------------------

function my_ps() { ps $@ -u $USER -o pid,%cpu,%mem,bsdtime,command ; }
function pp() { my_ps f | awk '!/awk/ && $0~var' var=${1:-".*"} ; }

# 这个函数与linux上的'killall'基本一致
# 但是与Solaris上的却不相同
function killps()   # 按进程名进行kill
{
    local pid pname sig="-TERM"   # 默认signal
    if [ "$#" -lt 1 ] || [ "$#" -gt 2 ]; then
        echo "Usage: killps [-SIGNAL] pattern"
        return;
    fi
    if [ $# = 2 ]; then sig=$1 ; fi
    for pid in $(my_ps| awk '!/awk/ && $0~pat { print $1 }' pat=${!#} ) ; do
        pname=$(my_ps | awk '$1~var { print $5 }' var=$pid )
        if ask "Kill process $pid <$pname> with signal $sig?"
            then kill $sig $pid
        fi
    done
}

function my_ip() # 获得IP地址
{
    MY_IP=$(/sbin/ifconfig ppp0 | awk '/inet/ { print $2 } ' | sed -e s/addr://)
    MY_ISP=$(/sbin/ifconfig ppp0 | awk '/P-t-P/ { print $3 } ' | sed -e s/P-t-P://)
}

function ii()   # 获得当前主机相关的信息
{
    echo -e "\nYou are logged on ${RED}$HOST"
    echo -e "\nAdditionnal information:$NC " ; uname -a
    echo -e "\n${RED}Users logged on:$NC " ; w -h
    echo -e "\n${RED}Current date :$NC " ; date
    echo -e "\n${RED}Machine stats :$NC " ; uptime
    echo -e "\n${RED}Memory stats :$NC " ; free
    my_ip 2>&- ;
    echo -e "\n${RED}Local IP Address :$NC" ; echo ${MY_IP:-"Not connected"}
    echo -e "\n${RED}ISP Address :$NC" ; echo ${MY_ISP:-"Not connected"}
    echo
}

# 杂项工具:

function repeat()       # 重复n次的命令
{
    local i max
    max=$1; shift;
    for ((i=1; i <= max ; i++)); do  # --> C风格的语法
        eval "$@";
    done
}

function ask()
{
    echo -n "$@" '[y/n] ' ; read ans
    case "$ans" in
        y*|Y*) return 0 ;;
        *) return 1 ;;
    esac
}

#=========================================================================
#
# 按情况补全, complete命令 - BASH-2.04及其后续版本
# 大部分摘自bash 2.05文档
# 和Ian McDonalds的'Bash completion'软件包(http://www.caliban.org/bash/index.shtml#completion)
# 某些特征可能需要使用bash-2.05a
#
#=========================================================================

if [ "${BASH_VERSION%.*}" \< "2.05" ]; then
    echo "You will need to upgrade to version 2.05 for programmable completion"
    return
fi

shopt -s extglob        # 必须的
set +o nounset          # 否则某些自动补全将会失败

complete -A hostname   rsh rcp telnet rlogin r ftp ping disk
complete -A export     printenv
complete -A variable   export local readonly unset
complete -A enabled    builtin
complete -A alias      alias unalias
complete -A function   function
complete -A user       su mail finger

complete -A helptopic  help     # 通常与内建命令一样
complete -A shopt      shopt
complete -A stopped -P '%' bg
complete -A job -P '%'     fg jobs disown

complete -A directory  mkdir rmdir
complete -A directory   -o default cd

# 压缩
complete -f -o default -X '*.+(zip|ZIP)'  zip
complete -f -o default -X '!*.+(zip|ZIP)' unzip
complete -f -o default -X '*.+(z|Z)'      compress
complete -f -o default -X '!*.+(z|Z)'     uncompress
complete -f -o default -X '*.+(gz|GZ)'    gzip
complete -f -o default -X '!*.+(gz|GZ)'   gunzip
complete -f -o default -X '*.+(bz2|BZ2)'  bzip2
complete -f -o default -X '!*.+(bz2|BZ2)' bunzip2
# Postscript,pdf,dvi.....(译者: 打印格式相关)
complete -f -o default -X '!*.ps'  gs ghostview ps2pdf ps2ascii
complete -f -o default -X '!*.dvi' dvips dvipdf xdvi dviselect dvitype
complete -f -o default -X '!*.pdf' acroread pdf2ps
complete -f -o default -X '!*.+(pdf|ps)' gv
complete -f -o default -X '!*.texi*' makeinfo texi2dvi texi2html texi2pdf
complete -f -o default -X '!*.tex' tex latex slitex
complete -f -o default -X '!*.lyx' lyx
complete -f -o default -X '!*.+(htm*|HTM*)' lynx html2ps
# 多媒体
complete -f -o default -X '!*.+(jp*g|gif|xpm|png|bmp)' xv gimp
complete -f -o default -X '!*.+(mp3|MP3)' mpg123 mpg321
complete -f -o default -X '!*.+(ogg|OGG)' ogg123



complete -f -o default -X '!*.pl'  perl perl5

# 这是一个'通用的'补全函数 - 当命令具有一个所谓的"长选项"模式it works when commands have
# 的时候, 它就会工作, 比如: 'ls --all' 代替 'ls -a'

_get_longopts () 
{ 
    $1 --help | sed  -e '/--/!d' -e 's/.*--\([^[:space:].,]*\).*/--\1/'| \
grep ^"$2" |sort -u ;
}

_longopts_func ()
{
    case "${2:-*}" in
	-*)	;;
	*)	return ;;
    esac

    case "$1" in
	\~*)	eval cmd="$1" ;;
	*)	cmd="$1" ;;
    esac
    COMPREPLY=( $(_get_longopts ${1} ${2} ) )
}
complete  -o default -F _longopts_func configure bash
complete  -o default -F _longopts_func wget id info a2ps ls recode


_make_targets ()
{
    local mdef makef gcmd cur prev i

    COMPREPLY=()
    cur=${COMP_WORDS[COMP_CWORD]}
    prev=${COMP_WORDS[COMP_CWORD-1]}

    # 如果之前的参数为-f, 那就返回可能的补全文件名. 
    # 我们可以让它更智能一些, 并且返回匹配的
    # `makefile Makefile *.mk', 不管存在与否
    case "$prev" in
        -*f)    COMPREPLY=( $(compgen -f $cur ) ); return 0;;
    esac

    # 如果我们需要一个选项, 那就返回可能的posix选项
    case "$cur" in
        -)      COMPREPLY=(-e -f -i -k -n -p -q -r -S -s -t); return 0;;
    esac

    # 前尝试`makefile'再尝试`Makefile'
    if [ -f makefile ]; then
        mdef=makefile
    elif [ -f Makefile ]; then
        mdef=Makefile
    else
        mdef=*.mk               # 局部约定
    fi

    # 在我们扫描目标文件之前, 察看makefile文件名是否
    # 使用-f指定
    for (( i=0; i < ${#COMP_WORDS[@]}; i++ )); do
        if [[ ${COMP_WORDS[i]} == -*f ]]; then
            eval makef=${COMP_WORDS[i+1]}       # eval for tilde expansion(波浪号扩展)
            break
        fi
    done

        [ -z "$makef" ] && makef=$mdef

    # 如果我们有特别偏爱的补全单词, 
    # 那么可以限制的补全这个单词
    if [ -n "$2" ]; then gcmd='grep "^$2"' ; else gcmd=cat ; fi

    # 如果我们不想使用*.mk, 我们可以使用
    # 或者使用test -f $makef或者使用输入重定向
    COMPREPLY=( $(cat $makef 2>/dev/null | awk 'BEGIN {FS=":"} /^[^.#   ][^=]*:/ {print $1}' | tr -s ' ' '\012' | sort -u | eval $gcmd ) )
}

complete -F _make_targets -X '+($*|*.[cho])' make gmake pmake


# cvs(1) 补全
_cvs ()
{
    local cur prev
    COMPREPLY=()
    cur=${COMP_WORDS[COMP_CWORD]}
    prev=${COMP_WORDS[COMP_CWORD-1]}

    if [ $COMP_CWORD -eq 1 ] || [ "${prev:0:1}" = "-" ]; then
        COMPREPLY=( $( compgen -W 'add admin checkout commit diff \
        export history import log rdiff release remove rtag status \
        tag update' $cur ))
    else
        COMPREPLY=( $( compgen -f $cur ))
    fi
    return 0
}
complete -F _cvs cvs

_killall ()
{
    local cur prev
    COMPREPLY=()
    cur=${COMP_WORDS[COMP_CWORD]}

    # 获得进程列表(第一个sed表达式处理
    # swap out出去的进程, 第二个
    # 获得进程的basename)
    COMPREPLY=( $( /usr/bin/ps -u $USER -o comm  | \
        sed -e '1,1d' -e 's#[]\[]##g' -e 's#^.*/##'| \
        awk '{if ($0 ~ /^'$cur'/) print $0}' ))

    return 0
}

complete -F _killall killall killps


# 一个元命令补全函数, 用于sudo(8)这种命令, 
# 需要先对这个命令进行补全, 然后需要按照这个命令自己的补全定义进行补全
#  - 当前并不是非常可靠(比如 mount和umount命令
# 就不能很好的工作), 但还是很有用的 - 作者, Ian McDonald, 我修改了一下. 

_my_command()
{
    local cur func cline cspec
    
    COMPREPLY=()
    cur=${COMP_WORDS[COMP_CWORD]}

    if [ $COMP_CWORD = 1 ]; then
	COMPREPLY=( $( compgen -c $cur ) )
    elif complete -p ${COMP_WORDS[1]} &>/dev/null; then
	cspec=$( complete -p ${COMP_WORDS[1]} )
	if [ "${cspec%%-F *}" != "${cspec}" ]; then
	    # complete -F &lt;function&gt;
	    #
	    # COMP_CWORD和COMP_WORDS()不是只读的,
	    # 所以我们可以在传递到补全例程之前, 
	    # 设置它们
	
	    # 设置当前的标志号减1
	    COMP_CWORD=$(( $COMP_CWORD - 1 ))
	    # 获得函数名
	    func=${cspec#*-F }
	    func=${func%% *}
	    # 获得去掉第一个命令后的命令行
	    cline="${COMP_LINE#$1 }"
	    # 分离当前命令, 传递给数组
		COMP_WORDS=( $cline )
	    $func $cline
	elif [ "${cspec#*-[abcdefgjkvu]}" != "" ]; then
	    # complete -[abcdefgjkvu]
	    #func=$( echo $cspec | sed -e 's/^.*\(-[abcdefgjkvu]\).*$/\1/' )
	    func=$( echo $cspec | sed -e 's/^complete//' -e 's/[^ ]*$//' )
	    COMPREPLY=( $( eval compgen $func $cur ) )
	elif [ "${cspec#*-A}" != "$cspec" ]; then
	    # complete -A &lt;type&gt;
	    func=${cspec#*-A }
	func=${func%% *}
	COMPREPLY=( $( compgen -A $func $cur ) )
	fi
    else
	COMPREPLY=( $( compgen -f $cur ) )
    fi
}


complete -o default -F _my_command nohup exec eval trace truss strace sotruss gdb
complete -o default -F _my_command command type which man nice

# 本地变量:
# mode:shell-script
# sh-shell:bash
# End:
