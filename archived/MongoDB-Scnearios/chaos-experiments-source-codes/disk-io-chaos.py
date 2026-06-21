import pymongo
import threading

mongo_host = 'localhost'
mongo_port = 27017

def perform_io_operations():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        db = client.test_db
        collection = db.test_collection

        for _ in range(10000):
            data = {"key": "value"} 
            collection.insert_one(data) 

            # For read operation:
            # query = {}  # Define your query criteria
            # result = collection.find(query)  # Execute the find operation
            # Process or iterate through the result if needed

        client.close()
    except Exception as e:
        print(f"I/O spike occurred: {e}")

def simulate_disk_io_spike():
    threads = []
    for _ in range(10):
        t = threading.Thread(target=perform_io_operations)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    print("Simulating disk I/O spike on MongoDB...")
    try:
        simulate_disk_io_spike()
        print("Disk I/O spike simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
