from utils import generate_reply
from config import MAX_HISTORY
import memory

def chat():
    history = memory.initialize_memory()
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        memory.store_in_memory(history, "user", user_input)
        response = generate_reply(user_input)

        memory.store_in_memory(history, "ai", response)

        print("AI:", response)

if __name__ == "__main__":
    chat()
    