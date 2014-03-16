delimiter $$

USE bookkeeping
$$

DROP PROCEDURE IF EXISTS twitter_delete_row_v1
$$

CREATE PROCEDURE twitter_delete_row_v1(
  _screen_name VARCHAR(255)
)
BEGIN

  DELETE FROM twitter WHERE screen_name = _screen_name;
END
$$
