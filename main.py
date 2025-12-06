from ollama import Client
from colorama import Fore, Back, Style

isContinue = True

while isContinue:
    question = input(Fore.RED + "What's your question? Type 'exit' to quit.\n")
    if question == "exit":
        print(Fore.BLUE + "Thank you for playing!")
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
          print(Fore.GREEN + part.message.content, end='', flush=True)
        print("\n")