from tkinter import *
def callback():
    a=E1.get()
    label1.configure(text='APEN')
    label1.configure(bg='blue',fg=('red'))
    label2.configure(text=a)
root = Tk()
root.title("cua so 1")
root.geometry("800x800")
#root2 = Tk()
#root2.title("cua so 2")

label1 = Label(root, text="Applied Programing in\n Engineering",font=("Times New Roman",24,'bold italic underline'),fg='blue',bg='yellow')
label1.grid(row=0, column=0,columnspan=2)
label2 = Label(root, text="label 2",font=("Times New Roman",24))
label2.grid(row=1, column=0)
label3 = Label(root, text="label 3",font=("Times New Roman",24))
label3.grid(row=1, column=1)

E1=Entry(font=("Arial", 50),width=20)
E1.insert(0, 'hello')
E1.grid(row=2, column=0,columnspan=2)

B1 = Button(text="B1",font=("times",24),command=callback)
B1.grid(row=3, column=0,columnspan=2)

mainloop()