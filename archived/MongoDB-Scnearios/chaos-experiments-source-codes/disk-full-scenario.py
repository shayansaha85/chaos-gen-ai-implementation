import pymongo

mongo_host = 'localhost'
mongo_port = 27017

def fill_disk_space():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        db = client.test_db
        collection = db.test_collection

        while True:
            data = {"key": "value"}
            collection.insert_one(data)
    except Exception as e:
        print(f"Disk space filled: {e}")

if __name__ == "__main__":
    print("Simulating disk full scenario on MongoDB...")
    try:
        fill_disk_space()
    except KeyboardInterrupt:
        print("Experiment stopped.")
