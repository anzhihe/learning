CREATE TABLE `mismatch_response` (
  `response_id` INT AUTO_INCREMENT,
  `user_id` INT,
  `topic_id` INT,
  `response` TINYINT,
  PRIMARY KEY (`response_id`)
);
