# CocoaMySQL dump
# Version 0.7b5
# http://cocoamysql.sourceforge.net
#
# Host: localhost (MySQL 5.0.37)
# Database: hfmysql
# Generation Time: 2007-09-10 10:13:51 -0400
# ************************************************************

# Dump of table store_info
# ------------------------------------------------------------

CREATE TABLE `store_info` (
  `store_id` int(11) NOT NULL auto_increment,
  `address` varchar(50) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `manager` varchar(50) NOT NULL,
  PRIMARY KEY  (`store_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

INSERT INTO `store_info` (`store_id`,`address`,`phone`,`manager`) VALUES ('1','23 Maple','555-6712','Joe');
INSERT INTO `store_info` (`store_id`,`address`,`phone`,`manager`) VALUES ('2','1902 Amber Ln','555-3478','Susan');
INSERT INTO `store_info` (`store_id`,`address`,`phone`,`manager`) VALUES ('3','100 E. North St.','555-0987','Tara');
INSERT INTO `store_info` (`store_id`,`address`,`phone`,`manager`) VALUES ('4','17 Engleside','555-6554','Gordon');


# Dump of table store_inventory
# ------------------------------------------------------------

CREATE TABLE `store_inventory` (
  `toy_id` int(11) NOT NULL,
  `store_id` int(11) NOT NULL,
  `inventory` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `store_inventory` (`toy_id`,`store_id`,`inventory`) VALUES ('5','1','34');
INSERT INTO `store_inventory` (`toy_id`,`store_id`,`inventory`) VALUES ('5','3','12');
INSERT INTO `store_inventory` (`toy_id`,`store_id`,`inventory`) VALUES ('5','1','5');
INSERT INTO `store_inventory` (`toy_id`,`store_id`,`inventory`) VALUES ('6','2','10');
INSERT INTO `store_inventory` (`toy_id`,`store_id`,`inventory`) VALUES ('6','4','24');
INSERT INTO `store_inventory` (`toy_id`,`store_id`,`inventory`) VALUES ('9','1','50');
INSERT INTO `store_inventory` (`toy_id`,`store_id`,`inventory`) VALUES ('9','2','2');
INSERT INTO `store_inventory` (`toy_id`,`store_id`,`inventory`) VALUES ('9','2','18');
INSERT INTO `store_inventory` (`toy_id`,`store_id`,`inventory`) VALUES ('12','4','28');
INSERT INTO `store_inventory` (`toy_id`,`store_id`,`inventory`) VALUES ('12','4','11');


# Dump of table toy_info
# ------------------------------------------------------------

CREATE TABLE `toy_info` (
  `toy_id` int(11) NOT NULL,
  `toy` varchar(30) default NULL,
  `color` varchar(30) NOT NULL,
  `cost` decimal(5,2) default NULL,
  `weight` decimal(5,2) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `toy_info` (`toy_id`,`toy`,`color`,`cost`,`weight`) VALUES ('1','whiffleball','white','312E3935','302E3330');
INSERT INTO `toy_info` (`toy_id`,`toy`,`color`,`cost`,`weight`) VALUES ('2','whiffleball','yellow','322E3230','302E3430');
INSERT INTO `toy_info` (`toy_id`,`toy`,`color`,`cost`,`weight`) VALUES ('3','whiffleball','blue','312E3935','302E3330');
INSERT INTO `toy_info` (`toy_id`,`toy`,`color`,`cost`,`weight`) VALUES ('4','frisbee','green','332E3530','302E3530');
INSERT INTO `toy_info` (`toy_id`,`toy`,`color`,`cost`,`weight`) VALUES ('5','frisbee','yellow','312E3530','302E3230');
INSERT INTO `toy_info` (`toy_id`,`toy`,`color`,`cost`,`weight`) VALUES ('6','kite','red','352E3735','312E3230');
INSERT INTO `toy_info` (`toy_id`,`toy`,`color`,`cost`,`weight`) VALUES ('7','kite','blue','352E3735','312E3230');
INSERT INTO `toy_info` (`toy_id`,`toy`,`color`,`cost`,`weight`) VALUES ('8','kite','green','332E3135','302E3830');
INSERT INTO `toy_info` (`toy_id`,`toy`,`color`,`cost`,`weight`) VALUES ('9','yoyo','white','342E3235','302E3530');
INSERT INTO `toy_info` (`toy_id`,`toy`,`color`,`cost`,`weight`) VALUES ('10','yoyo','yellow','312E3530','302E3230');


