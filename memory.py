def initialize_memory():
    # Initialize memory or data structures here
    return []

def store_in_memory(history: list, role: str, content: str):
    # Store data in memory
    history.append({"role": role, "content": content})

def retrieve_latest_memory(history: list, max_length: int):
    # Retrieve the latest memory or data
    return "Latest memory content: " + history[-max_length:]

    