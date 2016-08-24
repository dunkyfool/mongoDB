import pymongo as mg
from bson.objectid import ObjectId
import sys

port1 = 30001
port2 = 30002
port3 = 30003

def insert(num):
  # connect to mongoDB
  client = mg.MongoClient('localhost',port1)
  #print 'MongoClient',client

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
  _id = db['user1'].insert_one(user).inserted_id
  #print _id
  return _id

def update():
  db = mg.MongoClient('localhost',port1)
  _id_list = []
  for doc in db['test']['user1'].find({'No':{'$lte':50}}):
    #print doc['_id'], type(doc['_id'])
    _id = doc['_id']
    value = doc['No']
    db['test']['user1'].update({'_id':_id},{'$set':{'No':value+10}})
    _id_list += [_id]
  return _id_list

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
    print type(doc)

def verify(num):
  # insert 
  print 'Insert value',num
  _id = insert(num)
  print 'ObjectID: ',_id# , type(_id)
  #_id = ObjectId('57bd4f2eb7b3f24d78385716')

  # check 
  prime = mg.MongoClient('localhost',port1)
  sec1 = mg.MongoClient('localhost',port2)
  sec2 = mg.MongoClient('localhost',port3)

  #print prime['test']['user1'].find({'_id':_id})
  #print type(prime['test']['user1'].find({'_id':_id}))
  origin_data = []
  bak1 = []
  bak2 = []
  for doc in prime['test']['user1'].find({'_id':_id}):
    origin_data += [doc]
  for doc in sec1['test']['user1'].find({'_id':_id}):
    bak1 += [doc]
  for doc in sec2['test']['user1'].find({'_id':_id}):
    bak2 += [doc]

  #print origin_data
  #print bak1
  #print bak2
  if origin_data == bak1:
    print 'Secondary1 backup successfully'
  else:
    print 'Secondary1 FAIL to backup'
  if origin_data == bak2:
    print 'Secondary2 backup successfully'
  else:
    print 'Secondary2 FAIL to backup'

def verify_update():
  _id_list = update()

  prime = mg.MongoClient('localhost',port1)
  sec1 = mg.MongoClient('localhost',port2)
  sec2 = mg.MongoClient('localhost',port3)

  for _id in _id_list:
      origin_data = []
      bak1 = []
      bak2 = []
      for doc in prime['test']['user1'].find({'_id':_id}):
        origin_data += [doc]
      for doc in sec1['test']['user1'].find({'_id':_id}):
        bak1 += [doc]
      for doc in sec2['test']['user1'].find({'_id':_id}):
        bak2 += [doc]

      #print origin_data
      #print bak1
      #print bak2
      print 'ObjectID', _id
      if origin_data == bak1:
        print 'Secondary1 backup successfully'
      else:
        print 'Secondary1 FAIL to backup'
      if origin_data == bak2:
        print 'Secondary2 backup successfully'
      else:
        print 'Secondary2 FAIL to backup'

if __name__=="__main__":
  pass

  # parser
  arg_list = sys.argv
  #print arg_list

  if arg_list[1]=='1': _ = insert(int(arg_list[2]))
  elif arg_list[1]=='2': check()
  elif arg_list[1]=='3': verify(int(arg_list[2]))
  elif arg_list[1]=='4': _ = update()
  elif arg_list[1]=='5': verify_update()

