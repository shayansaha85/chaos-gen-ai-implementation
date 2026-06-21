import pymongo
import threading

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



def perform_complex_queries():
    try:
        client = pymongo.MongoClient(mongo_uri)
        db = client[mongo_db_name]
        collection = db[mongo_coll_name]

        result = collection.aggregate([
            {"$group": {"_id": "$category", "total": {"$sum": "$amount"}}},
            {"$match": {"total": {"$gt": 1000}}}
        ])

        for doc in result:
            print(doc)

        client.close()
    except Exception as e:
        print(f"Query complexity failed: {e}")

def simulate_query_complexity():
    threads = []
    for _ in range(10):
        t = threading.Thread(target=perform_complex_queries)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("Simulating query complexity on MongoDB...")
    try:
        simulate_query_complexity()
        print("Query complexity simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
