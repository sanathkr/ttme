delimiter $$

USE ttmeDB
$$

CREATE TABLE IF NOT EXISTS Users(
  id INT AUTO_INCREMENT,
  username VARCHAR(64),
  password VARCHAR(64),
  persons_id INT,

  PRIMARY KEY(id),
  FOREIGN KEY (persons_id) REFERENCES Persons (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

$$
