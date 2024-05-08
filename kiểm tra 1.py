#bài tập giao diện
from tkinter import *
root = Tk()
def chuyendoi():
    global a   
    if a == 0:
        b = E3.get()
        c = E2.get()
        E3.delete(0,END)
        E2.delete(0,END)
        label2.configure(text="From USD")
        label3.configure(text="To VN")
        E2.insert(0, b)
        E3.insert(0, c)
        
    if a ==1:
        b = E3.get()
        c = E2.get()
        E3.delete(0,END)
        E2.delete(0,END)
        label2.configure(text="From VN")
        label3.configure(text="To USD") 
        E3.insert(0, c)
        E2.insert(0, b)
        
    if a ==1:
        a = 0
    else: a =1

def tinh():
    global a
    if a == 1:
        try:
            tien = int(E1.get())
            tinh=tien*24835
            label4.configure(text = '{} US Dollar ='.format(tien))
            label5.configure(text = '{} Vietnamese Dongs'.format(tinh))
        except:
             label5.configure(text = 'NHẬP SỐ LƯỢNG TIỀN CẦN ĐỔI')
             E1.delete(0,END)
    if a == 0:
        try:
            tien = int(E1.get())
            tinh=tien/24835
            label4.configure(text = '{} Vietnamese Dongs ='.format(tien))
            label5.configure(text = '{} US Dollar'.format(tinh))
        except:
             label5.configure(text = 'NHẬP SỐ LƯỢNG TIỀN CẦN ĐỔI')
             E1.delete(0,END)

root.title("MONEY EXCHANGE")
root.geometry("800x300")

E1=Entry(font=("Arial", 25),width=10)
E1.place(x=20,y=50)

E2=Entry(font=("", 25),width=10)
E2.place(x=300,y=50)
E2.insert(0, "USD")

E3=Entry(font=("", 25),width=10)
E3.place(x=580,y=50)
E3.insert(0, "VND")


B1 = Button(text="-><-",font=("Arial", 15),command=chuyendoi)
B1.place(x=500,y=50)

a=1

B2 = Button(text="Convert",font=("Arial", 20),bg='blue',fg="white", command=tinh)
B2.place(x=600,y=130)

label1 = Label(root, text= "Amount",font=("Arial", 22))
label1.place(x=20,y=10)

label2 = Label(root, text= "From USD",font=("Arial", 22))
label2.place(x=300,y=10)

label3 = Label(root, text= "To VN",font=("Arial", 22))
label3.place(x=580,y=10)

label4 = Label(root, text= "",font=("Arial", 22))
label4.place(x=20,y=130)

label5 = Label(root, text= "",font=("Arial", 22))
label5.place(x=20,y=180)

E1.bind('<Return>', lambda dummy = 0:tinh())


mainloop()
