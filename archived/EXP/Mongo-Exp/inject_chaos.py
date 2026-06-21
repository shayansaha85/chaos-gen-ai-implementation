import time
import connection_overload_2
import datetime
import sys

start_time = datetime.datetime.now()
content = "\n"
content = content + "CHAOS START TIME : " + str(start_time) + "\n"
connection_overload_2.simulate_connection_overload(int(sys.argv[1].split("=")[-1]))
end_time = datetime.datetime.now()
content = content + "CHAOS END TIME : " + str(end_time) + "\n"

file = open("./LOGS/CHAOS_TIMING.txt", "w")
file.write(content)
file.close()
print("Chaos Injection Completed")