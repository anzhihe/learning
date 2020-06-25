CREATE TABLE `email_list` (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(20),
  `last_name` VARCHAR(20),
  `email` VARCHAR(60),
  PRIMARY KEY (`id`)
);

INSERT INTO `email_list` VALUES (1, 'Denny', 'Bubbleton', 'denny@mightygumball.net');
INSERT INTO `email_list` VALUES (2, 'Irma', 'Werlitz', 'iwer@aliensabductedme.com');
INSERT INTO `email_list` VALUES (3, 'Elbert', 'Kreslee', 'elbert@kresleesprockets.biz');
INSERT INTO `email_list` VALUES (5, 'Don', 'Draper', 'draper@sterling-cooper.com');
