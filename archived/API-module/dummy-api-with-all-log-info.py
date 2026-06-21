import logging
import time
from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

api_time = {}

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

mongo_uri = "mongodb://localhost:27017/"
client = MongoClient(mongo_uri)
db = client.admin
collection = db.TEST

def fetch_from_mongo():
    logging.debug('Fetching data from MongoDB')
    query_start_time = time.time()
    query_result = collection.find({})
    query_time = time.time() - query_start_time
    output = ""
    for data in query_result:
        output += str(data).replace("'", '"')
    return output, query_time

@app.route("/fetch", methods=["GET"])
def fetch():
    api_start_time = time.time()
    data, query_time = fetch_from_mongo()
    api_time["rt"] = time.time() - api_start_time

    logging.info(f'Data fetched successfully - Query Time: {query_time}s - API Time: {api_time["rt"]}s')
    return data

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    response_time = time.time() - request.start_time
    status_code = response.status_code
    latency = response_time - api_time["rt"]

    throughput = 1 / response_time if response_time != 0 else 0

    app.logger.info(
        f"Response Time: {response_time}s - HTTP Status Code: {status_code} - Latency: {latency}s - Throughput: {throughput}/s"
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)
