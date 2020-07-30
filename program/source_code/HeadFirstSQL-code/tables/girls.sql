
# Dump of table girls
# ------------------------------------------------------------

CREATE TABLE `girls` (
  `girl_id` int(11) default NULL,
  `girl` varchar(20) default NULL,
  `toy_id` int(11) default NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `girls` (`girl_id`,`girl`,`toy_id`) VALUES ('1','Jane','3');
INSERT INTO `girls` (`girl_id`,`girl`,`toy_id`) VALUES ('2','Sally','4');
INSERT INTO `girls` (`girl_id`,`girl`,`toy_id`) VALUES ('3','Cindy','1');
INSERT INTO `girls` (`girl_id`,`girl`,`toy_id`) VALUES ('4','Mandy','1');
