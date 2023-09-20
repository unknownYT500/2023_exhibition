
#import...
import sys
import os
import speech_recognition as s_r
import webbrowser as wb
import urllib
import pyttsx3
from datetime import date
from datetime import datetime
import funcfile

#text_speech
textspeech = pyttsx3.init()

pyttsx3.init().say("chat bot started")
textspeech.runAndWait()



os.system("color a")
def work():
    global digit_exists
    try:

        #Voice Input...
        vc = funcfile.voice()



        if "hello" in vc:
            textspeech.say("hello sir Shubham")
            textspeech.runAndWait()
            work()


        elif "YouTube" in vc:
            textspeech.say("opening youtube")
            wb.open("youtube.com")
            textspeech.runAndWait()
            work()

        elif "Google" in vc:
            textspeech.say("opening google")
            wb.open("google.com")
            textspeech.runAndWait()
            work()

        elif "." in vc:
            textspeech.say("opening "+ vc)
            wb.open(vc)
            textspeech.runAndWait()
            work()

        elif "introduce" in vc or "introduction" in vc:
            textspeech.say('''I am a personal AI chat bot created by the computer exhibition team lead by Master Shubham.
            I am just a prototype but i am still capable of doing your personal tasks and solve issues using the web AI as well.
            I use chat GPT 3.5 as my web source.
            It was nice talking to you''')
            textspeech.runAndWait()
            work()


        elif "search" in vc:
            textspeech.say("Please say the Thing to be searched")
            textspeech.runAndWait()
            vc2 = funcfile.voice()
            wb.open(vc2)
            textspeech.runAndWait()
            work()

        elif "time" in vc:
            # Get the current date and time
            current_time = datetime.now()

            current_year = current_time.year
            current_day_of_week = current_time.strftime('%A')
            current_month = current_time.strftime('%B')
            current_day_name = current_time.strftime('%A')
            current_day = current_time.day



            # Extract hour, minute, and second
            current_hour = current_time.hour
            current_minute = current_time.minute
            current_second = current_time.second

            time = str(datetime.now())
            textspeech.say(f"{current_day} {current_month} {current_year} .Time right now is {current_hour} {current_minute}  ")
            textspeech.runAndWait()
            work()

        else:
            textspeech.say(funcfile.chat_with_gpt(vc))
            textspeech.runAndWait()
            work()


    except Exception as e:
        print(e)
        work()

work()