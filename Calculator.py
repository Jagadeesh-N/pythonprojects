#calculator with python
from tkinter import *
import math
calc=Tk()
calc.geometry("280x340")
#LABEL creation
calc.title("CALCULATOR")
#entry to display
e=Entry(calc,width=42,bd=8)
e.place(x=0,y=20)
#action performed after button pressed
def set_Text(txt): #enter the text when buttons are pressed
    idx=len(e.get())
    e.insert(idx,txt)

def all_clear(): #for ac button
    e.delete(0,END)

def back_space():#function like backspace
    txt=e.get()
    e.delete(0,END)
    e.insert(0,txt[:-1])

def sq_root():  #function like squareroot
    txt=math.sqrt(float(e.get()))
    e.delete(0,END)
    e.insert(0,txt)
def square():
    txt=int(e.get())**2
    e.delete(0,END)
    e.insert(0,txt)
def cube():
    txt=int(e.get())**3
    e.delete(0,END)
    e.insert(0,txt)
def logr():
    txt=math.log(int(e.get()))
    e.delete(0,END)
    e.insert(0,txt)
def sine():
    txt=math.sin(int(float(e.get())))
    e.delete(0,END)
    e.insert(0,txt)
def cosine():
    txt=math.cos(int(float(e.get())))
    e.delete(0,END)
    e.insert(0,txt)
def degree():
    txt=math.degrees(int(e.get()))
    e.delete(0,END)
    e.insert(0,txt)
    
def equals():
    x = e.get()
    answer = eval(x)
    e.delete(0, 'end')
    e.insert(0, answer)

    
    

#buttons creation and perform action
AC=Button(calc,text="AC",width=8,height=2,command=lambda:all_clear()).place(x=0,y=60)
back=Button(calc,text="<--",width=8,height=2,command=lambda:back_space()).place(x=70,y=60)
percent=Button(calc,text="%",width=8,height=2,command=lambda:set_Text("%")).place(x=140,y=60)
divi=Button(calc,text="/",width=8,height=2,command=lambda:set_Text("/")).place(x=210,y=60)
log=Button(calc,text="log",width=8,height=2,command=lambda:logr()).place(x=0,y=100)
sq=Button(calc,text="x^2",width=8,height=2,command=lambda:square()).place(x=70,y=100)
cu=Button(calc,text="x^3",width=8,height=2,command=lambda:cube()).place(x=140,y=100)
tan=Button(calc,text="degree",width=8,height=2,command=lambda:degree()).place(x=210,y=100)
B1=Button(calc,text="(",width=8,height=2,command=lambda:set_Text("(")).place(x=0,y=140)
B2=Button(calc,text=")",width=8,height=2,command=lambda:set_Text(")")).place(x=70,y=140)
sin=Button(calc,text="sin",width=8,height=2,command=lambda:sine()).place(x=140,y=140)
cos=Button(calc,text="cos",width=8,height=2,command=lambda:cosine()).place(x=210,y=140)
seven=Button(calc,text="7",width=8,height=2,command=lambda:set_Text("7")).place(x=0,y=180)
eight=Button(calc,text="8",width=8,height=2,command=lambda:set_Text("8")).place(x=70,y=180)
seven=Button(calc,text="9",width=8,height=2,command=lambda:set_Text("9")).place(x=140,y=180)
mulp=Button(calc,text="*",width=8,height=2,command=lambda:set_Text("*")).place(x=210,y=180)
four=Button(calc,text="4",width=8,height=2,command=lambda:set_Text("4")).place(x=0,y=220)
five=Button(calc,text="5",width=8,height=2,command=lambda:set_Text("5")).place(x=70,y=220)
six=Button(calc,text="6",width=8,height=2,command=lambda:set_Text("6")).place(x=140,y=220)
minus=Button(calc,text="-",width=8,height=2,command=lambda:set_Text("-")).place(x=210,y=220)
one=Button(calc,text="1",width=8,height=2,command=lambda:set_Text("1")).place(x=0,y=260)
two=Button(calc,text="2",width=8,height=2,command=lambda:set_Text("2")).place(x=70,y=260)
three=Button(calc,text="3",width=8,height=2,command=lambda:set_Text("3")).place(x=140,y=260)
plus=Button(calc,text="+",width=8,height=2,command=lambda:set_Text("+")).place(x=210,y=260)
sqrt=Button(calc,text=u"\u221A",width=8,height=2,command=lambda:sq_root()).place(x=0,y=300)
zero=Button(calc,text="0",width=8,height=2,command=lambda:set_Text("0")).place(x=70,y=300)
dot=Button(calc,text=".",width=8,height=2,command=lambda:set_Text(".")).place(x=140,y=300)
equal=Button(calc,text="=",width=8,height=2,command=lambda:equals(),bg="orange").place(x=210,y=300)
calc.resizable(0,0)
calc.mainloop()
