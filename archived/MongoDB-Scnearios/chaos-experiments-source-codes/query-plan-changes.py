import pymongo

mongo_host = 'localhost'
mongo_port = 27017

def perform_query_plan_changes():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        db = client.test_db
        collection = db.test_collection

        result_1 = collection.find({"category": "Electronics"})
        for doc in result_1:
            print(doc)

        result_2 = collection.find({"amount": {"$gt": 1000}})

        for doc in result_2:
            print(doc)

        client.close()
    except Exception as e:
        print(f"Query plan changes failed: {e}")

if __name__ == "__main__":
    print("Simulating query plan changes on MongoDB...")
    try:
        perform_query_plan_changes()
        print("Query plan changes simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
