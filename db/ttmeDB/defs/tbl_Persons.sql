delimiter $$

USE ttmeDB
$$

CREATE TABLE IF NOT EXISTS Persons(
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,

  # Twitter handles
  twitter_id VARCHAR(16),
  twitter_screen_name VARCHAR(100),

  PRIMARY KEY(id),
  INDEX ix_person_twitter_scrname USING HASH (twitter_screen_name)

) ENGINE=InnoDB DEFAULT CHARSET=latin1;

$$
