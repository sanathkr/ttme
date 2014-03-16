delimiter $$

USE bookkeeping
$$

DROP PROCEDURE IF EXISTS twitter_get_mentionsTimelineStats_v1
$$

CREATE PROCEDURE twitter_get_mentionsTimelineStats_v1(
  _screen_name VARCHAR(255)
)
BEGIN

  SELECT mentions_timeline_maxid as maxid,
         mentions_timeline_sinceid as sinceid
    FROM twitter
    WHERE screen_name = _screen_name;
END
$$
