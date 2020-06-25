# CocoaMySQL dump
# Version 0.7b5
# http://cocoamysql.sourceforge.net
#
# Host: localhost (MySQL 5.0.37)
# Database: hfmysql
# Generation Time: 2007-09-07 12:28:32 -0400
# ************************************************************

# Dump of table car_table
# ------------------------------------------------------------

CREATE TABLE `car_table` (
  `VIN` varchar(16) default NULL,
  `make` varchar(20) default NULL,
  `model` varchar(20) default NULL,
  `color` varchar(20) default NULL,
  `price` decimal(7,2) default NULL,
  `year` varchar(4) default NULL,
  `car_id` int(11) NOT NULL auto_increment,
  PRIMARY KEY  (`car_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

INSERT INTO `car_table` (`VIN`,`make`,`model`,`color`,`price`,`year`,`car_id`) VALUES (NULL,'Porsche','Boxter','silver','39393939392E3939','1998','1');
INSERT INTO `car_table` (`VIN`,`make`,`model`,`color`,`price`,`year`,`car_id`) VALUES (NULL,'Jaguar','XJ',NULL,'39393939392E3939','2000','2');
INSERT INTO `car_table` (`VIN`,`make`,`model`,`color`,`price`,`year`,`car_id`) VALUES (NULL,'Cadillac','Escalade','red','39393939392E3939','2002','3');


