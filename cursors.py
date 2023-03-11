'''JUST AN EXAMPLE OF HOW TO SHOW DIFFERENT CURSORS!!'''

from tkinter import *
root=Tk()
cursors =[
        "arrow",
        "circle",
        "clock",
        "cross",
        "dotbox",
        "exchange",
        "fleur",
        "heart",
        "man",
        "mouse",
        "pirate",
        "plus",
        "shuttle",
        "sizing",
        "spider",
        "spraycan",
        "star",
        "target",
        "tcross",
        "trek"
]
  
  
  
# Iterate through all cursors
for cursor in cursors:
    Button(root,text=cursor,cursor=cursor).pack()
  
  
