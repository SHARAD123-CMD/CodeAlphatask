def chatbot():

    print("===== BASIC CHATBOT =====")
    print("Type 'bye' to exit.\n")

    while True:

        user = input("You: ").lower()

        if user == "hi" or user == "hello":
            print("Bot: Hi! How are you?")

        elif user == "how are you":
            print("Bot: I am fine, thanks for asking!")

        elif user == "your name":
            print("Bot: I am a Python Chatbot.")

        elif user == "goodbye":
            print("Bot: Goodbye! Have a nice day.")
            break

        elif user == "bye":
            print("Bot: Chat ended.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Run chatbot
chatbot()