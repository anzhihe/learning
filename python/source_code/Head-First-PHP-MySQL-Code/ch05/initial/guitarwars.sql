CREATE TABLE `guitarwars` (
  `id` INT AUTO_INCREMENT,
  `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `name` VARCHAR(32),
  `score` INT,
  PRIMARY KEY (`id`),
  KEY `name` (`name`)
);

INSERT INTO `guitarwars` VALUES (1, '2008-04-22 14:37:34', 'Paco Jastorius', 127650);
INSERT INTO `guitarwars` VALUES (2, '2008-04-22 21:27:54', 'Nevil Johansson', 98430);
INSERT INTO `guitarwars` VALUES (3, '2008-04-23 09:06:35', 'Eddie Vanilli', 345900);
INSERT INTO `guitarwars` VALUES (4, '2008-04-23 09:12:53', 'Belita Chevy', 282470);
INSERT INTO `guitarwars` VALUES (5, '2008-04-23 09:13:34', 'Ashton Simpson', 368420);
INSERT INTO `guitarwars` VALUES (6, '2008-04-23 14:09:50', 'Kenny Lavitz', 64930);
