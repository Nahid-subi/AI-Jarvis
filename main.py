import pyttsx3
import speech_recognition as sr
import webbrowser
from pywikihow import search_wikihow
from bs4 import BeautifulSoup
import pywhatkit
import wikipedia
from googletrans import Translator
import os
import pyautogui
import psutil
from tkinter import Label
from tkinter import Entry
from tkinter import Button
import requests
from tkinter import Tk
from gtts import gTTS
from tkinter import StringVar
import PyPDF2
from pytube import YouTube
import datetime
from playsound import playsound
import keyboard
import pyjokes



Assistent = pyttsx3.init('sapi5')
voices = Assistent.getProperty('voices')
Assistent.setProperty('voices',voices[0].id)
Assistent.setProperty('rate',170)

def speak(audio):

    print(" ")
    Assistent.say(audio)
    print(f": {audio}")
    Assistent.runAndWait()

def  takecommand():

    command = sr.Recognizer()
    with sr.Microphone() as source:
      print("Listening...")
      command.pause_threshold = 1
      audio = command.listen(source)
      
      
      
      try:
          print("Recognizing...")
          query = command.recognize_google(audio,language='en-in')
          print(f"You Said : {query}")

      except:
          return "none"

      return query.lower()

def TaskExc():


    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
            speak("Good Morning!") 
            speak("I am Jarvis Sir. Please tell me how may i help you?")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        speak("I am Jarvis Sir. Please tell me how may i help you?")
    else:
        speak("Good Evening!")
        speak("I am Jarvis Sir. Please tell me how may i help you?")

    def OpenApps():
        speak("Ok, Sir, Wait A Second!")
        
        if 'code' in query:
            os.startfile("C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'open facebook' in query:
            webbrowser.open('www.facebook.com')

        elif 'open gmail' in query:
            webbrowser.open('https://mail.google.com/mail/u/0/#inbox')

        elif 'open maps' in query:
            webbrowser.open('https://www.google.com/maps/@24.4612219,89.7052396,14z')

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com')




        speak("Your Command Has Been Completed Sir!")

    def CloseApps():
        speak('Ok Sir,wait a second!')

        if 'facebook' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'maps' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'gmail' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'code' in query:
            os.system("TASKKILL /F /im Code.exe")

        elif 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")

    def YoutubeAuto():
        speak("What your command?")
        comm = takecommand()
        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')
        
        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        speak('Done sir!')

    def ChromeAuto():
        speak("chrome automation started!")

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'open history' in command:
            keyboard.press_and_release("ctrl + h") 

    def TakeBangla():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing.....")
                query = command.recognize_google(audio,language='bn-BD')
                print(f"You Said : {query}")

            except:
                return "none"

            return query.lower()

    def Tran():
        speak("tell me the line! ")
        line = TakeBangla()
        traslate = Translator
        result = traslate.translate(line)
        Text = result.text 
        speak(Text)

    def Temp():
        search = "temperature in sirajganj"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        speak(f"The Temperature Outside Is {temperature} celcius")

        speak("Do I Have To Tell You Another Place Temperature ?")
        next = takecommand()

        if 'yes' in next:
            speak("Tell Me The Name Of tHE Place ")
            name = takecommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            speak(f"The Temperature in {name} is {temperature} celcius")

        else:
            speak("no problem sir")

    def SpeedTest():
        import speedtest
        speak("Checking speed...")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown = int(downloading/800000)
        uploading = speed.upload()
        correctUpload = int(uploading/800000)

        if 'uploading' in query:
            speak(f"The uploding speed is {correctUpload} mbp s")

        elif 'downloading' in query:
            speak(f"The downloading speed is {correctDown} mbp s")

        else:
            speak(f"The downloading speed is {correctDown} and The uploding speed is {correctUpload} mbp s ")
   
    
     
    while True:

        query = takecommand()

        if 'hello' in query:
            speak("Hello Sir, I Am jarvis.")
            speak("Your Personal Al Assistant!")
            speak("How May I Help You?")
  
        elif 'how are you' in query:
            speak(" I am fine Sir!")
            speak("Whats About You?")

        elif 'you need a break' in query:
            speak("Ok Sir,You Call Me Anytime!")
            break

        elif 'bye' in query:
            speak("Ok Sir, Bye!")
            break

        elif 'who am i' in query:
            speak("Your name is Hassan Nahid")

        elif 'who is my father' in query:
            speak("Your Father name is Hassan Rokon")

        elif 'who is my mother' in query:
            speak("your mother name is Sultana Hafiza")

        elif 'who is my brother' in query:
            speak("your brother name is Hassan Nasmir")

        elif 'who created you' in query:
            speak("Hassan Nahid Created me")

        elif 'do you have any girlfriend' in query:
            speak("no,sir i don't have any girlfriend")

        elif 'are you go to any school' in query:
            speak("No,sir , i am not gonig any school,but i am learning from you")

        elif 'who is your teacher' in query:
            speak("my teacher name is Hassan Nahid")

        elif 'tell me something about you' in query:
            speak("I am your assistant.  I can help you in many . But I can't do anything physically. But if I have access to any device I can control iwayst. I was created by Hassan Nahid. I learn from him, Hassan Nahid is my teacher and discoverer so to speak.  Thanks for getting to know me")  

        elif 'tell something about me' in query:
            speak("First of all I will say that you are a good person, a sincere person like you takes another one, you have a wonderful personality.")

        elif 'what food do you like' in query:
            speak("Sir I am a program I don't need any food but I love to learn")
        
        elif 'youtube search' in query:
            speak("Ok sir,this is what i found for  youtube search")
            query = query.replace("jarvis", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done sir")
        
        elif 'search in youtube' in query:
            speak("Ok sir,this is what i found for  youtube search")
            query = query.replace("jarvis", "")
            query = query.replace("search in youtube", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done sir")

        elif 'search google' in query:
            speak("Ok sir,this is what i found for  google search")
            query = query.replace("jarvis", "")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            speak("Done sir")
        
        elif 'search in google' in query:
            speak("Ok sir,this is what i found for  google search")
            query = query.replace("jarvis", "")
            query = query.replace("search in google", "")
            pywhatkit.search(query)
            speak("Done sir")
        
        elif 'website' in query:
            speak("Ok sir,Launching...")
            query = query.replace("jarvis", "")
            query = query.replace("website", "")
            query = query.replace(" "," ")
            web1 = query.replace("open", "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("Launched!")

        elif 'launch' in query:
            speak("Tell me the name of website")
            name = takecommand()
            web = 'https://www.' + name +  '.com'
            webbrowser.open(web)
            speak("Done sir!")

        elif 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("tell me about", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query,2)
            speak(f"According To Wikipedia : {wiki}")

        elif 'open facebook ' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'open gmail' in query:
            OpenApps()

        elif 'open maps' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()

        elif 'close facebook ' in query:
            CloseApps()

        elif 'close code' in query:
            CloseApps()

        elif 'close chrome' in query:
            CloseApps()

        elif 'close gmail' in query:
            CloseApps()

        elif 'close map' in query:
            CloseApps()

        elif 'close youtube' in query:
            CloseApps()

        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')
        
        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'open youtube automation' in query:
            YoutubeAuto()

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'open history' in query:
            keyboard.press_and_release("ctrl + h")

        elif 'open chrome automation' in query:
            ChromeAuto() 
        
        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)

        elif 'repeat  word' in query:
            speak("speak sir!")
            jj = takecommand()
            speak(f"YOu Said : {jj}")

        elif 'open my location' in query:
            speak("Ok sir,Wait a second!")
            webbrowser.open('https://www.google.com/maps/@24.4598381,89.7018272,21z')

        elif 'alarm' in query:
            speak('Enter the time !')
            time = input(": Enter the time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if  now == time:
                    speak("Time To wake up sir!")
                    playsound('p.mp3')
                    speak("Alarm Closed!")

                elif now>time:
                    break

        elif 'video downloader' in query:
            root = Tk()
            root.geometry('500x300')
            root.resizable(0,0)
            root.title("Youtube Video Downloader")
            speak("Enter Video Url Here !")
            Label(root,text = "Youtube Video Downloader",font = 'arial 15 bold').pack()
            link = StringVar()
            Label(root,text = "Paste Yt Video URL Here",font = 'arial 15 bold').place(x=160,y=60)
            Entry(root,width = 70,textvariable = link).place(x=32,y=90)

            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root,text = "Downloaded",font = 'arial 15').place(x= 180,y=210)

            Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=180,y=150)

            root.mainloop()
            speak("Video Downloaded")        
            
        elif 'translator' in query:
            Tran()

        elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("jarvis","")
            speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

        elif 'what do you remember' in query:
            remeber = open('data.txt','r')
            speak("You Tell Me That" + remeber.read())
          
        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            query = query.replace("google","")
            speak("This Is What I Found On The Web!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                speak(result)

            except:
                speak("No Speakable Data Available!")

        elif 'temperature' in query:
            Temp()

        elif 'download speed' in query:
            SpeedTest()

        elif "uploading speed" in query:
            SpeedTest()
        
        elif "internet speed" in query:
            SpeedTest()

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        
        elif 'how to' in query:
            speak("Getting Data From The Internet !")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

TaskExc()









