import chaos_experiments
import collector
import data_for_genAI_generator
import genAI_interaction_api
import sendEmail
import concurrent.futures
import json


normal_data_file = open("normal_condition.json", "r")
normal = json.loads(normal_data_file.read())
normal_data_file.close()

under_chaos_data_file = open("under_chaos_condition.json", "r")
under_chaos = json.loads(under_chaos_data_file.read())
under_chaos_data_file.close()

food_for_genai = data_for_genAI_generator.genAI_data_generator(normal, under_chaos)
genAI_interaction_api.askChaos(food_for_genai)
sendEmail.drop_email()