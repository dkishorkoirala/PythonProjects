from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot named RaiseYouAll
raise_you_all = ChatBot(
    'RaiseYouAll',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, I do not understand. Could you please rephrase?',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Train the chatbot on English language data
trainer = ChatterBotCorpusTrainer(raise_you_all)
trainer.train("chatterbot.corpus.english")

# Function to interact with the AI assistant
def chat_with_raise_you_all():
    print("Hello! I am RaiseYouAll, your AI assistant. How can I help you today?")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("RaiseYouAll: Goodbye! Have a great day!")
                break
            response = raise_you_all.get_response(user_input)
            print(f"RaiseYouAll: {response}")
        except (KeyboardInterrupt, EOFError):
            print("\nRaiseYouAll: Goodbye! Have a great day!")
            break

# Start the conversation
chat_with_raise_you_all()