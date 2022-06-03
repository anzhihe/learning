/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50724
Source Host           : 192.168.182.10:3306
Source Database       : TestDB03

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2019-03-07 08:30:10
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for BookType
-- ----------------------------
DROP TABLE IF EXISTS `BookType`;
CREATE TABLE `BookType` (
  `ID` int(11) NOT NULL,
  `TypeName` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of BookType
-- ----------------------------
INSERT INTO `BookType` VALUES ('1', '计算机');
INSERT INTO `BookType` VALUES ('2', '法律');
INSERT INTO `BookType` VALUES ('3', '外语');
INSERT INTO `BookType` VALUES ('4', '经济');
INSERT INTO `BookType` VALUES ('5', '健康与养生');
INSERT INTO `BookType` VALUES ('6', '物理');
INSERT INTO `BookType` VALUES ('7', '化学');
INSERT INTO `BookType` VALUES ('8', '生理');
INSERT INTO `BookType` VALUES ('9', '会计学');
INSERT INTO `BookType` VALUES ('10', '社会学');
