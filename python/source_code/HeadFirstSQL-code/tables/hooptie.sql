# CocoaMySQL dump
# Version 0.7b5
# http://cocoamysql.sourceforge.net
#
# Host: localhost (MySQL 5.0.37)
# Database: hfmysql
# Generation Time: 2007-09-07 12:11:16 -0400
# ************************************************************

# Dump of table hooptie
# ------------------------------------------------------------

CREATE TABLE `hooptie` (
  `color` varchar(20) default NULL,
  `year` varchar(4) default NULL,
  `make` varchar(20) default NULL,
  `mo` varchar(20) default NULL,
  `howmuch` float(10,3) default NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `hooptie` (`color`,`year`,`make`,`mo`,`howmuch`) VALUES ('silver','1998','Porsche','Boxter','17992.539');
INSERT INTO `hooptie` (`color`,`year`,`make`,`mo`,`howmuch`) VALUES (NULL,'2000','Jaguar','XJ','15995.000');
INSERT INTO `hooptie` (`color`,`year`,`make`,`mo`,`howmuch`) VALUES ('red','2002','Cadillac','Escalade','40215.898');


