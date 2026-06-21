import pymongo
import threading
import time

mongo_host = 'localhost'
mongo_port = 27017

def perform_operations(duration):
    start_time = time.time()
    try:
        while time.time() - start_time < duration:
            client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
            db = client.admin
            collection = db.TEST

            # Perform some operations (for example, fetching server status)
            server_status = db.command("serverStatus")
            print(f"Server Status: {server_status}")

            time.sleep(1)  # Simulate some processing time
            
            client.close()  # Close the connection to release resources

    except Exception as e:
        print(f"Operation failed: {e}")

def simulate_connection_overload(duration):
    threads = []
    for _ in range(1000):  # Creating 10 threads for concurrent connections (adjust as needed)
        t = threading.Thread(target=perform_operations, args=(duration,))
        threads.append(t)
        t.start()

    time.sleep(duration)  # Run the operations for the specified duration

    # Stop threads after the specified duration
    for thread in threads:
        thread.join()

# if __name__ == "__main__":
#     print("Simulating connection overload to MongoDB for 120 seconds...")
#     simulate_connection_overload(120)  # Simulating for 120 seconds
