#Project-Jarvis
#A virtual Assistant at its beginning level.
#Author - "Sandesh Parit"

import speech_recognition as sr
import webbrowser 
import pyttsx3
import musicLibrary

#Global variables
recogniser = sr.Recognizer()
engine = pyttsx3.init()

#funciions for command anad speak functionality
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open my account" in c.lower():
        webbrowser.open("https://www.linkedin.com/in/sandesh-parit-718213356/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com/Sandesh2713")
    #for playing music from another library.
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song] 
        webbrowser.open(link)

#the process of handling the request
if __name__ == "__main__":
    speak("Initialising Jarvis...")
    while True:
        #listen for the wake word of Jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        # recognize speech using Sphinx
        print("Listening...")
        try:
            #using sr to record the command
            with sr.Microphone() as source:
                audio = r.listen(source, timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            #if user alerts the program with jarvis then we shall move to next steps of algorithm
            if(word.lower() == "jarvis"):
                speak("Ya")
                #listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active ... ")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(command)

                    processCommand(command)

        #error raising if no command was recorded.
        except Exception as e:
            print("Error; {0}".format(e))