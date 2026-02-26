from utils import generate_reply
from config import MAX_HISTORY
import memory

def chat():
    history = memory.initialize_memory()
    while True:
        user_input = input("You: ")

        if user_input.lower() == "/exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "/history":
            print(memory.format_history(history))
            continue
        elif user_input.lower() == "/latest":
            print(memory.retrieve_latest_memory(history, MAX_HISTORY))
            continue
        elif user_input.lower() == "/clear":
            memory.clear_history(history)
            print("Chat history cleared.")
            continue

        memory.store_in_memory(history, "user", user_input)
        response = generate_reply(history)

        memory.store_in_memory(history, "ai", response)
        print("AI:", response)

if __name__ == "__main__":
    chat()
    