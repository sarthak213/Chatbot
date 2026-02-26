from config import MAX_HISTORY

def initialize_memory():
    # Initialize memory or data structures here
    return []

def store_in_memory(history: list, role: str, content: str):
    # Store data in memory
    history.append({"role": role, "content": content})
    if len(history) > MAX_HISTORY:
        history[:] = history[-MAX_HISTORY:]

def retrieve_latest_memory(history: list, max_length: int):
    # Retrieve the latest memory or data
    latest_message = history[-max_length:]
    if not latest_message:
        return "No memory available."
    lines= ["Latest memory content: "]
    for message in latest_message:
        role = "User" if message["role"] == "user" else "AI"
        lines.append(f"{role}: {message['content']}")
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

def clear_history(history: list):
    # Clear the conversation history
    history.clear()

    