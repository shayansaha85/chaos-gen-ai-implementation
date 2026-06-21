

def genAI_data_generator(normal, under_chaos):

    genAI_data_format = {
        "normal_condition" : {
            "average_latency" : "",
            "max_latency" : "",
            "error_rate" : ""
        },
        "under_chaos" : {
            "average_latency" : "",
            "max_latency" : "",
            "error_rate" : ""
        }
    }

    genAI_data_format["normal_condition"]["average_latency"] = normal["average_latency"]
    genAI_data_format["normal_condition"]["max_latency"] = normal["max_latency"]
    genAI_data_format["normal_condition"]["error_rate"] = normal["error_rate"]

    genAI_data_format["under_chaos"]["average_latency"] =  under_chaos["average_latency"]
    genAI_data_format["under_chaos"]["max_latency"] =  under_chaos["max_latency"]
    genAI_data_format["under_chaos"]["error_rate"] =  under_chaos["error_rate"]


    return genAI_data_format


