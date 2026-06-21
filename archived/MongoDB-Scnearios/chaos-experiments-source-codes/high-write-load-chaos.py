import pymongo
import threading

mongo_host = 'localhost'
mongo_port = 27017

def perform_write_operations():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        db = client.test_db
        collection = db.test_collection

        for _ in range(1000):
            data = {"key": "value"}
            collection.insert_one(data)

        client.close()
    except Exception as e:
        print(f"Write operation failed: {e}")

def simulate_high_write_load():
    threads = []
    for _ in range(10):
        t = threading.Thread(target=perform_write_operations)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("Simulating high write load on MongoDB...")
    try:
        simulate_high_write_load()
        print("High write load simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
