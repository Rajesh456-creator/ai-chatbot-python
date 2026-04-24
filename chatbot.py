def chatbot():
    print("AI Chatbot 🤖: Hello! Type 'exit' to quit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Bot: Goodbye! 👋")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("Bot: Hello! How can I help you? 😊")

        elif "how are you" in user_input:
            print("Bot: I'm just code, but I'm doing great! 😄")

        elif "your name" in user_input:
            print("Bot: I'm your AI Chatbot 🤖")

        elif "ai" in user_input:
            print("Bot: AI is the future! 🚀")

        else:
            print("Bot: Sorry, I don't understand that yet.")

if __name__ == "__main__":
    chatbot()
