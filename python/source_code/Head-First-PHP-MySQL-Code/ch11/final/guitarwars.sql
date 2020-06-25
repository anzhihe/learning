CREATE TABLE `guitarwars` (
  `id` INT AUTO_INCREMENT,
  `date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `name` VARCHAR(32),
  `score` INT,
  `screenshot` VARCHAR(64),
  `approved` TINYINT(1) DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `name` (`name`)
);

INSERT INTO `guitarwars` VALUES (1, '2008-05-01 20:37:23', 'Paco Jastorius', 127650, 'pacosscore.gif', 1);
INSERT INTO `guitarwars` VALUES (2, '2008-05-01 20:37:02', 'Nevil Johansson', 98430, 'nevilsscore.gif', 1);
INSERT INTO `guitarwars` VALUES (3, '2008-05-01 20:36:45', 'Jacob Scorcherson', 389740, 'jacobsscore.gif', 1);
INSERT INTO `guitarwars` VALUES (4, '2008-05-01 20:36:07', 'Belita Chevy', 282470, 'belitasscore.gif', 1);
INSERT INTO `guitarwars` VALUES (5, '2008-05-01 20:37:40', 'Phiz Lairston', 186580, 'phizsscore.gif', 1);
INSERT INTO `guitarwars` VALUES (6, '2008-05-01 20:38:00', 'Kenny Lavitz', 64930, 'kennysscore.gif', 1);
INSERT INTO `guitarwars` VALUES (7, '2008-05-01 20:38:23', 'Jean Paul Jones', 243260, 'jeanpaulsscore.gif', 1);
INSERT INTO `guitarwars` VALUES (8, '2008-06-20 15:46:31', 'Owen Owens', 500, 'unverified.gif', 0);
INSERT INTO `guitarwars` VALUES (9, '2008-05-01 21:14:56', 'Leddy Gee', 308710, 'leddysscore.gif', 1);
INSERT INTO `guitarwars` VALUES (10, '2008-05-01 21:15:17', 'T-Bone Taylor', 354190, 'tbonesscore.gif', 1);
INSERT INTO `guitarwars` VALUES (11, '2008-06-20 15:47:29', 'Ruby Toupee', 1000, 'unverified.gif', 0);
INSERT INTO `guitarwars` VALUES (12, '2008-05-02 20:32:54', 'Biff Jeck', 314340, 'biffsscore.gif', 1);
INSERT INTO `guitarwars` VALUES (13, '2008-05-02 20:36:28', 'Pez Law', 322710, 'pezsscore.gif', 0);
INSERT INTO `guitarwars` VALUES (14, '2008-05-05 23:28:07', 'Jacob Scorcherson', 465730, 'jacobsscore2.gif', 1);
