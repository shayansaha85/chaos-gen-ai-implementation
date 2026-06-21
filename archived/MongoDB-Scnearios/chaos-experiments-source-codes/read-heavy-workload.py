import pymongo
import threading

mongo_host = 'localhost'
mongo_port = 27017

def perform_read_operations():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        db = client.test_db
        collection = db.test_collection

        for _ in range(1000):
            query = {} 
            result = collection.find(query) 


        client.close()
    except Exception as e:
        print(f"Read operation failed: {e}")

def simulate_read_heavy_workload():
    threads = []
    for _ in range(10):
        t = threading.Thread(target=perform_read_operations)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("Simulating read-heavy workload on MongoDB...")
    try:
        simulate_read_heavy_workload()
        print("Read-heavy workload simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
