import concurrent.futures
import time


def function_1():
    print(time.time())

def function_2():
    print(time.time())

def function_3():
    print(time.time())

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:

    future_1 = executor.submit(function_1)
    future_2 = executor.submit(function_2)
    future_3 = executor.submit(function_3)

    result_function_1 = future_1.result()
    result_function_2 = future_2.result()
    result_function_3 = future_3.result()

print("Result from function 1:", result_function_1)
print("Result from function 2:", result_function_2)
print("Result from function 3:", result_function_3)
