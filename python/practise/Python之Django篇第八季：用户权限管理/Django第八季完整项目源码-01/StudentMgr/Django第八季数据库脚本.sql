/*
 Navicat Premium Data Transfer

 Source Server         : mysql_dev
 Source Server Type    : MySQL
 Source Server Version : 50727
 Source Host           : 192.168.182.10:3306
 Source Schema         : django_v8_db

 Target Server Type    : MySQL
 Target Server Version : 50727
 File Encoding         : 65001

 Date: 08/03/2022 10:56:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Basic_Faculty
-- ----------------------------
DROP TABLE IF EXISTS `Basic_Faculty`;
CREATE TABLE `Basic_Faculty`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

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
-- Table structure for Basic_Major
-- ----------------------------
DROP TABLE IF EXISTS `Basic_Major`;
CREATE TABLE `Basic_Major`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `faculty_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE,
  INDEX `Basic_Major_faculty_id_e403f15f_fk_Basic_Faculty_id`(`faculty_id`) USING BTREE,
  CONSTRAINT `Basic_Major_faculty_id_e403f15f_fk_Basic_Faculty_id` FOREIGN KEY (`faculty_id`) REFERENCES `Basic_Faculty` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 42 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

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
INSERT INTO `Basic_Major` VALUES (41, '计算机测试888', 2);

-- ----------------------------
-- Table structure for Stu_Student
-- ----------------------------
DROP TABLE IF EXISTS `Stu_Student`;
CREATE TABLE `Stu_Student`  (
  `sno` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `gender` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `birthday` date NOT NULL,
  `mobile` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `address` varchar(250) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `start_date` date NOT NULL,
  `status` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `faculty_id` int(11) NOT NULL,
  `major_id` int(11) NOT NULL,
  PRIMARY KEY (`sno`) USING BTREE,
  INDEX `Stu_Student_faculty_id_33ccb2d0_fk_Basic_Faculty_id`(`faculty_id`) USING BTREE,
  INDEX `Stu_Student_major_id_077e77d1_fk_Basic_Major_id`(`major_id`) USING BTREE,
  CONSTRAINT `Stu_Student_faculty_id_33ccb2d0_fk_Basic_Faculty_id` FOREIGN KEY (`faculty_id`) REFERENCES `Basic_Faculty` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `Stu_Student_major_id_077e77d1_fk_Basic_Major_id` FOREIGN KEY (`major_id`) REFERENCES `Basic_Major` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of Stu_Student
-- ----------------------------
INSERT INTO `Stu_Student` VALUES ('1705001', '李明', '男', '1990-10-10', '13512345544', 'liming@abc.com', '上海市', '2017-09-01', '毕业', 2, 5);
INSERT INTO `Stu_Student` VALUES ('1806001', '郑晓飞', '女', '1991-05-01', '13900998877', 'zhengxiaofei@qq.com', '南京市', '2018-09-01', '在校', 6, 19);
INSERT INTO `Stu_Student` VALUES ('1906001', '王雷', '男', '1992-10-27', '18912321453', 'wanglei@sohu.com', '江苏省苏州市', '2019-09-01', '在校', 6, 20);
INSERT INTO `Stu_Student` VALUES ('1906002', '徐亚飞', '女', '1992-11-29', '18933442211', 'xuyf@qq.com', '广东省广州市', '2019-09-01', '在校', 6, 20);
INSERT INTO `Stu_Student` VALUES ('1906003', '刘小雨', '男', '1993-02-01', '13823149087', 'liuxiaoyu@163.com', '浙江省杭州市', '2019-09-01', '在校', 6, 20);
INSERT INTO `Stu_Student` VALUES ('1906004', '陈鹏', '男', '1993-01-04', '13512098709', 'chenpeng@263.com', '江苏省常州市', '2019-09-01', '在校', 6, 20);
INSERT INTO `Stu_Student` VALUES ('1906005', '马忠和', '男', '1992-11-19', '13212340081', 'mazhonghe@sohu.com', '北京市', '2019-09-01', '在校', 6, 20);
INSERT INTO `Stu_Student` VALUES ('1906006', '刘小平', '男', '1993-04-05', '13900225544', 'liuxp@263.com', '陕西省西安市', '2019-09-01', '休学', 6, 20);

-- ----------------------------
-- Table structure for Stu_StudentImage
-- ----------------------------
DROP TABLE IF EXISTS `Stu_StudentImage`;
CREATE TABLE `Stu_StudentImage`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `remark` varchar(250) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 29 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of Stu_StudentImage
-- ----------------------------
INSERT INTO `Stu_StudentImage` VALUES (4, '202108041411.jpg', '测试图片', '2021-08-03 21:10:12.000000');
INSERT INTO `Stu_StudentImage` VALUES (5, '202108045019.png', '黑衣服的漂亮女孩', '2021-08-02 23:55:26.000000');
INSERT INTO `Stu_StudentImage` VALUES (7, '202108044485.jpg', '白衣服的漂亮女孩', '2021-07-28 23:55:34.000000');
INSERT INTO `Stu_StudentImage` VALUES (8, '202108046541.jpg', '男生的合影', '2021-06-10 23:59:31.000000');
INSERT INTO `Stu_StudentImage` VALUES (9, '202108047597.png', '帅气的男孩', '2021-08-01 23:59:34.000000');
INSERT INTO `Stu_StudentImage` VALUES (10, '202108042185.jpg', '卡通女孩', '2021-08-04 23:59:43.000000');
INSERT INTO `Stu_StudentImage` VALUES (11, '202108041220.jpg', '张三的图片', '2021-08-04 23:59:47.000000');
INSERT INTO `Stu_StudentImage` VALUES (12, '202108041420.jpg', '非常好看的紫色的夜景', '2021-08-04 23:59:51.000000');
INSERT INTO `Stu_StudentImage` VALUES (13, '202108047484.jpg', '好看的随拍图片', '2021-08-04 23:59:58.000000');
INSERT INTO `Stu_StudentImage` VALUES (14, '202108057849.jpg', '唯美图片：美丽的夜景', '2021-08-05 00:00:05.000000');
INSERT INTO `Stu_StudentImage` VALUES (15, '202108056114.jpg', '唯美图片：紫色的白云', '2021-08-05 00:00:08.000000');
INSERT INTO `Stu_StudentImage` VALUES (16, '202108052537.jpg', '好美的图', '2021-08-05 00:00:17.000000');
INSERT INTO `Stu_StudentImage` VALUES (17, '202108053791.jpg', '唯美图片：粉色的白云', '2021-08-05 00:08:47.000000');
INSERT INTO `Stu_StudentImage` VALUES (18, '202108052149.jpg', '', '2021-08-05 00:08:49.000000');
INSERT INTO `Stu_StudentImage` VALUES (19, '202108059840.jpg', '', '2021-08-05 00:08:51.000000');
INSERT INTO `Stu_StudentImage` VALUES (20, '202108058408.jpg', '乡间小路', '2021-08-05 00:08:54.000000');
INSERT INTO `Stu_StudentImage` VALUES (21, '202108053567.jpg', '紫色的夜空', '2021-08-05 00:08:56.000000');
INSERT INTO `Stu_StudentImage` VALUES (22, '202108058137.jpg', '绚丽的光', '2021-08-05 00:10:39.000000');
INSERT INTO `Stu_StudentImage` VALUES (23, '202108051943.jpg', '漂亮的花', '2021-08-05 00:10:42.000000');
INSERT INTO `Stu_StudentImage` VALUES (24, '202108052421.jpg', '好美的天空', '2021-08-05 00:10:45.000000');
INSERT INTO `Stu_StudentImage` VALUES (27, '202108057998.jpg', 'python课程', '2021-08-05 08:39:31.000000');
INSERT INTO `Stu_StudentImage` VALUES (28, '202203083242.png', '', '2022-03-08 01:10:47.000000');

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 57 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add Faculty', 7, 'add_faculty');
INSERT INTO `auth_permission` VALUES (26, 'Can change Faculty', 7, 'change_faculty');
INSERT INTO `auth_permission` VALUES (27, 'Can delete Faculty', 7, 'delete_faculty');
INSERT INTO `auth_permission` VALUES (28, 'Can view Faculty', 7, 'view_faculty');
INSERT INTO `auth_permission` VALUES (29, 'Can add Major', 8, 'add_major');
INSERT INTO `auth_permission` VALUES (30, 'Can change Major', 8, 'change_major');
INSERT INTO `auth_permission` VALUES (31, 'Can delete Major', 8, 'delete_major');
INSERT INTO `auth_permission` VALUES (32, 'Can view Major', 8, 'view_major');
INSERT INTO `auth_permission` VALUES (33, 'Can add Student', 9, 'add_student');
INSERT INTO `auth_permission` VALUES (34, 'Can change Student', 9, 'change_student');
INSERT INTO `auth_permission` VALUES (35, 'Can delete Student', 9, 'delete_student');
INSERT INTO `auth_permission` VALUES (36, 'Can view Student', 9, 'view_student');
INSERT INTO `auth_permission` VALUES (37, 'Can add StudentImage', 10, 'add_studentimage');
INSERT INTO `auth_permission` VALUES (38, 'Can change StudentImage', 10, 'change_studentimage');
INSERT INTO `auth_permission` VALUES (39, 'Can delete StudentImage', 10, 'delete_studentimage');
INSERT INTO `auth_permission` VALUES (40, 'Can view StudentImage', 10, 'view_studentimage');
INSERT INTO `auth_permission` VALUES (41, 'Can add Account', 11, 'add_account');
INSERT INTO `auth_permission` VALUES (42, 'Can change Account', 11, 'change_account');
INSERT INTO `auth_permission` VALUES (43, 'Can delete Account', 11, 'delete_account');
INSERT INTO `auth_permission` VALUES (44, 'Can view Account', 11, 'view_account');
INSERT INTO `auth_permission` VALUES (45, 'Can add Roles', 12, 'add_roles');
INSERT INTO `auth_permission` VALUES (46, 'Can change Roles', 12, 'change_roles');
INSERT INTO `auth_permission` VALUES (47, 'Can delete Roles', 12, 'delete_roles');
INSERT INTO `auth_permission` VALUES (48, 'Can view Roles', 12, 'view_roles');
INSERT INTO `auth_permission` VALUES (49, 'Can add Permission', 13, 'add_permission');
INSERT INTO `auth_permission` VALUES (50, 'Can change Permission', 13, 'change_permission');
INSERT INTO `auth_permission` VALUES (51, 'Can delete Permission', 13, 'delete_permission');
INSERT INTO `auth_permission` VALUES (52, 'Can view Permission', 13, 'view_permission');
INSERT INTO `auth_permission` VALUES (53, 'Can add Menu', 14, 'add_menu');
INSERT INTO `auth_permission` VALUES (54, 'Can change Menu', 14, 'change_menu');
INSERT INTO `auth_permission` VALUES (55, 'Can delete Menu', 14, 'delete_menu');
INSERT INTO `auth_permission` VALUES (56, 'Can view Menu', 14, 'view_menu');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id`, `group_id`) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id`) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id`, `permission_id`) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int(11) NULL DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (7, 'basicweb', 'faculty');
INSERT INTO `django_content_type` VALUES (8, 'basicweb', 'major');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');
INSERT INTO `django_content_type` VALUES (9, 'studentweb', 'student');
INSERT INTO `django_content_type` VALUES (10, 'studentweb', 'studentimage');
INSERT INTO `django_content_type` VALUES (11, 'userweb', 'account');
INSERT INTO `django_content_type` VALUES (14, 'userweb', 'menu');
INSERT INTO `django_content_type` VALUES (13, 'userweb', 'permission');
INSERT INTO `django_content_type` VALUES (12, 'userweb', 'roles');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 27 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2021-06-20 02:22:57.244605');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2021-06-20 02:22:57.306278');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2021-06-20 02:22:57.379084');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2021-06-20 02:22:57.401024');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2021-06-20 02:22:57.408032');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2021-06-20 02:22:57.438923');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2021-06-20 02:22:57.454881');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2021-06-20 02:22:57.471836');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2021-06-20 02:22:57.478850');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2021-06-20 02:22:57.492331');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2021-06-20 02:22:57.494299');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2021-06-20 02:22:57.501280');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2021-06-20 02:22:57.514245');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2021-06-20 02:22:57.527210');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2021-06-20 02:22:57.541173');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2021-06-20 02:22:57.549152');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2021-06-20 02:22:57.565110');
INSERT INTO `django_migrations` VALUES (18, 'basicweb', '0001_initial', '2021-06-20 02:22:57.584063');
INSERT INTO `django_migrations` VALUES (19, 'sessions', '0001_initial', '2021-06-20 02:22:57.601548');
INSERT INTO `django_migrations` VALUES (20, 'studentweb', '0001_initial', '2021-06-20 02:22:57.621494');
INSERT INTO `django_migrations` VALUES (21, 'studentweb', '0002_studentimage', '2021-08-04 01:03:38.286399');
INSERT INTO `django_migrations` VALUES (22, 'userweb', '0001_initial', '2021-08-08 10:35:42.794291');
INSERT INTO `django_migrations` VALUES (23, 'userweb', '0002_roles', '2022-02-18 10:10:27.105252');
INSERT INTO `django_migrations` VALUES (24, 'userweb', '0003_auto_20220218_1013', '2022-02-18 10:13:45.024759');
INSERT INTO `django_migrations` VALUES (25, 'userweb', '0004_menu_permission', '2022-03-04 11:23:46.038227');
INSERT INTO `django_migrations` VALUES (26, 'userweb', '0005_auto_20220304_1156', '2022-03-04 11:57:06.227792');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('0lalwwh4fguqb1zyjjojaxtg53jv5nfb', '.eJw1j9GKhDAMRX9l6PO6JNW22qf9EGGobXQL2g5aYWGYf5_YYd9ucg_JvU9xHrQL-xRrXmKKQViBACi-RHIb8TSeg-768dRatePZEXr2Aj3cXjZKpRLdTMgE6JlpoJ6JRz5iiTlV38yKfUPBj6cKpFg7mFgTXOyWp7hev7AdULad0uZa0-biylv_S2n5iy6HnJYfN_lvnzf2_U6u0L3EmlOCxAb6BuUNwbbGyoGZ1R3lXqt9ENmAbLC_QW-lsXj1pBDL_xGO5NFxFSNdrUWsVTuI1-sNg05YiQ:1nKr8m:FCoNjdhwmwCeT6bdQLPqBnNG3I9FfiOfvPzwLP7Cacc', '2022-03-04 08:28:52.713501');
INSERT INTO `django_session` VALUES ('2o6dz6ybjir6eajjiwx5kbac5dgxxfkn', '.eJxNz8GOhCAMBuBXmXBeNy0CKqd9EJMJQnVJFCaKySaTefcpzmVvbf8vLTzFedAu7FOseYkpBmEFAqD4EsltxN14Dkb142mMbsdTEXrOAj3cXjZK5RJqJmQBZmYN1LN45COWmNOVd7PmvKPgx1MH0lw7mLgmqHbLU1zrLWwHlK3Spqtj2lxceep_KS1_0eWQ0_LjJv_t88a538kVupd4vVOCxAb6BuUNwbadlQOb1R3lfn3tQ2QDbQOqEtlbqeuZEMu_JSxkI_GG2mptUYnX6w2owlSJ:1nR8pr:Odrns2T5fi3aa7wRiwNP-IFDsPkLE15g2Qdx3rfLzjo', '2022-03-21 16:35:19.690225');
INSERT INTO `django_session` VALUES ('2sonaz3gaodt8an1hjdn2nfkpql2308u', '.eJx9VMuOozAQ_JXI57D4bcJp_2MyiowfGa8AR2CkXUX5922TyQBRZi4WbneXu6raXNE0ugHVV9TGc-iDRTUiGBO0R73uHOyO00Hy6jhJKdhx4o4YOLPuoofUuT7NGdw7AhlYesjGroKMSxxDCrGfz5UXcK6cNcdJWCfgW-MGvh3OuV1sQpvvIuxAKONCqhx2nQ4tRM2H689_g4429uffujG_TOzg3AxOJ3dKYe6TYkoKXBWE7giumarpAXJaPabTTO2eQgvMIGuHec0FZOVrbEgrkK8MUnNcC4luQMYNXRhHoHNqwwic31DZ6DGY0msztelfCTifkU7_icO8H9NkQaEy9D5uA50-uzmSxS-1MXGC8FdgiK0bly3IPC27pZc5Bhr1n-A6wfVz3qWN2pboHaSF2pMNJmWLSV5SSO3dV6G8BicqjsE7ofLKpAOAYGbfvN55XYCNYMQFwnGweVQIBuk_QmsHB1lvV5SHhuxXwAcpKQAbDxarRmfrOZaAMA3Zz2fpbvs7Bl1jwKDdx03_hPEp9u0dTKJP7BopoUgQ_wSwYZclHRdu9BU3tv8Gdhn7pa-t6Q9q_DsIRaSClXL1AuI-JjM5tiWnBM1PkjIorg4W1K6oos_kgi2MHmwRF4LsFUGx7k5JlV-mF_BKK0uhU8H8qrvtyD4IyjXE0tFrjdZD_gBQGwA2_ylY7uGV-atn8aiv1vVScZbHUOAf6tcPCTS-3f4DvFuKTg:1nRPH1:DoAZpAbc45bTu7VsQ2_GX4wtlslr_IXQT1z2cHby_tY', '2022-03-22 10:08:27.680146');
INSERT INTO `django_session` VALUES ('4zr2wye5618xcv1hombgi4ziodoe8zag', '.eJw1j9GKhDAMRX9l6PO6JLW12qf9EGGobXQL2g5aYWGYf5_YYd9ucg_JvU9xHrQL-xRrXmKKQViBACi-RHIb8TSeQ6f68ew63Y6nIvTsBXq4vWyUSiXUTMgEdDPTQD0Tj3zEEnOqvpk1-4aCH08dSLN2MLEmuNgtT3G9fmE7oGyV7sy1ps3Flbf-l9LyF10OOS0_bvLfPm_s-51coXuJNacEiQ30Dcobgm2NlQMzqzvKvVb7ILIB2WB_g8EqY_HqSSGW_yMcyaPjKka6WotY63YQr9cbg91YjA:1nM3ZG:Cfad8VieBXS2D8UVDmi8N79oUKquiRQc8P6xrZlIRD4', '2022-03-07 15:57:10.623835');
INSERT INTO `django_session` VALUES ('jmgo8psmymlz0r0qzi6m77f4t0daen53', '.eJw1j9GKhDAMRX9l6PO6JNVW7dN-iDDUNroFbQdtYWGYf5_YYd9ucg_JvU9RTjqEeYotrSEGL4xAABRfItqdeJrKqLthKlqrdiodoWPP08MeeaeYK9EthEyAXpgGGph4pDPkkGL1-0Wx35N3U1GeFGsLM2uCi93THLbrF7YjyrZTur_WtNuw8db9Ulz_gk0-xfXHzu7bpZ19d5DNdM-h5pQgsYGhQXlDMG1v5MjMZs98r9U-iGxANjjcYDSqM6q-8SH_H-FIDi1X6aWttYi1akfxer0BhV9YlQ:1nKsUM:mAsGqBDJQ7STYSIftGd9Anvp21mPgHbNKrohhpn3Loc', '2022-03-04 09:55:14.724794');
INSERT INTO `django_session` VALUES ('mhf74vbjy6xb9ejhkfliujl2hhr8ujv8', '.eJxVj0GOgzAMRa-Csh4q28ElzaoHQaoCuKNIhFAIq6p3H4M0i3pl-z9_22-zb7Ia_zZT_o1zHI03CEDmx8whiVbd3lrXdzsP8Ox29xx71UZZwlqSzOUkbgygBJNoDuKUWPIWS8zzqTdi1aHtA6qSch-nwxlt4wis09C2pBAn7V4ZCZjZ3V-vy5CTSsMqocijxPMgAsIarjVBhdYDeDzGp7CVx_nDP4JQI1dEvmk9NMeGMZZvk1tNrkL0rASYz-cP7FpLMw:1mbOX7:hGQalOn7zoLTFKpl5EikdZ1jZTyKhQvenH5MoHHBD10', '2021-10-29 22:50:05.269606');
INSERT INTO `django_session` VALUES ('s1hjbr74lfmv0c5rzo1mphkwdvvlm5m5', '.eJxVj8sOgyAQRX_FsK7NDPhAVv0QEwM6NiQiRnFl_PeOJk1TVnDPzZnhEPtGqzCHmOLbz34QRiCAFA8x20D8avdaadfuZQ9ju-txcMwGWuyaAs3pbjQlADdKSXwH0txY4uaTj_PNC1JsqJ1FJiE6P11mVIWWoDQfjilYP_3SAprqhZV69jEw7Veyibrk750kSMyhyiVkqAyAwcsw2S119ze-FYQcqwzQFGjKazYNPv1LmlzqDBnX7BHn-QGBU0tI:1mbRY3:nuxgNC4jxQYoxwnyorReVjrHGML_xtUiLzd7d0mv5fo', '2021-10-30 02:03:15.773153');
INSERT INTO `django_session` VALUES ('vqh5kbe4i85qgx2lzo2zua3mw15c4dl6', '.eJw1j8GKwzAMRH-l-Lwpkh07iU_7IYHi2ErWkNglsWGh9N-rBHobaR7SzEvUg3ZhX2LNS0wxCCsQAMWPSG4jnsY6mLYfqzFajbUl9OwFerq9bJTKRbQzIRNgZqaBeiae-Ygl5nT53azZ7yj4sepAmrWDiTXByW55iuv5C9WAUrXadOeaNhdX3vo_Sst_dDnktPy6yd993tj3O7lCjxKvnBIkNtA3KG8IVnVWDsys7iiPq9oXQWhA3WCwrbFanW9CLN8jHMmj4yqddFctYq3VIN7vD4MMWIk:1mXjCN:sSKj0D3bQMzBOCm3Dn8YKR7cdOwPOALNIP65sulKJ7o', '2021-10-19 20:05:31.493052');

-- ----------------------------
-- Table structure for user_Account
-- ----------------------------
DROP TABLE IF EXISTS `user_Account`;
CREATE TABLE `user_Account`  (
  `loginid` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `loginpwd` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `status` tinyint(1) NOT NULL,
  `department` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `position` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `mobile` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `create_time` datetime(6) NULL DEFAULT NULL,
  `edit_time` datetime(6) NULL DEFAULT NULL,
  PRIMARY KEY (`loginid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_Account
-- ----------------------------
INSERT INTO `user_Account` VALUES ('1001', '50567b4ee38a72113f9f094160a76c76', '陈晓东', 1, '信息部', '网络工程师', '13912345678', 'chengxiaodong@abc.com', '2022-03-08 04:45:37.000000', '2021-08-12 10:37:29.000000', '2022-03-08 01:40:56.000000');
INSERT INTO `user_Account` VALUES ('1002', '925b3909b2b56a523300c685a68c593f', '王小进', 1, '销售部', '主管', '13482038888', '13482034096@163.com', '2021-10-16 12:00:34.000000', '2021-06-20 13:00:18.000000', '2022-02-21 15:57:09.000000');
INSERT INTO `user_Account` VALUES ('1003', '50567b4ee38a72113f9f094160a76c76', '陈鹏', 1, '销售部', '大客户专员', '18812345432', 'chenpeng@163.com', '2022-03-08 03:50:18.000000', '2021-05-20 20:24:12.000000', '2022-03-08 00:39:57.000000');
INSERT INTO `user_Account` VALUES ('1004', '50567b4ee38a72113f9f094160a76c76', '柳亚子', 1, '财务部', '主管', '13099887788', 'liuyazi@qq.com', '2022-03-08 03:48:34.000000', '2021-04-20 21:12:44.000000', '2022-03-08 01:41:12.000000');
INSERT INTO `user_Account` VALUES ('1005', '50567b4ee38a72113f9f094160a76c76', '姚文彩', 1, '财务部', '专员', '13411223344', 'yaowencai@163.com', '2021-03-27 21:02:50.000000', '2021-04-20 21:13:05.000000', NULL);
INSERT INTO `user_Account` VALUES ('1007', '50567b4ee38a72113f9f094160a76c76', '王小鹏', 0, '销售部', '主管', '13900993311', 'chenxiaodong@abc.com', '2021-03-02 20:21:40.000000', '2021-05-28 21:08:23.000000', NULL);
INSERT INTO `user_Account` VALUES ('1008', '925b3909b2b56a523300c685a68c593f', '刘磊', 1, '人力资源部', '主管', '13909871234', 'liulei@abc.com', NULL, '2021-08-14 13:28:59.000000', NULL);
INSERT INTO `user_Account` VALUES ('1009', '50567b4ee38a72113f9f094160a76c76', '卢西奥', 1, '信息部', '安全管理员', '13900997755', 'luxiao@abc.com', NULL, '2022-02-21 09:21:47.000000', NULL);

-- ----------------------------
-- Table structure for user_Menu
-- ----------------------------
DROP TABLE IF EXISTS `user_Menu`;
CREATE TABLE `user_Menu`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `icon` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `order` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 10 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_Menu
-- ----------------------------
INSERT INTO `user_Menu` VALUES (1, '基础数据', 'fa fa-sitemap', 10);
INSERT INTO `user_Menu` VALUES (2, '学生管理', 'fa fa-users', 20);
INSERT INTO `user_Menu` VALUES (3, '用户角色', 'fa fa-id-card-o', 30);

-- ----------------------------
-- Table structure for user_Permission
-- ----------------------------
DROP TABLE IF EXISTS `user_Permission`;
CREATE TABLE `user_Permission`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `url` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `order` int(11) NULL DEFAULT NULL,
  `menu_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `user_Permission_menu_id_2ede3c4e_fk_user_Menu_id`(`menu_id`) USING BTREE,
  CONSTRAINT `user_Permission_menu_id_2ede3c4e_fk_user_Menu_id` FOREIGN KEY (`menu_id`) REFERENCES `user_Menu` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_Permission
-- ----------------------------
INSERT INTO `user_Permission` VALUES (1, '院系管理', '/basic/faculty/', 1010, 1);
INSERT INTO `user_Permission` VALUES (2, '专业管理', '/basic/major/', 1020, 1);
INSERT INTO `user_Permission` VALUES (3, '学生信息', '/student/info/', 2010, 2);
INSERT INTO `user_Permission` VALUES (4, '学生照片', '/student/image/', 2020, 2);
INSERT INTO `user_Permission` VALUES (5, '登录账号', '/user/account/', 3010, 3);
INSERT INTO `user_Permission` VALUES (6, '角色信息', '/user/roles/', 3020, 3);
INSERT INTO `user_Permission` VALUES (7, '菜单管理', '/user/menu/', 3030, 3);
INSERT INTO `user_Permission` VALUES (8, '权限管理', '/user/permission/', 3040, 3);

-- ----------------------------
-- Table structure for user_Permission_roles
-- ----------------------------
DROP TABLE IF EXISTS `user_Permission_roles`;
CREATE TABLE `user_Permission_roles`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `permission_id` int(11) NOT NULL,
  `roles_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_Permission_roles_permission_id_roles_id_441073fd_uniq`(`permission_id`, `roles_id`) USING BTREE,
  INDEX `user_Permission_roles_roles_id_eb019eb2_fk_user_Roles_id`(`roles_id`) USING BTREE,
  CONSTRAINT `user_Permission_role_permission_id_1157df4b_fk_user_Perm` FOREIGN KEY (`permission_id`) REFERENCES `user_Permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `user_Permission_roles_roles_id_eb019eb2_fk_user_Roles_id` FOREIGN KEY (`roles_id`) REFERENCES `user_Roles` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_Permission_roles
-- ----------------------------
INSERT INTO `user_Permission_roles` VALUES (8, 1, 1);
INSERT INTO `user_Permission_roles` VALUES (30, 1, 2);
INSERT INTO `user_Permission_roles` VALUES (20, 1, 9);
INSERT INTO `user_Permission_roles` VALUES (1, 2, 1);
INSERT INTO `user_Permission_roles` VALUES (12, 2, 2);
INSERT INTO `user_Permission_roles` VALUES (21, 2, 9);
INSERT INTO `user_Permission_roles` VALUES (31, 2, 10);
INSERT INTO `user_Permission_roles` VALUES (28, 3, 2);
INSERT INTO `user_Permission_roles` VALUES (16, 3, 3);
INSERT INTO `user_Permission_roles` VALUES (22, 3, 9);
INSERT INTO `user_Permission_roles` VALUES (18, 3, 10);
INSERT INTO `user_Permission_roles` VALUES (13, 4, 2);
INSERT INTO `user_Permission_roles` VALUES (17, 4, 3);
INSERT INTO `user_Permission_roles` VALUES (23, 4, 9);
INSERT INTO `user_Permission_roles` VALUES (29, 5, 3);
INSERT INTO `user_Permission_roles` VALUES (24, 5, 9);
INSERT INTO `user_Permission_roles` VALUES (25, 6, 9);
INSERT INTO `user_Permission_roles` VALUES (2, 7, 1);
INSERT INTO `user_Permission_roles` VALUES (26, 7, 9);
INSERT INTO `user_Permission_roles` VALUES (3, 8, 1);
INSERT INTO `user_Permission_roles` VALUES (27, 8, 9);

-- ----------------------------
-- Table structure for user_Roles
-- ----------------------------
DROP TABLE IF EXISTS `user_Roles`;
CREATE TABLE `user_Roles`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `desc` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_Roles
-- ----------------------------
INSERT INTO `user_Roles` VALUES (1, '管理员', '具有所有功能的管理权限');
INSERT INTO `user_Roles` VALUES (2, '老师', '具有老师功能的权限');
INSERT INTO `user_Roles` VALUES (3, '教务主任', '教务主任的权限');
INSERT INTO `user_Roles` VALUES (9, '超级管理员', 'f大撒反对撒');
INSERT INTO `user_Roles` VALUES (10, '辅导员', '班级辅导员');

-- ----------------------------
-- Table structure for user_Roles_account
-- ----------------------------
DROP TABLE IF EXISTS `user_Roles_account`;
CREATE TABLE `user_Roles_account`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `roles_id` int(11) NOT NULL,
  `account_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `user_Roles_account_roles_id_account_id_fea93de4_uniq`(`roles_id`, `account_id`) USING BTREE,
  INDEX `user_Roles_account_account_id_0592418f_fk_user_Account_loginid`(`account_id`) USING BTREE,
  CONSTRAINT `user_Roles_account_account_id_0592418f_fk_user_Account_loginid` FOREIGN KEY (`account_id`) REFERENCES `user_Account` (`loginid`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 16 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user_Roles_account
-- ----------------------------
INSERT INTO `user_Roles_account` VALUES (9, 1, '1002');
INSERT INTO `user_Roles_account` VALUES (7, 2, '1002');
INSERT INTO `user_Roles_account` VALUES (13, 2, '1003');
INSERT INTO `user_Roles_account` VALUES (1, 2, '1009');
INSERT INTO `user_Roles_account` VALUES (11, 3, '1003');
INSERT INTO `user_Roles_account` VALUES (14, 9, '1001');
INSERT INTO `user_Roles_account` VALUES (10, 9, '1002');
INSERT INTO `user_Roles_account` VALUES (12, 10, '1003');
INSERT INTO `user_Roles_account` VALUES (15, 10, '1004');

SET FOREIGN_KEY_CHECKS = 1;
