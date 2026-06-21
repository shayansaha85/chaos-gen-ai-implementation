import pymongo
import threading
import time

mongo_host = 'localhost'
mongo_port = 27017

def perform_operations():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        db = client.admin
        collection = db.TEST


        server_status = db.command("serverStatus")
        collection_stats = db.command("collStats", "TEST")

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
