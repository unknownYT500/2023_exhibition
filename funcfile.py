#import...
import sys
import speech_recognition as s_r
import webbrowser
import urllib
import pyttsx3
from datetime import date
from datetime import datetime
import os
import datetime
from tkinter.filedialog import askopenfile
import hashlib
import datetime
import json
import tkinter as tk
import speech_recognition as s_r
import webbrowser
import urllib
import pyttsx3
from datetime import date
from datetime import datetime
from tkinter import *
import googletrans
import speech_recognition
import textblob
from tkinter import ttk, messagebox
import time
from gtts import gTTS
from tkinter import filedialog
import pyperclip
from tkinter import filedialog
from profanity import profanity
import pyaudio
import pyttsx3
import socket
from termcolor import colored
import openai
import yfinance as yf
import tradingview_ta
import time



openai.api_key = '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'






def voice():
    try:
        # functions...


        r = s_r.Recognizer()
        my_mic = s_r.Microphone(device_index=1)  # my device index is 1, you have to put your device index

        with my_mic as source:
            audio = r.listen(source)  # take voice input from the microphone

        #store
        Vtext = r.recognize_google(audio)
        return Vtext

    except Exception as e:
        print("error")
        voice()

    print("voice()")



def filewriter(filename,text):
    os.system("echo "+text+" > "+filename+".txt")

def windowmaker(window_name,title,logo,mnsize,mxsize):
    window_name = Tk()

    #size and info

    window_name.geometry("800x800")
    window_name.minsize(mnsize)
    window_name.maxsize(mxsize)
    window_name.title(title)
    image_icon = PhotoImage(file=logo)
    window_name.iconphoto(False, image_icon)

    window_name.mainloop()


def internet_stat():
    on = colored('online', 'green', attrs=['reverse', 'blink'])
    of = colored('offline', 'red', attrs=['reverse', 'blink'])
    while True:
        try:
            s = socket.create_connection(
                ("www.geeksforgeeks.org", 80))
            if s is not None:
                s.close
            return on
        except OSError:
            pass
        return of


def date_time():
    current_time = datetime.datetime.now()

    return current_time

def button_sound():
    os.system("start interface-124464.mp3")


def logging(user_input,type):
    with open("log.txt", "a") as file:
        file.write(f" {user_input} {type}\n")

def logging_exit():
    with open("log.txt", "a") as file:
        file.write("\n")

def open_file():
    file = askopenfile(mode ='r', filetypes =[('All Files','')])
    if file is not None:
        content = file.read()
        return content


def chat_with_gpt(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )
    print("chat with gpt")
    return response.choices[0].text.strip()




def text_to_speech(Text):
    text_speech = pyttsx3.init()

    today = date.today()

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")

    text_speech.say(Text)

    text_speech.runAndWait()


def get_current_stock_price(ticker):
    try:
        # Create a Ticker object for the specified stock
        stock = yf.Ticker(ticker)
        # Get the current price of the stock
        current_price = stock.history(period="1d")["Close"].iloc[-1]

        cp = {
            ticker : current_price
        }

        final_stat = cp[ticker]
        return final_stat

    except Exception as e:
        print(f"Error occurred: {e}")


def is_market_open():
    # Get the current time
    current_time = time.localtime()

    # Extract the current hour from the time object
    current_hour = current_time.tm_hour

    # Perform conditional statements based on the hour
    if 9 <= current_hour < 15:
        return True
    else:
        return False


def chat_gpt_vc():
    try:
        # functions...

        text_speech = pyttsx3.init()

        today = date.today()

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

        r = s_r.Recognizer()
        my_mic = s_r.Microphone(device_index=1)  # my device index is 1, you have to put your device index

        with my_mic as source:

            audio = r.listen(source)  # take voice input from the microphone
            return audio.lower()

    except Exception as e:
        print(e)



# Function to extract numbers from a string and calculate their sum
def sum_numbers_in_string(input_string):
    numbers = []  # List to store the extracted numbers

    # Iterate through each character in the input string
    current_number = ''
    for char in input_string:
        if char.isdigit() or (char == '.' and '.' not in current_number):
            current_number += char
        elif current_number:
            numbers.append(float(current_number))
            current_number = ''

    # Add the last number if it exists
    if current_number:
        numbers.append(float(current_number))

    # Calculate the sum of the extracted numbers
    total_sum = sum(numbers)

    return total_sum


#Function to extract numbers from a string and calculate their subtraction
def subtract_numbers_in_string(input_string):
    numbers = []  # List to store the extracted numbers

    # Iterate through each character in the input string
    current_number = ''
    for char in input_string:
        if char.isdigit() or (char == '.' and '.' not in current_number):
            current_number += char
        elif current_number:
            numbers.append(float(current_number))
            current_number = ''

    # Add the last number if it exists
    if current_number:
        numbers.append(float(current_number))

    # Check if there are at least two numbers for subtraction
    if len(numbers) < 2:
        return "Insufficient numbers for subtraction."

    # Calculate the subtraction of the extracted numbers
    result = numbers[0]
    for num in numbers[1:]:
        result -= num

    return result



# Function to extract numbers from a string and calculate their multiplication
def multiply_numbers_in_string(input_string):
    numbers = []  # List to store the extracted numbers

    # Iterate through each character in the input string
    current_number = ''
    for char in input_string:
        if char.isdigit() or (char == '.' and '.' not in current_number):
            current_number += char
        elif current_number:
            numbers.append(float(current_number))
            current_number = ''

    # Add the last number if it exists
    if current_number:
        numbers.append(float(current_number))

    # Check if there are at least two numbers for multiplication
    if len(numbers) < 2:
        return "Insufficient numbers for multiplication."

    # Calculate the multiplication of the extracted numbers
    result = 1
    for num in numbers:
        result *= num

    return result


# Function to extract numbers from a string and calculate their division
def divide_numbers_in_string(input_string):
    numbers = []  # List to store the extracted numbers

    # Iterate through each character in the input string
    current_number = ''
    for char in input_string:
        if char.isdigit() or (char == '.' and '.' not in current_number):
            current_number += char
        elif current_number:
            numbers.append(float(current_number))
            current_number = ''

    # Add the last number if it exists
    if current_number:
        numbers.append(float(current_number))

    # Check if there are at least two numbers for division
    if len(numbers) < 2:
        return "Insufficient numbers for division."

    # Check for division by zero
    if 0 in numbers[1:]:
        return "Division by zero is not allowed."

    # Calculate the division of the extracted numbers
    result = numbers[0]
    for num in numbers[1:]:
        result /= num

    return result