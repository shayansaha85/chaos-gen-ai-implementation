import psutil
import datetime
import time
import json

log_file_path = './LOGS/system_stats.log'

def log_metrics(metrics):
    with open(log_file_path, 'a') as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_data = {"Timestamp": timestamp, "System_Logs": metrics}
        log_file.write(json.dumps(log_data) + "\n")


def collect_all_metrics():
    try:
        cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
        cpu_p = sum(cpu_percent)
        log_metrics({"CPU_Percentage": cpu_p})

        memory_percent = psutil.virtual_memory().percent
        log_metrics({"Memory_Percentage": memory_percent})

        disk_usage = psutil.disk_usage('/')
        disk_output = f"Total: {disk_usage.total / (1024 * 1024 * 1024):.2f} GB, Used: {disk_usage.used / (1024 * 1024 * 1024):.2f} GB, Free: {disk_usage.free / (1024 * 1024 * 1024):.2f} GB, Percentage Used: {disk_usage.percent}%"
        log_metrics({"Disk_Usage": disk_output})

        net_io = psutil.net_io_counters(pernic=True)
        networkData = { "data" : [] }

        for interface, stats in net_io.items():
            networkData["data"].append(f"Interface: {interface}, Bytes sent: {stats.bytes_sent}, Bytes received: {stats.bytes_recv}, Packets sent: {stats.packets_sent}, Packets received: {stats.packets_recv}")

        log_metrics({"Network_Stats": networkData})

    
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    print()
    print("SysLog Collection Started... Press Ctrl + C to stop collecting data")
    print("\n")

    duration = 60
    try:
        while True:
            start_time = time.time()
            collected_data = []
            while time.time() - start_time < duration:
                collect_all_metrics()
                time.sleep(5)
            print("Metrics collection and logging complete for this iteration.")
            time.sleep(30)
    except KeyboardInterrupt:
        print("Process interrupted.")
