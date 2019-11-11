#! /usr/bin/python3
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
dblist = myclient.database_names()
print(dblist)

# myExam database

mydb = myclient["pyExam"]
mycol = mydb["users"]

for x in mycol.find():
    print(x)
