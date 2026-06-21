import pymongo
import threading
import time

mongo_host = 'localhost'
mongo_port = 27017

def perform_long_running_query():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        db = client.test_db
        collection = db.test_collection

        result = collection.find({"category": "Electronics"})
        for doc in result:
            print(doc)
            time.sleep(1)

        client.close()
    except Exception as e:
        print(f"Query interrupted: {e}")

def simulate_interrupted_queries():
    thread = threading.Thread(target=perform_long_running_query)
    thread.start()

    time.sleep(5)
    thread.join()

if __name__ == "__main__":
    print("Simulating interrupted queries on MongoDB...")
    try:
        simulate_interrupted_queries()
        print("Interrupted queries simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
