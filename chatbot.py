print("Simple Chatbot")
print("Type 'bye' to exit")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi there!")

    elif user == "how are you":
        print("Bot: I'm doing great!")

    elif user == "what is your name":
        print("Bot: I am a simple Python chatbot.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I didn't understand that.") 