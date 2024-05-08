from tkinter import *
root = Tk()

def nut1():
    global a
    global b
    global c    
    if a ==0:
        b = E2.get()
        c = E1.get()
        E2.delete(0,END)
        E1.delete(0,END)
        label1.configure(text="ANH")
        label2.configure(text="VIỆT")
        E1.insert(0, b)
        E2.insert(0, c)
        
    if a ==1:
        b = E2.get()
        c = E1.get()
        E2.delete(0,END)
        E1.delete(0,END)
        label1.configure(text="VIỆT")
        label2.configure(text="ANH") 
        E2.insert(0, c)
        E1.insert(0, b)
        
    if a ==1:
        a = 0
    else: a =1


def nut2():
    global a
    global b
    global c
    global AV
    global VA
    b = E2.get()
    c = E1.get()
    if a == 1:
     if c in AV:
        E2.delete(0,END)
        E2.insert(0, AV[c])
    if a ==0:
      if c in VA:
         E2.delete(0,END)
         E2.insert(0, VA[c])   
            
        

    
root.title("TRANSLATE")
root.geometry("700x500")

label1 = Label(root, text="ANH",font=("Arial", 19))
label1.place(x=110,y=50)

label2 = Label(root, text="VIỆT",font=("Arial", 19))
label2.place(x=550,y=50)

AV={"hello":"xin chào",
    "room":"phòng",
    "table":"cái bàn",
    "chair":"cái ghế",
    "name":"tên"}
VA={"xin chào":"hello",
    "phòng":"room",
    "cái bàn":"table",
    "cái ghế":"chair",
    "tên":"name"
    }

E1=Entry(font=("Arial", 25),width=13)
E1.place(x=50,y=100)
E2=Entry(font=("Arial", 25),width=13)
E2.place(x=440,y=100)
a=1
B1 = Button(text="<->",font=("Arial", 19), command = nut1)
B1.place(x=330,y=50)
B2 = Button(text="Translate",font=("Arial", 19),command=nut2)
B2.place(x=300,y=150)

mainloop()
