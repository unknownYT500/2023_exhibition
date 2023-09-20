# import...
import datetime
import tkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys
import os
import speech_recognition as s_r
import webbrowser
import urllib
import pyttsx3
from datetime import date
from datetime import datetime
import funcfile

import random
import time
import threading
import funcfile
from funcfile import voice
import sys
import os
from tkinter import *
import os
import sys
import speech_recognition as s_r
import webbrowser
import urllib
import pyttsx3
from tkinter import ttk, messagebox
import customtkinter as ctk
from PIL import Image
import subprocess
from termcolor import colored
import atexit
import keyboard
from gtts import gTTS
import requests
import dateutil
import dateutil.parser
import matplotlib
from nsetools import Nse


nse = Nse()


# logging application start
funcfile.logging("program started", "main.py")

# window theme
ctk.set_appearance_mode("dark")

# declaring window base
window_name = ctk.CTk()

# widow size and info

window_name.geometry("1000x600")
window_name.minsize(1225, 600)
window_name.maxsize(1225, 600)
window_name.title("Computer_Exhibition_Test_Run")
logo_icon = PhotoImage(file="bfxskillathon_logo.png")
window_name.iconphoto(False, logo_icon)

# nav bar
# provides access to common functions
nav_bar = ctk.CTkScrollableFrame(master=window_name, height=578, width=200, border_color="blue", border_width=1).place(
    x=0, y=0)

# NetAvailability
# Checking whether online or offline
if funcfile.internet_stat() == "online":
    int_status = ctk.CTkLabel(master=nav_bar, text_color="#7CFC00", width=190,
                              text="Internet status: " + funcfile.internet_stat()).place(x=10, y=10)
    funcfile.logging("Internet_status:Online", "NetAvailability")

elif funcfile.internet_stat() == "offline":
    int_status = ctk.CTkLabel(master=nav_bar, text_color="red", width=190,
                              text="Internet status: " + funcfile.internet_stat()).place(x=10, y=10)
    funcfile.logging("Internet_status:Offline", "NetAvailability")

# mainframe...
# Section which holds all the necessary information provided by the application
main_frame = ctk.CTkScrollableFrame(master=window_name, height=578, width=746, border_width=1,
                                    border_color="red").place(x=230, y=0)

# q_pan_start...
# quick panel that provides information to user about itself
q_pan_start = ctk.CTkFrame(master=window_name, height=592, width=220, border_color="blue", border_width=1).place(
    x=1000, y=0)
q_pan_st_l1 = ctk.CTkLabel(master=q_pan_start, text="QUICK PANEL", text_color="blue", width=200).place(x=1010,
                                                                                                       y=10)
q_pan_exp = ctk.CTkLabel(master=q_pan_start,
                         text='''This panel provides quick access\nto necessary functions of your\nwindow''',
                         height=100, width=200).place(x=1010, y=60)


# frames...
# All the frames which are to be represented on the main frame and displays the desired output of any kind on it


# Homepage
# starting page which is actually like an introduction page which provides brief details about the application
def home_page():
    home_Page = ctk.CTkScrollableFrame(master=window_name, height=578, width=746, border_width=1,
                                       border_color="red").place(x=230, y=0)

    #home page
    #dummy stocks

    stock_display = ctk.CTkTextbox(master=home_Page, width=730, height=560)
    stock_display.place(x=240, y=10)







    funcfile.logging("home_page visited", "home_page()")

    # Quick pannel
    # for the quick access to its accessories
    q_pan_home = ctk.CTkFrame(master=window_name, height=592, width=220, border_color="blue", border_width=1).place(
        x=1000, y=0)

    q_pan_l1 = ctk.CTkLabel(master=q_pan_home, text="QUICK PANNEL", text_color="blue", width=200).place(x=1010,
                                                                                                        y=10)




# button for home_page()
home_btn = ctk.CTkButton(master=nav_bar, text="HOME", width=190, command=lambda: (home_page())).place(x=10, y=50)


