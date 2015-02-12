import psycopg2
import os
import web
from ConfigParser import SafeConfigParser


def getConnection():
  config = SafeConfigParser()
  config.read(os.path.join(os.getcwd(),'config/klpconfig.ini'))
  db = config.get('Database','dbname')
  username = config.get('Database','user')
  passwd = config.get('Database','passwd')
  dsn = "dbname="+db+" user="+username+" host='localhost' password="+passwd
  connection = psycopg2.connect(dsn)
  return connection

def getWebDbConnection():
  config = SafeConfigParser()
  config.read(os.path.join(os.getcwd(),'config/klpconfig.ini'))
  dbname = config.get('Database','dbname')
  username = config.get('Database','user')
  passwd = config.get('Database','passwd')
  dbtype='postgres'
  connection = web.database(dbn=dbtype,user=username,pw=passwd.strip('\''),db=dbname)
  return connection

def getWebDbConnection1():
  config = SafeConfigParser()
  config.read(os.path.join(os.getcwd(),'config/klpconfig.ini'))
  dbname = config.get('Database1','dbname')
  username = config.get('Database1','user')
  passwd = config.get('Database1','passwd')
  dbtype='postgres'
  print "dbn="+dbtype+",user="+username+",pw="+passwd+",db="+dbname
  connection = web.database(dbn=dbtype,user=username,pw=passwd.strip('\''),db=dbname)
  return connection
