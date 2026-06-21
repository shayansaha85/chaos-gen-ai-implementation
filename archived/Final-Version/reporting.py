import genAI_interaction_api
import question_sets
import sendEmail

question_sets.generate_ask()

question_file = open("genai_questions.txt", "r")
prompt = question_file.read()
question_file.close()

genAI_interaction_api.askChaos(prompt)
sendEmail.drop_email()