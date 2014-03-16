delimiter $$

USE ttmeDB
$$

CREATE TABLE IF NOT EXISTS Contacts(
  id INT AUTO_INCREMENT,
  users_id INT,
  persons_id INT,

  PRIMARY KEY(id),
  FOREIGN KEY(users_id) REFERENCES Users(id),
  FOREIGN KEY(persons_id) REFERENCES Persons(id)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

$$
