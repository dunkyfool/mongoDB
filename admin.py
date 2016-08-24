import pymongo as mg
import sys

port1 = 32771
port2 = 32771

def insert():
  # connect to mongoDB
  client = mg.MongoClient('localhost',port1)
  print 'MongoClient',client

  # database
  #db_list = client.database_names()
  #print 'show dbs'
  #print db_list #unicode
  #for idx in db_list:
  #  db = client[idx]
  #  print db

  # collection
  db = client['test']
  #collection_list = db.collection_names()
  #print 'show collections'
  #print collection_list #unicode

  # insert document to collection
  user = {'name':'Jackie','age':27}
  db['user1'].insert_one(user)

def check():
  # connect to mongoDB
  client = mg.MongoClient('localhost',port2)

  db = client['test']
  collection = db['user1']
  for doc in collection.find({'age':{'$lte':50}}):
    print doc

if __name__=="__main__":
  pass

  # parser
  arg_list = sys.argv
  #print arg_list

  if arg_list[1]=='1': insert()
  elif arg_list[1]=='2': check()

