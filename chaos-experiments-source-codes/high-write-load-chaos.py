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



def perform_write_operations():
    try:
        client = pymongo.MongoClient(mongo_uri)
        db = client[mongo_db_name]
        collection = db[mongo_coll_name]

        for _ in range(1000):
            data = {"key": "value"}
            collection.insert_one(data)

        client.close()
    except Exception as e:
        print(f"Write operation failed: {e}")

def simulate_high_write_load():
    threads = []
    for _ in range(10):
        t = threading.Thread(target=perform_write_operations)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("Simulating high write load on MongoDB...")
    try:
        simulate_high_write_load()
        print("High write load simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
