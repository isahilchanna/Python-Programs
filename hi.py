import pyautogui as py
import time
i=0

while not i>=100:
    py.typewrite("{}")# put your thing that you wanna send !!
    py.press("enter")
    i+=1
    inputt=str(input())
    if inputt =='{}':# anything
        break
    py.FAILSAFE=False
