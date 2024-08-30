from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

client = MongoClient("mongodb://localhost:27017/")
db = client.new_db
collection = db.db_new
# var = collection.insert_one({"name": "Billy"}).inserted_id
for document in collection.find():
    pprint(document)

# print(collection)
# print(document)
# print(var)
