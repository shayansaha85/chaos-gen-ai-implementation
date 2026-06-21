mongo_health_file = open("./LOGS/MONGO_HEALTH.log", "r")
data = mongo_health_file.read().strip()
mongo_health_file.close()

chaosTime_file = open("./LOGS/CHAOS_TIMING.txt", "r")
data_time = chaosTime_file.read().strip()
chaosTime_file.close()

sysLog_file = open("./LOGS/system_stats.log", "r")
data_sysLog = sysLog_file.read().strip()
sysLog_file.close()

genAIPrompt  = "MONGO LOGS :\n\n" + data + "\n\n\n" + "SYSTEM STATS:\n\n" + data_sysLog +  "\n\n\nCHAOS TESTING TIMEFRAME:\n\n" + data_time + "\n\n" + "I have done Connection Overload Chaos experiment over Mongo DB. After analysing the logs with Chaos Start and End time, please provide full insights about the behavior of mongodb during chaos testing, how it behaved, what are the assumptions, recommendation, root cause analysis. And pin point all the issues that occured during the chaos testing"

file = open("genai_prompt.txt", "w")
file.write(genAIPrompt)
file.close()
print("GenAI Prompt Generated")