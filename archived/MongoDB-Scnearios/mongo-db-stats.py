import pymongo
import datetime

# MongoDB connection parameters
mongo_host = 'localhost'
mongo_port = 27017

def log_metrics(metrics):
    with open('mongodb_all_metrics_log.txt', 'a') as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"Timestamp: {timestamp}\n")
        for key, value in metrics.items():
            log_file.write(f"{key}: {value}\n")
        log_file.write("\n")

def collect_all_metrics():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)

        connections = client.admin.command("serverStatus")['connections']
        log_metrics({"Connections": connections})

        network = client.admin.command("serverStatus")['network']
        log_metrics({"Network Traffic": network})

        memory = client.admin.command("serverStatus")['mem']
        log_metrics({"Memory Usage": memory})

        locks = client.admin.command("serverStatus")['locks']
        log_metrics({"Locks": locks})

        opcounters = client.admin.command("serverStatus")['opcounters']
        log_metrics({"Opcounters": opcounters})

        db = client.TEST
        collection_stats = db.command("collStats", "test_collection")
        log_metrics({"Collection Statistics": collection_stats})

        index_usage = db.test_collection.index_information()
        log_metrics({"Index Usage": index_usage})

        client.close()
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    print("Collecting all MongoDB metrics and logging...")
    try:
        collect_all_metrics()
        print("Metrics collection and logging complete.")
    except KeyboardInterrupt:
        print("Process interrupted.")
