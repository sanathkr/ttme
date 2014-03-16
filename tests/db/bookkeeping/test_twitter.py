import pytest
from db.bookkeeping import twitter

class TestTwitterBookkeepingTable:

  @pytest.fixture(scope="function")
  def twitterobj(self, request):

    self.screen_name = "superpowerbutterbunny31415"
    self.cleanup()

    request.addfinalizer(self.cleanup)
    return twitter

  def cleanup(self):
    twitter.delete_forTestOnly(self.screen_name)


  def test_getAndUpdate_mentionsTimelineStats(self, twitterobj):

    # There should be no entry in the table
    stats = twitterobj.getMentionsTimelineStats(self.screen_name)
    assert stats is None

    # Insert one row
    maxid = 1
    sinceid = 2
    twitterobj.updateMentionsTimelineStats(self.screen_name, maxid, sinceid)
    stats = twitterobj.getMentionsTimelineStats(self.screen_name)
    assert stats is not None
    assert stats['maxid'] == maxid
    assert stats['sinceid'] == sinceid


    # Update with new values
    maxid = 1000
    sinceid = 2000
    twitterobj.updateMentionsTimelineStats(self.screen_name, maxid, sinceid)
    stats = twitterobj.getMentionsTimelineStats(self.screen_name)
    assert stats is not None
    assert stats['maxid'] == maxid
    assert stats['sinceid'] == sinceid




