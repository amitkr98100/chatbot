from chatbot.logic import generate_response
from chatbot.data_loader import load_data

# first time data load
load_data()

print("🤖 Chatbot Started (type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = generate_response(user_input)
    print("Bot:", response)