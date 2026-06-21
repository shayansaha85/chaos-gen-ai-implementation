import pymongo
import threading
import time
import subprocess
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

def simulate_network_jitter():
    delay_variation = random.randint(100, 300)  # Random delay between 100ms to 300ms
    if platform.system() == 'Linux':
        subprocess.run(["sudo", "tc", "qdisc", "add", "dev", "eth0", "root", "netem", "delay", f"{delay_variation}ms"])
    else:
        print("OS-level network/disk chaos using iptables/tc is unsupported on Windows. Skipping...")

    threads = []
    for _ in range(1000):
        t = threading.Thread(target=perform_operations)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    if platform.system() == 'Linux':
        subprocess.run(["sudo", "tc", "qdisc", "del", "dev", "eth0", "root", "netem", "delay", f"{delay_variation}ms"])
    else:
        print("OS-level network/disk chaos using iptables/tc is unsupported on Windows. Skipping...")

if __name__ == "__main__":
    print("Simulating network jitter on MongoDB...")
    try:
        simulate_network_jitter()
    except KeyboardInterrupt:
        print("Experiment stopped.")
