from birdy.twitter import UserClient
from db.bookkeeping import twitter as twitterbkdb

apiKey="1AGKJ7CSngPZUYIHx7DQ"
apiSecret="dDSKnzv3PjNtVqURsvFAe52hZIpmmYDGUg6CWAnOuA8"
sanath_accessToken="79386645-ftOEaqlof2cA8DoAkX5P5r7utwi3OwWU7ImI3BzeQ"
sanath_accessSecret="cWDjADGxjeRir5nylD2kKOc6P81x64BX2BFQYVgMGLFeq"

client = UserClient(apiKey, apiSecret, sanath_accessToken, sanath_accessSecret)

class TweetProcessorConfig(object):
  """
    Contains configuration information for tweet processor
  """
  def __init__(self):
    self.num_tweets_per_fetch = 20

class TweetProcessorStatus(object):
  """
    Stores info about tweets that have been processed for the given user.
  """
  def __init__(self, _client, _user):
    self.since_id = 0
    self.max_id = 0
    self.client = _client
    self.get()
    self.user = _user

  def isFirstCall(self):
    return self.since_id == 0

  def get(self):
    stats = twitterbkdb.getMentionsTimelineStats(self.user.screen_name)
    if stats is not None:
      maxid = stats['maxid']
      sinceid = stats['sinceid']

  def save(self):
    twitterbkdb.updateMentionsTimelineStats(self.user.screen_name,
        maxid,
        sinceid)


class User(object):
  """
    Represents a twitter user
  """
  def __init__(self, screen_name):
    self.screen_name = screen_name
    self.user_t = None
    self.getUser()
    self.id = self.user_t.id
    self.id_str = self.user_t.id_str

  def getUser(self):
    response = client.api.users.show.get(
        screen_name = self.screen_name
        )

    self.user_t = response.data


def GetFollowers(client, me):
  """
    Gets the IDs of users that the specified user follows
  """
  cursor = -1
  ids = list()

  while cursor != 0:
    response = client.api.followers.ids.get(
        user_id = me.id,
        cursor = cursor)
    ids.append(response.data.ids)
    cursor = response.data.next_cursor_str

def GetMentionUsers(client, me):
  """
    Gets all mention tweets of the user authorized in the client
  """

  config = TweetProcessorConfig();
  status = TweetProcessorStatus(client)

  if status.isFirstCall():
    mentions = client.api.statuses.mentions_timeline.get(
        count     =  config.num_tweets_per_fetch,
        trim_user = "true"
        ).data
  else:
    mentions = client.api.statuses.mentions_timeline.get(
        count = config.num_tweets_per_fetch,
        since_id  = status.since_id,
        trim_user = "true"
        ).data

  # Add all users that had mentioned me in a tweet
  talker_ids = list()
  for mention in mentions:
      user = mention.user;
      if (user.id_str != me.id_str):
        talker_ids.append(user.id_str)

  # TODO: Update status and save it to db

  return talker_ids


def FindAndSaveTalkers(client, me):
  """
    Function to find all the users that I talk to and save their IDs to database
  """

  me = User("prokilogrammer")
  talker_ids = GetMentionUsers(client, me)
  #SaveToDb(me, talker_ids)



