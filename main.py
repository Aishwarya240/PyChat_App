from ollama import Client
from colorama import Fore, Style
from ddgs import DDGS
import time

from logo import main as logo

print(Fore.CYAN + "AI Chat with DuckDuckGo Search + LLM Summaries Enabled!\n" + Style.RESET_ALL)
print(logo())
client = Client()
time.sleep(1)

def duckduckgo_search(query):
    print(Fore.YELLOW + "\n[Searching DuckDuckGo...]\n" + Style.RESET_ALL)

    # 🌤 Weather Search
    if "temperature" in query.lower() or "weather" in query.lower():
        with DDGS() as ddgs:
            try:
                result = ddgs.weather(query)
                temp = result.get("current", {}).get("temperature")
                cond = result.get("current", {}).get("sky")
                location = result.get("region")
                if temp:
                    return f"Location: {location}\nTemperature: {temp}°C\nCondition: {cond}"
                else:
                    return "Weather info not found."
            except:
                return "Weather info could not be retrieved."

    # 🔎 Normal Text Search
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append(
                f"Title: {r.get('title')}\n"
                f"Link: {r.get('href')}\n"
                f"Snippet: {r.get('body')}\n\n"
            )

    return "\n".join(results) if results else "No results found."

def summarize_with_llm(text):
    prompt = f"""
    Summarize the following search results in a simple, clear, and helpful way:

    {text}

    Provide a short, human-friendly summary.
    """

    messages = [{'role': 'user', 'content': prompt}]
    summary = ""

    for part in client.chat('llama2', messages=messages, stream=True):
        summary += part.message.content

    return summary


while True:
    question = input(Fore.RED + "Ask your question (or type 'exit'): " + Style.RESET_ALL)

    if question.lower() == "exit":
        print(Fore.GREEN + "Goodbye! Thanks for chatting!" + Style.RESET_ALL)
        break

    # 🔍 Search Mode
    if question.lower().startswith("search:"):
        query = question.split("search:", 1)[1].strip()

        raw_results = duckduckgo_search(query)
        print(Fore.MAGENTA + "\n[Raw Search Results Fetched]\n" + Style.RESET_ALL)
        print(Fore.WHITE + raw_results + Style.RESET_ALL)

        # ✨ Now summarize with LLM
        print(Fore.CYAN + "\n[Summarizing with LLM...]\n" + Style.RESET_ALL)
        summary = summarize_with_llm(raw_results)

        print(Fore.GREEN + summary + Style.RESET_ALL)
        print()
        continue

    # 💬 Normal Chat Mode
    messages = [{'role': 'user', 'content': question}]
    print(Fore.BLUE)
    for part in client.chat('llama2', messages=messages, stream=True):
        print(part.message.content, end='', flush=True)
    print(Style.RESET_ALL + "\n")
