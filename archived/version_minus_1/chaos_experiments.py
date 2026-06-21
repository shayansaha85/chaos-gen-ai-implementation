import requests, random
import time
import concurrent.futures
import threading

def inject_latency(api_url):
    print("*** LATENCY INJECTION STARTED ***")
    def make_api_request_with_delay():
        delay = random.uniform(0.1, 0.5)
        time.sleep(delay)
        response = requests.get(api_url)
        return response

    for _ in range(3000):
        api_response = make_api_request_with_delay()
        print(api_response.text)


def inject_traffic_spike(api_url):
    print("*** TRAFFIC SPIKE STARTED ***")
    def make_concurrent_requests():
        response = requests.get(api_url)
        print(response.text)

    threads = []
    for _ in range(3000):
        thread = threading.Thread(target=make_concurrent_requests)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def inject_faulty_response(api_url):
    print("*** FAULT RESPONSE INJECTION STARTED ***")
    def make_api_request_with_faulty_responses():
        response = requests.get(api_url)
        
        if random.random() < 0.6:
            response.status_code = 500
        
        return response

    for _ in range(3000): 
        api_response = make_api_request_with_faulty_responses()
        print(api_response.status_code)

def execute_all_together(api_url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        chaos1 = executor.submit(inject_latency, api_url)
        chaos2 = executor.submit(inject_faulty_response, api_url)
        chaos3 = executor.submit(inject_traffic_spike, api_url)
        concurrent.futures.wait([chaos1, chaos2, chaos3])

