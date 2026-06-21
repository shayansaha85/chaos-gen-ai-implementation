import logging
from flask import Flask
from pymongo import MongoClient

# Configure the Flask app
app = Flask(__name__)

# Configure the logging module
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_from_mongo():
    # Your MongoDB fetching code here
    logging.debug('Fetching data from MongoDB')
    mongo_uri = "mongodb://localhost:27017/"
    client = MongoClient(mongo_uri)
    db = client.admin
    collection = db.TEST
    query_result = collection.find({})
    output = ""
    for data in query_result:
        output = output + str(data).replace("'", '"')
    return output

@app.route("/fetch", methods=["GET"])
def fetch():
    data = fetch_from_mongo()
    logging.info('Data fetched successfully')
    return data

if __name__ == "__main__":
    app.run(debug=True)