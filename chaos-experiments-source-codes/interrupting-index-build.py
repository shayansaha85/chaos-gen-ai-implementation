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



def perform_index_build():
    try:
        client = pymongo.MongoClient(mongo_uri)
        db = client[mongo_db_name]
        collection = db[mongo_coll_name]

        collection.create_index([('index_field', pymongo.ASCENDING)], background=True)

        time.sleep(60)

        collection.drop_index('index_field_1')

        client.close()
    except Exception as e:
        print(f"Index build interrupted: {e}")

if __name__ == "__main__":
    print("Simulating interrupted index build on MongoDB...")
    try:
        thread = threading.Thread(target=perform_index_build)
        thread.start()

        time.sleep(10)
        thread.join()
        print("Index build interrupted.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
