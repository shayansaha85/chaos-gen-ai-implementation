import requests
import random
import concurrent.futures
import json

def inject_latency(api_url, exceptions):
    
    try:
        for _ in range(50):
            delay = random.uniform(0.1, 0.5)
            response = requests.get(api_url, timeout=delay)
            print(response.text)
            
    except Exception as e:
        exceptions.append({'chaos_type': 'latency', 'exception': str(e)})

def inject_faulty_response(api_url, exceptions):

    try:
        for _ in range(50):
            response = requests.get(api_url)
            if random.random() < 0.7:
                response.status_code = 500
                response.raise_for_status()
                print(response.text)
            
    except Exception as e:
        exceptions.append({'chaos_type': 'faulty_response', 'exception': str(e)})


def inject_traffic_spike(api_url, exceptions):
    try:
        for _ in range(50):
            with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
                futures = [executor.submit(requests.get, api_url) for _ in range(5)]
                for future in concurrent.futures.as_completed(futures):
                    response = future.result()
                    print(response.text)
            
    except Exception as e:
        exceptions.append({'chaos_type': 'traffic_spike', 'exception': str(e)})

def execute_chaos_experiments(api_url):
    exceptions = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        future_lat = executor.submit(inject_latency, api_url, exceptions)
        future_faulty = executor.submit(inject_faulty_response, api_url, exceptions)
        future_spike = executor.submit(inject_traffic_spike, api_url, exceptions)

        concurrent.futures.wait([future_lat, future_faulty, future_spike])

    save_exceptions_to_file(exceptions)

def save_exceptions_to_file(exceptions):
    with open('exceptions.json', 'w') as file:
        json.dump(exceptions, file, indent=4)

api_endpoint = 'http://127.0.0.1:5000/fetch'
execute_chaos_experiments(api_endpoint)
