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



def fill_disk_space():
    try:
        client = pymongo.MongoClient(mongo_uri)
        db = client[mongo_db_name]
        collection = db[mongo_coll_name]

        while True:
            data = {"key": "value"}
            collection.insert_one(data)
    except Exception as e:
        print(f"Disk space filled: {e}")

if __name__ == "__main__":
    print("Simulating disk full scenario on MongoDB...")
    try:
        fill_disk_space()
    except KeyboardInterrupt:
        print("Experiment stopped.")
