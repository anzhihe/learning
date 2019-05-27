#! /bin/bash
# is-spammer.sh: 鉴别一个垃圾邮件域
                                                          
# $Id: is-spammer, v 1.4 2004/09/01 19:37:52 mszick Exp $
# 上边这行是RCS ID信息.
#                                                         
#  这是附件中捐献脚本is_spammer.bash
#+ 的一个简单版本.
                                                          
# is-spammer &lt;domain.name&gt;
                                                          
# 使用外部程序: 'dig'
# 测试版本: 9.2.4rc5
                                                          
# 使用函数. 
# 使用IFS来分析分配在数组中的字符串. 
# 做一些有用的事: 检查e-mail黑名单. 

# 使用来自文本体中的domain.name:
# http://www.good_stuff.spammer.biz/just_ignore_everything_else
#                       ^^^^^^^^^^^
# 或者使用来自任意e-mail地址的domain.name: 
# Really_Good_Offer@spammer.biz
#                                                               
# 并将其作为这个脚本的唯一参数.
#(另: 你的Inet连接应该保证连接好)
#                                                               
# 这样, 在上边两个实例中调用这个脚本:
#       is-spammer.sh spammer.biz


# Whitespace == :Space:Tab:Line Feed:Carriage Return:
WSP_IFS=$'\x20'$'\x09'$'\x0A'$'\x0D'

# No Whitespace == Line Feed:Carriage Return
No_WSP=$'\x0A'$'\x0D'

# 域分隔符为点分10进制ip地址
ADR_IFS=${No_WSP}'.'

# 取得dns文本资源记录. 
# get_txt &lt;error_code&gt; &lt;list_query&gt;
get_txt() {

    # 分析在"."中分配的$1.
    local -a dns
    IFS=$ADR_IFS
    dns=( $1 )
    IFS=$WSP_IFS
    if [ "${dns[0]}" == '127' ]
    then
        # 查看此处是否有原因.
        echo $(dig +short $2 -t txt)
    fi
}

# 取得dns地址资源纪录. 
# chk_adr &lt;rev_dns&gt; &lt;list_server&gt;
chk_adr() {
    local reply
    local server
    local reason

    server=${1}${2}
    reply=$( dig +short ${server} )

    # 假设应答可能是一个错误码 . . .
    if [ ${#reply} -gt 6 ]
    then
        reason=$(get_txt ${reply} ${server} )
        reason=${reason:-${reply}}
    fi
    echo ${reason:-' not blacklisted.'}
}

# 需要从名字中取得 IP 地址.
echo 'Get address of: '$1
ip_adr=$(dig +short $1)
dns_reply=${ip_adr:-' no answer '}
echo ' Found address: '${dns_reply}

# 一个可用的应答至少是4个数字加上3个点.
if [ ${#ip_adr} -gt 6 ]
then
    echo
    declare query

    # 通过点中的分配进行分析. 
    declare -a dns
    IFS=$ADR_IFS
    dns=( ${ip_adr} )
    IFS=$WSP_IFS

    # 用8进制表示法将dns查询循序记录起来. 
    rev_dns="${dns[3]}"'.'"${dns[2]}"'.'"${dns[1]}"'.'"${dns[0]}"'.'

# 查看: http://www.spamhaus.org (传统地址, 维护的很好)
    echo -n 'spamhaus.org says: '
    echo $(chk_adr ${rev_dns} 'sbl-xbl.spamhaus.org')

# 查看: http://ordb.org (开放转发Open mail relay)
    echo -n '   ordb.org  says: '
    echo $(chk_adr ${rev_dns} 'relays.ordb.org')

# 查看: http://www.spamcop.net/ (你可以在这里报告spammer)
    echo -n ' spamcop.net says: '
    echo $(chk_adr ${rev_dns} 'bl.spamcop.net')

# # # 其他的黑名单操作 # # #

# 查看: http://cbl.abuseat.org.
    echo -n ' abuseat.org says: '
    echo $(chk_adr ${rev_dns} 'cbl.abuseat.org')

# 查看: http://dsbl.org/usage (不同的邮件转发mail relay)
    echo
    echo 'Distributed Server Listings'
    echo -n '       list.dsbl.org says: '
    echo $(chk_adr ${rev_dns} 'list.dsbl.org')

    echo -n '   multihop.dsbl.org says: '
    echo $(chk_adr ${rev_dns} 'multihop.dsbl.org')

    echo -n 'unconfirmed.dsbl.org says: '
    echo $(chk_adr ${rev_dns} 'unconfirmed.dsbl.org')

else
    echo
    echo 'Could not use that address.'
fi

exit 0

# 练习:
# -----

# 1) 检查脚本参数, 
#    并且如果必要的话, 可以使用合适的错误消息退出.

# 2) 察看调用这个脚本的时候是否在线, 
#    并且如果必要的话, 可以使用合适的错误消息退出.

# 3) 用一般变量来替换掉"硬编码"的BHL domain.

# 4) 通过对'dig'命令使用"+time="选项
#    来给这个脚本设置一个暂停.
