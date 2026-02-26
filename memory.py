import json
import os
from config import LATEST_EXCHANGE_PAIRS, MAX_FILE_SIZE_KB

def check_file_size(filepath: str) -> bool:
    if not os.path.exists(filepath):
        return False  
    file_size = os.path.getsize(filepath) / 1024  
    return file_size > MAX_FILE_SIZE_KB

def initialize_memory(session_file):
    # Initialize memory or data structures here
    if os.path.exists(session_file):
        with open(session_file, "r") as f:
            return json.load(f)
    return []

def trim_oldest_exchange(history: list):
    i = 0
    while i < len(history) - 1:
        if history[i]["role"] == "user" and history[i + 1]["role"] == "ai":
            del history[i:i + 2]
            return True
        i += 1
    return False

def store_in_memory(history: list, role: str, content: str, filepath: str):
    # Store data in memory
    history.append({"role": role, "content": content})
    with open(filepath, "w") as f:
        json.dump(history, f, indent=2)
    size_kb = os.path.getsize(filepath) / 1024
    if size_kb > MAX_FILE_SIZE_KB:
        history.pop()
        with open(filepath, "w") as f:
            json.dump(history, f, indent=2)
        return False, size_kb
    return True, size_kb

def retrieve_latest_memory(history: list):
    # Retrieve the latest memory or data
    if not history:
        return "No memory available."
    exchanges = []
    i = len(history) - 1
    while i > 0 and len(exchanges) < LATEST_EXCHANGE_PAIRS:
        current = history[i]
        previous = history[i - 1]
        if previous["role"] == "user" and current["role"] == "ai":
            exchanges.append((previous, current))
            i -= 2
        else:
            i -= 1
    if not exchanges:
        return "No complete exchanges yet."
    exchanges.reverse()  
    lines = [f"Last {len(exchanges)} exchange(s):"]

    for user_msg, ai_msg in exchanges:
        lines.append(f"User: {user_msg['content']}")
        lines.append(f"AI: {ai_msg['content']}")
        lines.append("")

    return "\n".join(lines)

def format_history(history: list) -> str:
    # Format the conversation history for display
    if not history:
        return "No conversation yet."
    lines = ["\n--- Chat History ---"]
    for message in history:
        role = "User" if message["role"] == "user" else "AI"
        lines.append(f"{role}: {message['content']}")
    lines.append("---------------------\n")
    return "\n".join(lines)

def clear_history(history: list, filepath: str):
    # Clear the conversation history
    history.clear()
    with open(filepath, "w") as f:
        json.dump([], f)