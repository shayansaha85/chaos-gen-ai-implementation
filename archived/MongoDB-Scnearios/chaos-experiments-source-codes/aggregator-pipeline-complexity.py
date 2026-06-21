import pymongo

mongo_host = 'localhost'
mongo_port = 27017

def perform_complex_aggregation():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        db = client.test_db
        collection = db.test_collection

        pipeline = [
            {"$match": {"category": "Electronics"}},
            {"$group": {"_id": "$subcategory", "total": {"$sum": "$amount"}}},
            {"$sort": {"total": -1}},
            {"$limit": 5},
        ]

        result = collection.aggregate(pipeline)

        for doc in result:
            print(doc)

        client.close()
    except Exception as e:
        print(f"Aggregation pipeline complexity failed: {e}")

if __name__ == "__main__":
    print("Simulating aggregation pipeline complexity on MongoDB...")
    try:
        perform_complex_aggregation()
        print("Aggregation pipeline complexity simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
