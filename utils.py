def generate_reply(message):

    if "Python" in message:
        return "So you like Python Huh? 😎"
    elif "Java" in message:
        return "Java is a great language too!"
    elif message.islower():
        return "I heard you say " + message.upper() + " in lowercase!"
    elif message.isupper():
        return "I heard you say " + message.lower() + " in uppercase!"
    else:
        return "I heard you say " + message
