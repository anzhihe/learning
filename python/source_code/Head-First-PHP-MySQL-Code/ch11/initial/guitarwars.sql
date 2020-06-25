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

INSERT INTO `guitarwars` VALUES (21, '2008-05-01 20:36:07', 'Belita Chevy', 282470, 'belitasscore.gif', 1);
INSERT INTO `guitarwars` VALUES (22, '2008-05-01 20:36:45', 'Jacob Scorcherson', 389740, 'jacobsscore.gif', 1);
INSERT INTO `guitarwars` VALUES (23, '2008-05-01 20:37:02', 'Nevil Johansson', 98430, 'nevilsscore.gif', 1);
INSERT INTO `guitarwars` VALUES (24, '2008-05-01 20:37:23', 'Paco Jastorius', 127650, 'pacosscore.gif', 1);
INSERT INTO `guitarwars` VALUES (25, '2008-05-01 20:37:40', 'Phiz Lairston', 186580, 'phizsscore.gif', 1);
INSERT INTO `guitarwars` VALUES (26, '2008-05-01 20:38:00', 'Kenny Lavitz', 64930, 'kennysscore.gif', 1);
INSERT INTO `guitarwars` VALUES (27, '2008-05-01 20:38:23', 'Jean Paul Jones', 243260, 'jeanpaulsscore.gif', 1);
INSERT INTO `guitarwars` VALUES (28, '2008-05-01 21:14:56', 'Leddy Gee', 308710, 'leddysscore.gif', 1);
INSERT INTO `guitarwars` VALUES (29, '2008-05-01 21:15:17', 'T-Bone Taylor', 354190, 'tbonesscore.gif', 1);
INSERT INTO `guitarwars` VALUES (31, '2008-05-02 20:32:54', 'Biff Jeck', 314340, 'biffsscore.gif', 1);
INSERT INTO `guitarwars` VALUES (32, '2008-05-02 20:36:38', 'Pez Law', 322710, 'pezsscore.gif', 1);
INSERT INTO `guitarwars` VALUES (34, '2008-05-05 23:28:07', 'Jacob Scorcherson', 465730, 'jacobsscore2.gif', 1);
INSERT INTO `guitarwars` VALUES (35, '2008-06-23 11:45:15', 'www.classhates.com', 999999999, 'classhates.png', 0);
INSERT INTO `guitarwars` VALUES (36, '2008-06-23 11:45:29', 'www.classhates.com', 999999999, 'classhates.png', 0);
INSERT INTO `guitarwars` VALUES (37, '2008-06-23 11:45:53', 'www.frowneycentral.com', 999999999, 'frowneycentral.png', 0);
INSERT INTO `guitarwars` VALUES (38, '2008-06-23 11:46:06', 'www.frowneycentral.com', 999999999, 'frowneycentral.png', 0);
INSERT INTO `guitarwars` VALUES (39, '2008-06-23 11:46:19', 'www.frowneycentral.com', 999999999, 'frowneycentral.png', 0);
INSERT INTO `guitarwars` VALUES (40, '2008-06-23 11:47:26', 'www.frowneycentral.com', 999999999, 'frowneycentral.png', 0);
INSERT INTO `guitarwars` VALUES (41, '2008-06-23 11:47:42', 'www.frowneycentral.com', 999999999, 'frowneycentral.png', 0);
INSERT INTO `guitarwars` VALUES (42, '2008-06-23 11:47:55', 'www.headlastlabs.com', 999999999, 'headlastlabs.png', 0);
INSERT INTO `guitarwars` VALUES (43, '2008-06-23 11:48:12', 'www.headlastlabs.com', 999999999, 'headlastlabs.png', 0);
INSERT INTO `guitarwars` VALUES (44, '2008-06-23 11:52:20', 'www.headlastlabs.com', 999999999, 'headlastlabs.png', 0);
INSERT INTO `guitarwars` VALUES (45, '2008-06-23 11:50:24', 'www.headlastlabs.com', 999999999, 'headlastlabs.png', 0);
INSERT INTO `guitarwars` VALUES (46, '2008-06-23 11:52:32', 'www.headlastlabs.com', 999999999, 'headlastlabs.png', 0);
