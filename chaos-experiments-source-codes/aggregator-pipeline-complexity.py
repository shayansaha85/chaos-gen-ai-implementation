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



def perform_complex_aggregation():
    try:
        client = pymongo.MongoClient(mongo_uri)
        db = client[mongo_db_name]
        collection = db[mongo_coll_name]

        pipeline = [
            {"$match": {"category": "Electronics"}},
            {"$group": {"_id": "$subcategory", "total": {"$sum": "$amount"}}},
            {"$sort": {"total": -1}},
            {"$limit": 5},
        ]

        result = collection.aggregate(pipeline)

        for doc in result:
            print(doc)

        client.close()
    except Exception as e:
        print(f"Aggregation pipeline complexity failed: {e}")

if __name__ == "__main__":
    print("Simulating aggregation pipeline complexity on MongoDB...")
    try:
        perform_complex_aggregation()
        print("Aggregation pipeline complexity simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