# workpage
# contains the work frame consisting of the most vital purpose for which the application is build
def work_page():
    verify_Page = ctk.CTkScrollableFrame(master=window_name, height=578, width=746, border_width=1,
                                       border_color="red").place(x=230, y=0)
    username = ctk.StringVar()
    password = ctk.StringVar()

    # Quick pannel
    q_pan_work = ctk.CTkFrame(master=window_name, height=592, width=220, border_color="blue",
                              border_width=1).place(
        x=1000, y=0)

    q_pan_l1 = ctk.CTkLabel(master=q_pan_work, text="QUICK PANNEL", text_color="blue", width=200).place(x=1010,
                                                                                                        y=10)

    #verification
    def verification():
        if username_entry.get() == "shubham" and pass_entry.get() == "shubham@2007":
            messagebox.showinfo("Verification","Successfull login")
            work_Page = ctk.CTkScrollableFrame(master=window_name, height=578, width=746, border_width=1,
                                               border_color="red").place(x=230, y=0)

            # Trading



        else:
            messagebox.showerror("Verification","Credentials dont match")



    #login credentials

    #username
    username_text = ctk.CTkLabel(master=verify_Page, text="USERNAME").place(x=250, y=15)

    username_entry = ctk.CTkEntry(master=verify_Page, width=650, height=40, textvariable=username)
    username_entry.place(x=250,y=40)

    #password
    pass_text = ctk.CTkLabel(master=verify_Page, text="PASSWORD").place(x=250, y=90)

    pass_entry = ctk.CTkEntry(master=verify_Page, width=650, height=40, textvariable=password)
    pass_entry.place(x=250, y=120)




    #submit
    submit_cred = ctk.CTkButton(master=verify_Page, text="LOGIN", width=190, command=lambda: verification()).place(x=250, y=180)




# button for work_page()
work_btn = ctk.CTkButton(master=nav_bar, text="WORK", width=190, command=lambda: work_page()).place(x=10, y=100)


# extrapage
# contains
def extra_page():
    extra_Page = ctk.CTkScrollableFrame(master=window_name, height=578, width=746, border_width=1,
                                        border_color="red").place(x=230, y=0)
    extra_l1 = ctk.CTkLabel(master=extra_Page, text="extra").place(x=250, y=15)
    funcfile.logging("extra_page visited", "extra_page()")

    # Quick panel
    q_pan_extra = ctk.CTkFrame(master=window_name, height=592, width=220, border_color="blue", border_width=1).place(
        x=1000, y=0)

    q_pan_l1 = ctk.CTkLabel(master=q_pan_extra, text="QUICK PANEL", text_color="blue", width=200).place(x=1010,
                                                                                                         y=10)

# button for extra_page()
extra_btn = ctk.CTkButton(master=nav_bar, text="EXTRA", width=190, command=lambda: extra_page()).place(x=10, y=150)


def about_page():
    about_Page = ctk.CTkScrollableFrame(master=window_name, height=578, width=746, border_width=1,
                                        border_color="red").place(x=230, y=0)
    about_l1 = ctk.CTkLabel(master=about_Page, text="ABOUT", text_color="#bbfcfc").place(x=550, y=15)
    funcfile.logging("about_page visited", "about_page()")

    about_l2 = ctk.CTkLabel(master=about_Page, text='''Hi! my name is Shubham Prateek tirkey and I welcome you to my
    skillathon project.\n I would like to thank the whole team of bfx prism for giving this opportunity to work on 
    this project\n This app is based on python GUI and its made to provide ease to the customers due to the usage of 
    dynamic functionalities\n The code is designed to meet all your needs and ''').place(x=240, y=50)

    # Quick pannel
    q_pan_about = ctk.CTkFrame(master=window_name, height=592, width=220, border_color="blue", border_width=1).place(
        x=1000, y=0)

    q_pan_l1 = ctk.CTkLabel(master=q_pan_about, text="QUICK PANEL", text_color="blue", width=200).place(x=1010,
                                                                                                         y=10)


about_btn = ctk.CTkButton(master=nav_bar, text="ABOUT", width=190, command=lambda: about_page()).place(x=10, y=200)


