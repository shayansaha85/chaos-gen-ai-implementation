import pymongo
import threading
import time

import yaml
import os
import platform

config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.yaml')
try:
    with open(config_path, 'r') as f:
        _config = yaml.safe_load(f)
        mongo_uri = _config.get('mongodb', {}).get('uri', 'mongodb://localhost:27017/')
        mongo_db_name = _config.get('mongodb', {}).get('database', 'admin')
        mongo_coll_name = _config.get('mongodb', {}).get('collection', 'TEST')
except Exception:
    mongo_uri = 'mongodb://localhost:27017/'
    mongo_db_name = 'admin'
    mongo_coll_name = 'TEST'



def perform_long_running_query():
    try:
        client = pymongo.MongoClient(mongo_uri)
        db = client[mongo_db_name]
        collection = db[mongo_coll_name]

        result = collection.find({"category": "Electronics"})
        for doc in result:
            print(doc)
            time.sleep(1)

        client.close()
    except Exception as e:
        print(f"Query interrupted: {e}")

def simulate_interrupted_queries():
    thread = threading.Thread(target=perform_long_running_query)
    thread.start()

    time.sleep(5)
    thread.join()

if __name__ == "__main__":
    print("Simulating interrupted queries on MongoDB...")
    try:
        simulate_interrupted_queries()
        print("Interrupted queries simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
