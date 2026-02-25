def generate_reply(message):
    return "I heard you say " + message


def chat():
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = generate_reply(user_input)
        print("AI:", response)


chat()