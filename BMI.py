from tkinter import *
root = Tk()

root.title("BMI CALCULATOR")
root.geometry("700x500")

def nut1():
    label1.configure(text="CHIỀU CAO (cm):",font=("Arial", 19))    
    label2.configure(text="CÂN NẶNG (kg):",font=("Arial", 19))
def nut2():
    label1.configure(text="HEIGHT (Inches)",font=("Arial", 19))    
    label2.configure(text="WEIGHT (Pounds)",font=("Arial", 19))
def tinh():
    global a
    a = color.get()
    if a==1:
        try:
            cao = int(E1.get())
            nang = int(E2.get())
            cao=cao/100
            bmi = nang/(cao*cao)
            label3.configure(text = 'BMI = {} '.format(bmi))
            E1.delete(0,END)
            E2.delete(0,END)
        except:
             label3.configure(text = 'NHẬP CHIỀU CAO VÀ CÂN NẶNG')
             E1.delete(0,END)
             E2.delete(0,END)

    if a==2:
        try:
            cao = int(E1.get())
            nang = int(E2.get())
            bmi = (nang/(cao*cao))*703
            label3.configure(text = 'BMI = {}'.format(bmi))
            E1.delete(0,END)
            E2.delete(0,END)
        except:
             label3.configure(text = 'Please insert Number')
             E1.delete(0,END)
             E2.delete(0,END)
        
label1 = Label(root, text="CHIỀU CAO (cm):",font=("Arial", 19))
label1.place(x=80,y=50)
label2 = Label(root, text="CÂN NẶNG (kg):",font=("Arial", 19))
label2.place(x=80,y=150)
label3 = Label(root, text="BMI =",font=("Arial", 19),fg='green')
label3.place(x=300,y=350)

E1=Entry(font=("Arial", 25),width=10)
E1.place(x=80,y=100)
E2=Entry(font=("Arial", 25),width=10)
E2.place(x=80,y=200)

color = IntVar()
redbutton = Radiobutton(text='Metric',font=("Arial", 19), var=color, value=1, command = nut1)
redbutton.place(x=400,y=100)
greenbutton = Radiobutton(text='English',font=("Arial", 19), var=color, value=2, command = nut2)
greenbutton.place(x=400,y=150)

a=0

B1 = Button(text="CALCULATE",font=("Arial", 19),command=tinh)
B1.place(x=200,y=280)

mainloop()
