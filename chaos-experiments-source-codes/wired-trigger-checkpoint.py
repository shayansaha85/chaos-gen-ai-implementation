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



def perform_checkpoint_interruption():
    try:
        client = pymongo.MongoClient(mongo_uri)
        db = client[mongo_db_name] 
        db.command("fsync", lock=True)

        time.sleep(5)

        db.command("fsyncUnlock")
        print("WiredTiger checkpoint interrupted.")

        client.close()
    except Exception as e:
        print(f"Checkpoint interruption failed: {e}")

if __name__ == "__main__":
    print("Simulating WiredTiger checkpoint interruption on MongoDB...")
    try:
        perform_checkpoint_interruption()
        print("WiredTiger checkpoint interruption simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
