from tkinter import *
def callback1():
    global c
    label3.configure(text="+")
    c=1
def callback2():
    global c
    label3.configure(text="-")
    c=2
def callback3():
    global c
    label3.configure(text="x")
    c=3
def callback4():
    global c
    label3.configure(text="/")
    c=4
def calculate():
    global c
    a = int(E1.get())
    b = int(E2.get())
    if c==4:
        if b == 0:
            label4.configure(text="b not 0")
        else:
            E3.insert(0, a/b)
    if c==1:
        E3.insert(0, a+b)
    if c==2:
        E3.insert(0, a-b)
    if c==3:
        E3.insert(0, a*b)
    
        
root = Tk()
root.title("may tinh")
root.geometry("800x800")

label1 = Label(root, text="NUMBER 1",font=("Times New Roman",24,))
label1.grid(row=0, column=0)
label2 = Label(root, text="NUMBER 2",font=("Times New Roman",24))
label2.grid(row=0, column=3)
label3 = Label(font=("Times New Roman",24))
label3.grid(row=2, column=2)
label4 = Label(font=("Times New Roman",24))
label4.grid(row=5, column=3)

E1=Entry(font=("Arial", 50),width=5)
E1.grid(row=2, column=0)
E2=Entry(font=("Arial", 50),width=5)
E2.grid(row=2, column=3)
E3=Entry(font=("Arial", 50),width=5)
E3.grid(row=5, column=2,columnspan=1)

c=0

calc_button1 = Button(text='+', font=('Times New Roman',24),command=callback1)
calc_button1.grid(row=3, column=0)
calc_button2 = Button(text='-', font=('Times New Roman',24),command=callback2)
calc_button2.grid(row=3, column=1)
calc_button3 = Button(text='x', font=('Times New Roman',24),command=callback3)
calc_button3.grid(row=3, column=2)
calc_button4 = Button(text='/', font=('Times New Roman',24),command=callback4)
calc_button4.grid(row=3, column=3)
calc_button5 = Button(text='=', font=('Times New Roman',24),command=calculate)
calc_button5.grid(row=4, column=2,columnspan=1)

mainloop()