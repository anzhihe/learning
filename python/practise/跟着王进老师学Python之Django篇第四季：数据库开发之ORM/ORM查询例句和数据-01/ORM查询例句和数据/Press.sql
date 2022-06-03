/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50724
Source Host           : 192.168.182.10:3306
Source Database       : TestDB03

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2019-03-07 08:30:27
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for Press
-- ----------------------------
DROP TABLE IF EXISTS `Press`;
CREATE TABLE `Press` (
  `PressID` int(11) NOT NULL,
  `PressName` varchar(255) NOT NULL,
  `PressCity` varchar(255) DEFAULT NULL,
  `PressTelNO` varchar(255) DEFAULT NULL,
  `PressEmail` varchar(255) DEFAULT NULL,
  `PressAddress` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`PressID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Press
-- ----------------------------
INSERT INTO `Press` VALUES ('18001', '江苏人民出版社', '南京', '025-83658096', 'jsrmbook@vip.163.com', '南京市湖南路1号');
INSERT INTO `Press` VALUES ('18002', '人民邮电出版社', '北京', '01067129213', 'Services@ptpress.com.cn', '北京市崇文区夕照寺街14号');
INSERT INTO `Press` VALUES ('18003', '科学出版社', '北京', '010-54267809', 'webmaster@mail.sciencep.com', '北京东黄城根北街16号');
INSERT INTO `Press` VALUES ('18004', '清华大学出版社', '北京', '010-62770175-3506', 'c-service@tup.tsinghua.edu.cn', '清华大学学研大厦 A 座');
INSERT INTO `Press` VALUES ('18005', '上海外语教育出版商', '上海', '021-65425300', 'marketing@sflep.com.cn', '上海市虹口区大连西路558号');
INSERT INTO `Press` VALUES ('18006', '建筑工业出版社', '北京', '010-68344573', 'market@china-building.com.cn', '北京市百万庄北里甲14号');
INSERT INTO `Press` VALUES ('18007', '电子工业出版社', '北京', '010-88258888', 'webmaster@phei.com.cn', '北京市万寿路南口金家村288号华信大厦');
INSERT INTO `Press` VALUES ('18008', '机械工业出版社', '北京', '010-88379833', 'cmpedu@cmpedu.com', ' 北京市西城区百万庄大街22号机械工业出版社');
INSERT INTO `Press` VALUES ('18009', '中山大学出版社', ' 广州', '020-84111995', 'master@zsup.com.cn', '广州市新港西路135号');
INSERT INTO `Press` VALUES ('18010', '西北工业大学出版社', '西安', '029-88492314', 'bjb@nwpup.com', '西安市友谊西路127号');
INSERT INTO `Press` VALUES ('18011', '苏州大学出版社', '苏州', '0512-45637812', 'Master@Sz.edu.cn', '苏州市倡风路345号');
INSERT INTO `Press` VALUES ('18012', '南京大学出版社', '南京', '025-54599321', 'Services@njedu.com.cn', '南京市北京西路32号');
INSERT INTO `Press` VALUES ('18013', '江南大学出版社', '无锡', '0510-34504132', 'Services@jn.edu.cn', '无锡市民进路23号');
