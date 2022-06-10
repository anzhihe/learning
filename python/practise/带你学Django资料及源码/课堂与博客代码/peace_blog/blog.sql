-- MySQL dump 10.13  Distrib 8.0.18, for macos10.14 (x86_64)
--
-- Host: localhost    Database: db_1907_blog
-- ------------------------------------------------------
-- Server version	5.7.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add user',6,'add_bloguser'),(22,'Can change user',6,'change_bloguser'),(23,'Can delete user',6,'delete_bloguser'),(24,'Can view user',6,'view_bloguser'),(25,'Can add banner',7,'add_banner'),(26,'Can change banner',7,'change_banner'),(27,'Can delete banner',7,'delete_banner'),(28,'Can view banner',7,'view_banner'),(29,'Can add friend link',8,'add_friendlink'),(30,'Can change friend link',8,'change_friendlink'),(31,'Can delete friend link',8,'delete_friendlink'),(32,'Can view friend link',8,'view_friendlink'),(33,'Can add article',9,'add_article'),(34,'Can change article',9,'change_article'),(35,'Can delete article',9,'delete_article'),(36,'Can view article',9,'view_article'),(37,'Can add comment',10,'add_comment'),(38,'Can change comment',10,'change_comment'),(39,'Can delete comment',10,'delete_comment'),(40,'Can view comment',10,'view_comment'),(41,'Can add tag',11,'add_tag'),(42,'Can change tag',11,'change_tag'),(43,'Can delete tag',11,'delete_tag'),(44,'Can view tag',11,'view_tag'),(45,'Can add category',12,'add_category'),(46,'Can change category',12,'change_category'),(47,'Can delete category',12,'delete_category'),(48,'Can view category',12,'view_category');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_article`
--

