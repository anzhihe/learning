/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50724
Source Host           : 192.168.182.10:3306
Source Database       : TestDB03

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2019-03-07 08:29:54
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for Author
-- ----------------------------
DROP TABLE IF EXISTS `Author`;
CREATE TABLE `Author` (
  `AuthorID` int(11) NOT NULL,
  `AuthorName` varchar(255) NOT NULL,
  `AuthorAge` int(11) DEFAULT NULL,
  `AuthorCity` varchar(255) DEFAULT NULL,
  `AuthorTelNo` varchar(255) DEFAULT NULL,
  `AuthorEMail` varchar(255) DEFAULT NULL,
  `AuthorWorkAddress` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`AuthorID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Author
-- ----------------------------
INSERT INTO `Author` VALUES ('1001', '戴有炜', '52', '台湾台北', '02-28612354', 'Services@hpb.tw', '台北市阳明山建业路73 巷 8 号');
INSERT INTO `Author` VALUES ('1002', '谢蓉', '45', '北京', '010-63583215', 'xierong@163.com', '北京市宣武区右安门西街8号');
INSERT INTO `Author` VALUES ('1003', '陈新仁', '48', '江苏南京', '025-45671432', 'chenrx@Gmail.com', '南京市中山北路38号');
INSERT INTO `Author` VALUES ('1004', '谢朝阳', '45', '广东广州', '020-56745689', 'xiezhaoyang@sohu.com', '广州市东山路48号');
INSERT INTO `Author` VALUES ('1005', '刘军', '38', '四川成都', '028-96754389', 'liujun@yahoo.com.cn', '成都市嵩山路48号');
INSERT INTO `Author` VALUES ('1006', '樊玲', '34', '福建福州', '0591-34245671', 'fanning@hotmail.com', '福州市建设路98号511室');
INSERT INTO `Author` VALUES ('1007', '刘淑颖', '42', '陕西西安', '0577-34244534', 'liusy@163.com', '西安市长许路777号');
INSERT INTO `Author` VALUES ('1008', '李明志', '56', '浙江杭州', '0571-35469120', 'limz@sohu.com', '杭州市西溪路25号');
INSERT INTO `Author` VALUES ('1009', '咸郎平', '52', '上海', '021-34140924', 'xianlp@china.com.cn', '上海市黄浦区淮海路45号');
INSERT INTO `Author` VALUES ('1010', '郝建设', '34', '上海', '021-34140542', 'haojianshe@sina.com.cn', '上海市徐汇区漕宝路1433号');
