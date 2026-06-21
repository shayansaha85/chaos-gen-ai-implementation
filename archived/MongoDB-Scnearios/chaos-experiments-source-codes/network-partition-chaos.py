import pymongo
import threading
import time
import subprocess

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

def simulate_network_partition():
    subprocess.run(["sudo", "iptables", "-A", "INPUT", "-p", "tcp", "--dport", "27017", "-j", "DROP"])

    threads = []
    for _ in range(1000):
        t = threading.Thread(target=perform_operations)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    subprocess.run(["sudo", "iptables", "-D", "INPUT", "-p", "tcp", "--dport", "27017", "-j", "DROP"])

if __name__ == "__main__":
    print("Simulating network partition on MongoDB...")
    try:
        simulate_network_partition()
    except KeyboardInterrupt:
        print("Experiment stopped.")
