# README

## Update
* Verify function (Please refer to "How to build it" section)

## Outline
* Purpose
* Pre-requisites
* How to build it
* Reference

## Purpose
1. Use docker to deploy MongoDB with replica set(one primary DB and two secondary DBs).
2. Use python(pymongo) to insert document on primary DB and find the copy on secondary DBs.

## Pre-requisites
Install Docker. 
```
curl -sSL https://get.docker.com/ubuntu/ | sudo sh
```
Pull MongoDB image.
```
docker pull mongo
```
Install pymongo
```
pip install pymongo
```

## How to build it
Set up docker network.
Add new network, my-mongo-cluster.
```
sh network.sh
```

Set up mongoDBs.
Use docker to deploy mongo1, mongo2 and mongo3 and mongo1 is primary DB.
Remember to run each of these commands in a separate terminal window, since we are not running these containers in a detached state.
```
sh db1.sh
sh db2.sh
sh db3.sh
```

Set up DB`s configure. 
- Enter mongo1.
```
docker exec -it mongo1 mongo
```
- Create new database, test.
```
db = (new Mongo(`localhost:27017`)).getDB(`test`)
```
- Enter configure. (Please refer to config)
```
config = {...}
```
- Initialize replica set
```
rs.initiate(config)
```

Use admin.py to verify.
```
# python admin.py MODE INSERT-VALUE
# insert mode
python admin.py 1 20

# check mode
python admin.py 2

# verify mode
python admin.py 3 20
```

## Reference
http://www.sohamkamani.com/blog/2016/06/30/docker-mongo-replica-set/
