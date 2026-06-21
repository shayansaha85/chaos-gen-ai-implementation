import requests
import time
from pymongo import MongoClient
import statistics, json

def collect_data(filename):

    def measure_response_time(api_url):
        response_times = []
        iterations = 100
        for _ in range(iterations):
            start_time = time.time()
            response = requests.get(api_url)
            end_time = time.time()
            response_time = end_time - start_time
            response_times.append(response_time)
        return statistics.mean(response_times)

    def measure_latency(api_url):
        latencies = []
        iterations = 100
        for _ in range(iterations):
            start_time = time.time()
            response = requests.get(api_url)
            end_time = time.time()
            latency = (end_time - start_time) * 1000 
            latencies.append(latency)
        return statistics.mean(latencies)

    def measure_error_rates(api_url):
        error_count = 0
        iterations = 100
        for _ in range(iterations):
            response = requests.get(api_url)
            if response.status_code != 200:
                error_count += 1
        return (error_count / iterations)*100

    def measure_mongodb_query_performance():
        query_times = []
        iterations = 10
        client = MongoClient('mongodb://localhost:27017/')
        db = client['admin']
        collection = db['TEST']

        for _ in range(iterations):
            start_time = time.time()
            result = collection.find_one({})
            end_time = time.time()
            query_execution_time = end_time - start_time
            query_times.append(query_execution_time)
        return statistics.mean(query_times)

    def gather_metrics(api_url):
        metrics = {}

        metrics['response_time'] = measure_response_time(api_url)
        metrics['latency'] = measure_latency(api_url)
        metrics['error_rate'] = measure_error_rates(api_url)
        metrics['query_time'] = measure_mongodb_query_performance()

        return metrics

    def save_metrics_to_json(metrics_data):
        with open(filename, 'w') as json_file:
            json.dump(metrics_data, json_file, indent=4)

    api_url = 'http://127.0.0.1:5000/fetch'
    metrics_data = gather_metrics(api_url)

    save_metrics_to_json(metrics_data)

    print("Metrics Data:")
    print(metrics_data)


# collect_data("metrics_before_chaos.json")
# collect_data("metrics_during_chaos.json")
collect_data("metrics_after_chaos.json")