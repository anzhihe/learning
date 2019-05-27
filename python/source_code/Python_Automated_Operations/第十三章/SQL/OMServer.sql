-- phpMyAdmin SQL Dump
-- version 3.4.8
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2014 年 07 月 13 日 16:12
-- 服务器版本: 5.5.28
-- PHP 版本: 5.2.17p1

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `OMServer`
--

-- --------------------------------------------------------

--
-- 表的结构 `module_list`
--

CREATE TABLE IF NOT EXISTS `module_list` (
  `ID` int(11) NOT NULL AUTO_INCREMENT COMMENT '模块ID号',
  `module_name` char(20) NOT NULL COMMENT '模块名称',
  `module_caption` char(255) NOT NULL COMMENT '模块功能描述',
  `module_extend` varchar(2000) NOT NULL COMMENT '模块前端扩展',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='模块列表' AUTO_INCREMENT=1008 ;

--
-- 转存表中的数据 `module_list`
--

INSERT INTO `module_list` (`ID`, `module_name`, `module_caption`, `module_extend`) VALUES
(1001, '查看系统日志', '[<b>功能说明</b>]<br> 查看所选服务器的操作系统日志信息', '返回信息行数：<input name="sys_param_1" id="sys_param_1" type="text" size="5" maxlength="3" value="50">'),
(1002, '查看最新登录', '[<b>功能说明</b>]<br> 查看所选服务器的最近的用户登录信息', '返回信息行数：<input name="sys_param_1" id="sys_param_1" type="text" size="5" maxlength="3" value="50">'),
(1003, '查看系统版本', '[<b>功能说明</b>]<br> 查看所选服务器操作系统的版本信息', ''),
(1004, '查看内核模块', '[<b>功能说明</b>]<br> 查看所选服务器操作系统的内核模块信息', ''),
(1005, '同步应用文件', '[<b>功能说明</b>]<br> 同步选择的应用文件(可动态添加)到所选的目标服务器', '选择同步文件：<select name="sys_param_1" id="sys_param_1"> <option value="nginx" selected>nginx启动脚本</option> <option value="nginx_config">nginx配置文件 </option> <option value="haproxy" selected>Haproxy配置文件</option> <option value="syslog" selected>syslog配置文件</option> <option value="sysctl" selected>sysctl配置文件</option> <option value="resin" selected>resin配置文件</option> <option value="resinhttpd" selected>resin_httpd</option> <option value="resinjar" selected>resin.jar</option> </select>'),
(1006, '查看应用配置', '[<b>功能说明</b>]<br> 查看指定的服务的配置信息', '进程服务名称：<select name="sys_param_1" id="sys_param_1">  <option value="resin" selected>resin</option>  <option value="nginx">nginx</option>  <option value="haproxy">haproxy</option>  <option value="apache">apache</option>  <option value="mysql">mysql</option>  <option value="lighttpd">lighttpd</option></select>'),
(1007, '重启进程服务', '[<b>功能说明</b>]<br> 重启目标服务器的指定的进程或服务', '进程服务名称： <select name="sys_param_1" id="sys_param_1">   <option value="resin" selected>resin</option>   <option value="nginx">nginx</option>   <option value="haproxy">haproxy</option>   <option value="apache">apache</option>   <option value="mysql">mysql</option>   <option value="lighttpd">lighttpd</option> </select>');

-- --------------------------------------------------------

--
-- 表的结构 `server_app_categ`
--

CREATE TABLE IF NOT EXISTS `server_app_categ` (
  `ID` int(11) NOT NULL AUTO_INCREMENT COMMENT '服务应用分类ID',
  `server_categ_id` int(11) NOT NULL COMMENT '服务功能分类ID',
  `app_categ_name` char(30) NOT NULL COMMENT '服务应用分类名称',
  PRIMARY KEY (`ID`),
  KEY `server_app_categ_ibfk_1` (`server_categ_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='服务应用分类表' AUTO_INCREMENT=3 ;

--
-- 转存表中的数据 `server_app_categ`
--

INSERT INTO `server_app_categ` (`ID`, `server_categ_id`, `app_categ_name`) VALUES
(1, 11, 'www.domain.com'),
(2, 11, 'bbs.domain.com');

-- --------------------------------------------------------

--
-- 表的结构 `server_fun_categ`
--

CREATE TABLE IF NOT EXISTS `server_fun_categ` (
  `ID` int(11) NOT NULL AUTO_INCREMENT COMMENT '服务功能分类ID',
  `server_categ_name` char(20) NOT NULL COMMENT '服务功能分类名称',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='服务功能分类表' AUTO_INCREMENT=14 ;

--
-- 转存表中的数据 `server_fun_categ`
--

INSERT INTO `server_fun_categ` (`ID`, `server_categ_name`) VALUES
(1, 'Linux.Lbalancing'),
(2, 'Linux.Sysadmin'),
(3, 'Linux.Backup'),
(4, 'Linux.Ice'),
(5, 'Linux.Logs'),
(6, 'Linux.Hadoop'),
(7, 'Linux.Cache'),
(8, 'Linux.Memcached'),
(9, 'Linux.Mysql'),
(10, 'Linux.Proxy'),
(11, 'Linux.Web'),
(12, 'Windows.Mssql'),
(13, 'Windows.Web');

-- --------------------------------------------------------

--
-- 表的结构 `server_history`
--

CREATE TABLE IF NOT EXISTS `server_history` (
  `ID` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `history_id` int(11) NOT NULL COMMENT '事件ID',
  `history_ip` char(15) NOT NULL COMMENT '事件IP地址',
  `history_user` char(15) NOT NULL COMMENT '事件用户名',
  `history_datetime` datetime NOT NULL COMMENT '事件时间',
  `db_datetime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '入库时间',
  `history_command` char(255) NOT NULL COMMENT '事件命令',
  PRIMARY KEY (`ID`),
  KEY `history_ip` (`history_ip`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT='操作事件表' AUTO_INCREMENT=1220 ;

--
-- 转存表中的数据 `server_history`
--

INSERT INTO `server_history` (`ID`, `history_id`, `history_ip`, `history_user`, `history_datetime`, `db_datetime`, `history_command`) VALUES
(1, 82, '192.168.1.20', 'root', '2014-06-02 15:29:06', '2014-06-02 08:12:09', 'df -m'),
(2, 82, '192.168.1.20', 'root', '2014-06-02 15:29:06', '2014-06-02 08:21:28', 'df -m'),
(3, 82, '192.168.1.20', 'root', '2014-06-02 15:29:06', '2014-06-02 08:34:11', 'df -m'),
(4, 90, '192.168.1.20', 'root', '2014-06-02 15:55:08', '2014-06-02 08:48:03', 'vi /etc/hosts'),
(5, 90, '192.168.1.20', 'root', '2014-06-02 15:55:08', '2014-06-02 09:01:28', 'vi /etc/hosts'),
(6, 97, '192.168.1.20', 'root', '2014-06-02 16:24:42', '2014-06-02 09:07:12', 'last'),
(7, 98, '192.168.1.20', 'root', '2014-06-02 16:25:34', '2014-06-02 09:08:04', 'time'),
(8, 99, '192.168.1.20', 'root', '2014-06-02 16:25:35', '2014-06-02 09:08:05', 'date'),
(9, 100, '192.168.1.20', 'root', '2014-06-02 16:25:41', '2014-06-02 09:08:11', 'ps -ef|grep java'),
(10, 101, '192.168.1.20', 'root', '2014-06-02 16:25:48', '2014-06-02 09:08:18', 'ps -ef|grep nginx'),
(11, 102, '192.168.1.20', 'root', '2014-06-02 16:26:04', '2014-06-02 09:08:33', 'df -h'),
(26, 104, '192.168.1.20', 'root', '2014-06-02 16:27:39', '2014-06-02 09:10:08', 'history'),
(27, 105, '192.168.1.20', 'root', '2014-06-03 13:20:52', '2014-06-03 05:48:52', 'update time.com.cn'),
(28, 106, '192.168.1.20', 'root', '2014-06-03 13:21:40', '2014-06-03 05:49:40', 'll'),
(29, 106, '192.168.1.20', 'root', '2014-06-03 13:21:40', '2014-06-03 05:49:49', 'll'),
(30, 107, '192.168.1.20', 'root', '2014-06-03 13:22:03', '2014-06-03 05:49:58', 'dig www.hainan.net'),
(31, 108, '192.168.1.20', 'root', '2014-06-03 13:27:34', '2014-06-03 05:55:39', 'vi /etc/profile'),
(32, 109, '192.168.1.20', 'root', '2014-06-03 13:27:48', '2014-06-03 05:55:41', 'source /etc/profile'),
(33, 101, '192.168.1.20', 'root', '2014-06-03 13:27:56', '2014-06-03 05:55:54', 'exit'),
(34, 101, '192.168.1.20', 'root', '2014-06-03 13:27:56', '2014-06-03 05:55:56', 'exit'),
(35, 101, '192.168.1.20', 'root', '2014-06-03 13:27:56', '2014-06-03 05:55:58', 'exit'),
(36, 102, '192.168.1.20', 'root', '2014-06-03 13:28:37', '2014-06-03 05:56:30', 'df'),
(37, 103, '192.168.1.20', 'root', '2014-06-03 13:29:17', '2014-06-03 05:57:10', 'nohup ls &'),
(38, 103, '192.168.1.20', 'root', '2014-06-03 13:29:17', '2014-06-03 05:57:13', 'nohup ls &'),
(39, 104, '192.168.1.20', 'root', '2014-06-03 13:29:23', '2014-06-03 05:57:16', 'nohup ls'),
(40, 104, '192.168.1.20', 'root', '2014-06-03 13:29:23', '2014-06-03 05:57:34', 'nohup ls'),
(41, 104, '192.168.1.20', 'root', '2014-06-03 13:29:23', '2014-06-03 05:57:35', 'nohup ls'),
(42, 104, '192.168.1.20', 'root', '2014-06-03 13:29:23', '2014-06-03 05:57:35', 'nohup ls'),
(43, 104, '192.168.1.20', 'root', '2014-06-03 13:29:23', '2014-06-03 05:57:35', 'nohup ls'),
(44, 104, '192.168.1.20', 'root', '2014-06-03 13:29:23', '2014-06-03 05:57:35', 'nohup ls');

-- --------------------------------------------------------

--
-- 表的结构 `server_list`
--

CREATE TABLE IF NOT EXISTS `server_list` (
  `server_name` char(13) NOT NULL COMMENT '主机名称',
  `server_wip` char(15) NOT NULL DEFAULT '' COMMENT '主机外网IP',
  `server_lip` char(12) NOT NULL DEFAULT '' COMMENT '主机内网IP',
  `server_op` char(10) NOT NULL DEFAULT '' COMMENT '主机操作系统',
  `server_app_id` int(11) NOT NULL COMMENT '服务应用分类ID',
  PRIMARY KEY (`server_lip`),
  KEY `server_list_ibfk_1` (`server_app_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='服务器列表';

--
-- 转存表中的数据 `server_list`
--

INSERT INTO `server_list` (`server_name`, `server_wip`, `server_lip`, `server_op`, `server_app_id`) VALUES
('sn2012-07-010', '10.11.100.10', '192.168.1.10', 'Linux', 1),
('sn2013-08-020', '10.11.100.20', '192.168.1.20', 'Linux', 1),
('sn2013-08-021', '10.11.100.21', '192.168.1.21', 'Linux', 2),
('sn2013-08-022', '10.11.100.22', '192.168.1.22', 'Linux', 2);

--
-- 限制导出的表
--

--
-- 限制表 `server_app_categ`
--
ALTER TABLE `server_app_categ`
  ADD CONSTRAINT `server_app_categ_ibfk_1` FOREIGN KEY (`server_categ_id`) REFERENCES `server_fun_categ` (`ID`);

--
-- 限制表 `server_history`
--
ALTER TABLE `server_history`
  ADD CONSTRAINT `server_history_ibfk_1` FOREIGN KEY (`history_ip`) REFERENCES `server_list` (`server_lip`);

--
-- 限制表 `server_list`
--
ALTER TABLE `server_list`
  ADD CONSTRAINT `server_list_ibfk_1` FOREIGN KEY (`server_app_id`) REFERENCES `server_app_categ` (`ID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
