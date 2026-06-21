from pymongo import MongoClient

mongo_uri = "mongodb://localhost:27017/"
client = MongoClient(mongo_uri)
db = client.admin
collection = db.TEST
query_result = collection.find({})
for data in query_result:
    print(type(data))
