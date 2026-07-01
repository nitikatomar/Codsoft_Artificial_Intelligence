import random
import time


def chatbot_response(user_input):
    # Input ko lowercase kar rahe hain taaki matching aasan ho
    user_input = user_input.lower().strip()

    # 1. Greetings (Alag-alag tareeqe se reply dene ke liye lists)
    greetings = ["hi", "hello", "hey", "namaste", "wassup"]
    greeting_replies = [
        "Hey! How's it going?",
        "Hello! How can I help you today?",
        "Hi there! What's up?"
    ]

    # 2. Well-being replies
    how_are_you_replies = [
        "I'm doing great, thanks for asking! How about you?",
        "All good here! Just waiting to chat. How's your day going?",
        "Doing awesome! Hope you are having a good day too."
    ]

    # 3. Fallback replies (Jab bot ko samajh na aaye)
    fallback_replies = [
        "Hmm, I didn't quite catch that. Could you say it differently?",
        "I'm still learning, so I didn't understand that. Try asking something else!",
        "Sorry, my rules don't cover that yet! Try saying 'hi' or 'help'."
    ]

    # --- Logic Checking ---

    # Check for Greetings
    if any(word in user_input for word in greetings):
        return random.choice(greeting_replies)

    # Check for Well-being
    elif "how are you" in user_input or "kaise ho" in user_input:
        return random.choice(how_are_you_replies)

    # Check for Identity
    elif "name" in user_input or "who are you" in user_input:
        return "I'm Buddy, a chatbot built for my CodSoft Internship Task 1!"

    # Check for Help
    elif "help" in user_input or "batao" in user_input:
        return "Sure! You can say 'hi', ask 'how are you', or ask for my name. Type 'bye' to close."

    # Default fallback if nothing matches
    else:
        return random.choice(fallback_replies)


# --- Main Conversation Loop ---
print("🤖 Chatbot: Hey! I am awake and ready to chat. (Type 'bye' to exit)")

while True:
    user_message = input("You: ")

    # Agar user bye bole toh loop yahi khatam
    if user_message.lower().strip() in ["bye", "exit", "quit", "alvida"]:
        print("🤖 Chatbot is typing...")
        time.sleep(1)
        print("🤖 Chatbot: Goodbye! Have a wonderful day ahead, and good luck with your internship! Bye!")
        break

    # Human touch: "Typing..." effect create karna
    print("🤖 Chatbot is typing...")
    time.sleep(1.2)  # 1.2 seconds ka pause software ko human feel dega

    # Get response and print
    response = chatbot_response(user_message)
    print("🤖 Chatbot:", response)
    print()  # Ek khali line space ke liye