# Task 4: Basic Rule-Based Chatbot

def get_reply(message):
    if message in ("hello", "hi", "hey"):
        return "Hi!"

    elif message == "how are you":
        return "I'm fine, thanks!"

    elif message == "what is your name":
        return "I'm a Python chatbot."

    elif message in ("thanks", "thank you"):
        return "You're welcome!"

    elif message in ("bye", "exit", "quit"):
        return "Goodbye!"

    else:
        return "Sorry, I don't understand. Try saying hello or how are you."


def main():
    print("Chatbot: Hello! Type a message. Type 'bye' to stop.")

    while True:
        # Ignore capital letters, extra spaces and ending punctuation.
        message = input("You: ").strip().lower()
        message = message.rstrip("!?.,")
        message = " ".join(message.split())

        if not message:
            print("Chatbot: Please type a message.")
            continue

        print("Chatbot:", get_reply(message))

        if message in ("bye", "exit", "quit"):
            break


if __name__ == "__main__":
    main()