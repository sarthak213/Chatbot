from utils import generate_reply
from config import MAX_HISTORY, LATEST_EXCHANGE_PAIRS
import memory
import os
from datetime import datetime

if not isinstance(LATEST_EXCHANGE_PAIRS, int) or LATEST_EXCHANGE_PAIRS <= 0:
    raise ValueError("LATEST_EXCHANGE_PAIRS must be a positive integer.")

def generate_session_filename():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"session_{timestamp}.json"

def chat():
    os.makedirs("chats", exist_ok=True)
    session_file = os.path.join("chats", generate_session_filename())
    history = memory.initialize_memory(session_file)
    print(f"Session started: {session_file}")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "/exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "/history":
            print(memory.format_history(history))
            continue
        elif user_input.lower() == "/latest":
            print(memory.retrieve_latest_memory(history))
            continue
        elif user_input.lower() == "/clear":
            memory.clear_history(history, session_file)
            print("Chat history cleared.")
            continue
        memory.store_in_memory(history, "user", user_input, session_file)
        response = generate_reply(history)
        memory.store_in_memory(history, "ai", response, session_file)
        print("AI:", response)

if __name__ == "__main__":
    chat()