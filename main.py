from ollama import Client

isContinue = True

while isContinue:
    question = input("What's your question? Type 'exit' to quit.\n")
    if question == "exit":
        print("Thank you for playing!")
        isContinue = False
        isContinue = False
    else:
        client = Client()

        messages = [
          {
            'role': 'user',
            'content': question,
          },
        ]

        for part in client.chat('llama2', messages=messages, stream=True):
          print(part.message.content, end='', flush=True)
        print("\n")