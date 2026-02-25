from config import MODEL_NAME, MAX_HISTORY, DEBUG_MODE, REVERSE_MODE

def generate_reply(message: str) -> str:
    if DEBUG_MODE:
        print(f"[DEBUG] Generating reply for message: {message}")
        if "Python" in message:
            return "So you like Python Huh? 😎"
        elif "Java" in message:
            return "Java is a great language too!"
        elif message.islower():
            return "I heard you say " + message.upper() + " in lowercase!"
        elif message.isupper():
            return "I heard you say " + message.lower() + " in uppercase!"
        elif REVERSE_MODE:
            return "I heard you say " + message[::-1] + " in reverse!"

    return "I heard you say " + message
