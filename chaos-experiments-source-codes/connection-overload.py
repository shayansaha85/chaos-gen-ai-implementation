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



def perform_operations():
    try:
        client = pymongo.MongoClient(mongo_uri)
        db = client[mongo_db_name]
        collection = db[mongo_coll_name]


        server_status = db.command("serverStatus")
        collection_stats = db.command("collStats", mongo_coll_name)

        print(f"Server Status: {server_status}")
        print(f"Collection Stats: {collection_stats}")

        while True:
            time.sleep(1)

    except Exception as e:
        print(f"Operation failed: {e}")

def simulate_connection_overload():
    threads = []
    for _ in range(1000):
        t = threading.Thread(target=perform_operations)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("Simulating connection overload to MongoDB...")
    try:
        simulate_connection_overload()
    except KeyboardInterrupt:
        print("Experiment stopped.")
