/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50727
Source Host           : 192.168.182.10:3306
Source Database       : StudentV4DB

Target Server Type    : MYSQL
Target Server Version : 50727
File Encoding         : 65001

Date: 2020-02-13 15:16:16
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for Student
-- ----------------------------
DROP TABLE IF EXISTS `Student`;
CREATE TABLE `Student` (
  `SNo` int(11) NOT NULL,
  `SName` varchar(100) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `Birthday` date NOT NULL,
  `Mobile` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Address` varchar(200) NOT NULL,
  `Image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`SNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Student
-- ----------------------------
INSERT INTO `Student` VALUES ('95001', '王进', '男', '2020-02-01', '13900998877', 'wangjin@abc.com', '江苏省南京市溧水区宝塔路11号', 'e8ec33473c6d16a19d280b8dc634758c.jpg');
INSERT INTO `Student` VALUES ('95002', '李四', '女', '1994-07-25', '13462312498', 'lisi@sohu.com', '上海市徐汇区漕宝路99弄', null);
INSERT INTO `Student` VALUES ('95003', '陈鹏', '男', '1995-03-04', '18987123123', 'chenpeng@163.com', '上海市闵行区银都路294号', null);
INSERT INTO `Student` VALUES ('95004', '张丽', '男', '1995-03-05', '13482034096', 'zhangli@iLync.cn', '上海市徐汇区习勤路100弄', null);
INSERT INTO `Student` VALUES ('95005', '刘向东', '女', '1995-03-06', '13787123123', 'liuxiangdong@iLync.cn', '上海市闵行区春申路295号', null);
INSERT INTO `Student` VALUES ('95006', '李明博', '男', '1995-03-07', '18932178905', 'zhangzhiqiang@sina.com', '上海市徐汇区柳州路101弄', null);
INSERT INTO `Student` VALUES ('95007', '张子强', '男', '1995-03-08', '17600715247', 'wwh@live.cn', '上海市闵行区虹梅南路296号', null);
INSERT INTO `Student` VALUES ('95008', '王文海', '女', '1995-03-09', '18238391838', '65212321@qq.com', '上海市徐汇区龙漕路102弄', null);
INSERT INTO `Student` VALUES ('95009', '刘慧娟', '男', '1995-03-10', '18876068428', 'liuhuijuan@iLync.cn', '上海市闵行区颛兴东路297号', null);
INSERT INTO `Student` VALUES ('95010', '陈敏', '女', '1995-03-11', '13513745019', 'chenming@sohu.com', '上海市徐汇区桂林路103弄', 'dae3aa26a0c8cfa950e6cbb98425b9d8.jpg');
INSERT INTO `Student` VALUES ('95011', '王云', '女', '1995-03-12', '13051421609', 'wangyun@gmail.com', '上海市闵行区开发区大道298号', '1fec845b4fc9065c249914047c2e32c7.jpg');
INSERT INTO `Student` VALUES ('95012', '沈璐', '男', '1995-03-13', '13889098199', 'shenlu@iLync.cn', '上海市徐汇区田东路104弄', '8892f98a849bdcc06eece1738d47c2bf.jpg');
INSERT INTO `Student` VALUES ('95013', '赵鹏飞', '男', '1995-03-14', '15026774790', 'chenpengfei@iLync.cn', '上海市闵行区都市路99号', '76c0581ba6f7c8d637f971be17848ef3.jpg');
INSERT INTO `Student` VALUES ('95014', '谢朝阳', '女', '1995-03-15', '18064451380', 'xiechaoyang@sohu.com', '上海市徐汇区钦州北路105弄', null);
INSERT INTO `Student` VALUES ('95015', '刘子歌', '男', '1995-03-16', '13902127970', '6533422@qq.com', '上海市闵行区都会路300号', null);
INSERT INTO `Student` VALUES ('95016', '陈照升', '男', '1995-03-17', '13339804561', 'chenzs@iLync.cn', '上海市徐汇区中山北路106弄', null);
INSERT INTO `Student` VALUES ('95017', '秦小路', '女', '1995-03-18', '13477481151', 'qinxl@sina.com', '上海市闵行区都庄路301号', null);
INSERT INTO `Student` VALUES ('95018', '张大宝', '男', '1995-03-19', '13915157742', 'zhangdb@sohu.com', '上海市徐汇区桂林东街107弄', null);
INSERT INTO `Student` VALUES ('95019', '刘佳', '男', '1995-03-20', '13352834332', 'liujia@sohu.com', '上海市闵行区剑川路302号', null);
INSERT INTO `Student` VALUES ('95020', '李伟', '女', '1995-03-21', '15990510922', 'lw@263.com', '上海市徐汇区桂林西街108弄', null);
INSERT INTO `Student` VALUES ('95021', '杨荣', '男', '1995-05-31', '13522341234', 'yangrong@iLync.cn', '江苏省泰州市姜堰区华港镇254号', null);
