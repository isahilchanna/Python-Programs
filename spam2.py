import pyautogui as py
import time

i= 1
def normal_spam(whatto_spam,how_muchtospam):
    global i
    while not i>=how_muchtospam:
        
        py.typewrite(whatto_spam)
        py.press("enter")
        time.sleep(1)
        print(i)
        i+=1
whatto_spam=input("what do you want to spam?")
how_muchtospam=int(input("how many times you wanna spam it?"))
normal_spam(whatto_spam,how_muchtospam)

py.FAILSAFE=False
