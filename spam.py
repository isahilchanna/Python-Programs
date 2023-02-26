import pyautogui as py
import time
import random
i=1
def gali_spam():
    global i
    time.sleep(5)
    while not i>=1000:
        
        choicee=["lauda","behenchod","behenkalauda","maadarchod","betichod"]
        choices=random.choice(choicee)
        py.typewrite(f"tu ek no ka {choices} hai")
        py.press("enter")
        time.sleep(1)
        print(i)
        i+=1
        

def normal_spam(whatto_spam,how_muchtospam):
    global i
    while not i>=how_muchtospam:
        time.sleep(5)
        py.typewrite(whatto_spam)
        py.press("enter")
        time.sleep(1)
        print(i)
        i+=1
        
def spam():
    qq=input("which kind of spam u want?n or g?!:")
    if qq =="n":
        whatto_spam=input("what do you want to spam?")
        how_muchtospam=int(input("how many times you wanna spam it?"))
        normal_spam(whatto_spam,how_muchtospam)
    elif qq=="g":
        gali_spam()
    else:
        print("you entered an invalid input")
        spam()
spam()
py.FAILSAFE=False
