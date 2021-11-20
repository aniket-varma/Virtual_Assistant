import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import time
import pyaudio
import webbrowser
import os
from googlesearch import search


brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print("Recognising.....")
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            # print(e)
            print("Say that again please......")
            return "None"
        return query

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12 ):
        speak("Good Morning! Sir")
    elif(hour>=12 and hour<18):
        speak("Good AfterNoon! Sir")
    else:
        speak("Good Evening! Sir")
    speak("I am jarvis version 2.0. Please tell me how may I help you sir?")

if __name__ == '__main__':

    wishMe()        
    while(True):
        q=takeCommand()
        q=q.lower()
        if 'wikipedia' in q:
            speak("Searching Wikipedia......")
            q=q.replace("wikipedia","")
            results=wikipedia.summary(q, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'hold on' in q:
            time.sleep(180)
        elif q=='none':
            continue
        elif 'open youtube' in q:
            webbrowser.get(brave_path).open("youtube.com")
        elif 'time' in q:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in q:
            codePath="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'play music' in q:
                music_dir="E:\\Songs"
                songs=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))

        elif 'go to sleep' in q:
            speak("Quitting sir")
            print("Quitting Sir")
            exit()
        elif 'set reminder' in q:
            speak("Sir please set the remainder by giving hours and minutes in twenty four hour format")
            rem_hours=int(input("Enter Hours: "))
            rem_mins=int(input("Enter Minutes: "))
            now=datetime.datetime.now()
            while(now.hour<=rem_hours or now.minute<=rem_mins):
                now=datetime.datetime.now()
                print("Running.....")
                if(now.hour==rem_hours and now.minute==rem_mins):
                    speak("Sir! Wake up, You have some important work to do")
                    r=sr.Recognizer()
                    with sr.Microphone() as source:
                        print("Listening.....")
                        r.pause_threshold=1
                        audio=r.listen(source)
                        try:
                            print("Recognising.....")
                            query = r.recognize_google(audio,language='en-in')
                            speak("Thanks for responding my call sir")
                            exit()
                        except:
                            speak("Sir as you are not waking up I am playing a song")
                            music_dir="E:\\Songs"
                            songs=os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir,songs[0]))
                time.sleep(60)              
        elif 'please open' in q:
            q=q.replace("please open","")
            for j in search(q, tld="com", num=1, stop=1, pause=2):
                speak("Here what I found in google")
                webbrowser.get(brave_path).open(j)
                