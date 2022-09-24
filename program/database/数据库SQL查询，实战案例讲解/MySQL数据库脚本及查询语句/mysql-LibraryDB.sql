/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50727
Source Host           : 192.168.182.10:3306
Source Database       : LibraryDB

Target Server Type    : MYSQL
Target Server Version : 50727
File Encoding         : 65001

Date: 2019-12-23 15:27:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for Author
-- ----------------------------
DROP TABLE IF EXISTS `Author`;
CREATE TABLE `Author` (
  `AuthorID` int(11) NOT NULL,
  `AuthorName` varchar(20) NOT NULL,
  `AuthorAge` tinyint(4) DEFAULT NULL,
  `AuthorCity` varchar(20) DEFAULT NULL,
  `AuthorTelNo` varchar(20) NOT NULL,
  `AuthorEMail` varchar(50) DEFAULT NULL,
  `AuthorWorkAddress` varchar(50) DEFAULT NULL,
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
INSERT INTO `Author` VALUES ('1009', '郎咸平', '52', '上海', '021-34140924', 'xianlp@china.com.cn', '上海市黄浦区淮海路45号');
INSERT INTO `Author` VALUES ('1010', '郝建设', '34', '上海', '021-34140542', 'haojianshe@sina.com.cn', '上海市徐汇区漕宝路1433号');

-- ----------------------------
-- Table structure for Book
-- ----------------------------
DROP TABLE IF EXISTS `Book`;
CREATE TABLE `Book` (
  `BookID` int(11) NOT NULL,
  `BookName` varchar(50) NOT NULL,
  `BookTypeID` int(11) DEFAULT NULL,
  `BookAuthor` int(11) DEFAULT NULL,
  `BookPrice` float DEFAULT NULL,
  `BookPressID` int(11) DEFAULT NULL,
  `BookIncoming` int(11) DEFAULT NULL,
  PRIMARY KEY (`BookID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Book
-- ----------------------------
INSERT INTO `Book` VALUES ('39001', 'Redhat从入门到精通', '1', '1005', '35.6', '18006', '10');
INSERT INTO `Book` VALUES ('39002', '轻松学会足底按摩', '5', '1002', '35.6', '18003', '5');
INSERT INTO `Book` VALUES ('39003', 'Windows Server 2008部署和管理指南', '1', '1001', '49', '18002', '25');
INSERT INTO `Book` VALUES ('39004', 'Windows Server 2008网络专业指南', '1', '1001', '49', '18002', '17');
INSERT INTO `Book` VALUES ('39005', 'Windows Server 2008活动目录专业指南', '1', '1001', '54', '18002', '13');
INSERT INTO `Book` VALUES ('39006', '疯狂英语之口语基础', '3', '1006', '54', '18009', '21');
INSERT INTO `Book` VALUES ('39007', '大学英语语法应用教程 ', '3', '1007', '17.5', '18010', '15');
INSERT INTO `Book` VALUES ('39008', '微观经济学原理(第3版)', '4', '1008', '25', '18004', '8');
INSERT INTO `Book` VALUES ('39009', '经济学的思维方式(第11版)', '4', '1009', '11.9', '18002', '4');
INSERT INTO `Book` VALUES ('39010', '蝴蝶效应经济学', '4', '1003', '21', '18007', '9');
INSERT INTO `Book` VALUES ('39011', '法律逻辑学', '2', '1010', '34.6', '18011', '14');
INSERT INTO `Book` VALUES ('39012', '刑法学', '2', '1004', '50.2', '18005', '27');
INSERT INTO `Book` VALUES ('39013', '婚姻法案例分析', '2', '1005', '23.2', '18003', '5');
INSERT INTO `Book` VALUES ('39014', '宪法纲要', '2', '1003', '15.9', '18006', '12');
INSERT INTO `Book` VALUES ('39015', '民事诉讼法纲要', '2', '1007', '21.6', '18005', '9');
INSERT INTO `Book` VALUES ('39016', '原子物理学', '6', '1003', '24.5', '18012', '4');
INSERT INTO `Book` VALUES ('39017', '社会学概论', '10', '1004', '20.3', '18003', '6');

-- ----------------------------
-- Table structure for BookType
-- ----------------------------
DROP TABLE IF EXISTS `BookType`;
CREATE TABLE `BookType` (
  `ID` int(11) NOT NULL,
  `TypeName` varchar(50) DEFAULT NULL,
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

-- ----------------------------
-- Table structure for BorrowBook
-- ----------------------------
DROP TABLE IF EXISTS `BorrowBook`;
CREATE TABLE `BorrowBook` (
  `ID` int(11) NOT NULL,
  `SNO` int(11) DEFAULT NULL,
  `BookID` int(11) DEFAULT NULL,
  `BorrowDate` datetime DEFAULT NULL,
  `ReturnDate` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of BorrowBook
-- ----------------------------
INSERT INTO `BorrowBook` VALUES ('1', '95009', '39001', '2009-03-25 23:13:00', '2009-04-24 23:13:00');
INSERT INTO `BorrowBook` VALUES ('2', '95001', '39002', '2009-03-25 23:13:00', '2009-04-24 23:13:00');
INSERT INTO `BorrowBook` VALUES ('3', '95006', '39006', '2009-03-25 23:13:00', '2009-04-24 23:13:00');
INSERT INTO `BorrowBook` VALUES ('4', '95004', '39006', '2009-07-25 23:13:00', '2009-08-24 23:13:00');
INSERT INTO `BorrowBook` VALUES ('5', '95001', '39007', '2009-03-25 23:13:00', '2009-04-24 23:13:00');
INSERT INTO `BorrowBook` VALUES ('6', '95002', '39007', '2009-08-25 23:13:00', '2009-09-24 23:13:00');
INSERT INTO `BorrowBook` VALUES ('7', '95003', '39007', '2009-03-25 23:13:00', '2009-04-24 23:13:00');
INSERT INTO `BorrowBook` VALUES ('8', '95004', '39007', '2009-03-25 23:13:00', '2009-04-24 23:13:00');
INSERT INTO `BorrowBook` VALUES ('9', '95007', '39008', '2010-08-08 00:09:00', '2011-09-07 00:09:00');
INSERT INTO `BorrowBook` VALUES ('10', '95004', '39008', '2010-12-08 00:09:00', '2011-01-07 00:09:00');
INSERT INTO `BorrowBook` VALUES ('11', '95001', '39008', '2010-12-08 00:09:00', '2011-01-07 00:09:00');
INSERT INTO `BorrowBook` VALUES ('12', '95002', '39008', '2010-12-08 00:09:00', '2011-01-07 00:09:00');
INSERT INTO `BorrowBook` VALUES ('13', '95005', '39009', '2010-04-12 00:16:00', '2011-05-11 00:16:00');
INSERT INTO `BorrowBook` VALUES ('14', '95006', '39009', '2010-12-08 00:16:00', '2011-01-07 00:16:00');
INSERT INTO `BorrowBook` VALUES ('15', '95002', '39010', '2010-12-08 00:20:00', '2011-01-07 00:20:00');
INSERT INTO `BorrowBook` VALUES ('16', '95003', '39010', '2010-12-08 00:20:00', '2011-01-07 00:20:00');
INSERT INTO `BorrowBook` VALUES ('17', '95004', '39010', '2010-12-08 00:20:00', '2011-01-07 00:20:00');
INSERT INTO `BorrowBook` VALUES ('18', '95005', '39011', '2010-12-08 00:29:00', '2011-01-07 00:29:00');
INSERT INTO `BorrowBook` VALUES ('19', '95003', '39012', '2010-12-08 01:02:00', '2011-01-07 01:02:00');
INSERT INTO `BorrowBook` VALUES ('20', '95005', '39012', '2010-12-08 01:03:00', '2011-01-07 01:03:00');
INSERT INTO `BorrowBook` VALUES ('21', '95009', '39013', '2010-12-08 01:04:00', '2011-01-07 01:04:00');
INSERT INTO `BorrowBook` VALUES ('22', '95003', '39016', '2010-11-08 00:09:00', '2010-12-08 00:09:00');
INSERT INTO `BorrowBook` VALUES ('23', '95008', '39008', '2010-12-08 17:25:00', '2011-01-07 17:25:00');
INSERT INTO `BorrowBook` VALUES ('24', '95005', '39007', '2017-07-19 16:28:00', '2017-08-18 16:28:00');

-- ----------------------------
-- Table structure for Course
-- ----------------------------
DROP TABLE IF EXISTS `Course`;
CREATE TABLE `Course` (
  `CNo` int(11) NOT NULL,
  `CName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`CNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Course
-- ----------------------------
INSERT INTO `Course` VALUES ('39001', '语文');
INSERT INTO `Course` VALUES ('39002', '数学');
INSERT INTO `Course` VALUES ('39003', '英语');
INSERT INTO `Course` VALUES ('39004', '物理');
INSERT INTO `Course` VALUES ('39005', '化学');

-- ----------------------------
-- Table structure for Employee
-- ----------------------------
DROP TABLE IF EXISTS `Employee`;
CREATE TABLE `Employee` (
  `EmpId` int(11) NOT NULL,
  `EmpName` varchar(100) DEFAULT NULL,
  `ReportId` int(11) DEFAULT NULL,
  PRIMARY KEY (`EmpId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Employee
-- ----------------------------
INSERT INTO `Employee` VALUES ('101', '陈晓明', null);
INSERT INTO `Employee` VALUES ('102', '王宁', '101');
INSERT INTO `Employee` VALUES ('103', '张楠', '101');
INSERT INTO `Employee` VALUES ('104', '郭春峰', '101');
INSERT INTO `Employee` VALUES ('105', '王小雨', '102');
INSERT INTO `Employee` VALUES ('106', '刘艺', '102');
INSERT INTO `Employee` VALUES ('107', '郝建', '103');
INSERT INTO `Employee` VALUES ('108', '王飞', '103');
INSERT INTO `Employee` VALUES ('109', '马建', '103');
INSERT INTO `Employee` VALUES ('110', '陈鹏', '103');
INSERT INTO `Employee` VALUES ('111', '朱爱华', '104');
INSERT INTO `Employee` VALUES ('112', '刘希', '104');

-- ----------------------------
-- Table structure for Press
-- ----------------------------
DROP TABLE IF EXISTS `Press`;
CREATE TABLE `Press` (
  `PressID` int(11) NOT NULL,
  `PressName` varchar(30) NOT NULL,
  `PressCity` varchar(20) DEFAULT NULL,
  `PressTelNO` varchar(20) NOT NULL,
  `PressEmail` varchar(50) DEFAULT NULL,
  `PressAddress` varchar(200) DEFAULT NULL,
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

-- ----------------------------
-- Table structure for SalesTable
-- ----------------------------
DROP TABLE IF EXISTS `SalesTable`;
CREATE TABLE `SalesTable` (
  `ID` int(11) NOT NULL,
  `PArea` char(10) DEFAULT NULL,
  `PMonth` char(10) DEFAULT NULL,
  `PName` char(20) DEFAULT NULL,
  `PSaleNO` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of SalesTable
-- ----------------------------
INSERT INTO `SalesTable` VALUES ('15001', '华东', '一月', '洗衣机', '4321');
INSERT INTO `SalesTable` VALUES ('15002', '华南', '一月', '洗衣机', '1234');
INSERT INTO `SalesTable` VALUES ('15003', '华北', '一月', '洗衣机', '8764');
INSERT INTO `SalesTable` VALUES ('15004', '西南', '一月', '洗衣机', '981');
INSERT INTO `SalesTable` VALUES ('15005', '华东', '二月', '洗衣机', '4766');
INSERT INTO `SalesTable` VALUES ('15006', '华南', '二月', '洗衣机', '12345');
INSERT INTO `SalesTable` VALUES ('15007', '华北', '二月', '洗衣机', '875');
INSERT INTO `SalesTable` VALUES ('15008', '西南', '二月', '洗衣机', '9821');
INSERT INTO `SalesTable` VALUES ('15009', '华东', '三月', '洗衣机', '776');
INSERT INTO `SalesTable` VALUES ('15010', '华南', '三月', '洗衣机', '667');
INSERT INTO `SalesTable` VALUES ('15011', '华北', '三月', '洗衣机', '1123');
INSERT INTO `SalesTable` VALUES ('15012', '西南', '三月', '洗衣机', '3321');
INSERT INTO `SalesTable` VALUES ('15013', '华东', '一月', '电冰箱', '9876');
INSERT INTO `SalesTable` VALUES ('15014', '华南', '一月', '电冰箱', '4321');
INSERT INTO `SalesTable` VALUES ('15015', '华北', '一月', '电冰箱', '665');
INSERT INTO `SalesTable` VALUES ('15016', '西南', '一月', '电冰箱', '1980');
INSERT INTO `SalesTable` VALUES ('15017', '华东', '二月', '电冰箱', '2314');
INSERT INTO `SalesTable` VALUES ('15018', '华南', '二月', '电冰箱', '1340');
INSERT INTO `SalesTable` VALUES ('15019', '华北', '二月', '电冰箱', '6542');
INSERT INTO `SalesTable` VALUES ('15020', '西南', '二月', '电冰箱', '12309');
INSERT INTO `SalesTable` VALUES ('15021', '华东', '三月', '电冰箱', '6543');
INSERT INTO `SalesTable` VALUES ('15022', '华南', '三月', '电冰箱', '231');
INSERT INTO `SalesTable` VALUES ('15023', '华北', '三月', '电冰箱', '9891');
INSERT INTO `SalesTable` VALUES ('15024', '西南', '三月', '电冰箱', '4321');
INSERT INTO `SalesTable` VALUES ('15025', '华东', '一月', '空调', '666');
INSERT INTO `SalesTable` VALUES ('15026', '华南', '一月', '空调', '777');
INSERT INTO `SalesTable` VALUES ('15027', '华北', '一月', '空调', '888');
INSERT INTO `SalesTable` VALUES ('15028', '西南', '一月', '空调', '999');
INSERT INTO `SalesTable` VALUES ('15029', '华东', '二月', '空调', '7655');
INSERT INTO `SalesTable` VALUES ('15030', '华南', '二月', '空调', '4543');
INSERT INTO `SalesTable` VALUES ('15031', '华北', '二月', '空调', '5431');
INSERT INTO `SalesTable` VALUES ('15032', '西南', '二月', '空调', '1345');
INSERT INTO `SalesTable` VALUES ('15033', '华东', '三月', '空调', '6543');
INSERT INTO `SalesTable` VALUES ('15034', '华南', '三月', '空调', '1278');
INSERT INTO `SalesTable` VALUES ('15035', '华北', '三月', '空调', '1922');
INSERT INTO `SalesTable` VALUES ('15036', '西南', '三月', '空调', '8612');

-- ----------------------------
-- Table structure for Score
-- ----------------------------
DROP TABLE IF EXISTS `Score`;
CREATE TABLE `Score` (
  `SNo` int(11) DEFAULT NULL,
  `CNo` int(11) DEFAULT NULL,
  `Result` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Score
-- ----------------------------
INSERT INTO `Score` VALUES ('95001', '39001', '89');
INSERT INTO `Score` VALUES ('95001', '39002', '71');
INSERT INTO `Score` VALUES ('95001', '39003', '92');
INSERT INTO `Score` VALUES ('95001', '39004', '64');
INSERT INTO `Score` VALUES ('95001', '39005', '78');
INSERT INTO `Score` VALUES ('95002', '39001', '67');
INSERT INTO `Score` VALUES ('95002', '39002', '92');
INSERT INTO `Score` VALUES ('95002', '39003', '56');
INSERT INTO `Score` VALUES ('95002', '39005', '98');
INSERT INTO `Score` VALUES ('95003', '39001', '86');
INSERT INTO `Score` VALUES ('95003', '39002', '93');
INSERT INTO `Score` VALUES ('95003', '39003', '95');
INSERT INTO `Score` VALUES ('95003', '39004', '86');
INSERT INTO `Score` VALUES ('95003', '39005', '76');
INSERT INTO `Score` VALUES ('95004', '39001', '78');
INSERT INTO `Score` VALUES ('95004', '39002', '89');
INSERT INTO `Score` VALUES ('95004', '39003', '93');
INSERT INTO `Score` VALUES ('95004', '39004', '92');
INSERT INTO `Score` VALUES ('95005', '39001', '73');
INSERT INTO `Score` VALUES ('95005', '39002', '89');
INSERT INTO `Score` VALUES ('95005', '39003', '88');
INSERT INTO `Score` VALUES ('95005', '39004', '99');
INSERT INTO `Score` VALUES ('95005', '39005', '85');

-- ----------------------------
-- Table structure for Stu
-- ----------------------------
DROP TABLE IF EXISTS `Stu`;
CREATE TABLE `Stu` (
  `SNo` int(11) NOT NULL,
  `SName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`SNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Stu
-- ----------------------------
INSERT INTO `Stu` VALUES ('95001', '陈晓明');
INSERT INTO `Stu` VALUES ('95002', '王宁');
INSERT INTO `Stu` VALUES ('95003', '张鹏');
INSERT INTO `Stu` VALUES ('95004', '陆建飞');
INSERT INTO `Stu` VALUES ('95005', '钟浩杰');

-- ----------------------------
-- Table structure for Student
-- ----------------------------
DROP TABLE IF EXISTS `Student`;
CREATE TABLE `Student` (
  `SNO` int(11) NOT NULL,
  `SName` varchar(20) NOT NULL,
  `Sage` tinyint(4) DEFAULT NULL,
  `Sex` char(2) DEFAULT NULL,
  `MobileNO` char(11) DEFAULT NULL,
  `StuEMail` varchar(50) DEFAULT NULL,
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
INSERT INTO `Student` VALUES ('95007', '汤小霞', '18', '女', '13311198045', 'tangxiaoxia@sina.com');
INSERT INTO `Student` VALUES ('95008', '周娟', '28', '女', '13305104322', 'Zhoujuan@163.com');
INSERT INTO `Student` VALUES ('95009', '陈鹏', '25', '男', '13801754092', 'chenpeng@163.com');
INSERT INTO `Student` VALUES ('95010', '陈小川', null, '女', '13768023485', 'chengxc@sohu.com');

-- ----------------------------
-- Table structure for Table1
-- ----------------------------
DROP TABLE IF EXISTS `Table1`;
CREATE TABLE `Table1` (
  `SNo` int(11) DEFAULT NULL,
  `SName` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Table1
-- ----------------------------
INSERT INTO `Table1` VALUES ('1', '张三');
INSERT INTO `Table1` VALUES ('2', '李四');
INSERT INTO `Table1` VALUES ('3', '王五');

-- ----------------------------
-- Table structure for Table2
-- ----------------------------
DROP TABLE IF EXISTS `Table2`;
CREATE TABLE `Table2` (
  `SNo` int(11) DEFAULT NULL,
  `Result` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Table2
-- ----------------------------
INSERT INTO `Table2` VALUES ('1', '86');
INSERT INTO `Table2` VALUES ('2', '91');
INSERT INTO `Table2` VALUES ('4', '78');
