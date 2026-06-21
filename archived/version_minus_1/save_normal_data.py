import collector


normal = collector.collector("http://127.0.0.1:5000/fetch")
file = open("normal_condition.json", "w")
file.write(str(normal).replace("'", '"'))
file.close()