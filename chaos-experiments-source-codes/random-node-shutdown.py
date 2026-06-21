import pymongo
import threading
import subprocess
import time
import random

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

        client.close()
    except Exception as e:
        print(f"Operation failed: {e}")

def simulate_random_node_shutdown():
    node_to_shutdown = f"{mongo_host}:{mongo_port}"

    threads = []
    for _ in range(10):
        t = threading.Thread(target=perform_operations)
        threads.append(t)
        t.start()

    time.sleep(random.randint(5, 10))

    subprocess.run(["mongo", "--host", node_to_shutdown, "--eval", "db.adminCommand({shutdown: 1})"])

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("Simulating random node shutdown on MongoDB...")
    try:
        simulate_random_node_shutdown()
        print("Random node shutdown simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
