# CocoaMySQL dump
# Version 0.7b5
# http://cocoamysql.sourceforge.net
#
# Host: localhost (MySQL 5.0.37)
# Database: hfmysql
# Generation Time: 2007-09-10 09:51:48 -0400
# ************************************************************

# Dump of table toy_ids
# ------------------------------------------------------------

CREATE TABLE `toy_ids` (
  `toy_id` int(11) NOT NULL auto_increment,
  `toy` varchar(30) NOT NULL,
  PRIMARY KEY  (`toy_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

INSERT INTO `toy_ids` (`toy_id`,`toy`) VALUES ('5','whiffleball');
INSERT INTO `toy_ids` (`toy_id`,`toy`) VALUES ('6','frisbee');
INSERT INTO `toy_ids` (`toy_id`,`toy`) VALUES ('9','kite');
INSERT INTO `toy_ids` (`toy_id`,`toy`) VALUES ('12','yoyo');


# Dump of table toy_other
# ------------------------------------------------------------

CREATE TABLE `toy_other` (
  `toy_id` int(11) NOT NULL,
  `store_id` int(11) NOT NULL,
  `color` varchar(30) NOT NULL,
  `inventory` int(11) default NULL,
  `address` varchar(30) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `toy_other` (`toy_id`,`store_id`,`color`,`inventory`,`address`) VALUES ('5','1','white','34','23 Maple');
INSERT INTO `toy_other` (`toy_id`,`store_id`,`color`,`inventory`,`address`) VALUES ('5','3','yellow','12','100 E. North St.');
INSERT INTO `toy_other` (`toy_id`,`store_id`,`color`,`inventory`,`address`) VALUES ('5','1','blue','5','23 Maple');
INSERT INTO `toy_other` (`toy_id`,`store_id`,`color`,`inventory`,`address`) VALUES ('6','2','green','10','1902 Amber Ln.');
INSERT INTO `toy_other` (`toy_id`,`store_id`,`color`,`inventory`,`address`) VALUES ('6','4','yellow','24','17 Engleside');
INSERT INTO `toy_other` (`toy_id`,`store_id`,`color`,`inventory`,`address`) VALUES ('9','1','red','50','23 Maple');
INSERT INTO `toy_other` (`toy_id`,`store_id`,`color`,`inventory`,`address`) VALUES ('9','2','blue','2','1902 Amber Ln.');
INSERT INTO `toy_other` (`toy_id`,`store_id`,`color`,`inventory`,`address`) VALUES ('9','2','green','18','1902 Amber Ln.');
INSERT INTO `toy_other` (`toy_id`,`store_id`,`color`,`inventory`,`address`) VALUES ('12','4','white','28','17 Engleside');
INSERT INTO `toy_other` (`toy_id`,`store_id`,`color`,`inventory`,`address`) VALUES ('12','4','yellow','11','17 Engleside');


