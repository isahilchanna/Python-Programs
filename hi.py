import pyautogui as py
import time
i=0

while not i>=100:
    py.typewrite("FUCKU")
    py.press("enter")
    i+=1
    inputt=str(input())
    if inputt =='mf':
        break
    py.FAILSAFE=False
