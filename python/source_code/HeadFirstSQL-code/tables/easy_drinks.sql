# Dump of table easy_drinks
# ------------------------------------------------------------

CREATE TABLE `easy_drinks` (
  `drink_name` varchar(16) default NULL,
  `main` varchar(20) default NULL,
  `amount1` decimal(3,1) default NULL,
  `second` varchar(20) default NULL,
  `amount2` decimal(4,2) default NULL,
  `directions` varchar(250) default NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

INSERT INTO `easy_drinks` (`drink_name`,`main`,`amount1`,`second`,`amount2`,`directions`) VALUES ('Kiss on the Lips','cherry juice',2.0,'apricot nectar',7.00,'serve over ice with straw');
INSERT INTO `easy_drinks` (`drink_name`,`main`,`amount1`,`second`,`amount2`,`directions`) VALUES ('Hot Gold','peach nectar',3.0,'orange juice',6.00,'pour hot orange juice in mug and add peach nectar');
INSERT INTO `easy_drinks` (`drink_name`,`main`,`amount1`,`second`,`amount2`,`directions`) VALUES ('Lone Tree','soda',1.5,'cherry juice',0.75,'stir with ice, strain into cocktail glass');
INSERT INTO `easy_drinks` (`drink_name`,`main`,`amount1`,`second`,`amount2`,`directions`) VALUES ('Greyhound','soda',1.5,'grapefruit juice',5.00,'serve over ice, stir well');
INSERT INTO `easy_drinks` (`drink_name`,`main`,`amount1`,`second`,`amount2`,`directions`) VALUES ('Indian Summer','apple juice',2.0,'hot tea',6.00,'add juice to mug and top off with hot tea');
INSERT INTO `easy_drinks` (`drink_name`,`main`,`amount1`,`second`,`amount2`,`directions`) VALUES ('Bull Frog','iced tea',1.5,'lemonade',5.00,'serve over ice with lime slice');
INSERT INTO `easy_drinks` (`drink_name`,`main`,`amount1`,`second`,`amount2`,`directions`) VALUES ('Soda and It','soda',2.0,'grape juice',1.00,'shake in cocktail glass, no ice');
INSERT INTO `easy_drinks` (`drink_name`,`main`,`amount1`,`second`,`amount2`,`directions`) VALUES ('Blackthorn','tonic water',1.5,'pineapple juice',1.00,'stir with ice, strain into cocktail glass with lemon twist');
INSERT INTO `easy_drinks` (`drink_name`,`main`,`amount1`,`second`,`amount2`,`directions`) VALUES ('Blue Moon','soda',1.5,'blueberry juice',0.75,'stir with ice, strain into cocktail glass with lemon twist');
INSERT INTO `easy_drinks` (`drink_name`,`main`,`amount1`,`second`,`amount2`,`directions`) VALUES ('Oh My Gosh','peach nectar',1.0,'pineapple juice',1.00,'stir with ice, strain into shot glass');
INSERT INTO `easy_drinks` (`drink_name`,`main`,`amount1`,`second`,`amount2`,`directions`) VALUES ('Lime Fizz','Sprite',1.5,'lime juice',0.75,'stir with ice, strain into cocktail glass');


