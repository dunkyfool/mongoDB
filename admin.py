import pymongo as mg
import sys

port1 = 30001
port2 = 30002
port3 = 30003

def insert(num):
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
  user = {'No':num}
  db['user1'].insert_one(user)

def check():
  # connect to secondary DB1
  client1 = mg.MongoClient('localhost',port2)

  db1 = client1['test']
  collection1 = db1['user1']
  for doc in collection1.find({'No':{'$lte':50}}):
    print doc

  # connect to secondary DB2
  client2 = mg.MongoClient('localhost',port3)

  db2 = client2['test']
  collection2 = db2['user1']
  for doc in collection2.find({'No':{'$lte':50}}):
    print doc

if __name__=="__main__":
  pass

  # parser
  arg_list = sys.argv
  #print arg_list

  if arg_list[1]=='1': insert(int(arg_list[2]))
  elif arg_list[1]=='2': check()

