import pymongo
import threading
import time

mongo_host = 'localhost'
mongo_port = 27017

def perform_index_build():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        db = client.test_db
        collection = db.test_collection

        collection.create_index([('index_field', pymongo.ASCENDING)], background=True)

        time.sleep(60)

        collection.drop_index('index_field_1')

        client.close()
    except Exception as e:
        print(f"Index build interrupted: {e}")

if __name__ == "__main__":
    print("Simulating interrupted index build on MongoDB...")
    try:
        thread = threading.Thread(target=perform_index_build)
        thread.start()

        time.sleep(10)
        thread.join()
        print("Index build interrupted.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
