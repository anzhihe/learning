CREATE TABLE `mismatch_user` (
  `user_id` INT AUTO_INCREMENT,
  `username` VARCHAR(32),
  `password` VARCHAR(40),
  `join_date` DATETIME,
  `first_name` VARCHAR(32),
  `last_name` VARCHAR(32),
  `gender` VARCHAR(1),
  `birthdate` DATE,
  `city` VARCHAR(32),
  `state` VARCHAR(2),
  `picture` VARCHAR(32),
  PRIMARY KEY (`user_id`)
);

INSERT INTO `mismatch_user` VALUES (1, 'sidneyk', '745c52f30f82d4323292dcca9eea0aee87feecc5', '2008-06-03 14:51:46', 'Sidney', 'Kelsow', 'F', '1984-07-19', 'Tempe', 'AZ', 'sidneypic.jpg');
INSERT INTO `mismatch_user` VALUES (2, 'nevilj', '12a20bcb5ed139a5f3fc808704897762cbab74ec', '2008-06-03 14:52:09', 'Nevil', 'Johansson', 'M', '1973-05-13', 'Reno', 'NV', 'nevilpic.jpg');
INSERT INTO `mismatch_user` VALUES (3, 'alexc', '676a6666682bd41bef5fd1c1f629fa233b1307a4', '2008-06-03 14:53:05', 'Alex', 'Cooper', 'M', '1974-09-13', 'Boise', 'ID', 'alexpic.jpg');
INSERT INTO `mismatch_user` VALUES (4, 'sdaniels', '1ff915f2fae864032e44cbe5a6cdd858500c9df7', '2008-06-03 14:58:40', 'Susannah', 'Daniels', 'F', '1977-02-23', 'Pasadena', 'CA', 'susannahpic.jpg');
INSERT INTO `mismatch_user` VALUES (5, 'ethelh', '53a56acb2a52f3815a2518e75029b071c298477a', '2008-06-03 15:00:37', 'Ethel', 'Heckel', 'F', '1943-03-27', 'Wichita', 'KS', 'ethelpic.jpg');
INSERT INTO `mismatch_user` VALUES (6, 'oklugman', 'df00f36c0b795c30a0409778d7f9db27a970f74f', '2008-06-03 15:00:48', 'Oscar', 'Klugman', 'M', '1968-06-04', 'Providence', 'RI', 'oscarpic.jpg');
INSERT INTO `mismatch_user` VALUES (7, 'belitac', '7c19dd287e03ae31ce190c4043b5a7f9795c41dc', '2008-06-03 15:01:08', 'Belita', 'Chevy', 'F', '1975-07-08', 'El Paso', 'TX', 'belitapic.jpg');
INSERT INTO `mismatch_user` VALUES (8, 'jasonf', '3da70cd115b7c3a7cebc2b5282706f07d185de9e', '2008-06-03 15:01:19', 'Jason', 'Filmington', 'M', '1969-09-24', 'Hollywood', 'CA', 'jasonpic.jpg');
INSERT INTO `mismatch_user` VALUES (9, 'dierdre', '08447be571e1c113f2f175472753ca5f5af454f3', '2008-06-03 15:01:51', 'Dierdre', 'Pennington', 'F', '1970-04-26', 'Cambridge', 'MA', 'dierdrepic.jpg');
INSERT INTO `mismatch_user` VALUES (10, 'baldpaul', '230dcb28e2d1dc19ec14990721e85cd5c5234245', '2008-06-03 15:02:02', 'Paul', 'Hillsman', 'M', '1964-12-18', 'Charleston', 'SC', 'paulpic.jpg');
INSERT INTO `mismatch_user` VALUES (11, 'jnettles', 'e511d793f532dbe0e0483538e11977f7b7c33b28', '2008-06-03 15:02:13', 'Johan', 'Nettles', 'M', '1981-11-03', 'Athens', 'GA', 'johanpic.jpg');
INSERT INTO `mismatch_user` VALUES (12, 'rubyr', '062e4a8476b1063e05caa69958e36a905f887619', '2008-06-03 15:02:24', 'Ruby', 'Reasons', 'F', '1972-09-18', 'Conundrum', 'AZ', 'rubypic.jpg');
