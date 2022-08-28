-- ----------------------------
-- Records of Basic_Faculty
-- ----------------------------
INSERT INTO `Basic_Faculty` VALUES (10, '人文与社会科学学院');
INSERT INTO `Basic_Faculty` VALUES (9, '信息科学技术学院');
INSERT INTO `Basic_Faculty` VALUES (4, '化学与材料科学学院');
INSERT INTO `Basic_Faculty` VALUES (8, '地球和空间科学学院');
INSERT INTO `Basic_Faculty` VALUES (7, '工程科学学院');
INSERT INTO `Basic_Faculty` VALUES (1, '数学科学学院');
INSERT INTO `Basic_Faculty` VALUES (2, '物理学院');
INSERT INTO `Basic_Faculty` VALUES (5, '生命科学学院');
INSERT INTO `Basic_Faculty` VALUES (3, '管理学院');
INSERT INTO `Basic_Faculty` VALUES (6, '计算机学院');
-- ----------------------------
-- Records of Basic_Major
-- ----------------------------
INSERT INTO `Basic_Major` VALUES (1, '数学与应用数学', 1);
INSERT INTO `Basic_Major` VALUES (2, '信息与科学计算', 1);
INSERT INTO `Basic_Major` VALUES (3, '物理学', 2);
INSERT INTO `Basic_Major` VALUES (4, '应用物理学', 2);
INSERT INTO `Basic_Major` VALUES (5, '天文学', 2);
INSERT INTO `Basic_Major` VALUES (6, '光电信息科学与工程', 2);
INSERT INTO `Basic_Major` VALUES (7, '核工程和核技术', 2);
INSERT INTO `Basic_Major` VALUES (8, '管理科学', 3);
INSERT INTO `Basic_Major` VALUES (9, '信息管理和信息系统', 3);
INSERT INTO `Basic_Major` VALUES (10, '金融学', 3);
INSERT INTO `Basic_Major` VALUES (11, '工商管理', 3);
INSERT INTO `Basic_Major` VALUES (12, '统计学', 3);
INSERT INTO `Basic_Major` VALUES (13, '化学', 4);
INSERT INTO `Basic_Major` VALUES (14, '材料物理', 4);
INSERT INTO `Basic_Major` VALUES (15, '材料化学', 4);
INSERT INTO `Basic_Major` VALUES (16, '高分子材料与工程', 4);
INSERT INTO `Basic_Major` VALUES (17, '生物科学', 5);
INSERT INTO `Basic_Major` VALUES (18, '生物技术', 5);
INSERT INTO `Basic_Major` VALUES (19, '计算机网络', 6);
INSERT INTO `Basic_Major` VALUES (20, '计算机应用', 6);
INSERT INTO `Basic_Major` VALUES (21, '计算机科学与技术', 6);
INSERT INTO `Basic_Major` VALUES (22, '软件工程', 6);
INSERT INTO `Basic_Major` VALUES (23, '理论与应用力学', 7);
INSERT INTO `Basic_Major` VALUES (24, '机械设计制造及其自动化', 7);
INSERT INTO `Basic_Major` VALUES (25, '测控技术与仪器', 7);
INSERT INTO `Basic_Major` VALUES (26, '能源与动力工程', 7);
INSERT INTO `Basic_Major` VALUES (27, '安全工程', 7);
INSERT INTO `Basic_Major` VALUES (28, '地球物理学', 8);
INSERT INTO `Basic_Major` VALUES (29, '地球化学', 8);
INSERT INTO `Basic_Major` VALUES (30, '大气科学', 8);
INSERT INTO `Basic_Major` VALUES (31, '环境科学', 8);
INSERT INTO `Basic_Major` VALUES (32, '电子信息工程', 9);
INSERT INTO `Basic_Major` VALUES (33, '通信工程', 9);
INSERT INTO `Basic_Major` VALUES (34, '自动化', 9);
INSERT INTO `Basic_Major` VALUES (35, '电子科学与技术', 9);
INSERT INTO `Basic_Major` VALUES (36, '信息安全', 9);
INSERT INTO `Basic_Major` VALUES (37, '英语', 10);
INSERT INTO `Basic_Major` VALUES (38, '考古学', 10);
INSERT INTO `Basic_Major` VALUES (39, '传播学', 10);
-- ----------------------------
-- Records of Stu_Student
-- ----------------------------
INSERT INTO `Stu_Student` (sno,name,gender,birthday,mobile,email,address,faculty_id,major_id,start_date, status) VALUES ('1705001', '李明', '男', '1990-10-10', '13512345544', 'liming@abc.com', '上海市', 2, 5, '2017-09-01', '毕业');
INSERT INTO `Stu_Student` (sno,name,gender,birthday,mobile,email,address,faculty_id,major_id,start_date, status) VALUES ('1806001', '郑晓飞', '女', '1991-05-01', '13900998877', 'zhengxiaofei@qq.com', '南京市', 6, 19, '2018-09-01', '在校');
INSERT INTO `Stu_Student` (sno,name,gender,birthday,mobile,email,address,faculty_id,major_id,start_date, status) VALUES ('1906001', '王雷', '男', '1992-10-27', '18912321453', 'wanglei@sohu.com', '江苏省苏州市', 6, 20, '2019-09-01', '在校');
INSERT INTO `Stu_Student` (sno,name,gender,birthday,mobile,email,address,faculty_id,major_id,start_date, status) VALUES ('1906002', '徐亚飞', '女', '1992-11-29', '18933442211', 'xuyf@qq.com', '广东省广州市', 6, 20, '2019-09-01', '在校');
INSERT INTO `Stu_Student` (sno,name,gender,birthday,mobile,email,address,faculty_id,major_id,start_date, status) VALUES ('1906003', '刘小雨', '男', '1993-02-01', '13823149087', 'liuxiaoyu@163.com', '浙江省杭州市', 6, 20, '2019-09-01', '在校');
INSERT INTO `Stu_Student` (sno,name,gender,birthday,mobile,email,address,faculty_id,major_id,start_date, status) VALUES ('1906004', '陈鹏', '男', '1993-01-04', '13512098709', 'chenpeng@263.com', '江苏省常州市', 6, 20, '2019-09-01', '在校');
INSERT INTO `Stu_Student` (sno,name,gender,birthday,mobile,email,address,faculty_id,major_id,start_date, status) VALUES ('1906005', '马忠和', '男', '1992-11-19', '13212340081', 'mazhonghe@sohu.com', '北京市', 6, 20, '2019-09-01', '在校');
INSERT INTO `Stu_Student` (sno,name,gender,birthday,mobile,email,address,faculty_id,major_id,start_date, status) VALUES ('1906006', '刘小平', '男', '1993-04-05', '13900225544', 'liuxp@263.com', '陕西省西安市', 6, 20, '2019-09-01', '在校');

