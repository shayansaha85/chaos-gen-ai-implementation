import time
import psutil
from pymongo import MongoClient
import json
from datetime import datetime

class Collector:
    def __init__(self, config):
        self.interval = config.get('collector', {}).get('interval_seconds', 2.0)
        self.mongo_uri = config.get('mongodb', {}).get('uri')
        self.db_name = config.get('mongodb', {}).get('database')
        self.collection_name = config.get('mongodb', {}).get('collection')
        self.running = False
        self.metrics_log = []
        self.client = MongoClient(self.mongo_uri, serverSelectionTimeoutMS=2000)

    def start(self):
        self.running = True
        while self.running:
            metrics = self._gather_metrics()
            self.metrics_log.append(metrics)
            time.sleep(self.interval)

    def stop(self):
        self.running = False

    def get_logs(self):
        return self.metrics_log

    def _gather_metrics(self):
        metrics = {
            "timestamp": datetime.now().isoformat(),
            "cpu_percent": psutil.cpu_percent(),
            "ram_percent": psutil.virtual_memory().percent,
        }
        
        try:
            db = self.client[self.db_name]
            start = time.time()
            db[self.collection_name].find_one()
            end = time.time()
            metrics["mongo_query_latency_ms"] = round((end - start) * 1000, 2)
            
            server_status = db.command("serverStatus")
            metrics["mongo_connections_current"] = server_status.get("connections", {}).get("current", 0)
            metrics["mongo_connections_available"] = server_status.get("connections", {}).get("available", 0)
        except Exception as e:
            metrics["mongo_error"] = str(e)

        return metrics
