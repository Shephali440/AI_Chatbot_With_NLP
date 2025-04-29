import nltk
import random
import string  # for punctuation
from nltk.stem import WordNetLemmatizer

# Download required NLTK packages
nltk.download('punkt')  # for tokenization
nltk.download('wordnet')  # for lemmatization

# Sample corpus for chatbot to understand
corpus = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "greeting_response": ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you?"],
    
    "goodbye": ["bye", "see you", "goodbye", "exit"],
    "goodbye_response": ["Goodbye!", "See you soon!", "Have a nice day!"],

    "name": ["what is your name", "who are you"],
    "name_response": ["I'm a simple AI chatbot.", "You can call me ChatBuddy."],

    "help": ["what can you do", "help me", "how can you help"],
    "help_response": ["I can answer basic queries and have a friendly chat with you!"]
}

lemmatizer = WordNetLemmatizer()

def preprocess(sentence):
    sentence = sentence.lower().translate(str.maketrans('', '', string.punctuation))
    tokens = sentence.split()
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmas

def respond(user_input):
    user_input = user_input.lower()
    processed_input = preprocess(user_input)

    for key in ["greeting", "goodbye", "name", "help"]:
        for word in corpus[key]:
            if word in user_input:
                return random.choice(corpus[f"{key}_response"])
    
    return "I'm sorry, I don't understand that. Can you please rephrase?"

def chat():
    print("ChatBot: Hi! I'm ChatBuddy. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("ChatBot:", random.choice(corpus["goodbye_response"]))
            break
        response = respond(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    chat()
