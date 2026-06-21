from flask import *
from pymongo import MongoClient


def fetch_from_mongo():

    mongo_uri = "mongodb://localhost:27017/"
    client = MongoClient(mongo_uri)
    db = client.admin
    collection = db.TEST
    query_result = collection.find({})
    output = ""
    for data in query_result:
        output = output + str(data).replace("'", '"')
    return output


print(fetch_from_mongo())

app = Flask(__name__)

@app.route("/fetch", methods = ["GET"])
def fetch():
    return fetch_from_mongo()

app.run(debug = True)



