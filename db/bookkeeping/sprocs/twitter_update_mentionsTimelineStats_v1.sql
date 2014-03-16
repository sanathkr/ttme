delimiter $$

USE bookkeeping
$$

DROP PROCEDURE IF EXISTS twitter_update_mentionsTimelineStats_v1
$$

CREATE PROCEDURE twitter_update_mentionsTimelineStats_v1(
  _screen_name VARCHAR(255),
  maxid BIGINT,
  sinceid BIGINT
)
BEGIN

  INSERT INTO twitter (screen_name, mentions_timeline_maxid, mentions_timeline_sinceid)
  VALUES (_screen_name, maxid, sinceid)
  ON DUPLICATE KEY UPDATE
    mentions_timeline_maxid = maxid,
    mentions_timeline_sinceid = sinceid;
END
$$
