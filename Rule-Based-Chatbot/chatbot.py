print("=================================")
print("      Rule-Based AI Chatbot")
print("=================================")
print("Type 'bye', 'exit', or 'quit' to end the conversation.")
print()

while True:
    user_input = input("You: ").lower().strip()

    # Exit commands
    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break

    # Greetings
    elif user_input in ["hi", "hello", "hey", "hii"]:
        print("Bot: Hello! How can I help you?")

    # How are you
    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking.")

    # Name
    elif "your name" in user_input:
        print("Bot: I'm a simple Rule-Based AI Chatbot.")

    # Help
    elif "help" in user_input:
        print("Bot: I can respond to greetings, basic questions, and exit commands.")

    # Thanks
    elif "thank" in user_input:
        print("Bot: You're welcome!")

    # Unknown input
    else:
        print("Bot: Sorry, I don't understand that yet.")