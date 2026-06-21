import openai

api_key = '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'
openai.api_key = api_key

file = open("API-module/app.log", "r")
content = file.read()
file.close()

documents = [
    content.strip()
]

print("Welcome to the Console-based Chat System!")
print("Type 'exit' to quit the chat.")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Combine user's input with provided documents
    context = ". ".join(documents) + ". " + user_input

    # Generate response from GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=context,
        max_tokens=50 
    )

    print(f"AI: {response['choices'][0]['text'].strip()}")
