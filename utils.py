from config import DEBUG_MODE, REVERSE_MODE

def generate_reply(history: list) -> str:
    last_message = None
    for message in reversed(history):
        if message["role"]=="user":
            last_message = message["content"]
            break
        if not last_message:
            return "Hello!"
        
    if DEBUG_MODE:
        print(f"[DEBUG] Generating reply for message: {last_message}")
        if "Python" in last_message:
            return "So you like Python Huh? 😎"
        elif "Java" in last_message:
            return "Java is a great language too!"
        elif last_message.islower():
            return "I heard you say " + last_message.upper() + " in lowercase!"
        elif last_message.isupper():
            return "I heard you say " + last_message.lower() + " in uppercase!"
        elif REVERSE_MODE:
            return "I heard you say " + last_message[::-1] + " in reverse!"

    return "I heard you say " + last_message