def terminal_page():
    funcfile.logging("terminal_page visited", "terminal_page()")

    terminal_Page = ctk.CTkScrollableFrame(master=window_name, height=578, width=746, border_width=1,
                                           border_color="red").place(x=230, y=0)

    # Quick pannel
    q_pan_terminal = ctk.CTkFrame(master=window_name, height=592, width=220, border_color="blue", border_width=1).place(
        x=1000, y=0)

    inp = ctk.StringVar()

    def input():
        try:
            cmd = inp.get()
            funcfile.logging(cmd, "command_line")
            if cmd == "clear":
                terminal_l1.delete(1.0, ctk.END)

            else:
                opt = subprocess.check_output(cmd, shell=True)
                terminal_l1.insert(ctk.END, opt)

            inp.set("")
        except Exception as e:
            terminal_l1.insert(ctk.END, e)

    terminal_entry = ctk.CTkEntry(master=terminal_Page, width=650, height=40, textvariable=inp)

    terminal_entry.place(x=250, y=540)

    terminal_l1 = ctk.CTkTextbox(master=terminal_Page, width=720, height=500)

    terminal_l1.place(x=250, y=15)

    terminal_button = ctk.CTkButton(master=terminal_Page, width=70, height=40, text="ENTER", command=lambda: input())
    terminal_button.place(x=905, y=540)

    # quick pannel...

    q_pan_l1 = ctk.CTkLabel(master=q_pan_terminal, text="QUICK PANEL", text_color="blue", width=200).place(x=1010,
                                                                                                            y=10)

    def clear():
        terminal_entry.delete(0, ctk.END)
        terminal_entry.insert(ctk.END, "clear")
        input()
        funcfile.logging("terminal-clear", "clear()")

    q_pan_b3 = ctk.CTkButton(master=q_pan_terminal, text="CLEAR", width=200, command=lambda: clear()).place(x=1010,
                                                                                                            y=60)

    def Ipcon():
        terminal_entry.delete(0, ctk.END)
        terminal_entry.insert(ctk.END, "ipconfig")
        input()
        funcfile.logging("terminal-Ipcon", "Ipcon()")

    q_pan_b1 = ctk.CTkButton(master=q_pan_terminal, text="IPCONFIG", width=200, command=lambda: Ipcon()).place(x=1010,
                                                                                                               y=110)

    def vwlog():
        terminal_entry.delete(0, ctk.END)
        terminal_entry.insert(ctk.END, "type log.txt")
        input()
        funcfile.logging("terminal-viewing_log", "vwlog()")

    q_pan_b2 = ctk.CTkButton(master=q_pan_terminal, text="VIEW LOG", width=200, command=lambda: vwlog()).place(x=1010,
                                                                                                               y=160)

    def cl_log():
        f = open("log.txt", "r+")
        f.seek(0)
        f.truncate()
        funcfile.logging("terminal-clearing_log", "cl_log()")

    q_pan_b4 = ctk.CTkButton(master=q_pan_terminal, text="CLEAR LOG", width=200, command=lambda: cl_log()).place(x=1010,
                                                                                                                 y=210)

    def wifi_pass():
        terminal_entry.delete(0, ctk.END)
        terminal_entry.insert(ctk.END, "netsh wlan export profile key=clear")
        input()
        funcfile.logging("terminal-wifi_password", "wifi_pass()")

    q_pan_b5 = ctk.CTkButton(master=q_pan_terminal, text="WIFI-PASS", width=200, command=lambda: wifi_pass()).place(
        x=1010, y=260)

    def Dir():
        terminal_entry.delete(0, ctk.END)
        terminal_entry.insert(ctk.END, "dir")
        input()
        funcfile.logging("terminal-directory", "Dir()")

    q_pan_b6 = ctk.CTkButton(master=q_pan_terminal, text="DIR", width=200, command=lambda: Dir()).place(x=1010, y=310)

    def Open_file():
        terminal_l1.insert(ctk.END, funcfile.open_file())
        funcfile.logging("terminal-Opening_file", "Open_file()")

    q_pan_b7 = ctk.CTkButton(master=q_pan_terminal, text="OPEN", width=200, command=lambda: Open_file()).place(x=1010,
                                                                                                               y=360)

    def Manual():
        terminal_entry.delete(0, ctk.END)
        terminal_entry.insert(ctk.END, "type manual.txt")
        input()
        funcfile.logging("terminal-viewing_manual", "Manual()")

    q_pan_b8 = ctk.CTkButton(master=q_pan_terminal, text="VIEW MANUAL", width=200, command=lambda: Manual()).place(
        x=1010, y=410)

    def Chat_GPT():
        def cinp():
            try:

                if inp.get() == "vc":
                    os.system("python px_vc_assistant.py")

                    clear()


                elif inp.get() != "quit":
                    response = funcfile.chat_with_gpt(inp.get())
                    terminal_l1.insert(ctk.END, response)



                else:
                    terminal_button.place(x=905, y=540)



            except Exception as e:
                print(e)

        terminal_button_c = ctk.CTkButton(master=terminal_Page, width=70, height=40, text="CHAT",
                                          command=lambda: cinp()).place(x=905, y=540)

        funcfile.logging(inp.get(), "Chat_GPT()")

    q_pan_b9 = ctk.CTkButton(master=q_pan_terminal, text="A.I. MODE", width=200, command=lambda: Chat_GPT()).place(
        x=1010, y=460)

    keyboard.add_hotkey("alt+c", lambda: clear())

    keyboard.add_hotkey("alt+c+l", lambda: cl_log())

    keyboard.add_hotkey("enter", lambda: input())


