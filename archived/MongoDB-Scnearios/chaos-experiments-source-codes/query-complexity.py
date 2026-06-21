import pymongo
import threading

mongo_host = 'localhost'
mongo_port = 27017

def perform_complex_queries():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        db = client.test_db
        collection = db.test_collection

        result = collection.aggregate([
            {"$group": {"_id": "$category", "total": {"$sum": "$amount"}}},
            {"$match": {"total": {"$gt": 1000}}}
        ])

        for doc in result:
            print(doc)

        client.close()
    except Exception as e:
        print(f"Query complexity failed: {e}")

def simulate_query_complexity():
    threads = []
    for _ in range(10):
        t = threading.Thread(target=perform_complex_queries)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("Simulating query complexity on MongoDB...")
    try:
        simulate_query_complexity()
        print("Query complexity simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
