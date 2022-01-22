from tkinter import*
import math
def add():
    a=int(ent1.get())
    b=int(ent2.get())
    c=a+b
    res.configure(text="result is"+str(c))
def sub():
    a=int(ent1.get())
    b=int(ent2.get())
    c=a-b
    res.configure(text="result is"+str(c))
def mul():
    a=int(ent1.get())
    b=int(ent2.get())
    c=a*b
    res.configure(text="result is"+str(c))
def div():
    a=int(ent1.get())
    b=int(ent2.get())
    c=a/b
    res.configure(text="result is"+str(c))
def sin():
    a=int(ent1.get())
    c=math.sin(a)
    res.configure(text="\tresult"+str(c))
def cos():
    a=int(ent1.get())
    c=math.cos(a)
    res.configure(text="\tresult"+str(c))
def tan():
    a=int(ent1.get())
    c=math.tan(a)
    res.configure(text="\tresult"+str(c))

w=Tk()
w.title("welcome to bs")
lbl1=Label(w,text="\tenter first no")
lbl1.grid(column=0,row=0)
ent1=Entry(w,width=20)
ent1.grid(column=1,row=0)

lbl2=Label(w,text="\tenter second no")
lbl2.grid(column=0,row=1)
ent2=Entry(w,width=20)
ent2.grid(column=1,row=1)

btn1=Button(w,text="ADD",command=add)
btn1.grid(column=0,row=2)
btn2=Button(w,text="sub",command=sub)
btn2.grid(column=1,row=2)
btn3=Button(w,text="mul",command=mul)
btn3.grid(column=0,row=3)
btn4=Button(w,text="div",command=div)
btn4.grid(column=1,row=3)
btn5=Button(w,text="sin",command=sin)
btn5.grid(column=0,row=5)
btn6=Button(w,text="cos",command=cos)
btn6.grid(column=0,row=6)
btn6=Button(w,text="tan",command=tan)
btn6.grid(column=0,row=7)
res=Label(w,text="\tResult:see here")
res.grid(column=0,row=4)    
    
    
    
    
