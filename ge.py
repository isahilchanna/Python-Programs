import tkinter as tk
from tkinter import ttk ,  Menu
from tkinter.messagebox import *
root=tk.Tk()
root.geometry('300x200')
root.title('Automated Sender')
root.iconbitmap('wp.ico')

import webbrowser
import pyautogui as pt
import time
import requests
pt.FAILSAFE = False
label=ttk.Label(text =b"Firstly open whatsapp app/web to run fast!!").pack()
entry=tk.IntVar()
entry_number=tk.Entry(root,text='Enter your number:',width=10,textvariable=entry)
entry_number.pack()
def save():
    save_info=tk.Button(root, text='Check?',command=save)
    save_info.pack()
    def save_details():
        number=str(entry.get())
        messagebox.showinfo("Checker!!","Checking!!!!")
        no ="91"+number
        link = f"https://api.ultramsg.com/instance15612/contacts/check?token=tvuys7sd46x6qn39&chatId={no}@c.us"  # Write the api here    
        Requests = requests.get(link)
        Object = Requests.json()
        Status = Object["Status"]

        if Status == "valid":
            label1=tk.Label(root, text="Number is in whatsapp...!").pack()
            text =tk.StringVar()
            texttosend=tk.Entry(root,textvariable=text)
            texttosend.insert("Enter the text to send:")
            texttosend.pack()
            webbrowser.open(f"https://wa.me/{no}?text={text.get()}")
                  
            time.sleep(3)
            pt.press("enter")
            return ("sent msg")

        elif Status == "invalid":
            print("Please check your number and retry...!!")
        else:
            print("Number is invalid...!!")
check_func=tk.Button(root,text="Start!?",command=save)
check_func.pack()  

