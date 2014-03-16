delimiter $$

USE bookkeeping
$$

CREATE TABLE IF NOT EXISTS twitter(
  screen_name VARCHAR(255) NOT NULL,
  mentions_timeline_maxid BIGINT NOT NULL DEFAULT -1,
  mentions_timeline_sinceid BIGINT NOT NULL DEFAULT-1,

  PRIMARY KEY(screen_name)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

$$

