import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init()

def speak(text):
    """Triggers the assistant to speak the text out loud."""
    engine.say(text)
    engine.runAndWait()

def greet_me():
    """Greets the user based on the current time."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your assistant. How can I help you today?")

def take_command():
    """Listens to microphone input and converts it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.pause_threshold = 1  
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
     
        query = recognizer.recognize_google(audio, language='en-in')
        print(print(f"You said: {query}\n"))
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

if __name__ == "__main__":
    greet_me()
    
    while True:
        query = take_command()

        if 'time' in query:
            str_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {str_time}")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube")

        # Task 4: Shut down the assistant
        elif 'stop' in query or 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a great day.")
            break
