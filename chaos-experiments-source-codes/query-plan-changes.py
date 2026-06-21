import pymongo

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



def perform_query_plan_changes():
    try:
        client = pymongo.MongoClient(mongo_uri)
        db = client[mongo_db_name]
        collection = db[mongo_coll_name]

        result_1 = collection.find({"category": "Electronics"})
        for doc in result_1:
            print(doc)

        result_2 = collection.find({"amount": {"$gt": 1000}})

        for doc in result_2:
            print(doc)

        client.close()
    except Exception as e:
        print(f"Query plan changes failed: {e}")

if __name__ == "__main__":
    print("Simulating query plan changes on MongoDB...")
    try:
        perform_query_plan_changes()
        print("Query plan changes simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
