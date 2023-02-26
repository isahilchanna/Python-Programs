from tkinter import *

root=Tk()
root.title("Calculator")
root.geometry("400x400")

# btn_1= Button(root,text="1",relief="ridge").grid(row=0,column=0)
# btn_2= Button(root,text="2",relief="ridge").grid(row=0,column=1)
# btn_3= Button(root,text="3",relief="ridge").grid(row=0,column=2)
# btn_4= Button(root,text="4",relief="ridge").grid(row=1,column=0)
# btn_5= Button(root,text="5",relief="ridge").grid(row=1,column=1)
# btn_6= Button(root,text="6",relief="ridge").grid(row=1,column=2)
# btn_7= Button(root,text="7",relief="ridge").grid(row=2,column=0)
# btn_8= Button(root,text="8",relief="ridge").grid(row=2,column=1)
# btn_9= Button(root,text="9",relief="ridge").grid(row=2,column=2)
# btn_10= Button(root,text="10",relief="ridge").grid(row=3,column=1)

num1=IntVar()
num2=IntVar()
def add():
    num=int(num1.get())
    num22=int(num2.get())
    result=num+num22
    ResultLbl=Label(root,text=result).grid(row=3,column=2)

def sub():
    num11=int(num1.get())
    num22=int(num2.get())
    result=num11-num22
    ResultLbl=Label(root,text=result).grid(row=3,column=2)

def multiply():
    num11=int(num1.get())
    num22=int(num2.get())
    result=num1*num2
    ResultLbl=Label(root,text=result).grid(row=3,column=2)


def divide():
    num11=int(num1.get())
    num22=int(num2.get())
    result=num1/num2
    ResultLbl=Label(root,text=result).grid(row=3,column=2)


EntryBtn1 =Entry(root,textvariable=num1,relief=RIDGE,width=10).grid(row=1,column=1,columnspan=1)
EntryBtn2 =Entry(root,textvariable=num2,relief=RIDGE,width=10).grid(row=2,column=1,columnspan=1)

AddBtn=Button(root,command=add,text="+",relief=RIDGE).grid(row=1,column=2)
SubBTn=Button(root,command=sub,text="-",relief=RIDGE).grid(row=2,column=2)
MultiplyBtn=Button(root,command=multiply,text="*",relief=RIDGE).grid(row=1,column=3)
DivideBtn=Button(root,command=divide,text="/",relief=RIDGE).grid(row=2,column=3 )

ResultLabel=Label(root,text="Result--").grid(row=3,column=1)
root.mainloop()
