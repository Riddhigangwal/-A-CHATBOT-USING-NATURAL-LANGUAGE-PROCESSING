# chatbot.py

"""
🤖 AI Chatbot using NLTK
Internship Task 3 - CODTECH IT Solutions
Author: Riddhi Gangwal

Description:
A simple rule-based chatbot built using Python and NLTK that responds to basic user queries
using predefined pattern-response pairs and reflections.
"""

import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK resources (run once)
def download_nltk_data():
    try:
        nltk.download('punkt')
        nltk.download('wordnet')
    except Exception as e:
        print("⚠️ Error downloading NLTK resources:", e)

# Define pattern-response pairs
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you today?"]
    ],
    [
        r"what is your name ?",
        ["I am CodBot, your internship chatbot assistant."]
    ],
    [
        r"how are you ?",
        ["I'm doing great, thank you!", "I'm just a bunch of code, but I feel awesome!"]
    ],
    [
        r"what can you do ?",
        ["I can chat with you, answer basic questions, and help you learn about NLP."]
    ],
    [
        r"(.*) your creator ?",
        ["I was created by Riddhi Gangwal as part of an internship project at CODTECH."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I live in the cloud, but I was created in India!"]
    ],
    [
        r"how to learn NLP ?",
        ["Start by learning Python, then explore NLTK and spaCy. There are many online courses and books!"]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I am here to help. Please tell me your question."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye!", "See you later!", "Thanks for chatting with me!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you rephrase that?", "Sorry, I don't have an answer to that yet."]
    ]
]

# Launch the chatbot
def start_chat():
    print("=" * 60)
    print("🤖 CodBot: Hello! I am your AI chatbot assistant.")
    print("Type 'bye', 'exit', or 'quit' to end the chat.")
    print("=" * 60)
    chat = Chat(pairs, reflections)
    chat.converse()

# Main
if __name__ == "__main__":
    download_nltk_data()
    start_chat()
