from db.common import sql

def getMentionsTimelineStats(screen_name):
  args = (screen_name,)
  sprocname = "twitter_get_mentionsTimelineStats_v1"

  with sql.CallSproc(sql.bookkeepingDB, sprocname, args) as cursor:
    result = cursor.fetchall()
    if len(result) == 0:
      return None

    # This query should return only one row
    row = result[0]
    return {'maxid'   : row[0],
            'sinceid' : row[1]}

  return None


def updateMentionsTimelineStats(screen_name, maxid, sinceid):
  args = (screen_name, maxid, sinceid)
  sprocname = "twitter_update_mentionsTimelineStats_v1"

  with sql.CallSproc(sql.bookkeepingDB, sprocname, args) as cursor:
    # No results will be returned by this query
    pass


def delete_forTestOnly(screen_name):
  args = (screen_name, )
  sprocname = "twitter_delete_row_v1"

  with sql.CallSproc(sql.bookkeepingDB, sprocname, args) as cursor:
    pass

