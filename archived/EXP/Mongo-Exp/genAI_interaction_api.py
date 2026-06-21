import openai
import topsecret

def askChaos(ask):
    
    openai.api_key = topsecret.fetch()["openai.apikey"]
    openai.organization = topsecret.fetch()["openai.orgid"]

    def ask_chat(question):
        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message['content']

    output = ask_chat(ask)
    output_file = open("result.md", "w")
    output_file.write(output)
    output_file.close()



ask_file = open("./genai_prompt.txt", "r")
prompt = ask_file.read().strip()
ask_file.close()


askChaos(prompt)
print("GenAI Output Generated")