DROP TABLE IF EXISTS `blog_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `title` varchar(100) NOT NULL,
  `intro` varchar(255) NOT NULL,
  `vnum` int(11) NOT NULL,
  `cover` varchar(100) NOT NULL,
  `is_top` tinyint(1) NOT NULL,
  `content` longtext NOT NULL,
  `category_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_article_category_id_7e38f15e_fk_blog_category_id` (`category_id`),
  KEY `blog_article_user_id_5beb0cc1_fk_blog_bloguser_id` (`user_id`),
  CONSTRAINT `blog_article_category_id_7e38f15e_fk_blog_category_id` FOREIGN KEY (`category_id`) REFERENCES `blog_category` (`id`),
  CONSTRAINT `blog_article_user_id_5beb0cc1_fk_blog_bloguser_id` FOREIGN KEY (`user_id`) REFERENCES `blog_bloguser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_article`
--

LOCK TABLES `blog_article` WRITE;
/*!40000 ALTER TABLE `blog_article` DISABLE KEYS */;
INSERT INTO `blog_article` VALUES (1,0,'2019-12-30 01:28:48.097928','2020-01-02 02:07:48.204107','史上最细致压枪教学：5分钟让你掌握压枪技巧 遇到韦神也能干趴他','史上最细致压枪教学：5分钟让你掌握压枪技巧 遇到韦神也能干趴他',120029,'article/2019/12/30/4afbfbedab64034fe4c38d781db354340a551d33.jpeg',0,'<p style=\"margin-top: 0px; margin-bottom: 0px; padding: 0px; line-height: 24px; color: rgb(51, 51, 51); text-align: justify; font-family: arial; white-space: normal; background-color: rgb(255, 255, 255);\"><span class=\"bjh-p\">相信玩过绝地求生的玩家都知道压枪这个概念，那么到底什么是压枪？新手该怎么练习呢？</span></p><p style=\"margin-top: 22px; margin-bottom: 0px; padding: 0px; line-height: 24px; color: rgb(51, 51, 51); text-align: justify; font-family: arial; white-space: normal; background-color: rgb(255, 255, 255);\"><span class=\"bjh-p\">本期就为大家带来了最详细的压枪教学，5分钟让你快速掌握吃鸡必备的压枪技巧！</span></p><p style=\"margin-top: 22px; margin-bottom: 0px; padding: 0px; line-height: 24px; color: rgb(51, 51, 51); text-align: justify; font-family: arial; white-space: normal; background-color: rgb(255, 255, 255);\"><span class=\"bjh-p\"><span class=\"bjh-strong\" style=\"font-size: 18px; font-weight: 700;\">一、什么是压枪？</span></span></p><p style=\"margin-top: 22px; margin-bottom: 0px; padding: 0px; line-height: 24px; color: rgb(51, 51, 51); text-align: justify; font-family: arial; white-space: normal; background-color: rgb(255, 255, 255);\"><span class=\"bjh-p\">我们都知道绝地求生的武器有后坐力，如果你不移动鼠标，只是单纯的点击左键进行射击，你的弹道会自动的往左右弹，并且你的枪口会一直往上跑！</span></p><p><span class=\"bjh-p\"><br/></span></p><p style=\"text-align: center;\"><img src=\"/media/article/content/4afbfbedab64034fe4c38d781db354340a551d33_20191230092820.jpeg\" title=\"\" alt=\"4afbfbedab64034fe4c38d781db354340a551d33.jpeg\"/></p><p style=\"margin-top: 26px; margin-bottom: 0px; padding: 0px; line-height: 24px; color: rgb(51, 51, 51); text-align: justify; font-family: arial; white-space: normal; background-color: rgb(255, 255, 255);\"><span class=\"bjh-p\">这是没有压枪的武器Scar扫射效果，我们从中不难看出，武器左右抖动的频率很低，上下移动频率极高，所谓的压枪只要能保证将你的枪口往下移动，保证你的子弹射击出去在一个点上，就算完成了！</span></p>',2,1),(2,0,'2019-12-30 01:30:29.593518','2020-01-03 00:45:17.959378','吃鸡新手教程，带你少走弯路走向“吃鸡巅峰”，朋友们看过来','吃鸡新手教程，带你少走弯路走向“吃鸡巅峰”，朋友们看过来',100001622,'article/2019/12/30/9f510fb30f2442a7f0413e160507584ed0130284.jpeg',1,'<p><span style=\"color: rgb(51, 51, 51); font-family: arial; text-align: justify; background-color: rgb(255, 255, 255);\">嗨！大家好，又见面了，今天小编带大家一起看看吃鸡游戏是怎么玩儿的，继续了解一下那些吃鸡大神们的各种套路，但是在你学会各种套路之前你还是要掌握一些基本知识的，只有根基扎好了，你才能够把楼层越建越高。今天小编就给你们打打根基。</span></p><p style=\"text-align: center;\"><img src=\"/media/article/content/u=1318925952,565209989&fm=173&app=49&f=JPEG_20191230093004.jpeg\" title=\"\" alt=\"u=1318925952,565209989&amp;fm=173&amp;app=49&amp;f=JPEG.jpeg\"/><span style=\"color: rgb(51, 51, 51); font-family: arial; text-align: justify; background-color: rgb(255, 255, 255);\">首先，在开启吃鸡游戏的时候，大家都会登上一个莫名其妙的飞机，然后飞向同一个地方，飞呀飞飞呀，飞在飞机上最好和你的队友们商量好跳在哪里，他到什么区域，有的人在飞机上说可以在居民区或者集装箱附近，因为这里东西不仅会多点，没错，小编也表示赞同，所以你们就跳到这里吧。</span></p>',1,1),(3,0,'2019-12-30 01:44:16.748151','2020-01-02 02:20:17.967497','你们的吃鸡新外观来了！反正不要钱，干嘛不点进来看看','你们的吃鸡新外观来了！反正不要钱，干嘛不点进来看看',1104,'article/2019/12/30/f8d24e3131a6426db8282c234a56738c.jpeg',0,'<p style=\"border: 0px; margin-top: 0.63em; margin-bottom: 1.8em; padding: 0px; counter-reset: list-1 0 list-2 0 list-3 0 list-4 0 list-5 0 list-6 0 list-7 0 list-8 0 list-9 0; color: rgb(25, 25, 25); font-family: &quot;PingFang SC&quot;, Arial, 微软雅黑, 宋体, simsun, sans-serif; white-space: normal; background-color: rgb(255, 255, 255);\"><span style=\"border: 0px; margin: 0px; padding: 0px;\">剑网3“怒海争锋”资料片火热测试中，除了已经上线的资料片武学调整，名剑大会“开房间”模式，全新战场匹配机制等诸多内容外，备受关注的海岛吃鸡地图——</span><span style=\"border: 0px; margin: 0px; padding: 0px;\">“沧溟绝境”</span><span style=\"border: 0px; margin: 0px; padding: 0px;\">也将于明日在测试服抢先体验，一场别开生面的海岛对决即将拉开序幕！</span></p><p style=\"border: 0px; margin-top: 0.63em; margin-bottom: 1.8em; padding: 0px; counter-reset: list-1 0 list-2 0 list-3 0 list-4 0 list-5 0 list-6 0 list-7 0 list-8 0 list-9 0; color: rgb(25, 25, 25); font-family: &quot;PingFang SC&quot;, Arial, 微软雅黑, 宋体, simsun, sans-serif; white-space: normal; background-color: rgb(255, 255, 255);\"><span style=\"border: 0px; margin: 0px; padding: 0px;\">与此同时，大家一直关注的新一代</span><span style=\"border: 0px; margin: 0px; padding: 0px;\">“吃鸡套”</span><span style=\"border: 0px; margin: 0px; padding: 0px;\">本次全部奉上，两种款式各有特色，三娘已经按捺不住激动的心情给你们爆料了！</span></p><p style=\"border: 0px; margin-top: 0.63em; margin-bottom: 1.8em; padding: 0px; counter-reset: list-1 0 list-2 0 list-3 0 list-4 0 list-5 0 list-6 0 list-7 0 list-8 0 list-9 0; color: rgb(25, 25, 25); font-family: &quot;PingFang SC&quot;, Arial, 微软雅黑, 宋体, simsun, sans-serif; white-space: normal; background-color: rgb(255, 255, 255);\"><span style=\"border: 0px; margin: 0px; padding: 0px;\">海岛吃鸡专属外观抢先看</span></p><p style=\"border: 0px; margin-top: 0.63em; margin-bottom: 1.8em; padding: 0px; counter-reset: list-1 0 list-2 0 list-3 0 list-4 0 list-5 0 list-6 0 list-7 0 list-8 0 list-9 0; color: rgb(25, 25, 25); font-family: &quot;PingFang SC&quot;, Arial, 微软雅黑, 宋体, simsun, sans-serif; white-space: normal; background-color: rgb(255, 255, 255);\"><span style=\"border: 0px; margin: 0px; padding: 0px;\">全新沧溟绝境外观“天河赋云”系列延续了过往“吃鸡套”一贯的设计风格，服装整体色调以黑色为主，在引入“夜行衣”概念的设计上结合“刺客”元素加以定制！打造出来的外观整体干练修身，</span><span style=\"font-weight: 700; border: 0px; margin: 0px; padding: 0px;\">完整</span><span style=\"border: 0px; margin: 0px; padding: 0px;\">与<span style=\"font-weight: 700; border: 0px; margin: 0px; padding: 0px;\">破损</span>的两种不同款式</span><span style=\"border: 0px; margin: 0px; padding: 0px;\">表现各具特色，气场十足！</span></p><p style=\"border: 0px; margin-top: 0.63em; margin-bottom: 1.8em; padding: 0px; counter-reset: list-1 0 list-2 0 list-3 0 list-4 0 list-5 0 list-6 0 list-7 0 list-8 0 list-9 0; color: rgb(25, 25, 25); font-family: &quot;PingFang SC&quot;, Arial, 微软雅黑, 宋体, simsun, sans-serif; white-space: normal; background-color: rgb(255, 255, 255);\"><span style=\"border: 0px; margin: 0px; padding: 0px;\">衣角边缘的破碎和斑驳的血迹等细节的融入，展现出侠士生死鏖战后的真实面貌。侠士可以等”沧溟绝境”玩法登陆正式服后，通过体验海岛吃鸡</span><span style=\"border: 0px; margin: 0px; padding: 0px;\">积攒“<span style=\"font-weight: 700; border: 0px; margin: 0px; padding: 0px;\">飞沙令</span>”进行兑换</span><span style=\"border: 0px; margin: 0px; padding: 0px;\">！</span></p><p style=\"text-align: center;\"><img src=\"/media/article/content/f8d24e3131a6426db8282c234a56738c_20191230094326.jpeg\" title=\"\" alt=\"f8d24e3131a6426db8282c234a56738c.jpeg\"/></p><p style=\"border: 0px; margin-top: 0.63em; margin-bottom: 1.8em; padding: 0px; counter-reset: list-1 0 list-2 0 list-3 0 list-4 0 list-5 0 list-6 0 list-7 0 list-8 0 list-9 0; color: rgb(25, 25, 25); font-family: &quot;PingFang SC&quot;, Arial, 微软雅黑, 宋体, simsun, sans-serif; white-space: normal; background-color: rgb(255, 255, 255);\"><span style=\"border: 0px; margin: 0px; padding: 0px;\">吃鸡奇趣道具抢先看</span></p><p style=\"border: 0px; margin-top: 0.63em; margin-bottom: 1.8em; padding: 0px; counter-reset: list-1 0 list-2 0 list-3 0 list-4 0 list-5 0 list-6 0 list-7 0 list-8 0 list-9 0; color: rgb(25, 25, 25); font-family: &quot;PingFang SC&quot;, Arial, 微软雅黑, 宋体, simsun, sans-serif; white-space: normal; background-color: rgb(255, 255, 255);\"><span style=\"border: 0px; margin: 0px; padding: 0px;\">隐匿和变身对于吃鸡玩家来说也是一门学问。适当的伪装既能适时保护自己，同时又不会影响游戏体验。也就是我们说的“有攻有防，攻防结合”，最大程度体验到游戏的魅力所在，也能将策略发挥到极致。</span></p><p style=\"border: 0px; margin-top: 0.63em; margin-bottom: 1.8em; padding: 0px; counter-reset: list-1 0 list-2 0 list-3 0 list-4 0 list-5 0 list-6 0 list-7 0 list-8 0 list-9 0; color: rgb(25, 25, 25); font-family: &quot;PingFang SC&quot;, Arial, 微软雅黑, 宋体, simsun, sans-serif; white-space: normal; background-color: rgb(255, 255, 255);\"><span style=\"border: 0px; margin: 0px; padding: 0px;\">而在全新的“沧溟绝境”地图当中，除了优化了复活机制并引入了海龙卷风圈等全新概念，还设计了一系列与新地图主题契合的</span><span style=\"border: 0px; margin: 0px; padding: 0px;\">吃鸡道具</span><span style=\"border: 0px; margin: 0px; padding: 0px;\">，令得海岛吃鸡的玩法变得更加有趣且富有战略性！</span></p><p style=\"text-align: center;\"><br/></p>',3,1);
/*!40000 ALTER TABLE `blog_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_article_tag`
--

DROP TABLE IF EXISTS `blog_article_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_article_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_article_tag_article_id_tag_id_818e752b_uniq` (`article_id`,`tag_id`),
  KEY `blog_article_tag_tag_id_f2afe66b_fk_blog_tag_id` (`tag_id`),
  CONSTRAINT `blog_article_tag_article_id_8db2395e_fk_blog_article_id` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`id`),
  CONSTRAINT `blog_article_tag_tag_id_f2afe66b_fk_blog_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `blog_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_article_tag`
