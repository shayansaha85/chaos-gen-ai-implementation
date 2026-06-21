

def fetch():

    config_file = open("./config.properties", "r")
    data = config_file.readlines()
    config_file.close()

    output = {}

    for x in data:
        output[x.strip().split('=')[0]] = x.strip().split("=")[-1]

    return output


print(fetch())