from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Define a function to get the output for selected option
def selection():
   selected = int(radio.get())
   if selected ==1:
      label.config(text="C++")
   elif selected==2:
      label.config(text="Python")
   elif selected==3:
      label.config(text="Java")

radio = IntVar()
Label(text="", font=('Aerial 11')).pack()

# Define radiobutton for each options
r1 = Radiobutton(win, text="C++", variable=radio, value=1, command=selection)

r1.pack(anchor=N)
r2 = Radiobutton(win, text="Python", variable=radio, value=2, command=selection)

r2.pack(anchor=N)
r3 = Radiobutton(win, text="Java", variable=radio, value=3, command=selection)

r3.pack(anchor=N)

# Define a label widget
label = Label(win)
label.pack()

win.mainloop()
