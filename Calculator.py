from tkinter import *
import math


root=Tk()
root.geometry("200x200")
root.title("Calculator")

num1=IntVar()
num2=IntVar()
Result=0
def add():
    global num1
    global  num2
    global Result
    n1=int(num1.get())
    n2=int(num2.get())
    Result=n1+n2
    return Result
def subtract():
    global num1
    global  num2
    global Result
    n1=int(num1.get())
    n2=int(num2.get())
    Result=n1-n2
    return Result

def divide():
    global num1
    global  num2
    global Result
    n1=int(num1.get())
    n2=int(num2.get())
    Result=n1/n2
    return Result

def multiply():
    global num1
    global  num2
    global Result
    n1=int(num1.get())
    n2=int(num2.get())
    Result=n1*n2
    return Result

def power():
    global num1
    global  num2
    global Result
    n1=int(num1.get())
    n2=int(num2.get())
    Result=n1**n2
    return Result


Entry_num1=Entry(root,width=10,textvariable=num1,relief=RIDGE)
Entry_num1.insert(0,"")
Entry_num1.grid(row=0,column=1)

Entry_num2=Entry(root,width=10,textvariable=num2,relief=RIDGE)
Entry_num2.insert(1,"")
Entry_num2.grid(row=1,column=1)





Add_Bttn=Button(root,text="/",command=divide,width=10,relief=RIDGE).grid(row=0,column=2)
Sub_Bttn=Button(root,text="-",command=subtract,width=10,relief=RIDGE).grid(row=2,column=1)
Divide_Bttn=Button(root,text="x",command=multiply,width=10,relief=RIDGE).grid(row=1,column=2)
Multiply_Bttn=Button(root,text="+",command=add,width=10,relief=RIDGE).grid(row=3,column=2)
Power_Bttn=Button(root,text="^",command=power,width=10,relief=RIDGE).grid(row=3,column=1)

def Show_ResultFn():
    Show_Result=Label(root,text=f"Result : {Result}",width=10,relief=RIDGE).grid(row=5,column=2)

Show_ResultLabel=Button(root,text="=",command=Show_ResultFn,width=10,relief=RIDGE).grid(row=5,column=2)
