from utils import generate_reply
from config import LATEST_EXCHANGE_PAIRS
import memory
import os
from datetime import datetime

if not isinstance(LATEST_EXCHANGE_PAIRS, int) or LATEST_EXCHANGE_PAIRS <= 0:
    raise ValueError("LATEST_EXCHANGE_PAIRS must be a positive integer.")

def generate_session_filename():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"session_{timestamp}.json"

def list_sessions():
    if not os.path.exists("chats"):
        return []
    files = [f for f in os.listdir("chats") if f.endswith(".json")]
    return sorted(files)

def chat():
    resume_mode = False
    os.makedirs("chats", exist_ok=True)
    session_file = os.path.join("chats", generate_session_filename())
    history = memory.initialize_memory(session_file)
    print(f"Session started: {session_file}")
    while True:
        user_input = input(f"[{os.path.basename(session_file)}] You: ")
        if user_input.lower() == "/exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "/sessions":
            sessions= list_sessions()
            if not sessions:
                print("No Previous sessions found.")
                continue
            else:
                print ("\nPrevious Sessions:")
                for idx, session in enumerate(sessions, 1):
                    print(f"{idx}. {session}")
                resume_mode = True
                continue
        elif user_input.lower().startswith("/resume"):
             if not resume_mode:
                print("Please use /sessions to view available sessions before resuming.")
                continue
             parts = user_input.split()
             if len(parts) != 2 or not parts[1].isdigit():
                print("Usage: /resume <session_number>")
                continue
             sessions = list_sessions()
             index = int(parts[1]) - 1
             if index < 0 or index >= len(sessions):
                print("Invalid session number.")
                continue
             session_file = os.path.join("chats", sessions[index])
             history = memory.initialize_memory(session_file)
             print(f"Resumed session: {sessions[index]}")
             resume_mode = False
             continue
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
       
        success, size = memory.store_in_memory(history, "user", user_input, session_file)
        if not success:
            print(f"⚠️ Message rejected. Session size limit ({size:.2f} KB) exceeded.")
            continue
        response = generate_reply(history)
        
        success, size = memory.store_in_memory(history, "ai", response, session_file)
        if not success:
            print(f"⚠️ AI response rejected. Session size limit ({size:.2f} KB) exceeded.")
            continue
        print("AI:", response)

if __name__ == "__main__":
    chat()