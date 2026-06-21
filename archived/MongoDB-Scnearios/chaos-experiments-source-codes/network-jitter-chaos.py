import pymongo
import threading
import time
import subprocess
import random

mongo_host = 'localhost'
mongo_port = 27017

def perform_operations():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        db = client.admin
        collection = db.TEST


        client.close()
    except Exception as e:
        print(f"Operation failed: {e}")

def simulate_network_jitter():
    delay_variation = random.randint(100, 300)  # Random delay between 100ms to 300ms
    subprocess.run(["sudo", "tc", "qdisc", "add", "dev", "eth0", "root", "netem", "delay", f"{delay_variation}ms"])

    threads = []
    for _ in range(1000):
        t = threading.Thread(target=perform_operations)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    subprocess.run(["sudo", "tc", "qdisc", "del", "dev", "eth0", "root", "netem", "delay", f"{delay_variation}ms"])

if __name__ == "__main__":
    print("Simulating network jitter on MongoDB...")
    try:
        simulate_network_jitter()
    except KeyboardInterrupt:
        print("Experiment stopped.")