terminal_btn = ctk.CTkButton(master=nav_bar, text="TERMINAL", width=190, command=lambda: terminal_page()).place(x=10,
                                                                                                                y=250)


def tool_page():
    tool_Page = ctk.CTkScrollableFrame(master=window_name, height=578, width=746, border_width=1,
                                       border_color="red").place(x=230, y=0)
    tool_l1 = ctk.CTkLabel(master=tool_Page, text="Tool").place(x=250, y=15)
    funcfile.logging("home_page visited", "home_page()")

    # Quick pannel
    q_pan_home = ctk.CTkFrame(master=window_name, height=592, width=220, border_color="blue", border_width=1).place(
        x=1000, y=0)

    q_pan_l1 = ctk.CTkLabel(master=q_pan_home, text="QUICK PANEL", text_color="blue", width=200).place(x=1010,
                                                                                                        y=10)


tool_btn = ctk.CTkButton(master=nav_bar, text="TOOL", width=190, command=lambda: tool_page()).place(x=10, y=300)


def exit():
    funcfile.logging("Exiting program", "exit([0])")
    funcfile.logging_exit()


def Voice():
    vtext = funcfile.voice()

    if vtext == "open home window":
        funcfile.text_to_speech("opening home page")
        home_page()

    elif vtext == "open work window":
        funcfile.text_to_speech("opening work page")
        work_page()

    elif vtext == "open extra window":
        funcfile.text_to_speech("opening extra page")
        extra_page()

    elif vtext == "open about window":
        funcfile.text_to_speech("opening about page")
        about_page()

    elif vtext == "open terminal window":
        funcfile.text_to_speech("opening terminal page")
        terminal_page()

    elif vtext == "hay chat GPT":
        start_speech = "yes i am listening"
        funcfile.text_to_speech(start_speech)
        voice_to_text = funcfile.voice()
        funcfile.text_to_speech(funcfile.chat_with_gpt(voice_to_text))

    elif vtext == "full voice control":
        pass

    else:
        print(vtext)
        funcfile.text_to_speech(vtext)

    funcfile.logging("voice","Voice(Chat_GPT())")


# shortcuts...

keyboard.add_hotkey("ctrl+win+h", lambda: home_page())

keyboard.add_hotkey("ctrl+win+w", lambda: work_page())

keyboard.add_hotkey("ctrl+win+e", lambda: extra_page())

keyboard.add_hotkey("ctrl+win+a", lambda: about_page())

keyboard.add_hotkey("ctrl+win+t", lambda: terminal_page())

keyboard.add_hotkey("ctrl+alt+m", lambda: Voice())

atexit.register(exit)

window_name.mainloop()
