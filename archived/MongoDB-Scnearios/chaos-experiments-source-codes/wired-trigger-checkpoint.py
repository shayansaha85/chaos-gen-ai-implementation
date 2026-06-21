import pymongo
import threading
import time

mongo_host = 'localhost'
mongo_port = 27017

def perform_checkpoint_interruption():
    try:
        client = pymongo.MongoClient(host=mongo_host, port=mongo_port)
        db = client.admin 
        db.command("fsync", lock=True)

        time.sleep(5)

        db.command("fsyncUnlock")
        print("WiredTiger checkpoint interrupted.")

        client.close()
    except Exception as e:
        print(f"Checkpoint interruption failed: {e}")

if __name__ == "__main__":
    print("Simulating WiredTiger checkpoint interruption on MongoDB...")
    try:
        perform_checkpoint_interruption()
        print("WiredTiger checkpoint interruption simulation completed.")
    except KeyboardInterrupt:
        print("Experiment stopped.")
