CREATE TABLE `mismatch_topic` (
  `topic_id` INT AUTO_INCREMENT,
  `name` VARCHAR(48),
  `category` VARCHAR(48),
  `category_id` INT,
  PRIMARY KEY (`topic_id`)
);

INSERT INTO `mismatch_topic` VALUES (1, 'Tattoos', 'Appearance', 1);
INSERT INTO `mismatch_topic` VALUES (2, 'Gold chains', 'Appearance', 1);
INSERT INTO `mismatch_topic` VALUES (3, 'Body piercings', 'Appearance', 1);
INSERT INTO `mismatch_topic` VALUES (4, 'Cowboy boots', 'Appearance', 1);
INSERT INTO `mismatch_topic` VALUES (5, 'Long hair', 'Appearance', 1);
INSERT INTO `mismatch_topic` VALUES (6, 'Reality TV', 'Entertainment', 2);
INSERT INTO `mismatch_topic` VALUES (7, 'Professional wrestling', 'Entertainment', 2);
INSERT INTO `mismatch_topic` VALUES (8, 'Horror movies', 'Entertainment', 2);
INSERT INTO `mismatch_topic` VALUES (9, 'Easy listening music', 'Entertinment', 2);
INSERT INTO `mismatch_topic` VALUES (10, 'The opera', 'Entertainment', 2);
INSERT INTO `mismatch_topic` VALUES (11, 'Sushi', 'Food', 3);
INSERT INTO `mismatch_topic` VALUES (12, 'Spam', 'Food', 3);
INSERT INTO `mismatch_topic` VALUES (13, 'Spicy food', 'Food', 3);
INSERT INTO `mismatch_topic` VALUES (14, 'Peanut butter & banana sandwiches', 'Food', 3);
INSERT INTO `mismatch_topic` VALUES (15, 'Martinis', 'Food', 3);
INSERT INTO `mismatch_topic` VALUES (16, 'Howard Stern', 'People', 4);
INSERT INTO `mismatch_topic` VALUES (17, 'Bill Gates', 'Peopel', 4);
INSERT INTO `mismatch_topic` VALUES (18, 'Barbara Streisand', 'People', 4);
INSERT INTO `mismatch_topic` VALUES (19, 'Hugh Hefner', 'People', 4);
INSERT INTO `mismatch_topic` VALUES (20, 'Martha Stewart', 'People', 4);
INSERT INTO `mismatch_topic` VALUES (21, 'Yoga', 'Activities', 5);
INSERT INTO `mismatch_topic` VALUES (22, 'Weightlifting', 'Activities', 5);
INSERT INTO `mismatch_topic` VALUES (23, 'Cube puzzles', 'Activities', 5);
INSERT INTO `mismatch_topic` VALUES (24, 'Karaoke', 'Activities', 5);
INSERT INTO `mismatch_topic` VALUES (25, 'Hiking', 'Activities', 5);
