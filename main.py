import os
import pyttsx3
import webbrowser
import psutil
import speech_recognition as sr
import time
from hiddenF import hidden_function

engine = pyttsx3.init() #initializer for speak() command
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use the female voice set to 1; set 

def speak(text):
    engine.say(text)
    engine.runAndWait()
    time.sleep(5)  #Pause for 5 seconds to allow the speech to complete

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def title():
    print("""
    _    ___  _ _     ____  ____  _    
    / \   \  \/// \ /\/  _ \/  _ \/ \ ||
    | |    \  / | | ||| | //| / \|| | //
    | |_/\ / /  | \_/|| |_\\\| \_/|| \// 
    \____//_/   \____/\____/\____/\__/  
                                        """)
    print("Voice Controlled Directory Manager - Made by max")
    print("Open source code available on GitHub")
    

while True:
    with sr.Microphone() as source:
        clear()
        title()
        speak("1. Say make to create a directory")
        speak("2. Say rename to rename a directory")
        speak("3. Say delete to delete a directory")
        speak("4. Say list to list directories")
        speak("5. Say link for more info")
        speak("6. Say exit to quit the program")
        print("listening...")
        r = sr.Recognizer()
        audio = r.listen(source)
        print("done listening...")

        try:
            command = r.recognize_google(audio)
            command = command.lower()#Lowercase the text so if commands dont break
            print("You said: " + command)# Output what was said

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

    if "make" in command:
        speak("Making directory")
        dir_name = command.replace("make", "").strip()
        os.system(f'mkdir "{dir_name}"')

    if "rename" in command:
        speak("Renaming directory")
        parts = command.replace("rename", "").strip().split(" to ")
        if len(parts) == 2:
            old_name = parts[0].strip()
            new_name = parts[1].strip()
            os.rename(old_name, new_name)
        else:
            speak("Please specify the old and new directory names correctly.")

    if "delete" in command:
        speak("Deleting directory")
        dir_name = command.replace("delete", "").strip()
        os.system(f'rmdir /S /Q "{dir_name}"')

    if "hidden" in command:
        speak("Accessing hidden function")
        hidden_function()
    
    if "list" in command:
        speak("Listing directories")
        os.system('dir')

    if "link" in command:
        speak("Opening GitHub link for more information")
        webbrowser.open("https://github.com/Xact1fy/lyubov")
        
    #add hidden function trigger
    if "exit" in command:
        speak("Exiting the program")
        break
