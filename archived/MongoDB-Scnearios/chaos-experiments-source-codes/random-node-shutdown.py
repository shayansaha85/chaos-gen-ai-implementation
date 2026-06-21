import pymongo
import threading
import subprocess
import time
import random

mongo_host = 'localhost'
mongo_port = 27017

def perform_operations():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        db = client.test_db
        collection = db.test_collection

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
