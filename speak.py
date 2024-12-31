import pyttsx3
import os
import datetime
import time
import wikipedia as wiki
from playsound import playsound 
import pyaudio
import speech_recognition as sr

#speaking properities

spk=pyttsx3.init()
voice=spk.getProperty("voices")
spk.setProperty('voice',voice[1].id)

# microphone 
def list():
    try:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("listning...")
            audio= r.listen(source)
            print("please wait i am working on it ...")
            task=r.recognize_google(audio)
            task=task.lower()
            print(task)
            return task
    except sr.UnknownValueError:
        speak("sorry , i couldn't understand the your commend ")
        speak("please speak again ")
        list()
    except sr.RequestError as e:
        speak(" please  check your  internet and speak again ")
        intr=input("")
        if intr=="ok" or intr=="yaa":
            list()
        else:
            return "exit"



# information search 
wiki.set_lang("en")
spk.setProperty('rate',155)
spk.setProperty('volume',1.0)




def agin():
    speak("now do you want to give another commend ")
    #task=input("now do you want to give another commend  \n")
    task=list()
    meth(task)


def wish():
    hr=datetime.datetime.now().hour
    if 0<=hr<=12:
       
        speak("good morning ")
        what()
    elif(12<=hr<=16):
        
        speak("good after noon ")
        what()
    else :
        
        speak("good evening ")
        what()
def time():
    now=datetime.datetime.now().strftime("%H:%M:%S")
    print("current time:",now)
    speak(f"current time is {now}")
    what()

def what():
    speak("what can i do for you ")
    #task=input("what can i do for you \n")
    task=list()
    if task=="\0" or task=='':
        speak("aaha")
        speak("please enter a commend or tell me")
        what()
    elif task=="exit" or task=="bye" or task=="good bye":
        #speak("ok  bye")
        speak(" ok byeee have a nice day see you soooon ")
    else:
        meth(task)

def meth(task):
    t=[task]
    for i in t:
        if "search" in i or  "google search" in i:
            search()
            agin()


        elif "play music" in i:
            speak("do you want to provid the path of the music")
            path=input("do you want to provid the path of the music")
        #path=list()
            if path=="yes" or path=="yaa" or path=="ok":
                songpath=input("enter the path of your favourite song")
                playsound(songpath)
            else:
                playsound("")


        elif "date" in i or "today date" in i:
            curr_date=datetime.datetime.now().strftime("%B %d,%Y")
            speak(f"today's date is {curr_date}")
            agin()

        elif "open calculator" in i or " open calc" in i or "calc" in i:
            speak("opening calculator")
            os.system("calc")
            agin()


        elif "open notepad" in i or "notepad" in i:
            speak("opening notepad")
            os.system("notepad")
            agin()

        elif "time" in i :
            time()
            agin()

        elif "wait" in i:
            speak("ok i am waiting for your commend")
            time.sleep(20)
            agin()

            
        elif "lock computer" in i or "lock pc" in i or "lock" in i:
            speak("locking computer")
            os.system("rundll32.exe user32.dll,LockWorkStation")
            agin()
    
        elif "your name" in i or "name" in i or "your name please" in i:
            speak("yaa i am akash's personal assistance and my name is eesha  ")

        elif "exit" in i or "bye" in i:
            speak("bye boss")
            speak("have a nice day see you soon boss")
        else:
            speak("sorry your enter the wrong commend")
            speak("do you want to know what can i do for you")
        #do=input("do you want to know what can i do for you")
            do=list()
            if do=="yes" or do=="yaa" or do=="ok":
                speak("great")
                speak("i can do this work for you")
                speak("i can provide an information about a particular topic for the you can enter search")
                speak("i can open calc and notepad")
                speak("screen lock or lock the pc ")
                speak("i can provide current time and date etc")
                speak("now")
                what()
        '''else:

            #task=input("please enter a commend \n ")
            list()
            if task=="exit":
                speak("bye boss")
                speak("have a nice day see you soon boss")
            else:
                meth(task)'''
def exit():
    speak("good bye")
    return 

def speak(commend):
    spk.say(commend)
    spk.runAndWait()


def search1():
    spk.say("do want new topic ")
    spk.runAndWait()
    to=list()
    #to=input("do you want new topic\n")
    if to=="yes" or to=="yaa":
        spk.say("well please tell me  the new topic name")
        spk.runAndWait()
        #text=input("enter the new topic name \n")
        text=list()
        topic(text)
    else:
        spk.say("ok then ")
        spk.runAndWait()
        what()
    


def search():
    spk.say("please tell me  the topic name")
    spk.runAndWait()
    text=list()
    #text=input("enter the topic name \n")
    topic(text)

def topic(txt):
    if txt=="no":
        agin()
    else:
        res=wiki.summary(txt,sentences=5)
        print(res)
        spk.say(res)
        spk.runAndWait()
        print(res)
        search1()

spk.say(" hi hello i am eesha")
spk.runAndWait()

def me():
    speak("please enter the password to login")
    #txt=list()
    txt=input(" please enter the password  \n")
    d=[txt]
    for i in d:
        if "1234" in i or "abcd" in i:
            speak("welcome boss ")
            wish()
        elif txt=="exit" or txt=="bye" or txt=="good bye":
        #speak("ok  bye")
            speak(" ok bye have a nice day see you soon ")
        else:
            speak("wrong password please try again")
            me()
me()
