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



def perform_io_operations():
    try:
        client = pymongo.MongoClient(mongo_uri)
        db = client[mongo_db_name]
        collection = db[mongo_coll_name]

        for _ in range(10000):
            data = {"key": "value"} 
            collection.insert_one(data) 

            # For read operation:
            # query = {}  # Define your query criteria
            # result = collection.find(query)  # Execute the find operation
            # Process or iterate through the result if needed

        client.close()
    except Exception as e:
        print(f"I/O spike occurred: {e}")

def simulate_disk_io_spike():
    threads = []
    for _ in range(10):
        t = threading.Thread(target=perform_io_operations)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("Simulating disk I/O spike on MongoDB...")
    try:
        simulate_disk_io_spike()
        print("Disk I/O spike simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
