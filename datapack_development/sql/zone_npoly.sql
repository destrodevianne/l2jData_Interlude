-- 
-- Table structure for table `zone_npoly`
-- 
DROP TABLE IF EXISTS `zone_npoly`;
CREATE TABLE `zone_npoly` (
  `id` int(11) NOT NULL,
  `order` int(11) NOT NULL,
  `x` int(11) NOT NULL,
  `y` int(11) NOT NULL,
  PRIMARY KEY  (`id`,`order`)
);

-- 
-- Dumping data for table `zone_npoly`
-- 

INSERT INTO `zone_npoly` (`id`, `order`, `x`, `y`) VALUES (11020, 0, -3800, -3300),
(11020, 1, 80242, 143523),
(11020, 2, 83676, 143507),
(11020, 3, 83688, 141483),
(11020, 4, 84080, 141471),
(11020, 5, 84080, 143510),
(11020, 6, 85036, 143512),
(11020, 7, 85046, 145750),
(11020, 8, 86136, 145736),
(11020, 9, 86120, 146905),
(11020, 10, 88416, 146896),
(11020, 11, 90465, 147173),
(11020, 12, 90494, 147573),
(11020, 13, 86780, 153625),
(11020, 14, 92601, 153518),
(11020, 15, 79180, 152845),
(11020, 16, 77166, 149886),
(11020, 17, 77143, 147395),
(11020, 18, 79157, 144755),
(11400, 0, -3991, -3759),
(11400, 1, 83327, 143509),
(11400, 2, 83031, 143121),
(11400, 3, 82475, 142974),
(11400, 4, 82174, 142486),
(11400, 5, 82333, 141833),
(11400, 6, 82955, 141507),
(11400, 7, 83288, 141763),
(11400, 8, 83683, 141814),
(11400, 9, 83680, 143500);