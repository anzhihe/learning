/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50724
Source Host           : 192.168.182.10:3306
Source Database       : TestDB03

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2019-03-07 08:30:03
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for Book
-- ----------------------------
DROP TABLE IF EXISTS `Book`;
CREATE TABLE `Book` (
  `BookID` int(11) NOT NULL,
  `BookName` varchar(255) DEFAULT NULL,
  `BookPrice` double DEFAULT NULL,
  `BookSumNo` int(11) DEFAULT NULL,
  `BookAuthorID` int(11) NOT NULL,
  `BookPressID` int(11) NOT NULL,
  `BookTypeID` int(11) NOT NULL,
  PRIMARY KEY (`BookID`),
  KEY `Book_BookAuthorID_d13ebba5_fk_Author_AuthorID` (`BookAuthorID`),
  KEY `Book_BookPressID_be23920e_fk_Press_PressID` (`BookPressID`),
  KEY `Book_BookTypeID_34e660be_fk_BookType_ID` (`BookTypeID`),
  CONSTRAINT `Book_BookAuthorID_d13ebba5_fk_Author_AuthorID` FOREIGN KEY (`BookAuthorID`) REFERENCES `Author` (`AuthorID`),
  CONSTRAINT `Book_BookPressID_be23920e_fk_Press_PressID` FOREIGN KEY (`BookPressID`) REFERENCES `Press` (`PressID`),
  CONSTRAINT `Book_BookTypeID_34e660be_fk_BookType_ID` FOREIGN KEY (`BookTypeID`) REFERENCES `BookType` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Book
-- ----------------------------
INSERT INTO `Book` VALUES ('39001', 'Redhat从入门到精通', '35.6', '10', '1005', '18006', '1');
INSERT INTO `Book` VALUES ('39002', '轻松学会足底按摩', '35.6', '5', '1002', '18003', '5');
INSERT INTO `Book` VALUES ('39003', 'Windows 2008部署和管理指南', '49', '25', '1001', '18002', '1');
INSERT INTO `Book` VALUES ('39004', 'Windows 2008网络专业指南', '49', '17', '1001', '18002', '1');
INSERT INTO `Book` VALUES ('39005', 'Windows 2008活动目录指南', '54', '13', '1001', '18002', '1');
INSERT INTO `Book` VALUES ('39006', '疯狂英语之口语基础', '54', '21', '1006', '18009', '3');
INSERT INTO `Book` VALUES ('39007', '大学英语语法应用教程 ', '17.5', '15', '1007', '18010', '3');
INSERT INTO `Book` VALUES ('39008', '微观经济学原理(第3版)', '25', '8', '1008', '18004', '4');
INSERT INTO `Book` VALUES ('39009', '经济学的思维方式(第11版)', '11.9', '4', '1009', '18002', '4');
INSERT INTO `Book` VALUES ('39010', '蝴蝶效应经济学', '21', '9', '1003', '18007', '4');
INSERT INTO `Book` VALUES ('39011', '法律逻辑学', '34.6', '14', '1010', '18011', '2');
INSERT INTO `Book` VALUES ('39012', '刑法学', '50.2', '27', '1004', '18005', '2');
INSERT INTO `Book` VALUES ('39013', '婚姻法案例分析', '23.2', '5', '1005', '18003', '2');
INSERT INTO `Book` VALUES ('39014', '宪法纲要', '15.9', '12', '1003', '18006', '2');
INSERT INTO `Book` VALUES ('39015', '民事诉讼法纲要', '21.6', '9', '1007', '18005', '2');
INSERT INTO `Book` VALUES ('39016', '原子物理学', '24.5', '4', '1003', '18012', '6');
INSERT INTO `Book` VALUES ('39017', '社会学概论', '20.3', '6', '1004', '18003', '10');
