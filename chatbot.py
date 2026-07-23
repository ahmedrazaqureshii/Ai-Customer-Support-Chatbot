# Simple AI Chatbot
# Author: Ahmed Raza Qureshi
# Status: Development Phase

import datetime


def get_time():
    current_time = datetime.datetime.now()
    return current_time.strftime("%H:%M:%S")


def chatbot_response(message):

    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you today?"

    elif "time" in message:
        return f"Current time is {get_time()}"

    elif "name" in message:
        return "I am Ahmed's AI Assistant 🤖"

    # TODO:
    # Add AI API integration here
    # Add memory system
    # Add database support
    # Add natural language processing


    else:
        return "I am still learning. More features coming soon!"


def start_chat():

    print("================================")
    print(" AI Chatbot Started 🤖")
    print(" Type 'exit' to stop")
    print("================================")


    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break


        response = chatbot_response(user_input)

        print("Bot:", response)



# Starting chatbot

if __name__ == "__main__":
    start_chat()
