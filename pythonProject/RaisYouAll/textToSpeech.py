import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text
        except:
            return "Sorry, I didn't catch that."

# Modify the chat function to use voice
def voice_chat():
    speak("Hello! I am RaiseYouAll, your AI assistant. How can I help you today?")
    while True:
        user_input = listen()
        if user_input.lower() in ["exit", "quit", "bye"]:
            speak("Goodbye! Have a great day!")
            break
        response = raise_you_all.get_response(user_input)
        print(f"RaiseYouAll: {response}")
        speak(str(response))