--

LOCK TABLES `blog_article_tag` WRITE;
/*!40000 ALTER TABLE `blog_article_tag` DISABLE KEYS */;
INSERT INTO `blog_article_tag` VALUES (1,1,1),(2,1,3),(3,2,1),(4,2,2),(5,2,3),(6,2,4),(7,3,1),(8,3,3),(9,3,4);
/*!40000 ALTER TABLE `blog_article_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_banner`
--

DROP TABLE IF EXISTS `blog_banner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_banner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `title` varchar(10) NOT NULL,
  `cover` varchar(100) NOT NULL,
  `link` varchar(200) NOT NULL,
  `position` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_banner`
--

LOCK TABLES `blog_banner` WRITE;
/*!40000 ALTER TABLE `blog_banner` DISABLE KEYS */;
INSERT INTO `blog_banner` VALUES (1,0,'2019-12-30 01:16:31.157388','2019-12-30 01:25:09.556885','和平精英1','banner/2019/12/30/01.jpg','https://www.baidu.com/',1),(2,0,'2019-12-30 01:16:48.990889','2019-12-30 01:16:48.990945','和平精英2','banner/2019/12/30/02.jpeg','https://www.baidu.com/',0),(3,0,'2019-12-30 01:16:59.402904','2019-12-30 01:16:59.402942','和平精英3','banner/2019/12/30/03.jpeg','https://www.baidu.com/',0);
/*!40000 ALTER TABLE `blog_banner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_bloguser`
--

DROP TABLE IF EXISTS `blog_bloguser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_bloguser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `phone` varchar(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_bloguser`
--

LOCK TABLES `blog_bloguser` WRITE;
/*!40000 ALTER TABLE `blog_bloguser` DISABLE KEYS */;
INSERT INTO `blog_bloguser` VALUES (1,'pbkdf2_sha256$120000$eUso7axOuPD3$fpb7zwC0ZTEyuW4gZ1I8LB+x24Ao3dVgL10Y+P3ezSI=','2020-01-02 02:07:59.401746',1,'xiaoyuan','','','xiaoyuan@qq.com',1,1,'2019-12-30 01:01:35.210448',''),(2,'pbkdf2_sha256$120000$v1Gn6VKV9sF5$MVb3Ax/k13NO5/76ECfLbjqfM/CXswCUIpxkc43+2Y4=',NULL,0,'xiaoyuan3','','','',0,1,'2020-01-01 12:32:15.246353','13812345679'),(3,'pbkdf2_sha256$120000$Rs8D7AOs3TPS$LrGsrH+ZspDVR6G/W+q1JN6MtX/lnjaUhe3Wsbcp/lk=',NULL,0,'xiaoyuan4','','','',0,1,'2020-01-01 12:32:32.779994','13812345987'),(4,'pbkdf2_sha256$120000$2Yym2aoUAnV2$Mge4CoLQxSZOqwiS0vrEozpvQi+1dk94V/PxUWb8qGk=',NULL,0,'xiaoyuan5','','','',0,1,'2020-01-01 12:33:29.743957','18512345678'),(5,'pbkdf2_sha256$120000$XnmVqXepct4w$r8v04p1MMj4Rp2EzbxYHv6JKUFpo5ABYog2cu3bKSmA=','2020-01-01 12:49:13.625250',0,'xiaoyuan6','','','',0,1,'2020-01-01 12:34:19.242160','18612345678'),(6,'pbkdf2_sha256$120000$CJGqUJqURm2b$O5U/sfomMUkaAKxMDLuLxy1j2VLSf0GeXsffEe97UMU=','2020-01-02 01:41:04.499721',0,'xiaoyuan11','','','',0,1,'2020-01-02 01:38:16.904121','13812345678'),(7,'pbkdf2_sha256$120000$1GEK8TTszVzD$uZ77yedoqgUctRtQlSvevtas4DvqshMAdhEurfSVltU=','2020-01-02 01:41:29.058273',0,'xiaoyuan12','','','',0,1,'2020-01-02 01:41:25.988619','13912345678');
/*!40000 ALTER TABLE `blog_bloguser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_bloguser_groups`
--

DROP TABLE IF EXISTS `blog_bloguser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_bloguser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bloguser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_bloguser_groups_bloguser_id_group_id_4388f522_uniq` (`bloguser_id`,`group_id`),
  KEY `blog_bloguser_groups_group_id_e04739c4_fk_auth_group_id` (`group_id`),
  CONSTRAINT `blog_bloguser_groups_bloguser_id_26d40e56_fk_blog_bloguser_id` FOREIGN KEY (`bloguser_id`) REFERENCES `blog_bloguser` (`id`),
  CONSTRAINT `blog_bloguser_groups_group_id_e04739c4_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_bloguser_groups`
--

LOCK TABLES `blog_bloguser_groups` WRITE;
/*!40000 ALTER TABLE `blog_bloguser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `blog_bloguser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_bloguser_user_permissions`
--

DROP TABLE IF EXISTS `blog_bloguser_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_bloguser_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bloguser_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_bloguser_user_permi_bloguser_id_permission_i_20c5c0f5_uniq` (`bloguser_id`,`permission_id`),
  KEY `blog_bloguser_user_p_permission_id_2a62b8fe_fk_auth_perm` (`permission_id`),
  CONSTRAINT `blog_bloguser_user_p_bloguser_id_3a67e1c8_fk_blog_blog` FOREIGN KEY (`bloguser_id`) REFERENCES `blog_bloguser` (`id`),
  CONSTRAINT `blog_bloguser_user_p_permission_id_2a62b8fe_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_bloguser_user_permissions`
--

LOCK TABLES `blog_bloguser_user_permissions` WRITE;
/*!40000 ALTER TABLE `blog_bloguser_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `blog_bloguser_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_category`
--

DROP TABLE IF EXISTS `blog_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(10) NOT NULL,
  `position` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_category`
--

LOCK TABLES `blog_category` WRITE;
/*!40000 ALTER TABLE `blog_category` DISABLE KEYS */;
INSERT INTO `blog_category` VALUES (1,0,'2019-12-30 01:26:59.360009','2019-12-30 01:26:59.360218','吃鸡教程',0),(2,0,'2019-12-30 01:27:04.722563','2019-12-30 01:27:04.722635','压枪教程',0),(3,0,'2019-12-30 01:43:59.532138','2019-12-30 01:43:59.532201','广告',0);
/*!40000 ALTER TABLE `blog_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_comment`
--

DROP TABLE IF EXISTS `blog_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `content` varchar(255) NOT NULL,
  `article_id` int(11) NOT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_comment_article_id_3d58bca6_fk_blog_article_id` (`article_id`),
  KEY `blog_comment_users_id_b92b6eff_fk_blog_bloguser_id` (`users_id`),
  CONSTRAINT `blog_comment_article_id_3d58bca6_fk_blog_article_id` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`id`),
  CONSTRAINT `blog_comment_users_id_b92b6eff_fk_blog_bloguser_id` FOREIGN KEY (`users_id`) REFERENCES `blog_bloguser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_comment`
--

LOCK TABLES `blog_comment` WRITE;
/*!40000 ALTER TABLE `blog_comment` DISABLE KEYS */;
INSERT INTO `blog_comment` VALUES (1,0,'2019-12-30 01:48:22.706668','2019-12-30 01:48:22.706818','不错呀',3,1),(2,0,'2019-12-30 01:52:48.026447','2019-12-30 01:52:48.026547','可以呀',1,1),(3,0,'2019-12-30 01:54:08.473405','2019-12-30 01:54:08.473444','真的不错呀',3,1),(4,0,'2019-12-30 01:59:48.145625','2019-12-30 01:59:48.145733','可以的',1,1),(5,0,'2020-01-02 02:07:07.446190','2020-01-02 02:07:07.446225','哈哈哈',3,1),(6,0,'2020-01-02 02:07:14.327959','2020-01-02 02:07:14.327995','可以的呀',3,1),(7,0,'2020-01-02 02:08:59.057285','2020-01-02 02:08:59.057333','好卡德生科技大胜靠德哈萨克较好的空间撒谎的吉安市可简单哈市',3,1);
/*!40000 ALTER TABLE `blog_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_friendlink`
--

DROP TABLE IF EXISTS `blog_friendlink`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_friendlink` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(255) NOT NULL,
  `link` varchar(200) NOT NULL,
  `position` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_friendlink`
--

LOCK TABLES `blog_friendlink` WRITE;
/*!40000 ALTER TABLE `blog_friendlink` DISABLE KEYS */;
INSERT INTO `blog_friendlink` VALUES (1,0,'2019-12-30 02:10:10.671418','2019-12-30 02:10:10.671493','百度','https://www.baidu.com/',0),(2,0,'2019-12-30 02:10:27.377316','2019-12-30 02:10:27.377376','hao123','https://www.hao123.com/',0);
/*!40000 ALTER TABLE `blog_friendlink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_tag`
--

DROP TABLE IF EXISTS `blog_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `blog_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `created_time` datetime(6) NOT NULL,
  `updated_time` datetime(6) NOT NULL,
  `name` varchar(10) NOT NULL,
  `position` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_tag`
--

LOCK TABLES `blog_tag` WRITE;
/*!40000 ALTER TABLE `blog_tag` DISABLE KEYS */;
INSERT INTO `blog_tag` VALUES (1,0,'2019-12-30 01:27:17.633351','2019-12-30 01:27:17.633394','游戏',0),(2,0,'2019-12-30 01:27:20.909616','2019-12-30 01:27:20.909659','光子',0),(3,0,'2019-12-30 01:27:25.418340','2019-12-30 01:27:25.418382','手游',0),(4,0,'2019-12-30 01:27:28.343892','2019-12-30 01:27:28.343937','充钱',0);
/*!40000 ALTER TABLE `blog_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_blog_bloguser_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_blog_bloguser_id` FOREIGN KEY (`user_id`) REFERENCES `blog_bloguser` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-12-30 01:16:31.160658','1','和平精英1',1,'[{\"added\": {}}]',7,1),(2,'2019-12-30 01:16:48.993943','2','和平精英2',1,'[{\"added\": {}}]',7,1),(3,'2019-12-30 01:16:59.404283','3','和平精英3',1,'[{\"added\": {}}]',7,1),(4,'2019-12-30 01:25:09.558453','1','和平精英1',2,'[{\"changed\": {\"fields\": [\"position\"]}}]',7,1),(5,'2019-12-30 01:26:59.361392','1','吃鸡教程',1,'[{\"added\": {}}]',12,1),(6,'2019-12-30 01:27:04.724420','2','压枪教程',1,'[{\"added\": {}}]',12,1),(7,'2019-12-30 01:27:17.635182','1','游戏',1,'[{\"added\": {}}]',11,1),(8,'2019-12-30 01:27:20.910594','2','光子',1,'[{\"added\": {}}]',11,1),(9,'2019-12-30 01:27:25.420609','3','手游',1,'[{\"added\": {}}]',11,1),(10,'2019-12-30 01:27:28.344824','4','充钱',1,'[{\"added\": {}}]',11,1),(11,'2019-12-30 01:28:48.106072','1','史上最细致压枪教学：5分钟让你掌握压枪技巧 遇到韦神也能干趴他',1,'[{\"added\": {}}]',9,1),(12,'2019-12-30 01:30:29.603987','2','吃鸡新手教程，带你少走弯路走向“吃鸡巅峰”，朋友们看过来',1,'[{\"added\": {}}]',9,1),(13,'2019-12-30 01:43:59.534239','3','广告',1,'[{\"added\": {}}]',12,1),(14,'2019-12-30 01:44:16.758733','3','你们的吃鸡新外观来了！反正不要钱，干嘛不点进来看看',1,'[{\"added\": {}}]',9,1),(15,'2019-12-30 01:48:22.708298','1','不错呀',1,'[{\"added\": {}}]',10,1),(16,'2019-12-30 01:52:48.027911','2','可以呀',1,'[{\"added\": {}}]',10,1),(17,'2019-12-30 01:54:08.474317','3','真的不错呀',1,'[{\"added\": {}}]',10,1),(18,'2019-12-30 01:59:48.147137','4','可以的',1,'[{\"added\": {}}]',10,1),(19,'2019-12-30 02:10:10.672862','1','百度',1,'[{\"added\": {}}]',8,1),(20,'2019-12-30 02:10:27.378765','2','hao123',1,'[{\"added\": {}}]',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(9,'blog','article'),(7,'blog','banner'),(6,'blog','bloguser'),(12,'blog','category'),(10,'blog','comment'),(8,'blog','friendlink'),(11,'blog','tag'),(4,'contenttypes','contenttype'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-12-27 07:54:24.179351'),(2,'contenttypes','0002_remove_content_type_name','2019-12-27 07:54:24.230767'),(3,'auth','0001_initial','2019-12-27 07:54:24.404086'),(4,'auth','0002_alter_permission_name_max_length','2019-12-27 07:54:24.435538'),(5,'auth','0003_alter_user_email_max_length','2019-12-27 07:54:24.442378'),(6,'auth','0004_alter_user_username_opts','2019-12-27 07:54:24.450650'),(7,'auth','0005_alter_user_last_login_null','2019-12-27 07:54:24.459258'),(8,'auth','0006_require_contenttypes_0002','2019-12-27 07:54:24.463681'),(9,'auth','0007_alter_validators_add_error_messages','2019-12-27 07:54:24.471637'),(10,'auth','0008_alter_user_username_max_length','2019-12-27 07:54:24.481998'),(11,'auth','0009_alter_user_last_name_max_length','2019-12-27 07:54:24.492254'),(12,'blog','0001_initial','2019-12-27 07:54:24.686720'),(13,'admin','0001_initial','2019-12-27 07:54:24.768658'),(14,'admin','0002_logentry_remove_auto_add','2019-12-27 07:54:24.780151'),(15,'admin','0003_logentry_add_action_flag_choices','2019-12-27 07:54:24.791013'),(16,'sessions','0001_initial','2019-12-27 07:54:24.834679'),(17,'blog','0002_auto_20191230_0857','2019-12-30 00:57:27.632341');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('rngz1fage9lfrbly9q2eemtqo9oid6tq','ZDdmNDg4ZDI0MjliMjZjZDg3NDYzM2RjYTFiODBmNDRlODZkZTQzNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzNzcxZjNlOGQ0NmUwZmEwZDdlNWY3ZmQxZWRjYTE3NTI1NjA1MDRiIn0=','2020-01-13 01:01:52.005892'),('tpfgrekbpqrt0vrnwnw18t2h07u96shi','ZDdmNDg4ZDI0MjliMjZjZDg3NDYzM2RjYTFiODBmNDRlODZkZTQzNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzNzcxZjNlOGQ0NmUwZmEwZDdlNWY3ZmQxZWRjYTE3NTI1NjA1MDRiIn0=','2020-01-16 02:07:59.403993');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-03 10:39:47
