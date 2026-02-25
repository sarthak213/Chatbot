from utils import generate_reply

def chat():
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = generate_reply(user_input)
        print("AI:", response)

if __name__ == "__main__":
    chat()