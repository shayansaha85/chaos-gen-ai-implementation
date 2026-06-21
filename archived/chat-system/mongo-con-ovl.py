import threading
import pymongo
import time
import sys

# MongoDB connection parameters
mongo_host = 'localhost'
mongo_port = 27017

# Function to perform read/write operations and log metrics
def perform_operations():
    client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
    db = client.test_db  # Replace 'test_db' with your database name
    collection = db.TEST  # Replace 'TEST' with your collection name

    # Adjust the number of iterations to increase read/write operations
    for _ in range(50):  # Change this number for desired read/write operations
        try:
            # Read operation
            start_time = time.time()
            result = collection.find_one()
            end_time = time.time()
            output = f"Read operation successful: {result}\nResponse Time (Read): {end_time - start_time} seconds\n"
            sys.stdout.write(output)

            # Write operation
            data = {'key': 'value'}  # Replace with your data for write operation
            start_time = time.time()
            collection.insert_one(data)
            end_time = time.time()
            output = f"Write operation successful\nResponse Time (Write): {end_time - start_time} seconds\n"
            sys.stdout.write(output)
        except Exception as e:
            error = f"Operation failed: {e}\n"
            sys.stderr.write(error)
    client.close()

# Simulate multiple operations using threads
def simulate_operations():
    threads = []
    for _ in range(10):  # Adjust the number of threads for parallel operations
        t = threading.Thread(target=perform_operations)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

# Function to simulate connection overload scenario
def simulate_connection_overload():
    client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
    # Adjust the number of iterations to increase connection attempts
    for _ in range(100):  # Change this number for desired connection attempts
        try:
            db = client.test_db  # Replace 'test_db' with your database name
            collection = db.TEST  # Replace 'TEST' with your collection name
            result = collection.find_one()
            output = f"Connection successful: {result}\n"
            sys.stdout.write(output)
        except Exception as e:
            error = f"Connection failed: {e}\n"
            sys.stderr.write(error)
    client.close()

# Function to get MongoDB throughput and save it to a file
def get_throughput():
    client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
    db = client.admin
    result = db.command('profile', -1)  # Get current profiling level
    profiling_output = f"Current profiling level: {result['was']}\n"
    sys.stdout.write(profiling_output)

    # Enable profiling for all operations (you might need to adjust the profiling level)
    db.set_profiling_level(pymongo.ProfilingLevel.ALL)

    # Wait for a while to collect profiling data
    time.sleep(5)  # Adjust the duration to collect profiling data

    # Disable profiling after data collection
    db.set_profiling_level(pymongo.ProfilingLevel.OFF)

    # Get profiling data
    profiling_data = list(db.system.profile.find())
    throughput = len(profiling_data)
    throughput_output = f"Throughput: {throughput} operations recorded in profiling data\n"

    # Save profiling data to a file
    with open('mongodb_throughput.txt', 'a') as file:
        file.write(throughput_output)
        for data in profiling_data:
            file.write(f"{data}\n")
    sys.stdout.write(throughput_output)

if __name__ == "__main__":
    print("Starting MongoDB connection overload and profiling experiment...")
    print("Press Ctrl+C to stop the experiment.")

    # Redirect stdout and stderr to a log file
    sys.stdout = open('mongodb_experiment_log.txt', 'w')
    sys.stderr = open('mongodb_experiment_error.txt', 'w')

    try:
        while True:
            t1 = threading.Thread(target=simulate_operations)
            t2 = threading.Thread(target=get_throughput)
            t3 = threading.Thread(target=simulate_connection_overload)
            t1.start()
            t2.start()
            t3.start()
            t1.join()
            t2.join()
            t3.join()
            time.sleep(5)  # Adjust the interval between experiments
    except KeyboardInterrupt:
        print("Experiment stopped.")
