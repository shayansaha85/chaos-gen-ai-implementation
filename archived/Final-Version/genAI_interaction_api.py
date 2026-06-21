import openai


def askChaos(ask):
    
    openai.api_key = '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'

    def ask_chat(question):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
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

