var outlookbar=new outlook();
var t;

t=outlookbar.addtitle('退出系统','indexpage',1)
outlookbar.additem('进入欢迎页面',t,'/admin/manFrame')
outlookbar.additem('点击退出登录',t,'/admin/logout')
outlookbar.additem('点击帐号注销',t,'/admin/logout')


t=outlookbar.addtitle('监控管理','sysmonitor',1)
outlookbar.additem('查看应用状态',t,'/admin/SysCondition/APP')
outlookbar.additem('查看数据库状态',t,'/admin/SysCondition/DB')
outlookbar.additem('查看扫描端口',t,'/admin/SysCondition/SAFE')

t=outlookbar.addtitle('关键监控','sysmonitor',1)
outlookbar.additem('监控列表',t,'/admin/FocusServer')
outlookbar.additem('添加监控',t,'/admin/FocusServer_do')

t=outlookbar.addtitle('报警过滤','sysmonitor',1)
outlookbar.additem('规则列表',t,'/admin/Alarmfilter')
outlookbar.additem('添加规则',t,'/admin/Alarmfilter_do')

t=outlookbar.addtitle('基本操作','Serviceplatform',1)
outlookbar.additem('查看系统日志',t,'/system/3101')
outlookbar.additem('查看最新登录',t,'/system/3102')
outlookbar.additem('查看系统版本',t,'/system/3103')
outlookbar.additem('查看内核模块',t,'/system/3104')
outlookbar.additem('查看监听端口',t,'/system/3105')
outlookbar.additem('查看系统用户',t,'/system/3106')
outlookbar.additem('查看系统组员',t,'/system/3107')
outlookbar.additem('查看启动服务',t,'/system/3108')
outlookbar.additem('查看计划任务',t,'/system/3109')
outlookbar.additem('查看活动用户',t,'/system/3110')
outlookbar.additem('查看应用配置',t,'/system/3111')
outlookbar.additem('查看异常用户',t,'/system/3112')
outlookbar.additem('查看被控成员',t,'/system/3113')
outlookbar.additem('查看请求成员',t,'/system/3114')
outlookbar.additem('查看缓存状态',t,'/system/3115')
outlookbar.additem('查看应用日志',t,'/system/3116')
outlookbar.additem('查看系统时间',t,'/system/3117')
outlookbar.additem('查看squid信息',t,'/system/3118')
outlookbar.additem('查看GTMIP库',t,'/system/3119')
outlookbar.additem('GTMIP库查询',t,'/system/3120')
outlookbar.additem('查看IDCA拓扑',t,'/idca.html')
outlookbar.additem('查看IDCC拓扑',t,'/idcc.html')
outlookbar.additem('查看  FX 拓扑',t,'/fx.html')

t=outlookbar.addtitle('管理菜单','Serviceplatform',1)
outlookbar.additem('重启RESIN服务',t,'/system/3200')
outlookbar.additem('重启Nginx服务',t,'/system/3201')
outlookbar.additem('重启Haproxy服务',t,'/system/3202')
outlookbar.additem('应用爬虫分析',t,'/system/3203')
outlookbar.additem('同步应用文件',t,'/system/3204')
outlookbar.additem('刷新Nagios',t,'/system/3205')
outlookbar.additem('webcheck探测',t,'/system/3206')
outlookbar.additem('端口响应测试',t,'/system/3207')
outlookbar.additem('批量修改密码',t,'/system/3208')
outlookbar.additem('更新Iptables',t,'/system/3209')
outlookbar.additem('重启socket服务',t,'/system/3210')
outlookbar.additem('重启组件服务',t,'/system/3211')




t=outlookbar.addtitle('LVS管理','LVSmanagement',1)
outlookbar.additem('性能图表',t,'/lvs/Performance/lvsip')
outlookbar.additem('数据中心',t,'/lvs/DataCenters')
outlookbar.additem('虚拟IP池',t,'/lvs/VIP')
outlookbar.additem('主机管理',t,'/lvs/Servers')
outlookbar.additem('监控模块',t,'/lvs/Monitors')


t=outlookbar.addtitle('系统帮助','syshelp',1)
outlookbar.additem('帮助信息',t,'#')
outlookbar.additem('意见反馈',t,'#')
outlookbar.additem('与我联系',t,'#')
