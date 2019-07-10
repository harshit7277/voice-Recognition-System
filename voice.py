import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[len(voices)-1].id)



def speak(audio):
    print('computer: '+ audio)
    engine.say(audio)
    engine.runAndWait()


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning')

    if currentH >=12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')


greetMe()


speak('Hello sir, I am your digital assist for u mr harshit')
speak('how may I help you')



def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query  =  r.recognize_google(audio,language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('sorry sir! i didn\'t get that ! try typiing the command  ')
        query = str (input('Command: '))

    return query


if __name__ == '__main__':

    while True:

        query = myCommand();
        query = query.lower()


        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['just doing my things!','I am fine!','Nice','I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'nothing' in  query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye sir, have a good day')
            sys.exit()

        elif 'hello' in query:
            speak('hello sir')
        elif 'bye' in query:
            speak('Bye sir,have a good day.')
            sys.exit()

        else:
            query = query
            speak('searching.....')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('got it.')
                    speak(results)
                except:
                    results = wikipedia.summary(query,sentences=2)
                    speak('got it')
                    speak('WIKIPEDIA says - ')
                    speak(results)
            except:
                webbrowser.open('www.google.com')
        speak('Next command! sir!')






