import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os  
import smtplib


engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')


engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Goog morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

        

    else:
        speak("Good Evening!")

    speak("I am joey sir, pleas tell me how may I help you")

def takecommand():
     command = sr.Recognizer()
     with sr.Microphone() as source:
        print("listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

     
     try:
        
        print("Recognizing...")
        query = command.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

     except Exception as e:
         print("say that again please...")
         return "None"
     return query




if __name__ == "__main__":
    speak("Bismillah")
    wishme()
    while True:
     query = takecommand().lower()

     if 'wikipedia' in query:
         speak('Searching Wikipedia...')
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query, sentences=1)
         speak("According to Wikipedia")
         print(results)
         speak(results)

     elif 'open youtube' in query:
         webbrowser.open("youtube.com")

     elif 'open google' in query:
         webbrowser.open("google.com")

     elif 'open stackoverflow' in query:
         webbrowser.open("stackboverflow.com")    

     elif 'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"sir, the time is {strTime}")

     elif 'play music' in query:
         music_dir = 'C:\\Users\\shahr\\OneDrive\\Desktop\\Jamia Hamdard Documents\\6Th Sem\\Study\Minor Project\\songs'
         songs = os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir, songs[0]))

     elif 'thank you' in query:
         speak("Thank you sir for your time!")
         exit()




