from ollama import Client

client = Client()

messages = [
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
]

for part in client.chat('llama2', messages=messages, stream=True):
  print(part.message.content, end='', flush=True)