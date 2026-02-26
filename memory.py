import json
import os
from config import LATEST_EXCHANGE_PAIRS

def initialize_memory(session_file):
    # Initialize memory or data structures here
    if os.path.exists(session_file):
        with open(session_file, "r") as f:
            return json.load(f)
    return []

def store_in_memory(history: list, role: str, content: str, filepath: str):
    # Store data in memory
    history.append({"role": role, "content": content})
    with open(filepath, "w") as f:
        json.dump(history, f, indent=2)


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