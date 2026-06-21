from datetime import datetime
from pymongo import MongoClient

# Define the start and end time for the log retrieval
start_time = datetime(2023, 12, 1, 1, 29, 59)
end_time = datetime(2023, 12, 1, 1, 33, 51)

# Connect to MongoDB
client = MongoClient('localhost', 27017)
db = client.admin  # Replace 'admin' with your database name
collection = db.TEST  # Replace 'log' with your collection name

# Query MongoDB for logs within the specified time range
logs_within_time_range = collection.find({
    'timestamp': {
        '$gte': start_time,
        '$lt': end_time
    }
})

# Iterate and print the logs
for log in logs_within_time_range:
    print(log)
