import MySQLdb
import ConfigParser

dbConnections = dict()
ttmeDB = "ttmeDB"
bookkeepingDB = "bookkeeping"

def getConnection(dbname):
  host = "localhost"
  user = "root"
  password = ""
  port = 3306

  global dbConnections

  if not dbConnections.has_key(dbname):
    dbConnections[dbname] = MySQLdb.connect(host = host,
        user = user,
        passwd = password,
        port = port,
        db = dbname)
    dbConnections[dbname].autocommit(True)

  return dbConnections[dbname]

class CallSproc(object):

  def __init__(self, _dbname,  _sprocname, _argtuple):
    self.sprocname = _sprocname
    self.argtuple = _argtuple
    self.connection = getConnection(_dbname)

  def __enter__(self):
    self.cursor = self.connection.cursor()
    self.cursor.callproc(self.sprocname, self.argtuple)
    return self.cursor

  def __exit__(self, type, value, traceback):
    self.cursor.close()
    # TODO: Add logging of exceptions
