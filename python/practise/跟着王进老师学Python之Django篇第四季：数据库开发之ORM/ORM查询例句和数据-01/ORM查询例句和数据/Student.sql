/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50724
Source Host           : 192.168.182.10:3306
Source Database       : TestDB03

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2019-03-07 08:30:34
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for Student
-- ----------------------------
DROP TABLE IF EXISTS `Student`;
CREATE TABLE `Student` (
  `SNO` int(11) NOT NULL,
  `SName` varchar(255) NOT NULL,
  `Age` int(11) DEFAULT NULL,
  `Gender` varchar(255) DEFAULT NULL,
  `Mobile` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`SNO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Student
-- ----------------------------
INSERT INTO `Student` VALUES ('95001', 'Alice', '32', '女', '13482034096', 'Alice@contoso.com');
INSERT INTO `Student` VALUES ('95002', 'Bob', '25', '男', '13305104593', 'Bob@163.com');
INSERT INTO `Student` VALUES ('95003', '张明', '23', '男', '13305104345', 'zhangming@Gmail.com');
INSERT INTO `Student` VALUES ('95004', '胡小光', '34', '男', '13305104322', 'Huxiaoguang@sohu.com');
INSERT INTO `Student` VALUES ('95005', '赵庆余', '25', '男', '18721675210', 'stoim@Gmail.com');
INSERT INTO `Student` VALUES ('95006', '王进', '32', '男', '13482034096', 'it.wangjin@Gamil.com');
INSERT INTO `Student` VALUES ('95007', '汤小霞', '23', '女', '13311198045', 'tangxiaoxia@sina.com');
INSERT INTO `Student` VALUES ('95008', '周娟', '28', '女', '13305104322', 'Zhoujuan@163.com');
INSERT INTO `Student` VALUES ('95009', '陈鹏', '25', '男', '13801754092', 'chenpeng@163.com');
INSERT INTO `Student` VALUES ('95010', '陈小川', null, '女', '13768023485', 'chengxc@sohu.com');
