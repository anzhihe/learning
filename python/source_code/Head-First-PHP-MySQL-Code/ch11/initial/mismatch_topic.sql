CREATE TABLE `mismatch_topic` (
  `topic_id` INT AUTO_INCREMENT,
  `name` VARCHAR(48),
  `category_id` INT,
  PRIMARY KEY (`topic_id`)
);

INSERT INTO `mismatch_topic` VALUES (1, 'Tattoos', 1);
INSERT INTO `mismatch_topic` VALUES (2, 'Gold chains', 1);
INSERT INTO `mismatch_topic` VALUES (3, 'Body piercings', 1);
INSERT INTO `mismatch_topic` VALUES (4, 'Cowboy boots', 1);
INSERT INTO `mismatch_topic` VALUES (5, 'Long hair', 1);
INSERT INTO `mismatch_topic` VALUES (6, 'Reality TV', 2);
INSERT INTO `mismatch_topic` VALUES (7, 'Professional wrestling', 2);
INSERT INTO `mismatch_topic` VALUES (8, 'Horror movies', 2);
INSERT INTO `mismatch_topic` VALUES (9, 'Easy listening music', 2);
INSERT INTO `mismatch_topic` VALUES (10, 'The opera', 2);
INSERT INTO `mismatch_topic` VALUES (11, 'Sushi', 3);
INSERT INTO `mismatch_topic` VALUES (12, 'Spam', 3);
INSERT INTO `mismatch_topic` VALUES (13, 'Spicy food', 3);
INSERT INTO `mismatch_topic` VALUES (14, 'Peanut butter & banana sandwiches', 3);
INSERT INTO `mismatch_topic` VALUES (15, 'Martinis', 3);
INSERT INTO `mismatch_topic` VALUES (16, 'Howard Stern', 4);
INSERT INTO `mismatch_topic` VALUES (17, 'Bill Gates', 4);
INSERT INTO `mismatch_topic` VALUES (18, 'Barbara Streisand', 4);
INSERT INTO `mismatch_topic` VALUES (19, 'Hugh Hefner', 4);
INSERT INTO `mismatch_topic` VALUES (20, 'Martha Stewart', 4);
INSERT INTO `mismatch_topic` VALUES (21, 'Yoga', 5);
INSERT INTO `mismatch_topic` VALUES (22, 'Weightlifting', 5);
INSERT INTO `mismatch_topic` VALUES (23, 'Cube puzzles', 5);
INSERT INTO `mismatch_topic` VALUES (24, 'Karaoke', 5);
INSERT INTO `mismatch_topic` VALUES (25, 'Hiking', 5);
