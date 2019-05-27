#!/bin/bash
# fc4upd.sh

# 脚本作者: Frank Wang.
# 本书作者作了少量修改.
# 授权在本书中使用.


#  使用rsync命令从镜像站点上下载Fedora 4的更新. 
#  为了节省空间, 如果有多个版本存在的话, 
#+ 只下载最新的包. 

URL=rsync://distro.ibiblio.org/fedora-linux-core/updates/
# URL=rsync://ftp.kddilabs.jp/fedora/core/updates/
# URL=rsync://rsync.planetmirror.com/fedora-linux-core/updates/

DEST=${1:-/var/www/html/fedora/updates/}
LOG=/tmp/repo-update-$(/bin/date +%Y-%m-%d).txt
PID_FILE=/var/run/${0##*/}.pid

E_RETURN=65        # 某些意想不到的错误.


# 一般rsync选项
# -r: 递归下载
# -t: 保存时间
# -v: verbose

OPTS="-rtv --delete-excluded --delete-after --partial"

# rsync include模式
# 开头的"/"会导致绝对路径名匹配. 
INCLUDE=(
    "/4/i386/kde-i18n-Chinese*" 
#   ^                         ^
# 双引号是必须的, 用来防止globbing.
) 


# rsync exclude模式
# 使用"#"临时注释掉一些不需要的包.
EXCLUDE=(
    /1
    /2
    /3
    /testing
    /4/SRPMS
    /4/ppc
    /4/x86_64
    /4/i386/debug
   "/4/i386/kde-i18n-*"
   "/4/i386/openoffice.org-langpack-*"
   "/4/i386/*i586.rpm"
   "/4/i386/GFS-*"
   "/4/i386/cman-*"
   "/4/i386/dlm-*"
   "/4/i386/gnbd-*"
   "/4/i386/kernel-smp*"
#  "/4/i386/kernel-xen*" 
#  "/4/i386/xen-*" 
)


init () {
    # 让管道命令返回可能的rsync错误, 比如, 网络延时(stalled network).
    set -o pipefail

    TMP=${TMPDIR:-/tmp}/${0##*/}.$$     # 保存精炼的下载列表.
    trap "{                                                   
        rm -f $TMP 2>/dev/null                                
    }" EXIT                             # 删除存在的临时文件.
}


check_pid () {
# 检查进程是否存在. 
    if [ -s "$PID_FILE" ]; then
        echo "PID file exists. Checking ..."
        PID=$(/bin/egrep -o "^[[:digit:]]+" $PID_FILE)
        if /bin/ps --pid $PID &>/dev/null; then
            echo "Process $PID found. ${0##*/} seems to be running!"
           /usr/bin/logger -t ${0##*/} \
                 "Process $PID found. ${0##*/} seems to be running!"
            exit $E_RETURN
        fi
        echo "Process $PID not found. Start new process . . ."
    fi
}


#  根据上边的模式,
#+ 设置整个文件的更新范围, 从root或$URL开始.
set_range () {
    include=
    exclude=
    for p in "${INCLUDE[@]}"; do
        include="$include --include \"$p\""
    done

    for p in "${EXCLUDE[@]}"; do
        exclude="$exclude --exclude \"$p\""
    done
}


# 获得并提炼rsync更新列表.
get_list () {
    echo $$ > $PID_FILE || {
        echo "Can't write to pid file $PID_FILE"
        exit $E_RETURN
    }

    echo -n "Retrieving and refining update list . . ."

    # 获得列表 -- 作为单个命令来运行rsync的话需要'eval'.
    # $3和$4是文件创建的日期和时间.
    # $5是完整的包名字.
    previous=
    pre_file=
    pre_date=0
    eval /bin/nice /usr/bin/rsync \
        -r $include $exclude $URL | \
        egrep '^dr.x|^-r' | \
        awk '{print $3, $4, $5}' | \
        sort -k3 | \
        { while read line; do
            # 获得这段运行的秒数, 过滤掉不用的包. 
            cur_date=$(date -d "$(echo $line | awk '{print $1, $2}')" +%s)
            #  echo $cur_date

            # 取得文件名. 
            cur_file=$(echo $line | awk '{print $3}')
            #  echo $cur_file

            # 如果可能的话, 从文件名中取得rpm的包名字. 
            if [[ $cur_file == *rpm ]]; then
                pkg_name=$(echo $cur_file | sed -r -e \
                    's/(^([^_-]+[_-])+)[[:digit:]]+\..*[_-].*$/\1/')
            else
                pkg_name=
            fi
            # echo $pkg_name

            if [ -z "$pkg_name" ]; then   #  如果不是一个rpm文件,
                echo $cur_file >> $TMP    #+ 然后添加到下载列表里.
            elif [ "$pkg_name" != "$previous" ]; then   # 发现一个新包.
                echo $pre_file >> $TMP                  # 输出最新的文件.
                previous=$pkg_name                      # 保存当前状态.
                pre_date=$cur_date
                pre_file=$cur_file
            elif [ "$cur_date" -gt "$pre_date" ]; then  #  如果是相同的包, 但是这个包更新一些, 
                pre_date=$cur_date                      #+ 那么就更新最新的. 
                pre_file=$cur_file
            fi
            done
            echo $pre_file >> $TMP                      #  TMP现在包含所有
                                                        #+ 提炼过的列表. 
            # echo "subshell=$BASH_SUBSHELL"

    }       # 这里的大括号是为了让最后这句"echo $pre_file >> $TMP"
            # 也能与整个循环一起放到同一个子shell ( 1 )中. 

    RET=$?  # 取得管道命令的返回状态. 

    [ "$RET" -ne 0 ] && {
        echo "List retrieving failed with code $RET"
        exit $E_RETURN
    }

    echo "done"; echo
}

# 真正的rsync下载部分. 
get_file () {

    echo "Downloading..."
    /bin/nice /usr/bin/rsync \
        $OPTS \
        --filter "merge,+/ $TMP" \
        --exclude '*'  \
        $URL $DEST     \
        | /usr/bin/tee $LOG

    RET=$?

        #  --filter merge,+/ 对于这个目的来说, 这句是至关重要的. 
        #  + 修饰语意为着包含, / 意味着绝对路径. 
        #  然后$TMP中排过序的列表将会包含升序的路径名, 
        #+ 并从"简化的流程"(shortcutting the circuit)中阻止下边的 --exclude '*'. 

    echo "Done"

    rm -f $PID_FILE 2>/dev/null

    return $RET
}

# -------
# Main
init
check_pid
set_range
get_list
get_file
RET=$?
# -------

if [ "$RET" -eq 0 ]; then
    /usr/bin/logger -t ${0##*/} "Fedora update mirrored successfully."
else
    /usr/bin/logger -t ${0##*/} "Fedora update mirrored with failure code: $RET"
fi

exit $RET
