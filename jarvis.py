import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir !!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir !!")
    else:
        speak("Good Evening Sir!!")
    
# function for listing and processing that command    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language= 'en-in')
        print("User said : ",query)
        speak(query)
        
    except Exception as e:
        print(e)
        speak("Say that again please...!!!")
        print("Say that again please....")
        speak("Say that again please...!!!")
        return "None"
    return query

#sendEmail fucntion
def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','Your_password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    speak("How can I help you Sir")
    while True:
        query = takeCommand().lower()

        #Logic for using the wikipedia
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir = "C:\\Users\hp\\Desktop\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            st = "Sir, the time is "+ strTime
            speak(st)
        elif "open code" in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to vishnu' in query:
            try:
                speak("What should I say !")
                content = takeCommand()
                to = "vishnupsingh523@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent SIR!")
            except Exception as e:
                print(e)
                speak("Sorry sir email is not sent.")
