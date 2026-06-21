import pymongo
import threading

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

def simulate_index_build_during_load():
    threads = []
    for _ in range(5):
        t = threading.Thread(target=perform_operations)
        threads.append(t)
        t.start()

    client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
    db = client.test_db
    collection = db.test_collection

    collection.create_index([('index_field', pymongo.ASCENDING)])

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("Simulating index build during load on MongoDB...")
    try:
        simulate_index_build_during_load()
        print("Index build during load simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
