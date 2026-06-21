import pymongo
import threading

mongo_host = 'localhost'
mongo_port = 27017

def perform_mixed_operations():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        db = client.test_db
        collection = db.test_collection

        for _ in range(500):
            query = {} 
            result = collection.find(query)

        for _ in range(500):
            data = {"key": "value"}
            collection.insert_one(data)

        client.close()
    except Exception as e:
        print(f"Mixed operation failed: {e}")

def simulate_mixed_workload():
    threads = []
    for _ in range(10):
        t = threading.Thread(target=perform_mixed_operations)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("Simulating mixed workload (read and write) on MongoDB...")
    try:
        simulate_mixed_workload()
        print("Mixed workload simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
